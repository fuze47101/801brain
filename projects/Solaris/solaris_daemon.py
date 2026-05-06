#!/usr/bin/env python3
"""
Solaris FZ-500 — Sensor Daemon
Reads 2× MAX31855 (SPI), SHT41 (I²C), optional MLX90640 (I²C)
POSTs time-series to FUZE Atlas /api/admin/solaris-tests/[id]/ingest

Usage:
  # Local only (console output, no Atlas upload):
  python3 solaris_daemon.py

  # With Atlas integration:
  SOLARIS_TEST_ID=test_001 ATLAS_TOKEN=your_token python3 solaris_daemon.py

  # Override duration (seconds):
  RUN_DURATION=300 python3 solaris_daemon.py
"""

import time, json, sys, os, signal
import spidev
import board
import adafruit_sht4x
import requests

# ── Config ──────────────────────────────────────────────
ATLAS_BASE    = os.environ.get("ATLAS_URL", "https://atlas.fuze47.com")
TEST_ID       = os.environ.get("SOLARIS_TEST_ID", "")
BEARER_TOKEN  = os.environ.get("ATLAS_TOKEN", "")
SAMPLE_HZ     = 1
RUN_DURATION  = int(os.environ.get("RUN_DURATION", "600"))
BUFFER_SIZE   = 60  # POST every 60 samples
# ────────────────────────────────────────────────────────

# ── SPI: MAX31855 ×2 ───────────────────────────────────
def read_max31855(bus, cs):
    """Read temperature from MAX31855. Returns (temp_c, fault_code)."""
    spi = spidev.SpiDev()
    spi.open(bus, cs)
    spi.max_speed_hz = 5_000_000
    spi.mode = 0
    raw = spi.readbytes(4)
    spi.close()

    val = (raw[0] << 24 | raw[1] << 16 | raw[2] << 8 | raw[3])
    fault = val & 0x7
    if fault:
        return None, fault

    tc_raw = (val >> 18) & 0x3FFF
    if tc_raw & 0x2000:
        tc_raw -= 16384
    return tc_raw * 0.25, 0

# ── I²C: SHT41 ─────────────────────────────────────────
i2c = board.I2C()
sht = adafruit_sht4x.SHT4x(i2c)
sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPREC

# ── Optional: MLX90640 ──────────────────────────────────
mlx = None
try:
    import adafruit_mlx90640
    mlx = adafruit_mlx90640.MLX90640(i2c)
    mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ
    print("[OK] MLX90640 thermal camera detected")
except Exception:
    print("[--] MLX90640 not found — running without thermal camera")

# ── Graceful shutdown ───────────────────────────────────
running = True
def handle_signal(sig, frame):
    global running
    running = False
    print("\n[!!] Shutting down...")
signal.signal(signal.SIGINT, handle_signal)
signal.signal(signal.SIGTERM, handle_signal)

# ── POST buffer to Atlas ────────────────────────────────
def post_to_atlas(samples):
    if not TEST_ID or not BEARER_TOKEN:
        return
    url = f"{ATLAS_BASE}/api/admin/solaris-tests/{TEST_ID}/ingest"
    try:
        resp = requests.post(url, json={"samples": samples}, headers={
            "Authorization": f"Bearer {BEARER_TOKEN}",
            "Content-Type": "application/json"
        }, timeout=10)
        if resp.status_code == 200:
            print(f"  [POST] {len(samples)} samples → Atlas OK")
        else:
            print(f"  [POST] Atlas returned {resp.status_code}: {resp.text[:100]}")
    except Exception as e:
        print(f"  [POST] Failed: {e}")

# ── Also save local CSV backup ──────────────────────────
csv_path = None
csv_file = None

def init_csv():
    global csv_path, csv_file
    ts = time.strftime("%Y%m%d_%H%M%S")
    csv_path = os.path.expanduser(f"~/solaris_run_{ts}.csv")
    csv_file = open(csv_path, "w")
    csv_file.write("elapsed_s,sample_n,tc_a_c,tc_b_c,air_temp_c,air_rh_pct\n")
    print(f"  [CSV] Logging to {csv_path}")

def write_csv(sample):
    if csv_file:
        csv_file.write(f"{sample['t']},{sample['n']},"
                       f"{sample.get('tc_a','')},{sample.get('tc_b','')},"
                       f"{sample.get('air_temp_c','')},{sample.get('air_rh_pct','')}\n")
        csv_file.flush()

# ── Main loop ───────────────────────────────────────────
def main():
    print("=" * 60)
    print("  SOLARIS FZ-500 — Sensor Daemon")
    print(f"  Duration: {RUN_DURATION}s @ {SAMPLE_HZ} Hz")
    print(f"  Atlas: {'CONNECTED' if TEST_ID else 'LOCAL ONLY (no TEST_ID)'}")
    print("=" * 60)

    init_csv()
    buffer = []
    t_start = time.time()
    sample_n = 0

    while running and sample_n < RUN_DURATION * SAMPLE_HZ:
        t0 = time.time()
        elapsed = t0 - t_start

        # Read thermocouples
        tc_a, fault_a = read_max31855(0, 0)
        tc_b, fault_b = read_max31855(0, 1)

        # Read SHT41
        try:
            air_t, air_h = sht.measurements
        except Exception:
            air_t, air_h = None, None

        # Read MLX90640 (optional, every 5th sample — it's slow)
        thermal_frame = None
        if mlx and sample_n % 5 == 0:
            try:
                frame = [0] * 768
                mlx.getFrame(frame)
                thermal_frame = [round(p, 1) for p in frame]
            except Exception:
                pass

        sample = {
            "t": round(elapsed, 2),
            "n": sample_n,
            "tc_a": round(tc_a, 2) if tc_a is not None else None,
            "tc_b": round(tc_b, 2) if tc_b is not None else None,
            "tc_a_fault": fault_a if fault_a else None,
            "tc_b_fault": fault_b if fault_b else None,
            "air_temp_c": round(air_t, 2) if air_t is not None else None,
            "air_rh_pct": round(air_h, 1) if air_h is not None else None,
        }
        if thermal_frame:
            sample["thermal"] = thermal_frame

        buffer.append(sample)
        write_csv(sample)
        sample_n += 1

        # Console output
        tc_a_s = f"{tc_a:.1f}°C" if tc_a else f"FAULT:{fault_a}"
        tc_b_s = f"{tc_b:.1f}°C" if tc_b else f"FAULT:{fault_b}"
        air_s  = f"{air_t:.1f}°C/{air_h:.0f}%" if air_t else "ERR"
        pct = int(elapsed / RUN_DURATION * 100)
        print(f"  [{pct:3d}%] {elapsed:6.1f}s  TC-A={tc_a_s}  TC-B={tc_b_s}  Air={air_s}")

        # Flush buffer to Atlas
        if len(buffer) >= BUFFER_SIZE:
            post_to_atlas(buffer)
            buffer = []

        # Maintain 1 Hz cadence
        dt = time.time() - t0
        if dt < 1.0 / SAMPLE_HZ:
            time.sleep(1.0 / SAMPLE_HZ - dt)

    # Final flush
    if buffer:
        post_to_atlas(buffer)

    if csv_file:
        csv_file.close()

    print("\n" + "=" * 60)
    print("  RUN COMPLETE")
    print(f"  Total samples: {sample_n}")
    print(f"  Duration: {time.time() - t_start:.1f}s")
    if csv_path:
        print(f"  CSV saved: {csv_path}")
    print("=" * 60)

if __name__ == "__main__":
    main()
