# Ledge Outdoors — Master Marketing Playbook

## Owner
Andrew (andrew@801inc.com) — Founder / Operator

## Workspace Sync
- **Ledge_Master folder** syncs between two machines: **Bond** (Mac Mini) and **DX**
- CLAUDE.md is the single source of truth regardless of which machine the session runs on
- Any session on either machine should read AND update this file

## Company
**Ledge Outdoors** — DTC outdoor gear brand
- Website: ledgeoutdoors.com
- Shopify store
- Also sells on Amazon

---

## Products

### Alaska Zero Degree King Size Sleeping Bag
- **Product URL:** `https://ledgeoutdoors.com/products/ledge-alaska-0-king-size-sleeping-bag-fits-4-adults-converts-to-2-bags-or-16ft-quilt`
- **Temperature rating:** 0 degrees
- **Size:** King size — 8 feet long, bigger than a queen mattress
- **Fits:** 4 adults
- **Converts to:** Two separate sleeping bags OR a 16-foot quilt (unzips both sides and extends full length)
- **Packing:** Compresses into a compact duffle bag (the "duffle bag holds a king size bed" hook)
- **Interior:** Real flannel inside
- **Price:** $199 (reduced from $229 as of March 29, 2026 — testing lower price point)
- **Shipping:** Free shipping
- **Key selling angles:**
  - Car camping / overlanding — fills a full-size truck bed
  - Family camping — fits 4 people
  - Versatility — 2 bags, 1 bag, or 16-foot quilt mode
  - Compression / portability — king size bed fits in a duffle
  - Cold weather capability — rated to 0 degrees

### Pulse Hydration
- Separate product line / brand under same umbrella
- Has its own Meta ad account: "Pulse Hydration (1314924...)"
- Pulse creators shipped: Hannah M., Nichol S., Antonio F., Dan S.
- Further product details TBD — Andrew to confirm

---

## Social Media Handles
- **Facebook Page:** Ledge Outdoors
- **Instagram:** @ledge_outdoor
- **TikTok:** @ledgeoutdoors (created March 2026)

---

## Tracking & Pixels

### Meta Pixel (Ledge Alaska)
- **Status:** Connected, firing on ledgeoutdoors.com
- **Ad account:** Runs under "Pulse Hydration" Meta ad account (1314924...) — both brands share the same Meta ad account

### TikTok Pixel (Ledge Alaska)
- **Pixel name:** Tik Tok Ledge Alaska
- **Pixel ID:** D6V033RC77U3AVTJ8D4G
- **Status:** Connected, receiving events (PageView, ViewContent, AddToCart, InitiateCheckout, CompletePayment)
- **Installation:** Via Shopify Customer Events (sandboxed iframe)
- **Events configured:** page_viewed, product_viewed, product_added_to_cart, checkout_started, checkout_completed
- **Note:** Old "801 TikTok Pixel" exists but is disconnected (was for Pulse)

### Shopify Customer Events Pixel Code (TikTok)
```javascript
!function (w, d, t) {
  w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie","holdConsent","revokeConsent","grantConsent"],ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e},ttq.load=function(e,n){var r="https://analytics.tiktok.com/i18n/pixel/events.js",o=n&&n.partner;ttq._i=ttq._i||{},ttq._i[e]=[],ttq._i[e]._u=r,ttq._t=ttq._t||{},ttq._t[e]=+new Date,ttq._o=ttq._o||{},ttq._o[e]=n||{};n=document.createElement("script");n.type="text/javascript",n.async=!0,n.src=r+"?sdkid="+e+"&lib="+t;e=document.getElementsByTagName("script")[0];e.parentNode.insertBefore(n,e)};
  ttq.load('D6V033RC77U3AVTJ8D4G');
  ttq.page();
}(window, document, 'ttq');

analytics.subscribe("page_viewed", (event) => {
  ttq.page();
});

analytics.subscribe("product_viewed", (event) => {
  ttq.track("ViewContent", {
    content_id: event.data?.productVariant?.id,
    content_name: event.data?.productVariant?.title,
    currency: event.data?.productVariant?.price?.currencyCode,
    value: event.data?.productVariant?.price?.amount
  });
});

analytics.subscribe("product_added_to_cart", (event) => {
  ttq.track("AddToCart", {
    content_id: event.data?.cartLine?.merchandise?.productVariant?.id,
    content_name: event.data?.cartLine?.merchandise?.productVariant?.title,
    currency: event.data?.cartLine?.merchandise?.productVariant?.price?.currencyCode,
    value: event.data?.cartLine?.merchandise?.productVariant?.price?.amount
  });
});

analytics.subscribe("checkout_started", (event) => {
  ttq.track("InitiateCheckout", {
    currency: event.data?.checkout?.currencyCode,
    value: event.data?.checkout?.totalPrice?.amount
  });
});

analytics.subscribe("checkout_completed", (event) => {
  ttq.track("CompletePayment", {
    currency: event.data?.checkout?.currencyCode,
    value: event.data?.checkout?.totalPrice?.amount
  });
});
```

---

## Live Ad Campaigns

### Meta — Alaska Check it Out (Awareness — April 17, 2026)
- **Status:** Active
- **Budget:** $2/day
- **Optimization:** Reach (Awareness)
- **Creative:** Existing Alaska UGC
- **URL:** Auto-apply ONLY5 + UTMs
- **Rationale:** Alaska awareness + organic search drove more sales than paid direct-response. $2/day keeps brand visible while Amazon handles conversions at $200 full price.

### Meta — Alaska 0 - go3 (April 12-17, 2026)
- **Status:** OFF (Paused April 17). $226.01 spent, 0 purchases.
- **Budget:** $25/day CBO
- **Optimization:** Website Purchase
- **Structure:** 1 campaign → 1 ad set → 5 ads (one per creator)
- **Creatives:** Rachel, Joe, Melanie, Vincent, Andrew (self-shot) — all Billo UGC + 1 self-shot
- **Advantage+ placements:** ON
- **Bid strategy:** Highest Volume
- **Multi-text testing:** 5 headlines × 5 primary texts × 5 descriptions
- **Targeting:** Broad
- **CTA:** Shop Now
- **Destination URLs (per creator, auto-apply ONLY5):**
  - Rachel: `https://ledgeoutdoors.com/discount/ONLY5?redirect=/products/ledge-alaska-0-king-size-sleeping-bag-fits-4-adults-converts-to-2-bags-or-16ft-quilt&utm_source=facebook&utm_medium=paid&utm_campaign=Alaska_Meta_1&utm_content=Rachel`
  - Vincent: `...&utm_content=Vincent`
  - Joe: `...&utm_content=Joe`
  - Melanie: `...&utm_content=Melanie`
  - AndrewP: `...&utm_content=AndrewP`
