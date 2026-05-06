# Helios — Project CLAUDE.md

## Owner
Andrew Peterson (andrew@801inc.com)

## Project Overview
**Helios** is the parent platform/brand for FUZE's hardware testing rigs. The Solaris FZ-500 is the first product under Helios. Helios sessions cover Raspberry Pi setup, flashing, networking, and hardware design iteration.

## Machines
- **Bond** — Mac Mini (office)
- **DX / DX23** — MacBook Pro (portable)
- Both sync via `801brain` GitHub repo (`fuze47101/801brain`)

## Network Environment
- **Office WiFi:** `Evoq-Biz` / `Allotrope#1` (UniFi managed, /22 subnet: 10.100.100.0-10.100.103.255)
- **Hotspot fallback:** `FX4` / `Jetflow101` (Andrew's phone, reliable for Pi first-boot)
- **Secondary WiFi:** `ISEEYOU2` / `Fuze47101`
- **UniFi controller:** 10.100.100.1

## Raspberry Pi Credentials (Standard)
- **Hostname:** per-device (e.g., `solaris`, `helios`)
- **Username:** `fuze`
- **Password:** `Fuze47101`
- **SSH:** enabled (password auth)

## Raspberry Pi Imager Settings (Template)
When flashing any new Pi for the Helios platform:
1. OS: Raspberry Pi OS Lite 64-bit
2. Click Next → Edit Settings
3. Hostname: `<device-name>`
4. Username: `fuze`
5. Password: `Fuze47101`
6. WiFi SSID: `FX4` (use hotspot for first boot — avoids enterprise network issues)
7. WiFi Password: `Jetflow101`
8. Country: `US`
9. Services tab → Enable SSH with password authentication
10. Save → Write

After first boot on hotspot, add office WiFi from command line:
```bash
sudo nmcli dev wifi connect "Evoq-Biz" password "Allotrope#1"
sudo nmcli dev wifi connect "ISEEYOU2" password "Fuze47101"
```

## Pi 5 Technical Notes
- GPIO chip is `/dev/gpiochip4` (NOT gpiochip0 like Pi 4)
- Use `libgpiod` v2 for GPIO control (NOT RPi.GPIO — incompatible with Pi 5)
- Install: `sudo apt install python3-libgpiod`
- CLI test: `sudo gpioset gpiochip4 23=1` (set GPIO 23 HIGH)
- SPI bus is shared: MISO (Pin 21) and SCLK (Pin 23) shared between all SPI devices
- Each SPI device gets its own CS/CE pin (CE0 = Pin 24, CE1 = Pin 26)
- Pi 5 GPIO can source 16mA at 3.3V — enough to directly drive SSR-25DA input (~5-10mA)

## Raspberry Pi MAC Prefixes (for network scanning)
Known Pi MAC prefixes: `2c:cf:67`, `d8:3a:dd`, `dc:a6:32`, `b8:27:eb`, `e4:5f:01`

Scan command:
```bash
arp -a | grep -i "2c:cf:67\|d8:3a:dd\|dc:a6:32\|b8:27:eb\|e4:5f:01"
```

## Design Iterations
- **Helios v3** — Current design iteration (as of "Helios Design 3" session)
- **Helios Expedry** — Variant/related project (repo: `fuze47101/helios_expredry`)

## Related Repos
- `fuze47101/helios` — Main Helios repo
- `fuze47101/helios_v3` — Version 3
- `fuze47101/helios_expredry` — Expedry variant
- `fuze47101/801brain/projects/Helios/` — Central brain project folder

## Sub-Projects
- **Solaris FZ-500** — See `projects/Solaris/CLAUDE.md` for full details

---

## Session History
- **Helios Design 3** — Flashed Raspberry Pi 5 with hostname `solaris` for the FZ-500 testing rig. Fought WiFi connectivity (Evoq-Biz enterprise network blocking new devices). Resolved by switching to FX4 phone hotspot for first boot. Username was set to `solaris` instead of `fuze` by Imager (used hostname as username) — reflashed with correct settings. Pi MAC not found on ARP table scan — reflashed with hotspot WiFi. Final config: hostname `solaris`, user `fuze`, password `Fuze47101`, WiFi `FX4`/`Jetflow101`, SSH enabled.

---

## Next Steps
- [ ] Confirm SSH into Solaris Pi over FX4 hotspot
- [ ] Initial Pi setup (apt update, python3-venv, git, i2c-tools, SPI/I2C enable)
- [ ] Add Evoq-Biz and ISEEYOU2 WiFi from command line after first boot
- [ ] Wire and test MAX31855 thermocouple boards
- [ ] Deploy solaris_daemon.py
- [ ] See Solaris CLAUDE.md for full hardware task list
