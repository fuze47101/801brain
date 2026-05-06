# Peterson Solar — Project CLAUDE.md

## Owner
Andrew Peterson (andrew@801inc.com) — project lead
Roger Peterson (Andrew's father) — property owner, end user

## Project Overview
Off-grid solar + battery storage installation for Roger Peterson's rural Utah property. Includes solar panels, single-axis post trackers, battery ESS (energy storage system), and diesel generator integration. The system must power the full property including a well pump with high surge current.

## Operating Mode
**Mode A — Full Off-Grid** (chosen)
- No grid connection, no utility interaction, no net metering
- Solar → Batteries → Diesel genny backup (auto-start when SOC low)
- Diesel genny wires into inverter's AC input as backup charging source
- Mode B (grid-tied with backup) is fallback if Mode A has issues
- Mode C (pure grid-tied) rejected — no resilience value

## System Sizing Target
- **Solar array:** ~20-30 kW (exact size TBD based on panel/tracker quotes)
- **Battery storage:** ~30-50 kWh usable (modular 16 kWh units preferred)
- **Inverter:** Grid-forming capable, off-grid mode, generator AC input with 2-wire auto-start
- **Well pump:** High surge current — need nameplate specs (HP, FLA, LRA) from Roger

## Key Decision: Battery Architecture
**Modular 16 kWh wins 7-2 over monolithic big battery:**
- Cost: modular cheaper per kWh
- Serviceability: swap one module vs replace entire pack
- Scalability: add modules later
- Handling: lighter individual units for rural install
- Thermal: distributed heat dissipation
- Warranty: replace failed module only
- Manufacturer transparency: more options
- Monolithic only wins on wiring simplicity and plug-and-play install

---

## Supplier Registry

### ESS (Inverter + Battery) — Active Quotes

**Sunwave** ⭐ LEADING CANDIDATE
- Off-grid capable, grid-forming
- Generator AC input with 2-wire auto-start support
- Right-sized quote received
- Parallel 2-unit configuration available
- Contact: Fred (email drafted for technical Q&A)
- Open question: NRTL listings beyond CSA? UL 1741 SA cert status?

**Japower**
- 3 quote options received (different capacity tiers)
- Doubled-up Tier 3 configurations priced
- Fallback path at ~$76,600
- Modular battery approach

**Sunpal / Megarevo**
- Quote received
- In comparison spreadsheet

**SolArk + Joy Chen**
- Fallback option
- SolArk is US-market standard for off-grid
- Joy Chen sourcing batteries

**Rejected:**
- Two 3-phase options — not compatible with residential single-phase property

### Panels — Quotes Needed
- **Simone Wang** — bundled quote (panels + trackers together, need her to unbundle for apples-to-apples)
- **LONGi** — Tier 1 direct, quote pending
- **Trina** — Tier 1 direct, quote pending
- **JA Solar** — Tier 1 direct, quote pending
- **Canadian Solar** — Tier 1 direct, quote pending
- **50% panel tariff** baked into all landed cost calculations

### Single-Axis Post Trackers — Quotes Needed
- **Simone Wang** — bundled with panels (need unbundled price)
- **Kesheng** — quote pending
- **PromiSteel** — quote pending
- **NCNF** — quote pending
- **AllEarth** — US-made benchmark, quote pending
- **25% tracker tariff** applied to all imports

---

## Cost Summary (as of last session)

### Known Costs
- ESS (inverter + battery): varies by supplier — see spreadsheet
- Local electrical work: included in BOM
- Foundation/mounting: included in BOM
- **Known total: ~$27,564** (ESS + electrical + foundations)

### Estimated Total
- **~$67,000** once panels, trackers, and shipping fill in

### Tariffs (blended ~35%)
- Panels: 50% tariff
- Trackers: 25% tariff
- ESS/inverters: varies
- Explicit ~$13K tariff allowance broken out in latest cost model

### Tax Credits
- **OBBBA killed the standard residential solar tax credit**
- **48E agricultural/LLC workaround** — potential path to retain credit
- If 48E works: payback drops to ~10 years
- Without 48E: simple payback ~19 years, ~14 years with 4% rate escalation

### ROI Table
4 scenarios compared: Tier 1, Tier 2, Tier 3 (Sunwave), Tier 3 (Japower backup)

---

## Diesel Generator Integration
- Roger has an existing diesel generator on property
- Need from Roger: make, model, kW rating, 2-wire auto-start capability
- Most Generac/Kohler/Cummins home standby units have 2-wire auto-start terminals
- Older pull-start portables do NOT — requires manual start
- If no auto-start: Mode A still works, Roger manually starts when inverter app pings low SOC (~2-3× per winter)

**Control logic:**
Solar → Batteries → SOC drops below threshold → Genny auto-start → Charges batteries → SOC recovers → Genny auto-stop

---

## Documents & Files
- **Peterson_Solar_Quote_Comparison.xlsx** — Master comparison spreadsheet (5 tabs: ESS, Battery Architecture, Panels, Trackers, Project Total)
- **Peterson_Solar_Design.html** — Interactive design document (Rev 3, off-grid architecture)
- **Peterson_Solar_Update_for_Roger.docx** — Summary document for Roger
- **Email_to_Fred_Sunwave.md** — Technical Q&A email draft for Sunwave

## Items Needed from Roger
1. ~~Well pump nameplate photo (HP, voltage, phase, FLA, LRA)~~ — Andrew says not needed, capacity target is set
2. **Diesel genny details** — make, model, kW rating, 2-wire auto-start terminals?

## Open Actions
- [ ] Send Fred (Sunwave) the technical Q&A email — covers off-grid mode, generator input, parallel config, well pump surge, NRTL listings
- [ ] Get Simone Wang to unbundle panel + tracker pricing separately
- [ ] Request Tier 1 panel direct quotes (LONGi, Trina, JA Solar, Canadian Solar)
- [ ] Request tracker quotes (Kesheng, PromiSteel, NCNF, AllEarth)
- [ ] Get diesel genny details from Roger
- [ ] Evaluate 48E ag/LLC tax credit path
- [ ] Final supplier decision in ~2 weeks (Sunwave leading)

---

## Gate Decision Framework

### Gate 1: Site Assessment ✅
- Rural Utah property, adequate solar resource
- Existing well pump (high surge), diesel genny on site

### Gate 2: System Sizing ✅
- ~20-30 kW solar, ~30-50 kWh battery, modular 16 kWh architecture

### Gate 3: Operating Mode ✅
- Mode A (full off-grid) chosen
- Mode B (grid-tied backup) as fallback
- Mode C (pure grid-tied) rejected

### Gate 4: Supplier Selection — IN PROGRESS
- Sunwave leading, Japower fallback
- Awaiting panel and tracker quotes

### Gate 5: Final Quote & Contract — PENDING
- Need all quotes in hand
- 2-week decision timeline communicated to Sunwave

---

## Session History
- **Peterson Solar 1** — Built CLAUDE.md rev 3 with off-grid architecture. Updated design doc with Sunwave + diesel integration, tariff transparency (~$13K explicit), new ROI table. Drafted Fred/Sunwave technical Q&A email. Created Roger update document (conversational, ~1.5 pages). Built Peterson_Solar_Quote_Comparison.xlsx with 5 tabs (ESS, Battery Architecture, Panels, Trackers, Project Total). Known costs $27,564, estimated total ~$67K. Key gaps: panel-only and tracker-only quotes from Simone Wang, Tier 1 panel direct quotes.
- **Peterson Solar 2** — Currently running (as of April 21, 2026). Updating spreadsheet and analysis.
