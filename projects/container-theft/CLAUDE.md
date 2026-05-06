# CLAUDE.md — Container SMCU1049407 Case Repo

> Read this first. This file is the working memory for any Claude session that opens this folder. Update it when facts change.

---

## What this repo is

A live case file for an ongoing dispute over **Container SMCU1049407** (sleeping bags, ~$24K of goods) that was hijacked at the Port of Seattle by a chain of US-side shipping agents who:

1. Filed it into US Customs without a valid Power of Attorney from the rightful importer (801, LLC)
2. Substituted the consignee on the master B/L (Great Way Trading & Transportation, possibly also "Greatland")
3. Misclassified the goods as "fishing line" instead of sleeping bags
4. Manufactured ~32 days of demurrage through their own delay
5. Lied about a customs "intensive inspection" that SSA Marine has confirmed never happened
6. Then invoiced the rightful owner ~$34,000 to release the goods (5x the agreed all-in DDP shipping cost)

The owner, Andrew Peterson (801, LLC), refused to pay. CBP Seattle has opened an active investigation. The container is currently held by Portland Container (a friendly bailee). Andrew's SLC attorney is being teed up.

This repo collects every piece of evidence, every contact, the venue analysis, and the deliverables (customer letter, attorney handoff brief).

---

## Folder layout

```
Container/
├── CLAUDE.md                                      ← you are here (working memory)
├── 01_Case_File/
│   └── CASE_FILE_SMCU1049407.md / .docx           ← master factual record + evidence index
├── 02_Customer_Comms/
│   └── Customer_Update_Worldwide_Distributors.md / .docx  ← letter to Andrew's customer
├── 03_Attorney_Package/
│   ├── Attorney_Handoff_Brief.md / .docx          ← cover memo for SLC counsel (Zack Winzeler)
│   └── Email_to_Zack_Winzeler.md / .docx          ← intro email to attorney
├── 04_Exhibits/
│   ├── Exhibit_D_DK_Internal_Review_the_bill.xls  ← DK's own cost workbook (~$27,682)
│   └── Exhibit_E_Great_Way_OEC_Invoice.pdf        ← $9,850 OSRA destination demurrage invoice
└── 05_CBP_Response/
    └── CBP_Response_to_CBPO_Butler.md / .docx     ← structured answers to 4/29 7-question info request
```

When new evidence arrives, drop it into `04_Exhibits/` with a clear name (`Exhibit_X_Description.ext`) and update both `CASE_FILE_SMCU1049407.md` (§11 Appendix) and this CLAUDE.md if the underlying fact picture changes.

---

## Cast of characters (so you don't have to re-derive every session)

### Our side
- **Andrew Peterson** — owner of 801, LLC; complainant; primary client. andrew@801inc.com / 801.809.6000. Also operates as **Ledge Sports** (andrew@ledgesports.com). Salt Lake City, Utah.
- **Aaron Peterson** — Utah Fab; sent the two 3/11/26 wires as a loan to Andrew. aaronp@utahfab.com.
- **Sabrina Fryer** — Utah Fab; executed the wires. sabrina@utahfab.com.
- **Worldwide Distributors** — Andrew's customer in Kent, WA; intended end recipient of the goods.

