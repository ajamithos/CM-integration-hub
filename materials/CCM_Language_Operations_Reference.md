# CCM Language & Operations Reference Brief

**Version:** 1.0 | **Purpose:** Ground all training materials and CM-facing content in operational reality

---

## How Work Gets Named

Work is **always** referenced by: **Title + Product/Placement**  
Work is **never** referenced by: Buy type alone

**Examples:** "the Tron FR" · "the Deliver Me ETP" · "the Predator Pause Ad" · "the Fan Four HE" · "the Roses HE"

---

## Common Placement Abbreviations

| Abbreviation | Meaning |
|---|---|
| FR | Feature Rotator |
| ETP | Enhanced Title Page |
| PTP / PTP+ | Premium Title Page / Plus |
| FITO | First Impression Takeover |
| SOV | Share of Voice |
| ROS | Run of Site |
| PVA | Prime Video Ads |
| ILB | Inline Banner |
| CSU | Campaign Setup |
| CSIO | Campaign Setup + IO processing |
| IO | Insertion Order |
| MPT | Media Plan Tool |
| PTS | Push to Sold |
| MG | Makegood |
| UD | Under-delivery |
| DIF | Deliver in Full |

---

## Key Systems

| System | What It's For | How It's Referenced |
|---|---|---|
| **Salesforce (SF)** | Assignment management, campaign records, IO/MPT storage | "the SF link," "SF opp," "open a CSU in SF" |
| **Rodeo** | DSP trafficking execution platform | "in Rodeo," "push to Rodeo," "live in Rodeo" |
| **OMS** | Order management, inventory booking | "update OMS," "book in OMS" |
| **MPT** | Media plan (Google Sheets/Excel) | "the MPT," "updated MPT" |
| **Prisma / MediaOcean** | IO management and processing | "process the IO," "Prisma link" |
| **Matrix** | Campaign tracking spreadsheet | "the matrix," "production matrix" |
| **SIM / APTIX** | Issue ticketing system | "open a SIM," "APTIX link" |

⚠️ **Critical:** Assignments live in **Salesforce**, not Rodeo. Rodeo is where you **execute**.  
⚠️ **Critical:** Do not edit OMS/Rodeo during an active AdOps optimization — this can cause defects.

---

## Assignment Types (in Salesforce)

- **Trafficking assignment** — Standard execution. Has child assignments (Internal QA, TOV Verification) that are NOT self-QA'd. Only the parent is self-QA'd.
- **CM Task** — Pilot assignment type. CCM opens it; CM executes it.
- **CSU / CSU optimization** — Campaign setup. AEs request with SF opp link, MPT, and IO.
- **Pre-launch optimization** — Product transitions (e.g., Pause Ads GA).
- **Re-trafficking** — Post-launch creative or date changes.

---

## PTS = Push to Sold

Campaigns are **not live** until PTS. This is a critical milestone tracked actively by the pod.

---

## How Work Gets Handed Off

**Real flow:** AE → CCM → CM

- **AE sends:** MPT/IO packages with SF opp links, Prisma links, specific asks
- **CCM opens:** Assignment in Salesforce, Slacks CM with the link
- **Stage 1/2:** CCM actively hands off assignments
- **Stage 3:** CM monitors their own queue; CCM communication is a heads-up, not a handoff

---

## Client Communication Roles

| Role | Responsibility |
|---|---|
| **AE** | Communicates directly with client/agency constantly (IOs, negotiations, preferences) |
| **CCM** | Strategic lead on ALL advertiser communications. Owns creative and launch-related client comms. |
| **CM** | No default client-facing responsibilities. Stage 3 CMs *may* own go-live confirmations and tag receipts — mutual decision with CCM. |

---

## Communication Style

**Urgency signals:** :alert: or :boom: = immediate action needed  
**Time anchors:** "goes live tonight," "launching in 8 days," "ASAP today"  
**Acknowledgment:** Emoji-only is standard (✅ 👀 🫡) — full sentences not required for receipt

**CM Best Practices:**
- Make suggestions and present feasible options — do not state things as fact
- Frame as: "Here's what I'm seeing — does this make sense?"
- Always loop in CCM before acting on anything client-adjacent
- Proactively communicate blockers to the Account Team
- "Blocked - CCM" is a last resort status

---

## Excluded from CM Partner Queue

- High Traffic Event Campaigns
- H1 SOV
- Homepage takeovers
- Amazon Managed & Self-Service campaigns

## Standard SLA

- Trafficking and Optimization: **1 business day** (same day when applicable)
- Up to 2 days during quarter turn / high traffic periods
