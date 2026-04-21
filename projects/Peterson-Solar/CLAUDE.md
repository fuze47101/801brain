# Peterson Solar Project — Working Memory

**Last updated:** April 20, 2026 (rev 4 — 5 new supplier quotes added; battery-only + tracker-only vendors flagged for pairing; ZRD pricing obtained from Torres Wang; Joy Chen = GSL Energy reconciled)
**Project owner:** Andrew (son), sourcing on behalf of Roger L. Peterson (father)
**Site:** 1324 E Green Meadows Ct, Erda, Utah 84074 — 5-acre property
**Problem:** ~$800/mo summer electric bills from continuous well pump; ~$3,500/yr total
**Strategy:** China-direct sourcing via Andrew's 25-year supplier relationships, dual-axis fenceline trackers + battery storage
**Architecture (rev 3):** **Full off-grid (Mode A)** with existing diesel genny as winter backup. No utility interconnection. RMP Schedule 137 not pursued. Roger's existing diesel handles multi-day cloudy stretches; battery handles day-to-day. Grid net billing economics too weak to justify UL 1741 SA cert requirement and Schedule 137 paperwork.
**Sourcing note:** These Chinese suppliers have been unusually slow and terse — they don't volunteer offerings, they quote oversized defaults, and they omit certs unless asked three times. Treat every new quote as "first draft" and expect to push for right-sizing + cert docs before it's usable.

---

## 1. Current status (one-liner per workstream)