### Defendants / adverse
- **DK Group** — multiple aliases at the same address (17800 Castleton St, Suite #569, City of Industry, CA 91748): DK USA, DK China Group, DK Intermodal Service, DK Trucking DBA United Shipping Inc, DK Freight. SCAC DKJC, MC #1557743, USDOT #4089849.
  - **Smile Wang** — operations / public face (op1@dkchinagroup.com, WeChat 13842618282)
  - **Lucas** — operations, uses personal Gmail qiang282646@gmail.com. **Made the key admission on 5/4 11:52 AM that DK handled both booking AND customs clearance.**
  - **Alice Zhang** — signed the SSA payment as "DK Freight"
- **Great Way Trading & Transportation Inc** — 32550 Central Ave, Union City, CA 94587. Domain great-way.com. Listed as consignee on the master B/L without authorization.
  - **Vicky Wang** (primary, OOO 5/1–5/5), **Miriam Wang** (miriamwang@great-way.com), **Bruce Jia** (brucejia@great-way.com), **Jenny Dam** (printed the OEC invoice).
- **OEC Group** — parent / deconsolidator behind the Great Way demurrage invoice. Disputes: dispute.sw@oecgroup.com.
- **Dahlen Foward Shipping Supply Chain (Shanghai) Co., Ltd.** — China-side counterparty; received the $6,474.61 DDP wire. (Spelling: Andrew writes "Foward" — confirm.)

### Friendlies / witnesses (do NOT name as defendants)
- **Portland Container** — Alison. Currently holds the container. Pissed at DK, friendly to Andrew, feeding intel.
- **SSA Marine** — Brittney Nguyen (U.S. Customs Status Dept., slcgvt@ssamarine.com), Tiffany (terminal ops), Cory (demurrage). Confirmed in writing that the container never left the terminal for inspection.
- **ICCB / International Customs Broker, Inc.** — Yiwei Liu, Licensed Customs Broker (op@iccbinc.com). Holds the POA timeline that proves the original entry was unauthorized.
- **High Hope** — Chinese factory; holds original commercial documents.

### US Government (active investigation)
- **CBP Seattle / North Harbor Trade** — SEATTLE-TRADE@cbp.dhs.gov, 206-553-1581.
  - **CBPO Butler** — investigator; sent Andrew a 7-question information request on 4/29/26.
  - **Officer Cobbs** and **Officer Parker** — initial CBP officers.

---

## Key identifiers (memorize these)

| Thing | Value |
|---|---|
| Container | **SMCU1049407** (40HC) |
| Master B/L | **SMLMSHCR5G527400** (often shortened to **SHCR5G527400**) |
| House B/L | OERT201701P02119 |
| CBP Entry | **DMF10020776** |
| Vessel | SM MUMBAI V.2601E |
| ETD / ETA | 18-Feb-26 Shanghai → 16-Mar-26 Seattle |
| **Last Free Day** | **March 20, 2026** |
| **CBP Fully Cleared** | **April 7, 2026** (8 business days after Andrew gave ICCB a valid POA on 3/29) |
| Container left SSA yard | April 21, 2026 |
| DK paid SSA | $14,617.02 (Purchase #C0007115444, VISA-8708) |
| DK invoiced Andrew | ~$34,000 |
| Agreed all-in DDP shipping (already paid) | **$6,474.61** wired 3/11/26 to Dahlen Foward |
| Factory payment (already paid) | $24,576.96 wired 3/11/26 to High Hope |

---

## House rules for working in this repo

1. **Treat the case file as the single source of truth.** When new evidence comes in, update `01_Case_File/CASE_FILE_SMCU1049407.md` first; everything else flows from it.

2. **Date the updates.** Add a "Last updated" line at the top of any file you modify, with a one-line summary of what changed.

3. **Distinguish facts from allegations.** Use "documented" / "per [source]" for things in evidence; use "Andrew alleges" / "to be confirmed" for things that aren't yet pinned down.

4. **Protect the confidential source.** An industry party told Andrew that DK has done this to other importers in 2026 alone, and asked not to be disclosed. Do not name or quote the source in any document that could be sent outside this repo. Corroboration paths in case file §5G.

5. **Preserve the spelling of "Foward."** Andrew writes Dahlen *Foward* Shipping Supply Chain. It might be a misspelling of "Forward" but until confirmed, keep his spelling so wire records and emails match.

6. **Friendly parties stay friendly.** Portland Container, SSA Marine, ICCB, Worldwide Distributors, Utah Fab — none of these are defendants. Don't draft anything that treats them as adverse without explicit instruction.

7. **Andrew's voice when he's angry.** He's been understandably hostile in some emails ("rotten thieving bastards," "you have no place to hide," etc.). When drafting documents that will go out under his name, dial it down: factual, sharp, professional. The 4/30 pro se letter is a useful exhibit but not the template.

8. **Sender discipline.** Informational comms (customer updates, CBP responses, internal records) go from Andrew. Demand letters, preservation letters, court filings go from his SLC attorney. See case file §8C.

9. **Don't drift into legal advice.** When discussing strategy with Andrew, frame as "things to raise with your SLC attorney." This isn't a law firm.

---

## Current open threads (as of last update)

- Awaiting Andrew's confirmation: "Greatland" vs. "Great Way" — same entity or two separate substitutions?
- Awaiting Andrew's confirmation: spelling of "Foward" / "Forward"
- Andrew has not yet responded to CBPO Butler's 4/29 7-question info request — coordinate with attorney before sending
- Original commercial docs from High Hope (China) not yet produced
- 7501 (Entry Summary) not yet located
- DK's actual invoice to Andrew (line-by-line $34K) not yet produced
- WeChat / WhatsApp logs with DK personnel not yet pulled

---

## Workflow when Andrew dumps more evidence

1. Read what he sent. Do not assume — extract names, dates, dollar amounts, identifiers.
2. Drop any attachments into `04_Exhibits/` with `Exhibit_X_Description.ext`.
3. Update `CASE_FILE_SMCU1049407.md` — usually one or more of: §2 Parties, §3 Timeline, §4 Financial, §5 Allegations, §11 Exhibits.
4. If the new fact changes strategy (venue, defendants, theories), update `Attorney_Handoff_Brief.md`.
5. If the new fact changes what Andrew tells his customer, update `Customer_Update_Worldwide_Distributors.md`.
6. Update this CLAUDE.md if the cast of characters or open threads changes.
7. Tell Andrew what you captured, in two or three sentences. Don't make him read the whole diff.
