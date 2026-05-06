# Email to Fred Qin (Sunwave) — Off-grid + right-sized quote request

**To:** fred.qfk@foxmail.com
**From:** Andrew Petersen
**Subject:** Peterson project — off-grid configuration questions and right-sized quote request
**Date:** April 10, 2026

---

Hi Fred,

Thanks for the Sunwave ESS proposal and the April 8 deck. We've reviewed it against the other quotes we're evaluating and Sunwave is looking very competitive on price. Before we move forward, I need to confirm a few technical points about the SEI-18K-USP inverter and get a right-sized quote for the actual system we want to build.

## System architecture we're planning

The Peterson residence in Utah is going to be configured as **fully off-grid** with the existing diesel generator integrated as winter backup. We are not pursuing utility interconnection with Rocky Mountain Power — the export credit is too low to be worth the paperwork, and the on-site diesel already handles multi-day cloudy weather, so we don't need the grid as a fallback.

The right-sized configuration for this site is:

- **2× SEI-18K-USP hybrid inverters** (paralleled, 36 kW total)
- **10× SW-LCT-16 LV LFP batteries** (160.8 kWh total)
- Panels and trackers sourced separately

## Technical questions

Please confirm the following about the SEI-18K-USP for off-grid operation:

1. **Pure off-grid / grid-forming mode.** Can the SEI-18K-USP operate as a grid-forming inverter with no utility connection at all? Does it require a grid reference to start up, or can it form a 120/240V split-phase AC waveform purely from battery power?

2. **Generator AC input.** Your datasheet shows a "Grid/Generator Input" — does this accept a diesel generator with 2-wire auto-start signal? Specifically:
   - Can the inverter automatically start the generator when battery SOC drops below a programmable threshold (e.g., 25%)?
   - Can it automatically stop the generator when SOC reaches a programmable upper threshold (e.g., 90%)?
   - Does the inverter provide a dry-contact relay output to trigger the generator's 2-wire start terminal?

3. **Paralleling 2 units.** Your datasheet says "Parallel Capacity: 1–9 Units." For a 2-unit parallel configuration:
   - Is a master/slave setup required, or are both units peers?
   - Do the two inverters share a single communication cable (CAN/RS485), and is the cable included?
   - Does the configuration require both inverter banks to share one battery bank, or can each inverter have its own set of batteries?
   - Is anti-islanding disabled automatically in off-grid mode, or does it need to be manually disabled?

4. **Surge / starting current.** The well pump on this site is a 240V single-phase unit (exact HP TBC). What is the peak surge current the SEI-18K-USP can deliver for motor starting? Specifically, can the inverter handle a 3–5× locked-rotor surge on a 5 HP motor for ~2 seconds?

5. **Certification for US permit.** We confirmed the inverter carries CSA C22.2 No. 107.1-16. Is there any additional North American listing (ETL, Intertek, NRTL equivalent) that would help us with the Tooele County electrical inspector? Any UL 9540 system-level listing for the inverter + battery combination?

## Right-sized quote request

Please send a formal quote for:

| Item | Qty |
|---|---|
| Sunwave SEI-18K-USP split-phase hybrid inverter | 2 |
| Sunwave SW-LCT-16 LV LiFePO4 battery (16.08 kWh) | 10 |
| Parallel communication cable kit for 2-unit parallel | 1 set |
| Battery interconnect cables for 10-battery bank | 1 set |
| Any required BMS master / control accessories | as needed |
| Schneider AC + DC breakers (as in your 72/192 quote, proportioned) | as needed |

Please quote FOB China (Hefei or nearest port), with:
- Lead time from PO to ready-to-ship
- 20 ft vs. 40 ft container volume and weight
- Payment terms
- Warranty details (especially the generator-input scenario — does the warranty cover inverters that are regularly AC-coupled to a diesel genny?)

## Timing

We are trying to make a supplier decision in the next 2 weeks so we can begin construction before July 4, 2026 for federal tax credit reasons. Fast turnaround on these questions would be very appreciated.

Thanks Fred — Sunwave is currently our leading candidate on price and if the off-grid operation confirms cleanly, we are ready to move.

Best,
Andrew Petersen
Peterson Solar Project
Erda, Utah