- **Multi-text copy bank:**
  - Primary V1: Hook-led ("This duffle bag holds a king size bed.")
  - Primary V2: Feature-led (direct specs)
  - Primary V3: Car camping / overlanding angle
  - Primary V4: Problem / solution angle
  - Primary V5: Urgency / offer-led ("50% off today")
  - Headlines: "A King Size Bed In a Duffle Bag" / "50% Off Today — Code ONLY5" / "Fits 4 Adults. Rated to 0°." / "The 16-Foot Quilt Sleeping Bag" / "8 Feet Long. Free Shipping."
  - Descriptions: "Code ONLY5 — 50% off today." / "Free shipping. Rated to 0°." / "Fits 4 adults. Real flannel." / "King size. Duffle sized." / "Half off today. Free ship."
- **Checkpoint rules:** $50 spent with 0 sales = pause and diagnose. $50 spent with 1+ sales = let ride to $150. Don't pull plug too early but don't bleed past $150 with 0 sales.
- **April 12 status:** $54.08 spent, 0 purchases, 1,522 impressions, 1,282 reach. CBO heavily favoring Andrew creative (61% of spend at $33.16). Decision: let it ride to $100 (~April 15-16) before pulling plug. If $100 with 0 sales = pause entire campaign and reassess landing page/price.

### Meta — Ledge Alaska 0° — UGC — Vincent (OLD)
- **Status:** TURNED OFF (April 12, 2026). $251.26 spent, 0 purchases. Dead.

### Meta — Ledge Alaska 0° — UGC — Rachel J. — Broad (OLD)
- **Status:** TURNED OFF (April 12, 2026). $373.76 spent, 1 purchase at $373.76 CPA ($199 sale from Kolin B., Buffalo MN). Rachel's creative is now running in Alaska 0 - go3 under CBO structure.

### Meta — New Awareness Campaign (OLD)
- **Status:** OFF. $10.67 spent, 6,133 reach. Previously drove first Alaska sale + abandoned cart. Left off to give go3 clean data; revisit later.

### Meta — Pulse Campaign Meta 1
- **Status:** Active (as of ~April 11, 2026)
- **Budget:** $25/day
- **Optimization:** Website Purchase
- **Creatives:** Pulse Dan, Pulse AndrewP, Pulse Hannah, Pulse Antonio, Pulse Nichol (5 ads under CBO)
- **Results (as of April 12):** 2 purchases, $57.49 spent, $28.75 avg CPA. Antonio has both purchases ($32.57 spent, $16.29 CPA, 1,046 reach). CBO correctly concentrating budget on Antonio (57% of spend). Nichol second at $12.89.
- **UTM fix (April 12):** Antonio's utm_content changed from V3_GrossBladder to "Antonio". Andrew's ad uses utm_content=AndrewP.
- **Sales:** Heather Hosker (Antonio, $16.01 CPA) + Nathan Rigney (Antonio, 4 units with ONLY5 50% off, $49.92 order, Haugan MT)
- **ONLY5 disabled on Pulse (April 12):** Nathan used ONLY5 (50% off) instead of BOGOTODAY (BOGO). ONLY5 now restricted to Alaska product only in Shopify.
- **"Message warning" badge:** Cosmetic only — WhatsApp Business verification not completed, requires API setup. Non-blocking, ignore.

### TikTok — Pulse Campaign Collage (renamed from Sales20260408222624)
- **Status:** Not delivering — out of campaign budget. TURN OFF.
- **Budget:** $30/day daily
- **Spend:** $100 total, 20,851 impressions, 182 clicks, 0.87% CTR, 0 conversions, 0 purchases.
- **Structure:** Smart Creative "Collage Videos" parent with AI_Editor_* and Pulse_Hydration_System-Narrated-* pool. TikTok auto-mixes into variants.
- **Verdict:** $100 spent, 0 sales. AI-remixed content gets 0.2-1.5% CTR vs Nichol's 10.99%. Dead campaign.

### TikTok — Pulse Videos ($5K lifetime campaign)
- **Status:** Active but all standalone ads are "Ended" or "Ad completed" — TikTok won't let paused ads restart in this campaign.
- **Spend:** $71.87 total. Nichol drove $68.62 of it (355 clicks, 10.99% CTR, $0.19 CPC).
- **Standalone creator ads:** Pulse Video Nichol (Ended), Pulse Video Dan (Ad completed), Pulse Video Hannah (Ad completed). All had URLs fixed with BOGOTODAY April 12, but TikTok killed the ad units when they were paused.
- **Fix:** Can't duplicate within this campaign — duplicates don't appear. Must create new campaign.