| Workstream | Status | Notes |
|---|---|---|
| Design doc | Rev 2 complete, OBBBA no-ITC baseline | `Peterson_Solar_Design.html` |
| Comparison sheet | 4 tabs, rev'd April 21 | `Peterson_Solar_Quote_Comparison.xlsx` |
| Panels | Simone Wang quoted $3,250 for 8-panel dual-axis bundle | Company name still pending |
| Trackers | **ZRD priced via Torres Wang @ $800/set FOB Qingdao (30 sets = 1× 20GP)** + Huayue drawing only (no price); Simone bundle numbers stand | Torres Wang is ZRD's sales rep; foundation bolts + wind sensor included |
| Inverter+battery (ESS) | **6 live quotes:** Sunpal/Megarevo, Japower (3 opts), Sunwave, LongKun, Kamada | Sunwave still LEADING CANDIDATE. LongKun + Kamada quotes need right-sizing. |
| Batteries only (no inverter) | **GSL Energy 157.6 kWh LiFePO4 @ $17,710 FOB** — **Joy Chen is at GSL** (WhatsApp rel.) = Alex Yan's formal sales | Pair with LV-bus inverter (Sunwave / SolArk / SRNE) |
| Local install | SolArk + Joy Chen batts — kept as fallback if Sunwave fails off-grid gates | |
| ITC status | **Residential 25D repealed by OBBBA 12/31/2025** — economics now assume $0 credit | 48E ag/LLC still open if construction begins by 7/4/2026 |
| RMP interconnection | **NOT PURSUED** — off-grid architecture eliminates the need | Net billing credit too weak to justify cert + paperwork burden |
| Diesel genny integration | AC input to hybrid inverter (Roger's existing unit) | Not a gating item; any hybrid we're looking at has a grid/gen input |
| Customs broker | Not engaged | Needed before any order |
| Load profile | **Known** — pump load characterized; sizing driven by Andrew's tier preference, not pump nameplate | n/a |

---

## 2. Key facts & gotchas

- **US residential service at the Peterson house:** 120/240V single-phase split. Any inverter that is not explicitly split-phase 120/240V 60Hz is out.
- **Roger is currently 100% on-grid** for all loads and has a **full-size diesel backup generator** already on site for outages. The diesel is the key enabler of Mode A — no need to keep RMP as winter backup.
- **OBBBA killed the residential ITC (Sec. 25D)** effective 12/31/2025. 2026 residential owners get $0 federal credit. Sec. 48E commercial ITC (30%) is still alive for projects that begin construction by **July 4, 2026**. If the system is owned by a farm/ranch/LLC business, it may qualify under 48E. **This is time-sensitive — CPA call is the highest-leverage action on the project right now.**
- **UL 1741 vs. UL 1741 SA — these are different.** UL 1741 (or equivalent CSA C22.2 No. 107.1) is a base product-safety listing and is sufficient for NEC 690.4(B) "listed equipment" in off-grid installations. UL 1741 SA (Supplement A) adds grid-support / anti-islanding / Rule 21 functions and is **only required for grid-interactive export** (utility interconnection). Mode A off-grid systems do NOT need UL 1741 SA.
- **Rocky Mountain Power Schedule 137 net billing pays ~$0.04–$0.05/kWh** (wholesale avoided cost) vs. ~$0.11–$0.12/kWh retail for imports. Export credit economics are too weak (< $500/yr on Tier 3) to justify the UL 1741 SA constraint and interconnection paperwork. This is why Mode A wins.
- **Current US tariff stack on Chinese solar gear (April 2026):**
  - Panels: ~50% (Sec. 301 + AD/CVD)
  - Inverters: ~25% (Sec. 301)
  - Batteries: ~25% (Sec. 301, stepped up Jan 2026)
  - Trackers: ~25% (Sec. 301)
  - Blended landed-cost premium: assume **~35% on top of FOB China**
- **Japower 80kWh/30kW unit** referenced in earlier design revs may not be a stock SKU. Laura's actual quote offers 80kWh/**18kW** (SRNE) or 100kWh/30kW (Solis).

---

## 3. Supplier quote registry

### 3A. Sunpal + Megarevo — ESS (quoted prior session)
- **Config:** 30kW split-phase hybrid + battery
- **Price:** $17,378 FOB
- **Cert:** UL (explicitly claimed)
- **Phase:** Split-phase 120/240V ✅
- **Status:** Best-documented option pre-Japower; still a contender

### 3B. Sunpal + Atess — ESS (quoted prior session)
- **Config:** 30kW 3-phase hybrid + battery
- **Price:** $19,458 FOB
- **Phase:** 3-phase ❌ — **NOT compatible with residential split-phase service**
- **Status:** 🚫 REJECTED

### 3C. Japower (Laura, laura@japowerenergy.com, +86 133 2260 3051) — quoted April 9–10, 2026
Three options; all-in-one integrated ESS (inverter + battery + breakers + combiner).

| | Option 1 | Option 2 | Option 3 |
|---|---|---|---|
| Battery | 80 kWh LV | 215 kWh | 100 kWh |
| Inverter | **SRNE 18kW split-phase 120/240V** | **Solis 60kW 480V 3-phase** | Solis 30kW split-phase 208/220/240V |
| UL cert | **Yes** (explicitly claimed for SRNE) | Not stated | Not stated |
| Included | 3× Schneider AC breakers, 1× Schneider DC breaker, 1× PV combiner | same | same |
| Price FOB | **$11,999** | $26,490 | $19,999 |
| Outdoor adder | +$1,000 (IP54 cabinet + AC + fire protection) | not stated | not stated |
| Warranty | not stated | 10 years | not stated |
| Residential fit | ✅ Good | 🚫 **480V 3-phase = commercial only** | ⚠️ OK, more expensive |

**Key insight:** Japower is an integrator, not a manufacturer. They're reselling SRNE and Solis inverters with their own battery packs. SRNE is a known brand with legitimate UL 1741 listings on some models — verify exact model and listing.

### 3D. Sunwave (Fred Qin, fred.qfk@foxmail.com, +86 15375424983) — quoted April 2, 2026
Separate components, not integrated cabinet. Preferred deck received April 8.

**Proposed system: 72 kW / 192 kWh**
| Line item | Qty | Unit price | Total |
|---|---|---|---|
| Sunwave SEI 18kW Split-Phase Hybrid Inverter (model SEI-18K-USP) | 4 | $3,042 | $12,168 |
| Sunwave SW-LCT-16 LV LiFePO4 battery (16.08 kWh, 51.2V/314Ah) | 12 | $1,308 | $15,696 |
| Shipping | — | — | (blank) |
| **Total FOB** | | | **$27,864** |

**Sunwave SEI-18K-USP inverter key specs:**
- Phase voltage 90–140V, line voltage 156–243V → split-phase 120/240V ✅
- Frequency 40–70 Hz
- 97.5% max efficiency, 97% CEC
- Parallel up to 9 units
- IP65, 5-year warranty
- **Certificate: CSA C22.2 No. 107.1-16, IEC62109-1/2, EN61000-6-1/3**
- CSA C22.2 107.1 is the Canadian equivalent of UL 1741 base product-safety listing. CSA is an NRTL recognized by OSHA and accepted by NEC 690.4(B) as "listed equipment" → **satisfies Tooele County permit requirement for off-grid install**
- ⚠️ No UL 1741 SA / IEEE 1547 / Rule 21 → would block RMP grid interconnection, but **NOT A BLOCKER FOR MODE A OFF-GRID** (rev 3 decision)
- Datasheet explicitly shows a **"Grid/Generator Input"** — purpose-built to accept a diesel genny on the AC input

**Sunwave SW-LCT-16 battery:**
- 16.08 kWh, 51.2V nominal, 314 Ah, LiFePO4
- 6,000+ cycles @ 25°C / 80% DOD, 15-year design life, **10-year warranty**
- IP54, UN38.3, IEC62619, **UL9540A (battery pack only)**
- LV bus — must pair with LV-compatible hybrid inverter

**$/unit math:**
- Battery: **$81.34/kWh** — best price on the table
- Inverter: **$169/kW** — also excellent

**But:** the total price ($27,864) is for **4× inverters and 12× batteries** (72kW / 192 kWh) — massively oversized for Roger's Tier 3 (60kW / 160 kWh target). At the per-unit rates, a right-sized Tier 3 Sunwave kit (2× 18kW inverter + 10× 16 kWh batteries = 36 kW / 160 kWh) would cost **$6,084 + $13,080 = $19,164 FOB** — dramatically undercuts Japower.

### 3E. Simone Wang (company TBD) — panels + trackers
- **Quoted:** $3,250 for 8-panel dual-axis bundle
- **Pending:** company name, panel spec (wattage, brand), tracker spec, cert docs
- **Status:** Promising on unit economics; waiting on details

### 3F. Joy Chen — **Shenzhen GSL Energy Co.** (same company as 3I — WhatsApp sidebar in Alibaba chat 2026-04-20 confirms)
- **Joy is the primary relationship at GSL; Alex Yan (sales21@gsl-energy.com) is the formal sales rep on the email side of the house.** Treat 3F and 3I as ONE supplier; **Joy is who actually produced the PI.**
- **Joy's formal quote (same $17,710 / 11-unit / indoor-rack PI that appears in 3I):**
  - 11× GSL-51-280 rack-mounted battery @ $1,575 each (14.33 kWh / 51.2 V LiFePO4)
  - 11× indoor rack @ $35 each
  - **$17,710 FOB, 157.6 kWh total**
- **She over-quoted.** 11 units = ~Tier 3; Roger's actual need depends on which tier we target. See right-size math in 3I.
- Earlier separate advice (before the formal PI): buy **SolArk inverter locally in the US** + source only GSL LV batteries from China — rationale for SolArk-local is weaker now that Mode A off-grid removes the UL 1741 SA requirement, but SolArk remains the best US-stocked LV-bus off-grid inverter.
- **Status:** Go back to Joy with **right-sized ask** keyed to Tier 1/2/3 (see 3I).

### 3G. LongKun Battery Group — Zoey Mai (Zoey@irichsolar.com, WhatsApp +1 713 875-0860) — Quote CLKQ25, dated 2026-04-16
- **Shenzhen-based integrator; sells both HV battery cabinets and inverters.**
- **Line items as quoted:**
  - 10× 40 kWh outdoor battery cabinet @ $10,022 = $100,220
    - REPT Grade A cells, **UL1973 / UL9540A** certified, 10 yr warranty, 6000 cycles
    - HV architecture: 358.4–460.8 V, 735×1125×2220 mm, 613 kg, CAN2.0 + RS485
  - 5× 30 kW "US Standard" hybrid inverter @ $5,381 = $26,905
    - 30 kW rated, 60 kW max PV, **160–800 V battery input (HV bus)**, 544×880×278 mm, 80 kg, 5 yr warranty
- **Total: $127,125 FOB (EXW)** · Lead time 25 days · T/T **100% in advance** · **Validity expires 2026-04-23 (7 days)**
- **As quoted = 400 kWh / 150 kW — ~2.5× Tier 3.** Classic commercial-default oversize.
- **Per-unit rates:** 40 kWh cabinet **$10,022** (~$250/kWh). 30 kW inverter **$5,381** (~$179/kW).
- **Right-sized math (unit × qty at per-unit rates):**

| Sizing tier | Battery cabinets | kWh | Inverters | kW inv | Battery FOB | Inverter FOB | **Total FOB** |
|---|---|---|---|---|---|---|---|
| **Tier 1** (30 kWh) | 1× 40 kWh | 40 | 1× 30 kW | 30 | $10,022 | $5,381 | **$15,403** |
| **Tier 2** (80 kWh) | 2× 40 kWh | 80 | 1× 30 kW | 30 | $20,044 | $5,381 | **$25,425** |
| **Tier 3** (160 kWh) | **4× 40 kWh** | **160** | 2× 30 kW | 60 | **$40,088** | $10,762 | **$50,850** |
| As-quoted | 10× 40 kWh | 400 | 5× 30 kW | 150 | $100,220 | $26,905 | $127,125 |

- **Tier 3 headline (Andrew's working number):** 4 cabinets alone ≈ **$40k battery FOB**, and you'd add 1–2 inverters to get to a full ESS. Against Sunwave right-sized ($19,164 FOB for the same 160 kWh) that's **~2× more expensive before tariffs** — LongKun only wins if the inverter side has capability Sunwave can't match.
- **⚠️ Unclear:** (a) Is the 30 kW "US Standard" inverter actually **split-phase 120/240 V**, or just rated for US grid freq? Text says "US Standard" but doesn't name phase topology. (b) UL listings shown are for the **battery only** (UL1973/UL9540A) — **no UL cert called out on the inverter**. (c) HV bus (160–800 V) means this inverter is NOT compatible with Sunwave, GSL, SolArk, or any LV-bus battery stack. If buying LongKun, it's LongKun-inverter + LongKun-cabinet, period.
- **Status:** ⚠️ Validity window tight; right-size + clarify before responding.

### 3H. Kamada / Shenzhen Kamada Electronic — James Tang (James@kmdpower.com, +86 13237437130) — PI KMD-260417025, dated 2026-04-17
- **Addressed "To: ledgesports, ATTN: Andrew Peterson"** — James identified Andrew's Ledge Sports domain, not the personal project.
- **Line items as quoted (6 sets — also oversized):**
  - 6× Hybrid inverter all-in-one "15 kW×2" 240 V split-phase @ $3,885 = $23,310
    - **"RatedPower: 15 KW×2" is ambiguous** — could mean 30 kW continuous (two 15 kW stacks in one enclosure) OR 15 kW rated / 2× peak. 1 pallet / 0.25 CBM / 88 kg per unit. HS 8504.40.3090.
  - 6× Kamada BESS, 16 kWh LiFePO4 pack (5 packs in parallel) @ $7,115 = $42,690
    - **Sizing unclear** — "Lithium battery pack: 16000wh, 5 pieces are connected in parallel" reads like each BESS unit is 5× 16 kWh = 80 kWh, BUT the picture shows a single 5-high rack. Could be 16 kWh total per set. 10 yr warranty, 20 yr life. HS 8507.60.0090.
  - Sea shipping DDP to **Erda (ZIP 84074)**: $8,500 for 35 days
- **Total $74,500 DDP, all-in** · T/T 50/50 · **Validity expires 2026-04-22 (5 days)**
- **Only DDP quote on the table** — directly comparable to Sunwave's ~$25,870 *landed*.
- **Per-set back-calc (quote ÷ 6):** ~$12,417 per set DDP (if the 6-set interpretation holds).
- **⚠️ Unclear:** (a) What is "a set" — one inverter + one 16 kWh battery, or one inverter + five 16 kWh batteries (80 kWh)? (b) UL / UL9540 status not mentioned anywhere. (c) Is the inverter grid-forming off-grid capable?
- **Status:** Promising DDP economics if sizing decodes favorably; urgent to reply before validity lapses.

### 3I. GSL Energy — Alex Yan (sales21@gsl-energy.com, +86 19926534667) — dated 2026-04-17
- **Shenzhen GSL Energy Co., Ltd. Pure battery shop; "Since 2006, served 80+ countries."** (Received same PDF twice — deduped.)
- **⚠️ SAME COMPANY AS 3F (Joy Chen)** — Alibaba chat sidebar 2026-04-20 confirms Joy Chen is listed at Shenzhen GSL Energy Co. Joy's informal "$1,609 LV batt" verbal matches GSL-51-280 at $1,575 to within negotiating noise.
- **Line items:**
  - 11× GSL-51-280 rack-mounted battery @ $1,575 = $17,325
    - 14.33 kWh each, 51.2 V / 280 Ah LiFePO4, 16s2p, **REPT Grade A cells**, integrated BMS + DC breaker + cables, "Protocol Selection on Screen", 10 yr warranty
  - 11× rack @ $35 = $385
- **Total $17,710 FOB** · Lead time 20 days · T/T 30% deposit + balance pre-shipment · Validity 15 days (expires ~2026-05-02)
- **Per-unit economics:** **$1,575/unit, ~$110/kWh, 14.33 kWh/unit** (indoor rack +$35/unit).
- **Quote was oversized** — Joy proposed 11 units ≈ 157.6 kWh. Right-size to the chosen tier:

| Sizing tier | Units (@ 14.33 kWh) | kWh delivered | Battery FOB | + indoor racks | Total FOB |
|---|---|---|---|---|---|
| **Tier 1** (30 kWh target) | **2** | 28.7 | $3,150 | $70 | **$3,220** |
| **Tier 2** (80 kWh target) | **6** | 86.0 | $9,450 | $210 | **$9,660** |
| **Tier 3** (160 kWh target) | **11** (or 10) | 157.6 (143.3) | $17,325 ($15,750) | $385 ($350) | **$17,710 ($16,100)** |

- **⚠️ CRITICAL:** Batteries only — **NO inverter offered**. Must be paired with an LV-bus hybrid inverter. Compatible candidates: Sunwave SEI-18K-USP (confirmed LV bus), SolArk 15K, SRNE HES series. NOT compatible with LongKun HV (160–800 V) or Japower HV options.
- **Outdoor cabinet:** Quote is for **indoor rack mount** — if deploying outside, need an IP-rated cabinet adder or a sheltered enclosure. Ask Joy about outdoor option.
- **Certs claimed:** "Grade A REPT cells" — need specific doc support for **UL1973, UL9540A, UN38.3, IEC62619**. Protocol list needed for BMS compatibility verification.
- **Status:** Strong battery-only option at any tier. Viable pairing examples:
  - **Tier 3:** GSL batt (11× indoor) $17,710 + Sunwave 2× 18K $6,084 = **$23,794 FOB** (vs $19,164 FOB for Sunwave-bundle — Sunwave bundle still wins by $4,630 but GSL gives negotiating leverage)
  - **Tier 2:** GSL batt (6× indoor) $9,660 + Sunwave 1× 18K $3,042 = **$12,702 FOB** for 86 kWh / 18 kW
  - **Tier 1:** GSL batt (2× indoor) $3,220 + Sunwave 1× 18K $3,042 = **$6,262 FOB** for 28.7 kWh / 18 kW

### 3J. Sunchaser / Shandong Zhaori New Energy Tech — ZRD Dual-Axis Tracker
**Contacts:** Torres Wang (Alibaba chat, sales rep) · solartracker@zhaoripv.com (general)

- **PRICING (from Torres Wang via Alibaba chat, 2026-04-20):** **$800/set FOB Qingdao**, MOQ 30 sets = 1× 20GP container
  - Exact price varies by panel size and panels/set — $800 is the working number pending final panel spec
  - **Included in price:** foundation bolts + wind sensor
  - **Optional adder:** Rain + Snow Sensor **+$50/set** (worth specifying for Utah winter — Erda gets meaningful snowfall)
- **Model family:** ZRD dual-axis tracker, Independent Drive, linear actuator + slewing drive + gear ring
- **Configs offered:** 2, 6, 8, or 10 panels per set (≤26 m² per set)
- **Components per set (from Solar Tracker Components.pdf):** mounting structure, control unit, E-W linear actuator, N-S linear actuator, connection screws, wind sensor, foundation bolts
- **Specs:** E-W ±45°, N-S 50° · ≤2° tracking accuracy · backtracking YES · 24 m/s in-op wind / 40 m/s stow · DC brushless gear motor · -40°C to +80°C · IP65 · RS485 + wireless · astronomical algorithm controller · hot-dipped galvanized steel or Superdyma
- **Certs:** CE, TÜV SÜD (shown on datasheet)
- **Warranty:** 3 years, extendable
- **Company pitch:** 12 years experience, 60+ countries exported
- **Container math:** 30 sets/20GP → if 8 panels/set then 240 panels/container; if 10 panels/set then 300 panels/container. Roger's Tier 3 at 550 W panels is ~54 panels — only ~20% of a minimum order. **MOQ mismatch** — need to either (a) aggregate a second buyer to hit 30 sets, (b) negotiate a smaller order at a premium, or (c) step up to a bigger system.
- **Outstanding questions to Torres (open):**
   - (a) **"How many panels fit on one set?"** — determines set quantity for Roger's pump-offset sizing
   - (b) **"Do you also provide cells?"** — asking whether ZRD sells panels too, which would collapse this into a single-supplier panels+trackers deal
- **Status:** First real price point on any tracker. Container MOQ is the hard question; waiting on Torres to size panels-per-set and confirm whether ZRD can bundle panels/cells.

### 3K. Huayue / Shandong Huayue (huayuenewenergy@uniquesolar.cn, https://huayuetracker.com/) — HYS-8PV-78-LSD or HYS-8PV-144-LSD
- **MECHANICAL DRAWING ONLY — NO PRICE, NO SPECS BEYOND DIMENSIONS.**
- **Model confusion:** Filename says `HYS-8PV-144-LSD.pdf`, title block inside the drawing says `HYS-8PV-78-LSD`. One of them is wrong — ask which they actually sell.
- **Layout:** 8-panel dual-axis, 4578 × 5316 mm envelope, 60° operating tilt, panel array 1134×4 + 20×3 = 4596 mm × 2279×2 + 20 = 4578 mm
- **Status:** Not yet a quote. Need to request formal PI + datasheet + certs.

---

## 4. Landed-cost quick reference (adds ~35% blended tariff to FOB; trackers ~25%)

### ESS options (inverter + battery)
| Option | FOB | Est. landed | kWh | kW inverter |
|---|---|---|---|---|
| ⭐ **Sunwave right-sized** (2× SEI-18K + 10× SW-LCT-16) | **$19,164** | **~$25,870** | 160.8 | 36 |
| GSL batt (11×) + Sunwave inverter (2× 18K) | $23,794 | ~$32,120 | 157.6 | 36 |
| Japower Opt 1 (outdoor) × 2 | $26,000 | ~$35,100 | 160 | 36 |
| Sunwave as-quoted (4× + 12×) | $27,864 | ~$37,600 | 192 | 72 |
| LongKun right-sized (1 cab + 1 inv) | $15,403 | ~$20,790 | 40 | 30 |
| LongKun Tier 3 equiv (4 cab + 2 inv) | ~$50,850 | ~$68,650 | 160 | 60 |
| Kamada 6-set DDP as-quoted | $74,500 | $74,500 *(DDP, inclusive)* | ~96–480 (sizing TBC) | ~90 |
| Japower Opt 3 × 2 | $39,998 | ~$54,000 | 200 | 60 |
| Sunpal/Megarevo | $17,378 | ~$23,460 | ~80 | 30 |
| SolArk-local + GSL batts (est) | ~$22,000 | ~$25,000 | ~140 | 15–20 |

### Battery-only
| Option | FOB | Est. landed | kWh |
|---|---|---|---|
| GSL Energy (11× GSL-51-280) | $17,710 | ~$23,900 | 157.6 |

### Trackers (FOB China; ~25% tariff)
| Option | Per set FOB | Est. per set landed | Panels/set | Notes |
|---|---|---|---|---|
| ZRD / Sunchaser (Torres) | $800 | ~$1,000 | 2 / 6 / 8 / 10 (TBC) | MOQ 30 sets/20GP; foundation bolts + wind sensor incl.; +$50 snow sensor |
| Huayue HYS-8PV | TBD | TBD | 8 | Drawing only |
| Simone Wang bundle (panels+tracker) | $3,250/8-panel set | ~$4,060/set | 8 | Only bundle price on table; company name TBC |

---

## 5. Open questions / blocking items

*(Load profile is known; well pump and diesel genny specs are NOT gating items — Mode A runs on any of the hybrids under consideration and the genny is just an AC input. 48E ag/LLC is worth chasing for the credit but is NOT a go/no-go gate.)*

**Decision driver = best price + install + supplier quality, right-sized to Andrew's chosen tier.** Everything below is in service of that.

1. **Sunwave (Fred Qin) — 3 clarifiers before we commit:**
   - (a) SEI-18K-USP grid-forming / pure-off-grid support confirmed?
   - (b) AC input takes a generator (simple source, no auto-start dependency)?
   - (c) 2-unit parallel config — master/slave, matched battery banks required?
2. **LongKun (Zoey Mai @ iRich Solar) — URGENT, expires 2026-04-23:**
   - (a) Is the 30 kW "US Standard" inverter actually split-phase 120/240 V?
   - (b) Any UL listing on the inverter itself (battery already has UL1973/9540A)?
   - (c) Right-sized PI for 1× cabinet + 1× inverter (or 2+1 / 3+1 for tier scaling).
3. **Kamada (James Tang @ Shenzhen Kamada / KMD Power) — URGENT, expires 2026-04-22:**
   - (a) What is "a set" — 16 kWh or 80 kWh of battery?
   - (b) Is the 15 kW×2 inverter one 30 kW unit or two 15 kW stacks, and is it grid-forming off-grid?
   - (c) Any UL9540 / UL1741 listing?
4. **ZRD / Torres Wang (open in Alibaba chat):**
   - (a) How many panels fit on one set (2/6/8/10)?
   - (b) Does ZRD also supply cells / panels?
   - (c) Can they ship <30 sets at a premium, or do we aggregate a second buyer?
5. **GSL (Joy Chen + Alex Yan, Shenzhen GSL Energy):**
   - (a) Right-sized PI at Tier 1 / Tier 2 / Tier 3 (2 / 6 / 10–11 units).
   - (b) UL1973 + UL9540A + UN38.3 + IEC62619 cert PDFs.
   - (c) Outdoor-cabinet option (quote was indoor rack only).
   - (d) BMS protocol list — confirm Sunwave SEI-18K-USP compatibility.
6. **Japower (Laura):** Does an 80 kWh / 30 kW integrated unit actually exist, and at what price? Exact SRNE model + UL listing number.
7. **Simone Wang:** Company name, panel brand/wattage, tracker spec, cert docs.
8. **Huayue:** Confirm model (`-78-LSD` vs `-144-LSD`), datasheet, price, certs.
9. **CPA call on 48E ag/LLC eligibility** — upside (~$17K on Tier 3) if it lands; not gating the supplier selection.
10. **Customs broker engagement** — landed-cost estimate for a 20 ft / 40 ft mixed container (inverters 8504.40.3090 / batteries 8507.60.0090 / trackers + panel HTS TBC).
11. **Tooele County building dept** — confirm CSA C22.2 107.1 satisfies NEC 690.4(B) (10-min call).

---

## 6. Rejected / closed items

- **Sunpal/Atess** — 3-phase, not residential-compatible ❌
- **Japower Option 2 (Solis 60kW 480V)** — 3-phase, not residential-compatible ❌
- **Residential ITC (25D)** — repealed by OBBBA; economics updated to reflect $0 credit
- **January 2026 battery tariff trigger** — already past; 25% rate is current
- **Separate battery shed** — eliminated by all-in-one ESS designs; outdoor cabinet at +$1,000 replaces it

---

## 7. Decision tree

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PETERSON SOLAR DECISION TREE                          │
└─────────────────────────────────────────────────────────────────────────┘

 GATE 1 ── TAX STRUCTURE ──────────────────────────────────────────────────
 │
 │  Can Roger's property be owned by a farm/ranch/LLC business?
 │
 ├─ YES → Section 48E path (30% ITC restored)
 │        ├─ MUST begin construction by 7/4/2026
 │        ├─ CPA engagement required NOW
 │        └─ Restores ~$17K on Tier 3 (payback drops from ~16 yrs to ~11)
 │
 └─ NO  → Section 25D residential path ($0 federal credit)
          └─ Economics already reflect this in design doc

 GATE 2 ── SIZING TIER (driven by Andrew's preference + tax outcome) ────
 │
 │  Load profile is known; sizing is a business decision, not a pump-plate lookup.
 │
 ├─ Tier 1 (9.9 kW / 30 kWh) — bill relief only
 ├─ Tier 2 (17.6 kW / 80 kWh) — summer slayer ⭐ default if 48E lands short
 └─ Tier 3 (29.7 kW / 160 kWh) — prepper / full offset ⭐ default if 48E lands

 GATE 3 ── OPERATING MODE (supersedes UL 1741 SA question) ───────────────
 │
 │  Rev 3 decision: Mode A chosen. Gate exists for documentation only.
 │
 ├─ MODE A: Full off-grid ⭐ CHOSEN
 │    ├─ No RMP interconnection, no Schedule 137
 │    ├─ Diesel genny on inverter AC input for winter backup
 │    ├─ NEC permit only — any NRTL-listed inverter (UL or CSA) acceptable
 │    ├─ Unlocks Sunwave as viable leading candidate
 │    └─ RMP service: drop it, or keep dormant behind a manual transfer switch
 │
 ├─ MODE B: Non-export grid-parallel (backup plan)
 │    ├─ Keep RMP connection, program inverter for zero export
 │    ├─ No UL 1741 SA required (not exporting)
 │    ├─ Still needs RMP non-export declaration
 │    └─ Would be the fallback if Tooele County objects to CSA-only cert
 │
 └─ MODE C: Grid-tied with export (REJECTED)
      ├─ Requires UL 1741 SA → blocks Sunwave
      ├─ Schedule 137 export credit ~$0.04–$0.05/kWh
      ├─ Net export value < $500/yr — not worth the constraint
      └─ Only revisit if Utah net billing economics improve dramatically

 GATE 4 ── SIZING TIER ────────────────────────────────────────────────────
 │
 │  Based on pump load + Andrew's prepper preference
 │
 ├─ Tier 1: 50% offset (9.9 kW / 30 kWh)            → ~$17,290 residential
 ├─ Tier 2: Summer slayer (17.6 kW / 80 kWh)        → ~$31,160 residential
 └─ Tier 3: Zombie apocalypse (29.7 kW / 160 kWh)   → ~$56,820 residential
    ⭐ Recommended if 48E works; still recommended on prepper grounds even if not

 GATE 5 ── ESS SOURCING (Tier 3 branch, Mode A off-grid) ─────────────────
 │
 │  Compare on $/landed, off-grid capability, cert status
 │
 ├─ ⭐ Sunwave right-sized (LEADING CANDIDATE, rev 3)
 │   → 2× SEI-18K-USP inverter + 10× SW-LCT-16 = 36 kW / 160.8 kWh
 │   → $19,164 FOB / ~$25,870 landed
 │   → CHEAPEST on table, best $/kWh on batteries
 │   → CSA listing satisfies NEC for off-grid install
 │   → OPEN: confirm off-grid mode + genny AC input + paralleling
 │
 ├─ GSL batt + Sunwave inverter (hybrid)
 │   → 11× GSL-51-280 + 2× Sunwave SEI-18K-USP = 36 kW / 157.6 kWh
 │   → $23,794 FOB / ~$32,120 landed
 │   → Leverage play if Sunwave balks on right-size; otherwise Sunwave bundle wins
 │
 ├─ Japower Opt 1 × 2 (outdoor)
 │   → $26,000 FOB / ~$35,100 landed
 │   → Most turnkey (all-in-one), UL claimed, 36 kW inverter power
 │   → BACKUP if Sunwave fails off-grid verification
 │
 ├─ LongKun right-sized (1 cab + 1 inv)
 │   → 40 kWh HV cabinet + 30 kW HV inverter = $15,403 FOB / ~$20,790 landed
 │   → Cheapest entry point but HV bus locks you into LongKun ecosystem
 │   → Undersized for Tier 3; stack 4 cab + 2 inv → ~$50,850 FOB / ~$68,650 landed
 │   → OPEN: inverter UL listing, split-phase 120/240V topology
 │
 ├─ Kamada 6-set DDP
 │   → $74,500 all-in DDP to Erda
 │   → Only DDP quote on table; eliminates customs/tariff uncertainty
 │   → Sizing ambiguity ("15 kW×2", 16 kWh vs 80 kWh/set) blocks comparison
 │   → DEAD IF sizing turns out to be on the small end; WINNER if on the big end
 │
 ├─ Japower Opt 3 × 2
 │   → $39,998 FOB / ~$54,000 landed
 │   → Matches original 60 kW spec, most inverter headroom
 │   → Most expensive China path; only if pump needs the extra headroom
 │
 └─ SolArk local + GSL/Joy batts
     → ~$25,000 est landed equivalent
     → FALLBACK if all China ESS options fail off-grid verification
     → SolArk is the most battle-tested off-grid inverter in the US market

 GATE 6 ── PANELS + TRACKERS ──────────────────────────────────────────────
 │
 │  Secondary decision — sourcing less risky than ESS
 │
 ├─ ZRD (Torres Wang) trackers standalone
 │   → $800/set FOB Qingdao, MOQ 30 sets/20GP, +$50 snow sensor optional
 │   → CE + TÜV SÜD, foundation bolts + wind sensor included
 │   → ISSUE: MOQ way larger than Roger's needs — aggregate buyer OR negotiate
 │   → OPEN: panels/set, does ZRD also sell panels/cells
 │
 ├─ Simone Wang bundle → $406/panel incl. tracker (if 8-panel $3,250 holds)
 │   → Single-source panels + trackers; simplest logistics
 │   → OPEN: company name, panel wattage/brand, tracker spec
 │
 ├─ Huayue HYS-8PV → drawing only, no price
 │   → Low priority until they quote
 │
 ├─ Separate LONGi/Trina/JA direct + tracker RFQ to Kesheng/PromiSteel/NCNF
 └─ Southeast Asian assembly (Vietnam/Cambodia/Thailand) to dodge AD/CVD
     → Verify current duty rates with customs broker before ordering

 GATE 7 ── INSTALL APPROACH ───────────────────────────────────────────────
 │
 ├─ DIY mechanical + licensed electrician for interconnection (plan of record)
 ├─ Full local installer bid (comparison baseline, likely 2–3× China-direct)
 └─ Hybrid: Andrew + Roger self-perform foundations, trackers, conduit;
         electrician handles ESS hookup, inspection, PTO
```

---

## 8. Next actions (in priority order)

1. **Reply to James (Kamada @ Shenzhen Kamada / `kmdpower.com`) — URGENT, expires 2026-04-22.** Decline 6-set size; decode what "a set" is (16 kWh vs 80 kWh), ask whether the 15 kW×2 is one 30 kW unit, UL9540 / UL1741 status, off-grid grid-forming.
2. **Reply to Zoey (LongKun @ iRich Solar) — URGENT, expires 2026-04-23.** Decline 10-cab/5-inv size; ask for right-sized 1 cab + 1 inv PI, inverter phase topology (split-phase 120/240?), and UL listing on the inverter.
3. **Reply to Fred (Sunwave)** — draft ready in outputs. Three-question email on off-grid / grid-forming, generator AC input, 2-unit paralleling. Requests a right-sized PI (2× SEI-18K + 10× SW-LCT-16).
4. **Reply to Torres (ZRD @ Shandong Zhaori)** — answer his open thread. Need panels/set, whether ZRD sells cells/panels, and whether they'll ship <30 sets at a premium.
5. **Reply to Joy / Alex (GSL)** — Joy's 11-unit quote was oversized; ask for Tier 1 / 2 / 3 PIs (2 / 6 / 10–11 units), UL1973 + UL9540A cert PDFs, outdoor-cabinet option, BMS protocol list.
6. **Schedule CPA call** re: 48E ag/LLC structure and 7/4/2026 deadline — upside, not gating.
7. **Reply to Laura (Japower)** — keep warm as backup; ask about 80 kWh / 30 kW integrated config and SRNE 18 kW exact UL listing number.
8. **Push Simone Wang** for company name, panel wattage/brand, tracker model, cert docs.
9. **Push Huayue** on `-78-LSD` vs `-144-LSD` model, full datasheet, price.
10. **Call Tooele County building dept** — confirm CSA C22.2 107.1 satisfies NEC 690.4(B) (10-min call).
11. **Engage a customs broker** for a landed-cost estimate on a mixed 40 ft container.
12. **Keep `Peterson_Solar_Quote_Comparison.xlsx` in sync** with any new supplier clarifications.

---
*This file is working memory for the Peterson solar project. Keep it updated as quotes arrive, decisions are made, and blockers clear.*
