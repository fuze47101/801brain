# Solaris FZ-500 — Project CLAUDE.md

## Owner
Andrew Peterson (andrew@801inc.com)

## Project Overview
**Solaris FZ-500** is a fabric/material testing rig built on a Raspberry Pi 5. It uses thermocouples, an IR lamp, and a heated plate to run controlled heat-soak tests on fabric samples. The rig logs temperature data to CSV for analysis. First demo target: Portland show.

## Parent Project
Helios — see `projects/Helios/CLAUDE.md` for Pi setup, networking, and credentials.

## Hardware

### Raspberry Pi 5
- **Hostname:** `solaris`
- **Username:** `fuze`
- **Password:** `Fuze47101`
- **SSH:** `ssh fuze@solaris.local`
- **WiFi (first boot):** `FX4` / `Jetflow101` (phone hotspot)
- **WiFi (office):** `Evoq-Biz` / `Allotrope#1`
- **WiFi (backup):** `ISEEYOU2` / `Fuze47101`
- **GPIO chip:** `/dev/gpiochip4` (Pi 5 specific)
- **OS:** Raspberry Pi OS Lite 64-bit

### Thermocouples (MAX31855 Breakout Boards)
Two K-type thermocouple channels via SPI:

**TC-A (MAX31855 #1 — CE0):**

| Wire | MAX31855 Pin | Pi 5 Physical Pin |
|------|-------------|-------------------|
| Power | Vin | Pin 1 (3.3V) |
| Ground | GND | Pin 6 (GND) |
| DO (data) | DO | Pin 21 (MISO — shared) |
| CS (chip select) | CS | Pin 24 (CE0 / GPIO 8) |
| CLK (clock) | CLK | Pin 23 (SCLK — shared) |

**TC-B (MAX31855 #2 — CE1):**

| Wire | MAX31855 Pin | Pi 5 Physical Pin |
|------|-------------|-------------------|
| Power | Vin | Pin 17 (3.3V — second 3V3 rail) |
| Ground | GND | Pin 9 or 14 (any GND) |
| DO (data) | DO | Pin 21 (MISO — SHARED with TC-A) |
| CS (chip select) | CS | Pin 26 (CE1 / GPIO 7) — ONLY CHANGE |
| CLK (clock) | CLK | Pin 23 (SCLK — SHARED with TC-A) |

**SPI pin sharing:** MISO (Pin 21), SCLK (Pin 23), and power/GND are shared by design. CS is what makes each board individually addressable. Use a mini breadboard to fan out shared pins cleanly.

**TC probe wiring:** Red wire in LEFT screw terminal, Yellow in RIGHT screw terminal.

### IR Lamp Control (SSR)
Binary on/off control of an IR heat lamp via Solid State Relay.

**Control wiring:**

| Pi Side | SSR Side |
|---------|----------|
| Pin 16 (GPIO 23) — "IR_LAMP_CTRL" | SSR DC(+) |
| Pin 14 (GND) | SSR DC(−) |
| 10kΩ pulldown from Pin 16 to Pin 14 | — |

**The pulldown is critical** — prevents SSR chatter during Pi boot (GPIO floats HIGH without it → lamp strobes).

**Mains side (DIY inline box):**
- Cut HOT wire of extension cord only (never neutral)
- Hot input → inline 3A fuse → SSR AC terminal 1
- SSR AC terminal 2 → Hot output to lamp
- Neutral and ground pass through untouched (wire nutted)
- Metal box, grounded, strain relief on all cables

**Safety layers:**
1. Thermal fuse (240°C one-shot) on lamp housing
2. Software watchdog — if TC > 250°C, force GPIO LOW + log
3. GFCI outlet upstream
4. 10kΩ pulldown for boot-safe default OFF

**IoT Relay upgrade (when it arrives):**
Replace DIY box with Digital Loggers "IoT Relay" (~$30). Same Pi wiring (GPIO 23 + GND to screw terminals). Plug lamp into "normally-off" outlet. 60-second swap, zero mains wiring.

### Heated Plate (SSR-40DA, PID controlled)
- Existing SSR-40DA drives cartridge heater in plate
- PID control via daemon
- Separate from IR lamp circuit

## Software

### Python Environment
```bash
cd ~ && python3 -m venv solaris-env && source solaris-env/bin/activate
pip install spidev smbus2 requests adafruit-circuitpython-sht4x adafruit-circuitpython-mlx90640
```

### GPIO Control (Pi 5)
```python
import gpiod

chip = gpiod.Chip('/dev/gpiochip4')  # Pi 5 = chip4
lamp_line = chip.get_line(23)
lamp_line.request(consumer="solaris", type=gpiod.LINE_REQ_DIR_OUT, default_val=0)

def lamp_on():
    lamp_line.set_value(1)

def lamp_off():
    lamp_line.set_value(0)
```

### CLI GPIO Test
```bash
sudo gpioset gpiochip4 23=1   # lamp ON
sudo gpioset gpiochip4 23=0   # lamp OFF
```

### Daemon Script
`solaris_daemon.py` — lives at `~/solaris_daemon.py` on the Pi (SCP from laptop)
- Reads TC-A and TC-B via SPI (CE0, CE1)
- Controls IR lamp via GPIO 23
- Logs timestamped CSV data
- Safety watchdog: emergency OFF if TC > setpoint

### Example Automated Test Cycle
```python
# 12-minute run:
t0 = time.time()
lamp_off()
# 0-60s: baseline, lamp off
while time.time() - t0 < 60: log_sample()
lamp_on()
# 60s-660s: 10-minute heat soak
while time.time() - t0 < 660: log_sample()
lamp_off()
# 660s-720s: 1-minute cooldown
while time.time() - t0 < 720: log_sample()
```

## Initial Pi Setup Commands (after first SSH)
```bash
# First boot setup
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv git i2c-tools python3-libgpiod
sudo raspi-config nonint do_spi 0
sudo raspi-config nonint do_i2c 0
sudo reboot

# After reboot — add office WiFi
sudo nmcli dev wifi connect "Evoq-Biz" password "Allotrope#1"
sudo nmcli dev wifi connect "ISEEYOU2" password "Fuze47101"

# Python environment
cd ~ && python3 -m venv solaris-env && source solaris-env/bin/activate
pip install spidev smbus2 requests adafruit-circuitpython-sht4x adafruit-circuitpython-mlx90640
```

## Safety Test Sequence (DIY SSR Box — before first use)
1. **Visual** — no bare conductors, cover on, strain reliefs tight
2. **Continuity (unplugged):**
   - Hot input → hot output: NO beep (SSR open)
   - Neutral input → neutral output: BEEP (pass-through)
   - Ground input → ground output: BEEP (pass-through)
   - Ground → metal box: BEEP (grounded)
3. **Manual SSR test:** 2× AA batteries to DC(+)/DC(−), re-check hot: BEEP (SSR closed)
4. **Plug in with NO lamp attached** — 10 sec, no smoke, no GFCI trip
5. **Lamp test (Pi disconnected)** — plug lamp in, should be OFF (SSR open)
6. **Pi control test:**
   - Land control wires + pulldown
   - Boot Pi → lamp stays OFF
   - `sudo gpioset gpiochip4 23=1` → lamp ON
   - `sudo gpioset gpiochip4 23=0` → lamp OFF

## Shopping List
**Amazon same-day (SLC):**
- SSR-25DA or SSR-40DA (Fotek) — $8-12
- 170-point mini breadboard — $3-4 (for SPI pin sharing)
- 120-piece DuPont jumper kit (M-M, M-F, F-F) — $8
- 10kΩ resistor 5-pack — $2
- Digital Loggers IoT Relay — ~$30 (upgrade from DIY box)

**Home Depot / Lowes (DIY SSR box):**
- 14 AWG 6ft indoor extension cord (3-prong) — $6
- 4x4 metal handy box + blank cover — $4
- Two 1/2" clamp strain reliefs — $4
- Inline AGC fuse holder + 3A slow-blow — $4
- Wire nuts (small pack) — $2
- Small rubber grommet — $1

## Assembly Checklist
- [x] Flash Pi 5 SD card (Raspberry Pi OS Lite 64-bit, hostname solaris, user fuze)
- [ ] SSH into Pi over FX4 hotspot
- [ ] Run initial setup (apt, SPI/I2C enable, reboot)
- [ ] Add Evoq-Biz WiFi from command line
- [ ] Wire TC-A (MAX31855 #1 on CE0) — smoke test
- [ ] Wire TC-B (MAX31855 #2 on CE1) — smoke test with breadboard pin sharing
- [ ] Build DIY SSR lamp control box (for Wednesday tests)
- [ ] Wire SSR box to Pi (GPIO 23 + GND + 10kΩ pulldown)
- [ ] Run safety test sequence on DIY box
- [ ] Deploy solaris_daemon.py
- [ ] Run first automated 12-minute test cycle
- [ ] Swap to IoT Relay when it arrives
- [ ] Portland show demo prep

## Key Deadlines
- **Wednesday** — First fabric test runs (need DIY SSR box built by then)
- **Portland show** — Full demo rig operational

---

## Session History
- **Helios Design 3** — Flashed Pi 5, fought WiFi (Evoq-Biz blocking), resolved with FX4 hotspot. Username mixup (Imager used hostname as username). Reflashed with correct settings. Left off at: Pi flashed, ready to boot on FX4 and SSH in.
- **Solaris** — Wired TC-A on CE0 (confirmed working). Planned TC-B wiring on CE1. Designed IR lamp SSR control circuit (GPIO 23 → SSR DC → mains lamp). Planned DIY inline SSR box build and IoT Relay upgrade. Wrote lamp control code for daemon. Discussed safety layers (thermal fuse, software watchdog, GFCI, pulldown). Shopping list finalized for Amazon same-day + Home Depot run.

---

## Related Files
- `~/Desktop/solaris_daemon.py` — Main daemon script (on laptop, SCP to Pi)
- `~/Desktop/Solaris_FZ500_Assembly_Guide.html` — Visual assembly guide
- `~/Desktop/helios/CLAUDE.md` — May contain older version of this info