### TikTok — Nichol Standalone (NEW — April 12, 2026)
- **Status:** Active, just launched
- **Budget:** Daily (campaign-level)
- **Optimization:** Purchase
- **Creative:** Nichol's original video ONLY. Automate Creative OFF. No AI remixing.
- **Text:** "No more moldy bladders. This $25 hydration system stays clean, detachable, easy to rinse. Buy 1 get 1 FREE today. Code BOGOTODAY"
- **URL:** `https://pulsehydration.com/discount/BOGOTODAY?redirect=%2Fproducts%2Fpulse-hydration&utm_source=tiktok&utm_medium=paid&utm_campaign=__CAMPAIGN_NAME__&utm_content=Nichol&tt_campaignid=__CAMPAIGN_ID__&utm_id=__CAMPAIGN_ID__`
- **Rationale:** Nichol had 10.99% CTR at $0.19 CPC — best performer in entire TikTok account. Previous 0 sales were due to missing BOGOTODAY auto-apply URL (fixed). This is the conversion test.
- **Missing: Antonio's TikTok ad** — still needs creation (clone Nichol's setup, swap video, utm_content=Antonio).
- **TikTok handle mismatch:** Pulse ads showing under @ledgeoutdoors handle instead of a @pulsehydration handle (doesn't exist yet).
- **Account balance:** Prepaid via Venmo. Banner warning "estimated to run out in 7 days" as of April 12. Top up by April 18.

### TikTok — Alaska Ledge (OLD)
- **Status:** Active (from March 21, 2026)
- **Budget:** $25/day
- **Optimization:** Add to Cart (couldn't get Complete Payment/rebate to work)
- **Creative:** Rachel's 9:16 vertical UGC video
- **Targeting:** Automatic (broad), US, age 25-54
- **Attribution:** 7-day click, 1-day view
- **Rebate offer:** Could not activate ($350/5 conversions)
- **Phone verification:** Blocked — number "already in use"

### Combined Daily Spend
- **~$100/day total** across all active campaigns (Alaska go3 $25 + Pulse Meta 1 $25 + Pulse TikTok $25 + Alaska TikTok $25)

---

## Content & Creative Assets

### Raw Footage Shot (March 29, 2026 — Campsite & Park)

**Videos:**
- **IMG_1306.MOV** — 13 seconds, 1080p landscape. Andrew carrying the duffle bag out and setting it on a campsite picnic table.
- **IMG_1307.MOV** — 67 seconds, 1080p landscape. THE MONEY SHOT. Andrew carries duffle to picnic table, removes bag from duffle, removes webbing straps, unrolls the sleeping bag across the entire 8-foot picnic table, unfolds over the sides and across the benches. Campsite setting with stream and trees in background.
- **IMG_1321.MOV** — 13 seconds, 1080p landscape. At the park — unzipping both sides and pulling the Alaska from one end to the other, extending it out to 16 feet.

**Photos:**
- Truck bed shots — Alaska bag filling a full-size truck bed with measuring tape showing scale (strong car camping / overlanding content)
- Compression sack at campsite with Ledge Outdoors branding visible (good for product pages and Amazon)
- Park shots showing full spread on grass

### Edited TikTok Ad V3 / FINAL (March 29, 2026)
- **Format:** 9:16 vertical, 480x854, 35.6 seconds
- **Status:** READY TO UPLOAD
- **Hook:** "Watch what comes out of this bag!" (upper left, first frame)
- **Text placement:** Upper left/center — fixed from V1's bottom-right issue
- **Text overlays:** All bold, positioned in TikTok-safe zone
- **Scenes:** Campsite duffle → unroll on picnic table → truck bed shot → park 16ft quilt spread
- **End card:** Black screen with "ledgeoutdoors.com / $199.00 / Free Shipping"
- **Voiceover:** Dan Dan AI voice
- **Price change:** Updated to $199 (testing vs $229)
- **Improvements over V1:** Hook text added, text moved to upper third, text bigger/bolder, truck bed shot added, end card with price/URL/free shipping added

### Edited TikTok Ad V1 (March 29, 2026)
- **Format:** 9:16 vertical (correct for TikTok)
- **Length:** ~34 seconds
- **Flow:** Compact duffle on picnic table → pull bag out → unroll → reveal size → cut to park showing full spread → Andrew picking it up to show scale
- **Text overlays:** "The Alaska zero degree king size sleeping bag" / "Eight feet long. Bigger than a queen mattress" / "Fits four adults. Converts to two separate bags or a sixteen foot quilt"
- **Voiceover:** Dan Dan AI voice (added in revision)
- **Tool used:** CapCut (desktop)

### Voiceover Script (for CapCut Text-to-Speech)
```
"This fits in a duffle bag." (carry to table)
"The Alaska zero degree king size sleeping bag." (pull it out)
"Watch this." (start unrolling)
"Eight feet long. Bigger than a queen mattress." (extends across table)
"Fits four adults. Converts to two separate bags or a sixteen foot quilt." (hangs over sides)
"Two twenty nine at ledgeoutdoors dot com." (final wide shot)
```

---

## Creative Feedback & Optimization Notes

### TikTok Ad Best Practices (Applied)
- **Hook in first 1-2 seconds is critical** — TikTok gives you 2-3 seconds before scroll. Use: "This duffle bag holds a king size bed" or "Watch what comes out of this bag"
- **Text overlays must be in upper third** — Bottom 15-20% is covered by caption bar and engagement buttons on TikTok. Bold white text with black outline/shadow.
- **Make text bigger** — V1 text was too small and in the bottom right corner
- **Auto-captions are essential** — Most people scroll with sound off. TikTok ads with captions significantly outperform.
- **Raw/authentic > polished** — Product demos perform better on TikTok than overproduced content
- **Ideal length:** 30-35 seconds for product demo ads

### V2 Improvements Identified
- [ ] Add bold hook text in first 1-2 seconds
- [ ] Move text overlays up and make them larger
- [ ] Add truck bed shots as a 3-4 second closing sequence before end card
- [ ] Add "ledgeoutdoors.com" end card
- [ ] Consider trending audio track from CapCut music library

### Ad Angles to Produce
1. **Alaska Truck Bed / Car Camping** — Target overlanding communities (r/overlanding, r/truckcampers). Truck bed photos are strong standalone content.
2. **Alaska Size Reveal / Camping** — The unrolling on the picnic table is the core viral moment
3. **Alaska 16-Foot Quilt Mode** — The park footage showing full 16-foot extension
4. **Pulse In-Use** — TBD when footage is shot

---

## Active Creators / UGC

### Alaska Sleeping Bag Creators (4 from Billo + 1 self-shot)
- **Rachel** — Billo UGC. Currently running in Meta and TikTok campaigns. Drove the only full-price Alaska sale ($199, Kolin in Buffalo MN, attributed to Rachel J. Broad ad on Meta).
- **Vincent** — Billo UGC. Has had delivery issues / "Message warning" in Meta. $205 spent, 0 sales.
- **Joe** — Billo UGC. Ready to use, going into Alaska Meta 1 campaign.
- **Melanie** — Billo UGC. Ready to use, going into Alaska Meta 1 campaign.
- **Andrew (self-shot)** — March 29 footage at campsite and park (the duffle-to-picnic-table unroll, IMG_1306/1307/1321). Going into Alaska Meta 1 campaign.
- **InVideo "Duffle Bag Holds a King Size Bed"** — first generation completed but quality is poor ("looks like dog shit" per Andrew, April 11). Full review (April 12) confirmed 3 fatal flaws: (1) Ledge logo overlaps "Thi" of "This" breaking the hook text in frame 1, (2) 5 seconds of black screen mid-video (frames 5-9, ~20% of runtime), (3) end card has no price/URL/discount code and "LIMITED TIME ONLY" text is clipped. DO NOT UPLOAD. Concept is sound — execution failed. Recommendation: rebuild manually in CapCut from IMG_1307.mov raw footage instead of regenerating in InVideo.

### Pulse Hydration Creators
- **Hannah M.** — Billo UGC. TikTok standalone ad (Pulse Video Hannah, 9.28% CTR, currently OFF). URL fixed with BOGOTODAY April 12.
- **Nichol S.** — Billo UGC. TikTok standalone ad (Pulse Video Nichol, 10.99% CTR — highest in account, currently OFF). URL fixed with BOGOTODAY April 12. CHAMPION CANDIDATE — turn on first.
- **Antonio F.** — Billo UGC. Meta champion ($5.34 CPA, drove Heather Hosker sale). TikTok standalone ad MISSING — needs to be created.
- **Dan S.** — Billo UGC. TikTok standalone ad (Pulse Video Dan, 5.48% CTR, currently OFF). URL fixed with BOGOTODAY April 12.

---

## Advertising Platforms
- **Meta (Facebook/Instagram)** — Active: Alaska 0 - go3 ($25/day) + Pulse Campaign Meta 1 ($25/day)
- **TikTok** — Active: Nichol Standalone (Pulse, daily) + Alaska Ledge Rev 3 (reactivated April 12). Pulse Campaign Collage dead ($100 spent, 0 sales in dashboard but 1 delayed Shopify-attributed sale). Pulse Videos campaign has "Ended" ads.
- **Reddit** — ON STANDBY. No funds currently. ~$119 total spent, 1 confirmed sale (Donna Nguyen, Pulse, $24.96 — Reddit click ID found in landing page URL despite Shopify classifying as "direct").
- **Amazon** — Product listing optimization needed

---

## Tools & Workflow
- **Shopify** — E-commerce platform for ledgeoutdoors.com
- **CapCut Desktop** — Primary video editing tool. Use "Script to Video" for AI-assembled edits, or manual timeline editing for more control.
- **CapCut Text-to-Speech** — For AI voiceover (Dan Dan voice used on V1 revision)
- **CapCut Auto Captions** — For generating on-screen text from voiceover
- **Meta Ads Manager** — Campaign management (under Pulse Hydration ad account)
- **TikTok Ads Manager** — Campaign management (ads.tiktok.com, Ledge Outdoors account)
- **TikTok Events Manager** — Pixel/event management
- **HeyGen CLI** — AI avatar video generation (CLI + API, V3 as of April 2026). Potential use: talking-head hooks with AI avatars, cut in real product footage via CapCut. Not yet tested. Lower priority than real UGC creators which outperform AI content 5-10x on CTR in current data.

---

## Completed Fixes
- **"Shipping calculated at checkout" removed** — Changed to "Free shipping" in Shopify theme language editor (Products → Product → Shipping policy html). Was creating doubt at the buy decision point.
- **"Subscription/recurring purchase" text** — Confirmed hidden (display:none), built-in Shopify element, not visible to customers. No action needed.
- **TikTok Add to Cart inflation** — TikTok reports ~38 Add to Carts but Shopify shows ~1-2 actual carts. TikTok is overcounting via attribution model. Real conversion work needs to happen on the product page.

## Known Issues / Gotchas
- **TikTok UI** — Notoriously confusing. Events Manager, Ads Manager, Business Center, Shop Center, and Seller Center all open in separate windows. TikTok Shop setup is separate from TikTok Ads — don't go down the warehouse/shipping flow.
- **TikTok phone verification** — Andrew's phone number shows "already in use" (likely tied to another TikTok account). May need a different number or remove from other account first.
- **TikTok rebate ($350/5 conversions)** — Could not activate because Submit Form event requires a real purchase to fire first. Revisit once purchases are coming in.
- **TikTok prepaid billing** — Unlike Meta, TikTok requires prepaid balance. Currently funded via Venmo in $10 increments.
- **Shopify pixel sandbox** — TikTok's Event Builder can't detect the pixel because it's installed via Shopify's sandboxed Customer Events iframe. Manual setup / custom code is required.
- **Meta ad account shared** — Both Ledge Outdoors and Pulse Hydration run under the same Meta ad account.
- **Shopify store slugs** — Ledge Outdoors = `admin.shopify.com/store/801inc` (NOT "ledge-outdoors"). Pulse Hydration = `admin.shopify.com/store/pulsehydration-com`. Use store switcher in top-right dropdown to toggle between stores.

---

## Session History
- **Ledge Marketing 1 & 2** — (Stored under "Improve product sales on social media" session). Set up Meta and TikTok pixels on Shopify. Installed TikTok pixel via Customer Events with full event subscription code. Set up Meta Alaska R1 campaign ($25/day, Purchase optimization). Set up TikTok Alaska Ledge campaign ($25/day, Add to Cart optimization). Fought TikTok Events Manager extensively. Both campaigns went live ~March 21, 2026. Verified both pixels firing. TikTok started delivering; Meta had delayed charge activation.
- **Ledge Marketing 3** — March 29, 2026. Shot raw footage at campsite and park. Set up CapCut. Edited first TikTok ad (Alaska sleeping bag unroll). Added Dan Dan voiceover. Got creative feedback. Session ended with file upload size issues.
- **Ledge Marketing 4** — March 29, 2026. Created Ledge_Master folder on Desktop. Built this CLAUDE.md by pulling context from all prior sessions.
- **Ledge Marketing 5** — April 1-6, 2026. Diagnosed zero-sales problem (~$700+ spent, 1,900+ sessions). Installed Microsoft Clarity on both stores. Identified mobile dead space as major conversion killer (Dawn theme slider sizing to tallest of 16 images). Applied V2 aggressive CSS fix to both Ledge Outdoors and Pulse Hydration theme.liquid (forces 70vw height, object-fit:cover). Fixed announcement bar (Welcome10 → ONLY5). Set up 50% off test (code ONLY5). Attempted TikTok ad group duplication to switch optimization from Add to Cart → Purchase. Identified auto-apply discount links as next high-leverage fix. Pulse has 2 sales ($37.43) confirming checkout works — Alaska's zero sales is a price/presentation issue. Pulse TikTok campaign lifetime budget bumped to $5K after "out of budget" stall. Noted Pulse hero image should be swapped to product shot (currently lifestyle/in-use).
- **Ledge Marketing 6** — April 9, 2026. First Alaska sale! $199 full price from Facebook (Kolin B., Buffalo MN). Fixed Shopify auto-fulfillment (was under Settings → General). Shipped order. Swapped Pulse hero image to clean product shot. Created BOGO offer for Pulse (code BOGOTODAY) — better margin than 50% off ($10 profit vs $1). Created new Pulse TikTok campaign: 4 creator videos (Hannah, Nichol, Antonio, Dan), Purchase optimization, Highest Volume bidding, $25/day, auto-apply URL. Identified Meta has zero Pulse campaigns — next priority. Updated Alaska ad strategy: auto-apply ONLY5 discount links needed on all platforms. Reddit Alaska V1 still dead (1 impression). Created full action plan document. Total spend to date: ~$1,370 across all platforms, 3 total sales ($236.43).
- **Ledge Marketing 7** — April 11-12, 2026. Major session across both brands.
  - **Alaska Meta:** Built new "Alaska 0 - go3" campaign (CBO $25/day, 5 ads: Rachel/Joe/Melanie/Vincent/Andrew, multi-text 5×5×5, auto-apply ONLY5 URLs with per-creator UTMs). Published and approved April 12. Turned OFF old Vincent UGC ($251 spent, 0 sales) and Rachel Broad ($374 spent, 1 sale at $374 CPA). go3 is now the only active Alaska Meta campaign.
  - **Pulse Meta:** Pulse Campaign Meta 1 launched ~April 11. First Pulse Meta sale: Heather Hosker via Antonio at $5.34 CPA (April 12). Also got Steven Farley via Google organic. Antonio identified as champion creator; CBO favoring Antonio + Nichol. "Message warning" badge confirmed cosmetic (WhatsApp verification), non-blocking.
  - **Pulse TikTok:** Diagnosed 522 clicks → 0 sales smoking gun: standalone creator ads (Nichol/Hannah/Dan) had bare product page URL without BOGOTODAY auto-apply or UTMs. Andrew fixed all editable URLs. AI-created ad URLs are locked but inherit from Collage Videos parent which has correct URL. Antonio's TikTok ad is missing entirely — needs creation. Clarified TikTok ad structure: "Collage Videos" is a Smart Creative parent with AI_Editor pool; standalone "Pulse Video Nichol/Hannah/Dan" are separate ads, NOT media inside the Collage pool. Account balance warning: ~7 days remaining, top up by April 18.
  - **InVideo Alaska review:** Full frame-by-frame review of "Duffle Bag Holds a King Size Bed" InVideo file. Found 3 fatal flaws: broken hook (logo overlaps text), 5 seconds of black screen mid-video, useless end card (no price/URL/code, text clipped). Verdict: DO NOT UPLOAD. Recommendation: manual CapCut build from IMG_1307.mov raw footage.
  - **Zeely Pulse test:** Generated Zeely prompt/script for Pulse Hydration UGC-style video. AI hallucinated two-hose bite valve on product. Recommendation: use Zeely for talking-head only (no product in shot), cut in real product photos via CapCut.
  - **CLAUDE.md corrections:** Fixed Alaska creator names (was Brady/David, corrected to Joe/Melanie). Updated Pulse creator entries with TikTok ad status and CTR data.
  - **Total spend to date:** ~$1,750+ across all platforms. ~5 total sales.
- **Ledge Marketing 7 (continued)** — April 12, 2026 (afternoon session).
  - **3rd Pulse sale:** Nathan Rigney (Haugan MT), 4 units, $49.92 via Apple Pay. Attributed to Antonio on Meta (Pulse_Meta_1). UTM Content was V3_GrossBladder — fixed to "Antonio". Used ONLY5 code (50% off) instead of BOGOTODAY.
  - **ONLY5 restricted to Alaska only** in Shopify. Was active on Pulse, causing margin leakage.
  - **Meta Pulse Meta 1:** Now $57.49 spent, 2 purchases (both Antonio), $28.75 avg CPA. Campaign healthy.
  - **Alaska go3:** $54.08 spent, 0 purchases. Hit $50 checkpoint. Decision: let ride to $100 (4 more days). CBO favoring Andrew creative at 61% of spend.
  - **TikTok Pulse diagnosis:** Collage campaign ($100 spent, 0 sales) is dead. Standalone Nichol/Hannah/Dan ads show "Ended"/"Ad completed" — TikTok won't restart paused ads. Duplication within campaign doesn't work.
  - **Nichol TikTok standalone:** Created brand new campaign for Nichol. Nichol's original video only, Automate Creative OFF, BOGOTODAY URL + UTMs, BOGO ad text. Live as of April 12 evening.
  - **Total spend to date:** ~$1,860+ across all platforms. ~6 total sales.
- **Ledge Marketing 8** — April 13, 2026. Resolved Microsoft Clarity setup for Ledge Outdoors. Discovered "Ledge" project (w6sb7lckxq) had been stuck in Microsoft approval queue for 2 weeks since initial Shopify integration setup (~April 1). Completed Shopify install via "Install on Shopify" button — now live and detecting visitors. Duplicate "Ledge Outdoors" project (wb9i8fol7d) created manually exists under same account (andrew@801inc.com) — to be deleted. Pulse Clarity (w6sco44957) confirmed working separately. All 3 Clarity projects under same Microsoft account but Pulse + Ledge Outdoors not visible in project dropdown — likely org/workspace issue, non-blocking. Total spend to date: ~$1,960+ (running ~$100/day across active campaigns).
- **Ledge Marketing 9** — April 15, 2026. Full cross-platform performance audit via Chrome MCP (browser automation).
  - **Shopify store access resolved:** Discovered Ledge Outdoors Shopify store slug is `801inc` (NOT `ledge-outdoors` — that was causing permission errors). Pulse is `pulsehydration-com`. Store switcher found in top-right dropdown.
  - **Meta Ads pulled:** Alaska go3 at $219.72 spent, 0 Meta-attributed purchases. CBO still heavily favoring AndrewP creative (61% of spend). Pulse Meta 1 at $144.77, 6 purchases — AndrewP now champion (4 purchases, $17.71 CPA), overtaking Antonio (2 purchases, $20.20 CPA).
  - **TikTok Ads pulled:** Alaska_R_ at $481.36 total, 17 "conversions" (AddToCart, not purchases), 0 actual sales. TikTok balance at $101.06 with 7-day warning.
  - **Shopify order audit (both stores):** Pulled all Pulse orders (#1008-#1020) and Ledge orders. Checked conversion summary for attribution on each order.
  - **NEW ALASKA SALE FOUND:** Alexander Salazar, $99.50 (ONLY5 50% off), April 14, from Google search. Second ever Alaska sale. NOT attributed to Meta go3 — came from organic Google search. Shipping cost was $32.65 (FedEx, 22 lb bag).
  - **5 NEW PULSE SALES since April 12:** Brett Edwards ($49.90, unknown source), Franklin Carter ($24.95, Facebook), Dean Zarzuela ($24.95, Instagram), Brian Herrera ($24.95, Facebook), Mike Fleming ($24.95, Google).
  - **Reddit sale discovered:** Donna Nguyen (#1010, Apr 8, $24.96) had Reddit click ID (rdt_cid) in landing page URL. First ever Reddit-attributed sale. Shopify misclassified as "direct."
  - **Brian Dwyer sale discovered:** #1011, Apr 8, $49.90, Google, full price, 2 units. Not previously tracked.
  - **Total sales now:** 15 confirmed orders across both brands (~$700+ revenue). Total spend: ~$2,260+.
  - **Key decision needed:** Alaska go3 at $219 with 0 Meta-attributed sales. Past $100 checkpoint. But a $99.50 Alaska sale DID happen from Google — could be ad-driven awareness. Recommend: pause go3, keep budget for Pulse Meta 1 which is printing money at $24 CPA.
- **Ledge Marketing 10** — April 17, 2026. Full platform scan + strategic pivots.
  - **Strategic decisions made:** Paused ALL Alaska paid ads (Meta go3 + TikTok Rev 3). Switched Alaska to awareness-only ($2/day). Doubled Pulse Meta 1 budget from $25/day to $50/day. Reasoning: Alaska awareness + organic search more impactful than paid direct-response; 3 Amazon sales at $200 full price in same timeframe.
  - **Alaska "Check it Out" awareness campaign:** Published by Andrew at $2/day, Reach optimization, auto-apply ONLY5 + UTMs.
  - **Meta Ads (April 17):** Alaska go3 OFF at $226.01 spent, 0 purchases. Pulse Meta 1 at $202.02 spent, 6 Meta-attributed purchases, $33.67 avg CPA (rose from $24.13 after budget doubling — learning phase). AndrewP: 4 purchases/$26.26 CPA. Antonio: 2 purchases/$30.41 CPA.
  - **TikTok (April 17):** Alaska_R_ paused at $482.20. Nichol Reboot active but $0 spent (NOT DELIVERING — needs diagnosis). Pulse Campaign Collage STILL ON at $262.48 spent — flagged twice to Andrew, not yet killed. Pulse Videos + Pulse Videos H1 paused.
  - **3 NEW Pulse sales today (April 17):**
    - #1021 Dan Loranger — $24.95, BOGOTODAY, 2 items, **Facebook/paid, Antonio creative, Pulse_Meta_1** (UTM confirmed)
    - #1022 Ilia Ortiz Torres — $24.95, full price, 1 item, **TikTok/paid, Pulse Campaign Collage** (UTM confirmed — FIRST TikTok-attributed Pulse sale with proper UTM!)
    - #1023 John Huffman — $24.95, full price, 1 item, **Instagram** (Meta)
  - **No new Alaska Shopify orders.** 2 Alaska sales on Amazon at $200 full price (reported by Andrew, not in Shopify).
  - **Key finding:** Pulse Campaign Collage produced its first properly-attributed TikTok sale (#1022). At $262 spent / 2 Shopify-attributed sales = ~$131 CPA. Still expensive but TikTok IS converting.
  - **Total Pulse sales now:** 16 orders (~$475+ revenue). Total Alaska Shopify: still 2 orders + 3 Amazon.
  - **Total spend to date:** ~$2,460+ across all platforms.
  - **New project:** Andrew wants to build boobsareneat.com — charity merch store (hats, tshirts, stickers) raising money for a cause.
- **Ledge Marketing 11** — April 18, 2026. Continued from session 10.
  - **Pulse JS error fixed:** Diagnosed and fixed the `searchModal.close` null reference error that was hitting 38% of Pulse sessions in Microsoft Clarity. Bug was in compiled `scripts.js` (Ride theme) — `closeSearchModal()` method calls `this.header.querySelector("details-modal")` which returns null because Pulse has no search in the header. Fix: monkey-patch script added to theme.liquid just before `</body>` that overrides `closeSearchModal` with a null-safe version. Verified working — method no longer throws when called.
  - **Pulse_AndrewP_TikTok campaign built:** New TikTok campaign ($25/day) with Andrew's moldy bladder hook video. Single video format, Automate Creative OFF, BOGOTODAY auto-apply URL with UTMs. Now the ONLY active TikTok campaign.
  - **Pulse Campaign Collage killed:** Finally turned off ($262.48 spent, 2 sales, ~$131 CPA).
  - **TikTok balance topped up:** +$200 added.

---

## Completed Fixes (Ledge Marketing 11 — April 18, 2026)
- [x] Diagnosed searchModal.close JS error on Pulse (38% of Clarity sessions). Root cause: Ride theme's `closeSearchModal()` in compiled `scripts.js` queries for `<details-modal>` element that doesn't exist (search disabled in header). Fix: monkey-patch script added to theme.liquid before `</body>` adds null check. Confirmed working — calling `closeSearchModal()` no longer throws.
- [x] Built new Pulse_AndrewP_TikTok campaign ($25/day, single video, BOGOTODAY auto-apply, no AI remixing). Now the ONLY active TikTok campaign.
- [x] Killed Pulse Campaign Collage on TikTok ($262.48 spent, 2 sales, ~$131 CPA)
- [x] Topped up TikTok balance +$200

## Completed Fixes (Ledge Marketing 10 — April 17, 2026)
- [x] Paused Alaska go3 on Meta ($226.01 spent, 0 purchases)
- [x] Paused Alaska TikTok Rev 3 ($482.20 spent, 0 purchase results)
- [x] Published Alaska "Check it Out" awareness campaign ($2/day, Reach optimization)
- [x] Doubled Pulse Meta 1 budget from $25/day to $50/day
- [x] Pulled attribution on all 3 new Pulse orders (#1021-#1023)
- [x] Confirmed first TikTok-attributed Pulse sale (#1022, Pulse Campaign Collage)

## Completed Fixes (Ledge Marketing 7 — April 12, 2026)
- [x] Alaska Meta: built and published "Alaska 0 - go3" campaign (CBO $25/day, 5 creators, multi-text 5×5×5, ONLY5 auto-apply URLs with per-creator UTMs)
- [x] Alaska Meta: turned off old Vincent UGC ($251 spent, 0 sales) and Rachel Broad ($374 spent, 1 sale at $374 CPA)
- [x] Pulse TikTok: fixed standalone creator ad URLs with BOGOTODAY auto-apply + UTMs (was bare product page — smoking gun for 0 sales)
- [x] Pulse Meta: launched Pulse Campaign Meta 1, got first sale (Antonio, $5.34 CPA)
- [x] InVideo Alaska: completed frame-by-frame review, identified 3 fatal flaws, verdict = DO NOT UPLOAD
- [x] CLAUDE.md: corrected Alaska creator names (Joe/Melanie, not Brady/David), updated Pulse creator entries with TikTok status/CTR
- [x] Zeely Pulse: generated prompt/script, identified AI hallucination issue (two-hose bite valve), pivoted to hybrid workflow recommendation

## Completed Fixes (Ledge Marketing 5)
- [x] Mobile dead space CSS fix V2 applied to Ledge Outdoors theme.liquid
- [x] Mobile dead space CSS fix V2 applied to Pulse Hydration theme.liquid
- [x] Announcement bar updated from "Welcome10" to "Use code ONLY5 for 50% off"
- [x] Microsoft Clarity installed on both stores (Pulse: w6sco44957 working since April 1. Ledge: w6sb7lckxq connected via Shopify integration April 13, was stuck in "waiting for approval" for 2 weeks)
- [x] Meta Awareness campaign — KEEP RUNNING. First Alaska sale ($199, full price) attributed to Facebook. Abandoned cart also from awareness. $2/day is strong ROAS.
- [x] Shopify auto-fulfillment turned off (was under Settings → General). Orders no longer auto-fulfill/archive.
- [x] Pulse TikTok campaign lifetime budget increased to $5,000
- [x] Pulse hero image swapped to clean product shot on white background
- [x] Pulse BOGO discount created (code: BOGOTODAY) — Buy 1 Get 1 Free
- [x] New Pulse TikTok campaign created: 4 creator videos, Purchase optimization, $25/day, Highest Volume bidding
- [x] Auto-apply URL for Pulse: https://pulsehydration.com/discount/BOGOTODAY?redirect=/products/pulse-hydration

---

## Performance Data (as of April 17, 2026)

### Meta — ~$1,230+ total spent (all-time, both brands)
- **Alaska 0 - go3:** OFF. $226.01 total spent, 0 purchases. Paused April 17.
- **Alaska Check it Out (Awareness):** Active, $2/day, Reach optimization. ~$12.77 spent, 7,644 reach as of April 17.
- **Pulse Campaign Meta 1:** $202.02 spent, **6 Meta-attributed purchases** (but 8+ Shopify-attributed from Facebook/Instagram), $33.67 avg CPA in Meta (rose from $24.13 after budget doubling to $50/day — possible learning phase). **AndrewP still champion** with 4 purchases/$26.26 CPA. Antonio: 2 purchases/$30.41 CPA.
- **Ledge Alaska 0° — Vincent (OLD):** $251.26 spent, 0 purchases. OFF.
- **Ledge Alaska 0° — Rachel Broad (OLD):** $373.76 spent, 1 purchase ($373.76 CPA). OFF.
- **Awareness Campaign (OLD):** $10.67 spent. OFF.
- **Key concern:** Pulse Meta 1 CPA rose after budget doubling. No new Meta-attributed purchases in the 2 days after increase ($57 additional spend). Could be learning phase — monitor closely.

### TikTok — Pulse — ~$334+ total spent (all Pulse TikTok campaigns)
- **Pulse Campaign Collage:** $262.48 spent, STILL RUNNING (needs to be killed). **BUT produced first properly-attributed TikTok sale** (#1022 Ilia Ortiz Torres, $24.95, April 17). Plus 1 earlier delayed Shopify-attributed sale. ~$131 CPA across 2 sales. Expensive but TikTok IS converting.
- **Pulse Videos ($5K lifetime):** $71.87 spent. Paused. All standalone ads ended.
- **Nichol Reboot (April 17):** Active but NOT DELIVERING — $0 spent. Needs diagnosis (ad review? bid? audience? balance?).
- **Antonio's TikTok ad:** Still MISSING — needs creation.
- **TikTok balance:** ~$101 remaining. 7-day warning. **Top up TODAY (April 17) or tomorrow at latest.**

### TikTok — Alaska — ~$482+ total spent (all Alaska TikTok campaigns)
- **Alaska_R_ (Rev 3):** PAUSED at $482.20. 0 actual purchase results ever.
- **All other Alaska TikTok campaigns:** OFF. Dead.
- **Zero actual Alaska TikTok sales ever.**

### Reddit — ~$119 total spent (ON STANDBY — 1 CONFIRMED SALE)
- **1 CONFIRMED SALE:** Donna Nguyen (Pulse, $24.96, Apr 8) — Reddit click ID confirmed.
- **Status:** All campaigns paused/standby. No budget allocated.

### Overall Numbers
- **Total all-time spend:** ~$2,460+ across all platforms
- **Current daily spend:** ~$52/day (Pulse Meta 1 $50/day + Alaska Awareness $2/day)
- **Shopify store slugs:** Ledge Outdoors = `801inc`, Pulse Hydration = `pulsehydration-com`
- **Total Pulse sales (2026, Shopify confirmed):** 16 orders, ~$475+ revenue
  - #1008 Patrick Pritchett — $12.48, Apr 2 (source TBD)
  - #1009 Donna Jennings — $12.48, Apr 5 (source TBD)
  - #1010 Donna Nguyen — $24.96, Apr 8, **Reddit** (rdt_cid confirmed), ONLY5, 2 items
  - #1011 Brian Dwyer — $49.90, Apr 8, **Google**, full price, 2 items
  - #1012 Steven Farley — $24.95, Apr 11, **Google organic**
  - #1013 Heather Hosker — $24.95, Apr 11, **Meta/Antonio**
  - #1014 Nathan Rigney — $49.92, Apr 13, **Meta/Antonio**, ONLY5, 4 items
  - #1015 Colton Wrisner — $24.95, Apr 13, **Direct**, full price
  - #1016 Brett Edwards — $49.90, Apr 13, **Unknown source**, BOGOTODAY, 3 items
  - #1017 Franklin Carter — $24.95, Apr 14, **Facebook**, BOGOTODAY, 2 items
  - #1018 Dean Zarzuela — $24.95, Apr 14, **Instagram**, BOGOTODAY, 2 items
  - #1019 Brian Herrera — $24.95, Apr 15, **Facebook**, full price, 1 item
  - #1020 Mike Fleming — $24.95, Apr 15, **Google**, full price, 1 item
  - #1021 Dan Loranger — $24.95, Apr 17, **Facebook/Antonio** (Pulse_Meta_1 UTM), BOGOTODAY, 2 items
  - #1022 Ilia Ortiz Torres — $24.95, Apr 17, **TikTok/Pulse Campaign Collage** (UTM confirmed), full price, 1 item
  - #1023 John Huffman — $24.95, Apr 17, **Instagram**, full price, 1 item
- **Total Alaska sales (2026, Shopify confirmed):** 2 orders + 3 Amazon
  - #20011019 Kolin Brierton — $199.00, Apr 6, **Facebook/Rachel** (full price)
  - #20011020 Alexander Salazar — $99.50, Apr 14, **Google**, ONLY5, 1 item
  - + 3 Amazon sales at ~$200 each (reported by Andrew April 17, not in Shopify)
- **Key insights:**
  - **Meta is the #1 paid driver** for Pulse. Facebook/Instagram = 8+ attributed Pulse sales. Antonio and AndrewP are champion creatives.
  - **Google organic/search is the #2 source** across BOTH brands (3 Pulse + 1 Alaska = 4 sales). Paid ads driving search behavior.
  - **TikTok produced its first properly-attributed sale** (#1022 via Pulse Campaign Collage). TikTok CAN convert — but at ~$131 CPA vs Meta's ~$34 CPA, it's 4x more expensive.
  - **Reddit produced a sale** despite being on standby — consider reactivating when budget allows.
  - **Alaska sells better on Amazon** ($200 full price, 3 sales) than Shopify ($199 + $99.50, 2 sales). Consider Amazon-first strategy for Alaska.
  - **BOGOTODAY is working** — 5+ orders used it. Customers are using the code.
  - **Pulse shipping cost is low** (~$5-7/order). Alaska shipping is HIGH ($32.65 for the 22 lb bag).
  - **Daily spend cut from ~$100/day to ~$52/day** by pausing Alaska paid ads. More efficient allocation.

---

## Active Tests (April 1, 2026)
- **50% off flash sale** — Alaska at ~$99, Pulse at ~$12.50. Codes: "only5" / "ONLY5". Limited to first 5 buyers. Testing whether checkout funnel works and whether price is the barrier.
- **Hero images updated** — Both product pages now show 50% off code prominently on main image
- **Free shipping text fixed** — Changed from "Shipping calculated at checkout" to "FREE SHIPPING" on product pages

---

## Next Steps / Open Items

### PRIORITY — Do First Next Session
- [x] ~~Pause Alaska go3 on Meta~~ — DONE April 17. $226.01 spent, 0 purchases.
- [x] ~~Pause Alaska TikTok Rev 3~~ — DONE April 17. $482.20 spent, 0 purchases.
- [x] ~~Scale Pulse Meta 1 to $50/day~~ — DONE April 17.
- [x] ~~Launch Alaska awareness campaign~~ — DONE April 17. "Alaska Check it Out" at $2/day.
- [ ] **URGENT: Turn OFF Pulse Campaign Collage on TikTok.** $262.48 spent. Produced 1 TikTok sale (#1022) but CPA is ~$131. Kill it before it burns more. (Flagged 3x now.)
- [ ] **URGENT: Top up TikTok prepaid balance.** $101 remaining, 7-day warning. Load $50-100 TODAY or ads stop.
- [ ] **Diagnose Nichol Reboot TikTok:** Active but $0 spent, not delivering. Check: ad review status, bid settings, audience, balance.
- [ ] Create Antonio's TikTok standalone ad (clone Nichol's setup, swap video, utm_content=Antonio).
- [ ] **Monitor Pulse Meta 1 CPA closely.** Rose from $24 to $34 after budget doubling. If CPA stays above $30 after 3 more days, consider dropping back to $35/day.
- [ ] **Build boobsareneat.com store** — New Shopify store for charity merch (hats, tshirts, stickers). Andrew has the domain. Plan: set up store, design products, apply ad learnings from Pulse/Alaska.

### High Priority
- [ ] Review Clarity session recordings (data collecting since April 1 on Pulse, April 13 on Ledge)
- [x] Fix JavaScript searchmodal.close null error on Pulse — FIXED April 18. Root cause: `closeSearchModal()` in compiled `scripts.js` calls `this.header.querySelector("details-modal")` which returns null (no search in header). Fix: monkey-patch in theme.liquid adds null check before `.close()`. Confirmed working.
- [ ] Do a test purchase on both stores to fire CompletePayment pixel events
- [ ] Investigate Alaska shipping cost problem — $32.65 to ship (22 lb bag via FedEx). Consider: Amazon FBA for Alaska (already selling 3 units there at $200), keep Shopify for Pulse.
- [ ] Build manual CapCut Alaska ad from IMG_1307.mov raw footage for awareness campaign creative refresh
- [ ] Set up API tokens for Meta Graph API + TikTok Marketing API

### Medium Priority
- [ ] Set up retargeting campaigns on Meta (Custom Audiences from website visitors)
- [ ] Consider reactivating Reddit with small budget — produced a confirmed sale despite being on standby
- [ ] Create @pulsehydration TikTok handle (brand mismatch with @ledgeoutdoors)
- [ ] Build email capture / nurture sequence
- [ ] Create separate truck bed / car camping ad targeting overlanding audiences
- [ ] Explore Amazon advertising for Alaska (already selling well organically there)

### Backlog
- [ ] Amazon listing optimization for Alaska sleeping bag
- [ ] Fix TikTok phone verification
- [ ] Revisit TikTok rebate once CompletePayment events are firing
- [ ] Fix Vincent's Reddit ad (Alaska_V1 — not delivering)
- [ ] Regenerate or manually rebuild InVideo Alaska ad
- [ ] Delete duplicate "Ledge Outdoors" Clarity project (wb9i8fol7d)
