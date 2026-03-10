"""
CM Integration Hub
========================
A self-contained reference and integration tool for Campaign Managers
from Stage 1 through Stage 3 under Model 2.

Built for local execution. No external servers. No databases.
Each CM runs their own copy on their own machine.

Language: English / Español (toggle in sidebar)
"""

import streamlit as st
import json
import os
from datetime import datetime, date
from pathlib import Path

# Detect if running on Streamlit Cloud vs. locally
IS_HOSTED = os.environ.get("STREAMLIT_SERVER_HEADLESS") == "true" or os.path.exists("/mount/src")

# ============================================================
# CONFIGURATION
# ============================================================

APP_TITLE = "CM Integration Hub"
APP_ICON = "🎯"
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

# Ask Zoyla — QuickSight Q chat agent embed URL.
# This is the direct agent link — bypasses the QuickSight sign-in page.
ASK_ZOYLA_URL = "https://us-east-1.quicksight.aws.amazon.com/sn/account/amazonbi/embed/share/accounts/764946308314/chatagents/d3547501-7a09-453c-bfda-c769e97d0e61"

# Navigation page definitions — key, icon, English label, Spanish label
NAV_PAGES = [
    ("home",       "🏠", "Dashboard",                     "Panel"),
    ("campaign",   "📋", "Navigating Campaign R&Rs",      "Navegando R&Rs de Campaña"),
    ("priority",   "⚡", "Prioritization",                "Priorización"),
    ("comms",      "💬", "Communication Tree",            "Árbol de Comunicación"),
    ("scenarios",  "🎯", "Scenario Practice",             "Práctica de Escenarios"),
    ("confidence", "📊", "Confidence Check",              "Control de Confianza"),
    ("notes",      "📝", "My Notebook",                    "Mi Cuaderno"),
    ("docs",       "📄", "Reference Documents",           "Documentos de Referencia"),
    ("progress",   "📈", "Progress Report",               "Informe de Progreso"),
]

# ============================================================
# LANGUAGE DICTIONARY
# ============================================================
# NOTE TO SJO TEAM: Review all Spanish ("es") translations below.
# AdOps-specific terms (trafficking, CCM, OMS, Rodeo, DSP, etc.)
# have been kept in English where that is the standard usage.
# Adjust any translations that do not match how your team speaks.
# ============================================================

LANG = {
    "en": {
        # -- Sidebar --
        "sidebar_language": "🌐 Language / Idioma",
        "sidebar_alias_label": "Your alias",
        "sidebar_alias_help": "Enter your Amazon alias (e.g., dcampos)",
        "sidebar_welcome": "Welcome, **{}**",
        # -- Home --
        "home_title": "CM Integration Hub",
        "home_tagline": "Everything you need to work with clarity, consistency, and confidence — in one place.",
        "home_footer": "Built for CMs in Model 2. Your reference from Stage 1 through Stage 3.",
        # -- Campaign Navigation --
         "cn_title": "Navigating Campaign R&Rs",
        "cn_subtitle": "Your reference for knowing when to act independently and when to check in.",
        "cn_ask_title": "🔵 ASK",
        "cn_ask_when": "**When to Ask**",
        "cn_ask_items": [
            "First time encountering an assignment type",
            "Client-facing decisions or communications",
            "Anything involving budget changes or flight modifications",
            "When instructions are ambiguous or incomplete",
            "When a creative asset does not match what the assignment describes",
            "When you are unsure about an advertiser's specific preferences or history"
        ],
        "cn_ask_who": "**Who to ask**: Your CCM first. If they are unavailable and it is time-sensitive, your AdOps mentor or M1.",
        "cn_attempt_title": "🟢 ATTEMPT",
        "cn_attempt_when": "**When to Attempt**",
        "cn_attempt_items": [
            "Assignment types you have completed before with QA approval",
            "Standard trafficking for DSP, Devices, STV, PVa",
            "Optimizations you have executed previously on this account",
            "CSU assignments that follow established patterns",
            "Updating the weekly tracker or shared production matrix",
            "Routine Slack updates to your CCM on assignment status"
        ],
        "cn_attempt_who": "**Then confirm**: Let your CCM know what you did. Stage 1 = CCM does QA. Stage 2 = CCM reviews. Stage 3 = you own it.",
        "cn_escalate_title": "🔴 ESCALATE",
        "cn_escalate_when": "**When to Escalate**",
        "cn_escalate_items": [
            "You have been blocked for 15+ minutes with no clear path forward",
            "A campaign is at risk of missing its launch date",
            "A client-facing error has occurred or may occur",
            "An SLA is at risk and you cannot resolve the blocker yourself",
            "You discover a discrepancy between OMS and Rodeo that affects delivery",
            "Your CCM is unavailable and the issue cannot wait"
        ],
        "cn_escalate_who": "**Escalate to**: Your CCM (first), then M1 or Account Team lead if CCM is unavailable.",
        "cn_15min_title": "⏱️ The 15-Minute Rule",
        "cn_15min_body": "If you have been stuck for 15 minutes without progress, stop trying to solve it alone. Reach out. This is not a sign of weakness — it is how partnerships work. Your CCM would rather hear from you at 15 minutes than discover a missed SLA at hour 3.",
        "cn_guardrails_title": "🚧 Guardrails — Never Do Without Checking",
        "cn_guardrails_items": [
            "Never modify flight dates without CCM confirmation",
            "Never send client-facing communications without CCM alignment (Stage 1-2)",
            "Never submit a trafficking assignment for a campaign type you have not done before without QA",
            "Never change budget allocations without explicit direction",
            "Never use 'Blocked - CCM' status without first attempting to resolve directly"
        ],
        # -- Campaign Nav: Stage-aware content --
        "cn_stage_header": "📍 You are in: **{}**",
        "cn_stage_change": "Change your stage in the sidebar.",
        "cn_stage1_focus": "Building trust and establishing communication patterns. Your CCM is your primary guide.",
        "cn_stage2_focus": "You are opening and executing assignments independently. Your CCM provides QA and strategic guidance.",
        "cn_stage3_focus": "You own your workflows end-to-end. Your partnership with your CCM is collaborative and strategic — not supervisory.",
        "cn_ask_items_s1": [
            "First time encountering an assignment type",
            "Client-facing decisions or communications",
            "Anything involving budget changes or flight modifications",
            "When instructions are ambiguous or incomplete",
            "When a creative asset does not match what the assignment describes",
            "When you are unsure about an advertiser's specific preferences or history",
        ],
        "cn_ask_items_s2": [
            "New assignment types you have not done independently yet",
            "Client-facing decisions or direct advertiser communications",
            "Budget changes, flight modifications, or inventory adjustments",
            "When instructions are ambiguous and you cannot resolve with the SOP or wiki",
            "When you are unsure about an advertiser's specific history or preferences",
        ],
        "cn_ask_items_s3": [
            "A genuinely new situation you have not encountered before — novel products, edge cases, unique client requests",
            "Strategic decisions with direct client or revenue impact",
            "Cross-account dependencies or conflicts that need alignment",
            "Situations where the SOP is silent or contradictory",
        ],
        "cn_ask_who_s1": "**Who to ask**: Your CCM first. If they are unavailable and it is time-sensitive, your AdOps mentor or M1.",
        "cn_ask_who_s2": "**Who to ask**: Your CCM for strategic or client-facing decisions. For execution questions, check the SOP first — then your CCM or Account Team.",
        "cn_ask_who_s3": "**Who to ask**: Your Account Team, M1, or CCM — whoever has the context. You decide who to loop in.",
        "cn_attempt_items_s1": [
            "Assignment types you have completed before with QA approval",
            "Standard trafficking for DSP, Devices, STV, PVa",
            "Optimizations you have executed previously on this account",
            "CSU assignments that follow established patterns",
            "Updating the weekly tracker or shared production matrix",
            "Routine Slack updates on assignment status",
        ],
        "cn_attempt_items_s2": [
            "All assignment types you have done before — execute independently",
            "Standard trafficking, optimizations, and CSU workflows",
            "Routine account team communications about status and timelines",
            "Troubleshooting delivery or creative issues using the SOP and wiki",
            "Proactively flagging potential issues to Account Team",
        ],
        "cn_attempt_items_s3": [
            "All assignments within your workflow scope — CSU, Optimization, Trafficking",
            "Self-QA all your own work before submission",
            "Account team communications related to your workflow — go-live confirmations, tag receipt, delivery updates",
            "Troubleshooting and resolving delivery issues end-to-end",
            "Coaching teammates on workflows, workarounds, and best practices",
            "Proactively tracking upcoming launches and live order health",
        ],
        "cn_attempt_who_s1": "**Then confirm**: Let your CCM know what you did. Your CCM will QA.",
        "cn_attempt_who_s2": "**Then confirm**: Your CCM reviews high-stakes work. Routine execution is yours.",
        "cn_attempt_who_s3": "**You own it.** Execute, QA, and communicate autonomously. Loop in your partner when strategic alignment is needed.",
        "cn_escalate_items_s1": [
            "You have been blocked for 15+ minutes with no clear path forward",
            "A campaign is at risk of missing its launch date",
            "A client-facing error has occurred or may occur",
            "An SLA is at risk and you cannot resolve the blocker yourself",
            "You discover a discrepancy between OMS and Rodeo that affects delivery",
            "Your CCM is unavailable and the issue cannot wait",
        ],
        "cn_escalate_items_s2": [
            "You have been blocked for 15+ minutes with no clear path forward",
            "A campaign is at risk of missing its launch date or SLA",
            "A client-facing error has occurred or may occur",
            "A discrepancy between OMS and Rodeo that you cannot resolve",
            "Your CCM is unavailable and the issue is time-sensitive",
        ],
        "cn_escalate_items_s3": [
            "A campaign is at risk and you cannot resolve it independently",
            "A client-facing error with material impact has occurred",
            "An issue requires cross-account or cross-team coordination beyond your scope",
            "A decision needs M1 or leadership visibility due to revenue or relationship risk",
        ],
        "cn_escalate_who_s1": "**Escalate to**: Your CCM (first), then M1 or Account Team lead if CCM is unavailable.",
        "cn_escalate_who_s2": "**Escalate to**: Your CCM for client impact. M1 or Account Team lead if CCM is unavailable.",
        "cn_escalate_who_s3": "**Escalate to**: Whoever has the authority to resolve it — M1, Account Team lead, or your CCM partner.",
        "cn_guardrails_s3": [
            "Never modify flight dates without confirming the downstream impact on delivery and pacing",
            "Never submit work without self-QA — you are your own quality gate",
            "Never change budget allocations without explicit direction from Account Team or AM",
            "Never take on cross-account work without confirming bandwidth and visibility with your partner",
        ],
        "cn_sop_title": "📋 SOP by Stage of Integration",
        "cn_sop_source": "From the [US-SJO Workflow SOP — Model 2](https://w.amazon.com/bin/view/Users/ajamitho/CM-UAT-Test/)",
        "cn_sop_duration": "**Duration:** Roughly 2–3 weeks — the CM will dictate based on confidence level",
        "cn_sop_s1_focus": "**Focus:** Building trust and establishing communication patterns.",
        "cn_sop_s2_focus": "**Focus:** CMs begin opening and executing assignments independently while CCMs continue to guide and QA.",
        "cn_sop_s3_focus": "**Focus:** CMs assume ownership of their workflows. Both partners should be engaging in projects or initiatives together.",
        "cn_sop_s3_note": "**To be clear:** This is an **equal and collaborative partnership** — CMs are not 'assistants' to CCMs, just as CCMs are not 'assistants' to AEs. We work together, always.",
        "cn_sop_ccm_title": "#### CCM Responsibilities",
        "cn_sop_cm_title": "#### CM Responsibilities",
        "cn_sop_s3_practice_title": "#### What This Looks Like in Practice",
        "cn_sop_s1_ccm": "- Schedule initial introduction call with CM\n- Align on **daily cadence** — 30–60 min block each morning and afternoon is highly recommended\n- Add CM to relevant account team chats and weekly syncs\n- Introduce CM in Account Team Slack channels\n- Open and assign tasks via Salesforce — **start with one at a time** until all types are covered\n- Have the CM shadow you as you open assignments; be on the call as they execute\n- **QA all CM assignments** (CM will self-QA in a later stage)\n- CC your CM in client communications\n- Provide direct guidance on campaign workflow as assignments come in and issues arise\n- Talk through previous experiences and outcomes",
        "cn_sop_s1_cm": "- Complete assignments with your CCM's guidance\n- Communicate updates, questions, blockers directly with CCM/Account Team via Slack\n- Consistently document key learnings and processes\n- Brainstorm ways to solve team and advertiser challenges using your knowledge and partnership",
        "cn_sop_s2_ccm": "- Keep up daily syncs\n- Shadow CMs as they open assignments\n- Transition to **QA-only role** for assignments\n- Lean on your CM during team calls to speak to updates, contingencies, blockers\n- Brainstorm projects alongside your CM — **this is an expected outcome of your partnership**\n  - What problems could you solve?\n  - Where could you use your strengths to make improvements?",
        "cn_sop_s2_cm": "- Open and complete assignments independently — CCM continues QA\n- Proactively communicate blockers and potential issues directly to Account Team\n- Work with AM and AE for guidance wherever applicable\n- Participate in internal account team meetings and provide updates on assignment/campaign statuses\n- Brainstorm projects alongside your CCM — **this is an expected outcome of your partnership**\n  - What problems could you solve?\n  - Where could you use your strengths to make improvements?",
        "cn_sop_s3_practice": "- **CM executes and self-QAs all assignments** — CSU, Optimization, and Trafficking\n- Standing calls / working sessions are recommended but no longer required\n- CM is a vocal, independent member of the Account Team\n- CM proactively tracks upcoming launches and live order health\n- CM communicates gaps, needs, and deadlines regularly — without being asked\n- CM begins coaching teammates on workflows, workarounds, and best practices\n- Both partners collaborate on projects and initiatives together\n- CCM continues to handle all creative development and communicates nuances with CM\n- CCM provides strategic guidance and supports CM development",
        "cn_sop_client_facing_title": "🎙️ Client-Facing CMs",
        "cn_sop_client_facing": "CMs with client-facing experience **can and should** own communications related to their workflow (i.e. go-live confirmations, confirming receipt of tags and trackers, etc.).\n\nThe decision to take on this responsibility **must be mutual**. If the CM expresses interest and does not have previous experience, CCMs should work with them to ensure all guidelines and boundaries are known.\n\n**Highly recommended:** Create an advertiser communication template for this purpose. The CCM remains the strategic lead of all advertiser communications.",
        "cn_checklist_title": "### ✅ Integration Alignment Checklist",
        "cn_checklist_caption": "Showing checklist for: **{}** — progress is saved locally.",
        "cn_checklist_complete": "{}/{} milestones completed for {}",
        "cn_checklist_s1": [
            "Initial introduction call with CCM completed",
            "Daily sync cadence established (morning + afternoon recommended)",
            "Added to account team Slack channels",
            "Added to weekly account team syncs / pod calls",
            "Added to account email distribution list",
            "Salesforce access confirmed — can view and execute assignments",
            "Regular syncs with CCM established or scheduled for the future",
        ],
        "cn_checklist_s2": [
            "Opened and completed at least one assignment independently",
            "CCM has transitioned to QA-only role for your assignments",
            "Actively providing updates in account team meetings",
            "Identified at least one project or initiative with CCM",
        ],
        "cn_checklist_s3": [
            "Self-QA'ing all assignments — no external review needed",
            "Full ownership of CSU, Optimization, and Trafficking workflows",
            "Proactively tracking upcoming launches and live orders",
            "Teaching or coaching teammates on workflows or workarounds",
        ],
        # -- Communication Decision Tree --
        "cdt_title": "Communication Decision Tree",
        "cdt_subtitle": "Situation-based routing. Find your scenario, follow the path.",
        "cdt_channel_title": "📡 Channel Guide",
        "cdt_channel_headers": ["Situation", "Channel", "Why"],
        "cdt_channel_rows": [
            ["Quick question about an active assignment", "Slack DM", "Fast, low-friction, preserves context"],
            ["Blocked — need help now", "Slack DM → escalate via Slack if no response in 15 min", "Urgency requires direct, documented communication"],
            ["Status update for the team", "Account team Slack channel", "Visible to everyone who needs it"],
            ["Error or risk notification", "Slack DM to CCM", "Direct, private, allows CCM to decide next steps"],
            ["End-of-day summary", "Slack DM to CCM", "Consistent cadence builds trust"],
            ["Client-facing communication (Stage 3)", "Email — using approved template", "Formal, trackable, CCM-aligned"]
        ],
        # -- Comm Tree: Stage-aware content --
        "cdt_stage_caption": "Showing guidance for: **{}** — change your stage in the sidebar",
        "cdt_what_happening": "### 📍 What is happening?",
        "cdt_box_question": "**❓ I have a question**",
        "cdt_box_blocked": "**🚧 I'm blocked**",
        "cdt_box_error": "**⚠️ I made an error**",
        "cdt_box_request": "**📨 Someone asked me something**",
        "cdt_box_update": "**📊 I need to give an update**",
        "cdt_blocked_responded": "⏱️ *CCM responded?*",
        "cdt_blocked_yes": "**Yes →** Follow their lead",
        "cdt_blocked_no_15": "**No (15 min) →**",
        "cdt_error_example": '💬 *"Heads up — caught an error on [Title]. [What happened]. Already [fix taken]. Wanted you to know."*',
        "cdt_request_acknowledge": "📌 **Acknowledge** in their channel",
        "cdt_update_who": "📌 *Who needs it?*",
        "cdt_update_ccm_only": "**CCM only →** Slack DM",
        "cdt_update_full_team": "**Full team →** Account Slack channel",
        "cdt_update_example": '💬 *"Update on [Title]: [status]. Next step: [plan]. Let me know if anything changes."*',
        # Stage 1-2 specific
        "cdt_s12_question_cta": "📌 **Slack DM → CCM**\n\n*Ask in real time. Don't batch.*",
        "cdt_s12_question_example": '💬 *"Quick question on the [Title] [placement] — [question]. Want to make sure I handle this correctly before submitting."*',
        "cdt_s1_blocked_escalation": "📌 **Slack CCM again** — note urgency\n\nIf still unresponsive → AdOps mentor",
        "cdt_s2_blocked_escalation": "📌 **Slack mentor or specialist team**\n+ async msg to CCM",
        "cdt_s12_blocked_example": '💬 *"Hey — blocked on [issue]. Reaching out to [name] so I don\'t miss SLA. Will update you."*',
        "cdt_s12_error_cta": "📌 **Slack DM → CCM immediately**\n\n*The moment you find it. Don't wait.*",
        "cdt_s12_request_flow": "**Then →** Slack CCM before fulfilling\n\n💬 To requester: *\"Got it — let me sync with [CCM].\"*\n\n💬 To CCM: *\"[Name] asked for [request]. Good to proceed?\"*",
        # Stage 3 specific
        "cdt_s3_question_cta": "📌 **Use your judgment first**\n\n*You've seen this before. Check your notes, then act.*\n\nIf truly unsure → Slack CCM",
        "cdt_s3_question_example": '💬 *"Quick question — [question]. I\'m leaning toward [approach]. Good to proceed or am I missing something?"*',
        "cdt_s3_blocked_escalation": "📌 **Escalate to specialist team**\n+ heads-up to CCM after",
        "cdt_s3_blocked_example": '💬 *"Blocked on [issue] — escalated to [team]. Letting you know for visibility."*',
        "cdt_s3_error_cta": "📌 **Assess impact → Slack CCM**\n\n*Pre-PTS: fix it, note it. Post-PTS: flag immediately.*",
        "cdt_s3_request_flow": "**Handle it →** Do the work, then loop in CCM\n\n💬 To requester: *\"On it — will send shortly.\"*\n\n💬 To CCM (after): *\"FYI — [Name] asked for [request]. Handled and sent.\"*",
        # Escalation path
        "cdt_escalation_title": "### 🔺 Escalation Path",
        "cdt_s12_esc1": "**Step 1 → CCM**\n\nYour CCM is always the first contact if you don't understand something. If unresponsive in the team channel, then Slack DM and note urgency.",
        "cdt_s12_esc2": "**Step 2 → Escalation**\n\nIf your CCM is unavailable after 15 minutes and the issue is time-sensitive, escalate to the appropriate specialist team or resource. Let your CCM know you escalated.",
        "cdt_s12_esc3": "**Step 3 → Account Team Lead**\n\nOnly if your CCM and specialist resources are unreachable and there is immediate client-facing risk or SLA breach.",
        "cdt_s3_esc1": "**Step 1 → Assess & Act**\n\nYou own your workflows. For questions within your scope, use your judgment and act. For anything outside your lane or with client impact, check with your CCM first.",
        "cdt_s3_esc2": "**Step 2 → Specialist Team or CCM**\n\nIf the issue requires expertise outside your knowledge, escalate to the appropriate specialist team. Give your CCM a heads-up for visibility.",
        "cdt_s3_esc3": "**Step 3 → Account Team Lead**\n\nOnly if specialist resources are unreachable and there is immediate client-facing risk or SLA breach. You should rarely need this path at Stage 3.",
        # Urgency signals
        "cdt_urgency_title": "### 🚨 Urgency Signals to Recognize",
        "cdt_urgency_emoji": "**Emoji signals:**\n- :alert: or :boom: = immediate action\n- ✅ 👀 🫡 = standard acknowledgment",
        "cdt_urgency_time": "**Time anchors:**\n- \"goes live tonight\"\n- \"launching in 8 days\"\n- \"ASAP today\" / \"by EOD\"",
        "cdt_urgency_doubt": "**When in doubt:**\n- Ask → is this urgent or FYI?\n- Check SLA timing\n- Default to proactive over silent",
        # -- Prioritization Framework --
        "pf_title": "Prioritization Framework",
        "pf_subtitle": "Five principles for deciding what to work on when everything feels urgent.",
        "pf_note": "There is no universal priority list. Context changes everything. These principles help you reason through the decision — they do not make it for you.",
        "pf_principles": [
            {
                "title": "1. Live campaigns before future campaigns",
                "body": "If something is live and broken, it takes priority over something that has not launched yet. A tracking pixel that is not firing on a live campaign matters more than a trafficking assignment due tomorrow."
            },
            {
                "title": "2. Client-facing risk before internal deadlines",
                "body": "If an issue could result in the client seeing something wrong — wrong creative, wrong dates, wrong delivery — it jumps the queue. Internal trackers and reports can wait; client trust cannot."
            },
            {
                "title": "3. Blocked work gets communicated, not buried",
                "body": "If you are blocked, do not silently move to the next task and hope the blocker resolves itself. Flag it. Tell your CCM. Then work on what you can while you wait. Blocked does not mean paused — it means parallel."
            },
            {
                "title": "4. SLA proximity drives urgency, not assignment order",
                "body": "A task due in 4 hours matters more than a task due in 3 days, even if the 3-day task arrived first. Check your SLAs every morning and re-sort your queue accordingly."
            },
            {
                "title": "5. When two things are equally urgent, choose the one with the most dependencies",
                "body": "If your trafficking assignment unblocks the creative team, QA, and the CCM's client update — do that one first. Unblocking other people multiplies your impact."
            }
        ],
        # -- Scenario Practice --
        "sp_title": "Scenario Practice",
        "sp_card_progress": "Card {} of {}",
        "sp_shuffle_btn": "🔀 Shuffle",
        "sp_category_label": "Category:",
        "sp_think_prompt": "💭 **Think about it first** — What would you do? How would you communicate? Who would you involve? What would you present to your CCM before acting?",
        "sp_reveal_btn": "🔍 Reveal Suggested Approach",
        "sp_prev_btn": "⬅️ Previous",
        "sp_next_btn": "Next ➡️",
        "sp_footer": "These scenarios are based on real CM/CCM partnership situations. There is no single 'right' answer — the suggested approaches show one way to navigate each situation with clarity and professionalism.",
        # -- Confidence Check --
        "cc_title": "Confidence Check",
        "cc_subtitle": "Rate yourself honestly. This is for you — nobody else sees it unless you choose to share.",
        "cc_instruction": "Select your current stage and score each area from 1 (not confident at all) to 5 (fully confident).",
        "cc_stage_label": "What stage are you in?",
        "cc_stages": ["Stage 1 — Building Trust", "Stage 2 — Becoming Independent", "Stage 3 — Full Partnership"],
        "cc_date_label": "Check-in date",
        "cc_dimensions": [
            {"key": "trafficking", "label": "Trafficking — I can open, execute, and submit assignments in Salesforce/Rodeo accurately"},
            {"key": "optimizations", "label": "Optimizations — I can execute optimization assignments with the right context"},
            {"key": "communication", "label": "Communication — I know who to contact, when, and how (Slack norms, daily syncs, escalation)"},
            {"key": "prioritization", "label": "Prioritization — I can reason through competing priorities using SLA proximity and dependencies"},
            {"key": "navigation", "label": "Navigation — I know when to Ask, Attempt, or Escalate"},
            {"key": "ambiguity", "label": "Ambiguity — I can make progress when instructions are unclear or incomplete"},
            {"key": "partnership", "label": "Partnership — I am building a real working relationship with my CCM and Account Team"},
            {"key": "independence", "label": "Independence — I am contributing value, not just completing tasks"}
        ],
        "cc_reflection_label": "Reflection — What is one thing you want your CCM to know?",
        "cc_reflection_placeholder": "Optional: what support do you need, what is going well, what is still hard...",
        "cc_save_btn": "Save Confidence Check",
        "cc_saved_msg": "✅ Saved! Timestamp: {}",
        "cc_history_title": "📈 Your Confidence Trend",
        "cc_no_history": "No previous checks saved yet. Complete your first one above.",
        "cc_report_title": "📋 Progress Report for 1:1s",
        "cc_report_desc": "Download a summary of your confidence trend to bring to **1:1 conversations** with your CCM, M1, or training facilitator. Use it to ground the conversation in specifics — where you feel strong, where you want support, and how your confidence has changed over time.",
        "cc_report_btn": "📥 Download Progress Report",
        "cc_report_preview": "👁️ Preview report before downloading",
        # -- My Notes --
        "notes_title": "My Notebook",
        "notes_subtitle": "Your space for notes, 1:1 prep, and tracking your progress. Everything here is saved locally on your machine.",
        "notes_placeholder": "Start typing your notes here...",
        "notes_save_btn": "💾 Save Notes",
        "notes_saved_msg": "✅ Notes saved.",
        "notes_download_btn": "📥 Download as Text File",
        # -- Reference Documents --
        "docs_title": "Reference Documents",
        "docs_subtitle": "View documents directly or download for offline use. Place .docx, .txt, or .md files in the `materials/` subfolder.",
        "docs_no_files": "No reference documents found in the materials folder. Place .docx, .pptx, .txt, or .md files in the `materials/` subfolder.",
        "docs_view_btn": "📖 View",
        "docs_download_btn": "📥 Download",
    },
    "es": {
        # -- Sidebar --
        "sidebar_language": "🌐 Idioma / Language",
        "sidebar_alias_label": "Tu alias",
        "sidebar_alias_help": "Ingresa tu alias de Amazon (ej., dcampos)",
        "sidebar_welcome": "Bienvenido/a, **{}**",
        # -- Home --
        "home_title": "CM Integration Hub",
        "home_tagline": "Todo lo que necesitas para trabajar con claridad, consistencia y confianza — en un solo lugar.",
        "home_footer": "Diseñado para CMs en Model 2. Tu referencia desde Stage 1 hasta Stage 3.",
        # -- Campaign Navigation --
         "cn_title": "Navegando R&Rs de Campaña",
        "cn_subtitle": "Tu referencia para saber cuándo actuar de forma independiente y cuándo consultar.",
        "cn_ask_title": "🔵 PREGUNTAR",
        "cn_ask_when": "**Cuándo Preguntar**",
        "cn_ask_items": [
            "Primera vez que encuentras un tipo de assignment",
            "Decisiones o comunicaciones dirigidas al cliente",
            "Cualquier cosa que involucre cambios de presupuesto o modificaciones de flight",
            "Cuando las instrucciones son ambiguas o incompletas",
            "Cuando un creative asset no coincide con lo que describe el assignment",
            "Cuando no estás seguro/a de las preferencias o historial específico del advertiser"
        ],
        "cn_ask_who": "**A quién preguntar**: Tu CCM primero. Si no está disponible y es urgente, tu mentor de AdOps o M1.",
        "cn_attempt_title": "🟢 INTENTAR",
        "cn_attempt_when": "**Cuándo Intentar**",
        "cn_attempt_items": [
            "Tipos de assignment que ya completaste con aprobación de QA",
            "Trafficking estándar para DSP, Devices, STV, PVa",
            "Optimizations que ya ejecutaste previamente en esta cuenta",
            "Assignments de CSU que siguen patrones establecidos",
            "Actualizar el tracker semanal o la production matrix compartida",
            "Actualizaciones rutinarias por Slack a tu CCM sobre el estado de assignments"
        ],
        "cn_attempt_who": "**Luego confirma**: Informa a tu CCM lo que hiciste. Stage 1 = CCM hace QA. Stage 2 = CCM revisa. Stage 3 = tú lo manejas.",
        "cn_escalate_title": "🔴 ESCALAR",
        "cn_escalate_when": "**Cuándo Escalar**",
        "cn_escalate_items": [
            "Llevas más de 15 minutos bloqueado/a sin un camino claro",
            "Una campaña está en riesgo de no cumplir su fecha de lanzamiento",
            "Ha ocurrido o puede ocurrir un error visible para el cliente",
            "Un SLA está en riesgo y no puedes resolver el bloqueo por tu cuenta",
            "Descubres una discrepancia entre OMS y Rodeo que afecta la entrega",
            "Tu CCM no está disponible y el problema no puede esperar"
        ],
        "cn_escalate_who": "**Escalar a**: Tu CCM (primero), luego M1 o líder del Account Team si CCM no está disponible.",
        "cn_15min_title": "⏱️ La Regla de los 15 Minutos",
        "cn_15min_body": "Si llevas 15 minutos sin avanzar, deja de intentar resolverlo solo/a. Comunícate. Esto no es señal de debilidad — es cómo funcionan las alianzas. Tu CCM prefiere saber a los 15 minutos que descubrir un SLA incumplido a las 3 horas.",
        "cn_guardrails_title": "🚧 Límites — Nunca Hagas Sin Consultar",
        "cn_guardrails_items": [
            "Nunca modifiques flight dates sin confirmación del CCM",
            "Nunca envíes comunicaciones al cliente sin alinearte con tu CCM (Stage 1-2)",
            "Nunca envíes un trafficking assignment de un tipo de campaña que no hayas hecho antes sin QA",
            "Nunca cambies asignaciones de presupuesto sin dirección explícita",
            "Nunca uses el estado 'Blocked - CCM' sin intentar resolverlo directamente primero"
        ],
        # -- Campaign Nav: Stage-aware content (ES) --
        "cn_stage_header": "📍 Estás en: **{}**",
        "cn_stage_change": "Cambia tu stage en la barra lateral.",
        "cn_stage1_focus": "Construyendo confianza y estableciendo patrones de comunicación. Tu CCM es tu guía principal.",
        "cn_stage2_focus": "Estás abriendo y ejecutando assignments de forma independiente. Tu CCM proporciona QA y orientación estratégica.",
        "cn_stage3_focus": "Tú manejas tus workflows de principio a fin. Tu alianza con tu CCM es colaborativa y estratégica — no supervisora.",
        "cn_ask_items_s1": [
            "Primera vez que encuentras un tipo de assignment",
            "Decisiones o comunicaciones dirigidas al cliente",
            "Cualquier cosa que involucre cambios de presupuesto o modificaciones de flight",
            "Cuando las instrucciones son ambiguas o incompletas",
            "Cuando un creative asset no coincide con lo que describe el assignment",
            "Cuando no estás seguro/a de las preferencias o historial específico del advertiser",
        ],
        "cn_ask_items_s2": [
            "Tipos de assignment nuevos que no has hecho de forma independiente",
            "Decisiones dirigidas al cliente o comunicaciones directas con el advertiser",
            "Cambios de presupuesto, modificaciones de flight o ajustes de inventario",
            "Cuando las instrucciones son ambiguas y no puedes resolverlo con el SOP o wiki",
            "Cuando no estás seguro/a del historial o preferencias específicas del advertiser",
        ],
        "cn_ask_items_s3": [
            "Una situación genuinamente nueva — productos nuevos, casos especiales, solicitudes únicas del cliente",
            "Decisiones estratégicas con impacto directo en el cliente o los ingresos",
            "Dependencias o conflictos entre cuentas que necesitan alineación",
            "Situaciones donde el SOP no dice nada o se contradice",
        ],
        "cn_ask_who_s1": "**A quién preguntar**: Tu CCM primero. Si no está disponible y es urgente, tu mentor de AdOps o M1.",
        "cn_ask_who_s2": "**A quién preguntar**: Tu CCM para decisiones estratégicas o del cliente. Para dudas de ejecución, revisa el SOP primero — luego tu CCM o Account Team.",
        "cn_ask_who_s3": "**A quién preguntar**: Tu Account Team, M1, o CCM — quien tenga el contexto. Tú decides a quién involucrar.",
        "cn_attempt_items_s1": [
            "Tipos de assignment que ya completaste con aprobación de QA",
            "Trafficking estándar para DSP, Devices, STV, PVa",
            "Optimizations que ya ejecutaste previamente en esta cuenta",
            "Assignments de CSU que siguen patrones establecidos",
            "Actualizar el tracker semanal o la production matrix compartida",
            "Actualizaciones rutinarias por Slack sobre el estado de assignments",
        ],
        "cn_attempt_items_s2": [
            "Todos los tipos de assignment que ya hiciste — ejecuta de forma independiente",
            "Trafficking estándar, optimizations y workflows de CSU",
            "Comunicaciones rutinarias al Account Team sobre estado y timelines",
            "Resolución de problemas de delivery o creative usando el SOP y wiki",
            "Señalar proactivamente posibles problemas al Account Team",
        ],
        "cn_attempt_items_s3": [
            "Todos los assignments dentro de tu alcance — CSU, Optimization, Trafficking",
            "Auto-QA todo tu trabajo antes de enviar",
            "Comunicaciones al Account Team relacionadas con tu workflow — confirmaciones de go-live, recibo de tags, actualizaciones de delivery",
            "Resolver problemas de delivery de principio a fin",
            "Orientar a compañeros sobre workflows, soluciones y mejores prácticas",
            "Rastrear proactivamente próximos lanzamientos y salud de órdenes activas",
        ],
        "cn_attempt_who_s1": "**Luego confirma**: Informa a tu CCM lo que hiciste. Tu CCM hará QA.",
        "cn_attempt_who_s2": "**Luego confirma**: Tu CCM revisa trabajo de alto impacto. La ejecución rutinaria es tuya.",
        "cn_attempt_who_s3": "**Tú lo manejas.** Ejecuta, haz QA y comunica de forma autónoma. Involucra a tu partner cuando se necesite alineación estratégica.",
        "cn_escalate_items_s1": [
            "Llevas más de 15 minutos bloqueado/a sin un camino claro",
            "Una campaña está en riesgo de no cumplir su fecha de lanzamiento",
            "Ha ocurrido o puede ocurrir un error visible para el cliente",
            "Un SLA está en riesgo y no puedes resolver el bloqueo por tu cuenta",
            "Descubres una discrepancia entre OMS y Rodeo que afecta la entrega",
            "Tu CCM no está disponible y el problema no puede esperar",
        ],
        "cn_escalate_items_s2": [
            "Llevas más de 15 minutos bloqueado/a sin un camino claro",
            "Una campaña está en riesgo de no cumplir su fecha de lanzamiento o SLA",
            "Ha ocurrido o puede ocurrir un error visible para el cliente",
            "Una discrepancia entre OMS y Rodeo que no puedes resolver",
            "Tu CCM no está disponible y el problema es urgente",
        ],
        "cn_escalate_items_s3": [
            "Una campaña está en riesgo y no puedes resolverlo de forma independiente",
            "Ha ocurrido un error visible para el cliente con impacto material",
            "Un problema requiere coordinación entre cuentas o equipos fuera de tu alcance",
            "Una decisión necesita visibilidad de M1 o liderazgo por riesgo de ingresos o relación",
        ],
        "cn_escalate_who_s1": "**Escalar a**: Tu CCM (primero), luego M1 o líder del Account Team si CCM no está disponible.",
        "cn_escalate_who_s2": "**Escalar a**: Tu CCM para impacto al cliente. M1 o líder del Account Team si CCM no está disponible.",
        "cn_escalate_who_s3": "**Escalar a**: Quien tenga la autoridad para resolverlo — M1, líder del Account Team, o tu CCM partner.",
        "cn_guardrails_s3": [
            "Nunca modifiques flight dates sin confirmar el impacto en delivery y pacing",
            "Nunca envíes trabajo sin auto-QA — tú eres tu propia puerta de calidad",
            "Nunca cambies asignaciones de presupuesto sin dirección explícita del Account Team o AM",
            "Nunca tomes trabajo de otra cuenta sin confirmar disponibilidad y visibilidad con tu partner",
        ],
        "cn_sop_title": "📋 SOP por Stage de Integración",
        "cn_sop_source": "Del [SOP de Workflow US-SJO — Model 2](https://w.amazon.com/bin/view/Users/ajamitho/CM-UAT-Test/)",
        "cn_sop_duration": "**Duración:** Aproximadamente 2–3 semanas — el CM dictará según su nivel de confianza",
        "cn_sop_s1_focus": "**Enfoque:** Construyendo confianza y estableciendo patrones de comunicación.",
        "cn_sop_s2_focus": "**Enfoque:** Los CMs comienzan a abrir y ejecutar assignments de forma independiente mientras los CCMs continúan guiando y haciendo QA.",
        "cn_sop_s3_focus": "**Enfoque:** Los CMs asumen la propiedad de sus workflows. Ambos partners deben estar colaborando en proyectos e iniciativas juntos.",
        "cn_sop_s3_note": "**Para ser claros:** Esta es una **alianza igualitaria y colaborativa** — los CMs no son 'asistentes' de los CCMs, así como los CCMs no son 'asistentes' de los AEs. Trabajamos juntos, siempre.",
        "cn_sop_ccm_title": "#### Responsabilidades del CCM",
        "cn_sop_cm_title": "#### Responsabilidades del CM",
        "cn_sop_s3_practice_title": "#### Cómo Se Ve en la Práctica",
        "cn_sop_s1_ccm": "- Programar llamada de introducción inicial con el CM\n- Alinear en **cadencia diaria** — bloque de 30–60 min cada mañana y tarde es altamente recomendado\n- Agregar al CM a chats relevantes del account team y syncs semanales\n- Presentar al CM en canales de Slack del Account Team\n- Abrir y asignar tareas vía Salesforce — **empezar con una a la vez** hasta cubrir todos los tipos\n- Que el CM te observe mientras abres assignments; estar en la llamada mientras ejecutan\n- **QA de todos los assignments del CM** (el CM hará self-QA en un stage posterior)\n- CC al CM en comunicaciones con el cliente\n- Dar orientación directa sobre workflow de campaña conforme llegan assignments\n- Compartir experiencias previas y resultados",
        "cn_sop_s1_cm": "- Completar assignments con la guía de tu CCM\n- Comunicar actualizaciones, preguntas, bloqueos directamente con CCM/Account Team vía Slack\n- Documentar consistentemente aprendizajes clave y procesos\n- Idear formas de resolver desafíos del equipo y advertiser usando tu conocimiento y alianza",
        "cn_sop_s2_ccm": "- Mantener syncs diarios\n- Observar a los CMs mientras abren assignments\n- Transicionar a **rol de solo-QA** para assignments\n- Apoyarse en tu CM durante llamadas de equipo para hablar de actualizaciones, contingencias, bloqueos\n- Idear proyectos junto con tu CM — **esto es un resultado esperado de tu alianza**\n  - ¿Qué problemas podrían resolver?\n  - ¿Dónde podrían usar sus fortalezas para mejorar?",
        "cn_sop_s2_cm": "- Abrir y completar assignments de forma independiente — el CCM continúa con QA\n- Comunicar proactivamente bloqueos y posibles problemas al Account Team\n- Trabajar con AM y AE para orientación donde aplique\n- Participar en reuniones internas del account team y dar actualizaciones de estado\n- Idear proyectos junto con tu CCM — **esto es un resultado esperado de tu alianza**\n  - ¿Qué problemas podrían resolver?\n  - ¿Dónde podrían usar sus fortalezas para mejorar?",
        "cn_sop_s3_practice": "- **El CM ejecuta y hace self-QA de todos los assignments** — CSU, Optimization y Trafficking\n- Llamadas regulares / sesiones de trabajo son recomendadas pero ya no requeridas\n- El CM es un miembro vocal e independiente del Account Team\n- El CM rastrea proactivamente próximos lanzamientos y salud de órdenes activas\n- El CM comunica brechas, necesidades y fechas límite regularmente — sin que se lo pidan\n- El CM comienza a orientar a compañeros sobre workflows, soluciones y mejores prácticas\n- Ambos partners colaboran en proyectos e iniciativas juntos\n- El CCM continúa manejando todo el desarrollo creativo y comunica matices al CM\n- El CCM proporciona orientación estratégica y apoya el desarrollo del CM",
        "cn_sop_client_facing_title": "🎙️ CMs con Contacto al Cliente",
        "cn_sop_client_facing": "Los CMs con experiencia de contacto al cliente **pueden y deben** manejar comunicaciones relacionadas con su workflow (ej. confirmaciones de go-live, confirmar recibo de tags y trackers, etc.).\n\nLa decisión de asumir esta responsabilidad **debe ser mutua**. Si el CM expresa interés y no tiene experiencia previa, los CCMs deben asegurarse de que todas las directrices y límites sean conocidos.\n\n**Altamente recomendado:** Crear una plantilla de comunicación con el advertiser para este propósito. El CCM sigue siendo el líder estratégico de todas las comunicaciones con el advertiser.",
        "cn_checklist_title": "### ✅ Lista de Verificación de Alineación de Integración",
        "cn_checklist_caption": "Mostrando lista para: **{}** — el progreso se guarda localmente.",
        "cn_checklist_complete": "{}/{} hitos completados para {}",
        "cn_checklist_s1": [
            "Llamada de introducción inicial con CCM completada",
            "Cadencia diaria de syncs establecida (mañana + tarde recomendado)",
            "Agregado/a a canales de Slack del account team",
            "Agregado/a a syncs semanales / llamadas del pod",
            "Agregado/a a lista de distribución de correo de la cuenta",
            "Acceso a Salesforce confirmado — puedes ver y ejecutar assignments",
            "Syncs regulares con CCM establecidos o programados para el futuro",
        ],
        "cn_checklist_s2": [
            "Abrió y completó al menos un assignment de forma independiente",
            "El CCM ha transicionado a rol de solo-QA para tus assignments",
            "Proporcionando actualizaciones activamente en reuniones del account team",
            "Identificado al menos un proyecto o iniciativa con CCM",
        ],
        "cn_checklist_s3": [
            "Haciendo self-QA de todos los assignments — sin revisión externa necesaria",
            "Propiedad completa de workflows de CSU, Optimization y Trafficking",
            "Rastreando proactivamente próximos lanzamientos y órdenes activas",
            "Enseñando u orientando a compañeros sobre workflows o soluciones",
        ],
        # -- Communication Decision Tree (ES) --
        "cdt_title": "Árbol de Decisión de Comunicación",
        "cdt_subtitle": "Enrutamiento basado en situaciones. Encuentra tu escenario, sigue el camino.",
        "cdt_channel_title": "📡 Guía de Canales",
        "cdt_channel_headers": ["Situación", "Canal", "Por qué"],
        "cdt_channel_rows": [
            ["Pregunta rápida sobre un assignment activo", "Slack DM", "Rápido, bajo esfuerzo, preserva contexto"],
            ["Bloqueado/a — necesito ayuda ahora", "Slack DM → escalar vía Slack si no hay respuesta en 15 min", "La urgencia requiere comunicación directa y documentada"],
            ["Actualización de estado para el equipo", "Canal de Slack del account team", "Visible para todos los que lo necesitan"],
            ["Notificación de error o riesgo", "Slack DM al CCM", "Directo, privado, permite al CCM decidir los siguientes pasos"],
            ["Resumen de fin de día", "Slack DM al CCM", "La cadencia constante construye confianza"],
            ["Comunicación al cliente (Stage 3)", "Email — usando plantilla aprobada", "Formal, rastreable, alineado con el CCM"]
        ],
        "cdt_stage_caption": "Mostrando guía para: **{}** — cambia tu stage en la barra lateral",
        "cdt_what_happening": "### 📍 ¿Qué está pasando?",
        "cdt_box_question": "**❓ Tengo una pregunta**",
        "cdt_box_blocked": "**🚧 Estoy bloqueado/a**",
        "cdt_box_error": "**⚠️ Cometí un error**",
        "cdt_box_request": "**📨 Alguien me pidió algo**",
        "cdt_box_update": "**📊 Necesito dar una actualización**",
        "cdt_blocked_responded": "⏱️ *¿Respondió el CCM?*",
        "cdt_blocked_yes": "**Sí →** Sigue su guía",
        "cdt_blocked_no_15": "**No (15 min) →**",
        "cdt_error_example": '💬 *"Aviso — encontré un error en [Título]. [Qué pasó]. Ya [acción tomada]. Quería que supieras."*',
        "cdt_request_acknowledge": "📌 **Confirma recibo** en su canal",
        "cdt_update_who": "📌 *¿Quién lo necesita?*",
        "cdt_update_ccm_only": "**Solo CCM →** Slack DM",
        "cdt_update_full_team": "**Todo el equipo →** Canal de Slack de la cuenta",
        "cdt_update_example": '💬 *"Actualización sobre [Título]: [estado]. Siguiente paso: [plan]. Avísenme si algo cambia."*',
        "cdt_s12_question_cta": "📌 **Slack DM → CCM**\n\n*Pregunta en tiempo real. No acumules.*",
        "cdt_s12_question_example": '💬 *"Pregunta rápida sobre el [Título] [placement] — [pregunta]. Quiero asegurarme de manejarlo bien antes de enviar."*',
        "cdt_s1_blocked_escalation": "📌 **Escríbele al CCM de nuevo** — señala urgencia\n\nSi sigue sin responder → Mentor de AdOps",
        "cdt_s2_blocked_escalation": "📌 **Escríbele al mentor o equipo especialista**\n+ msg asíncrono al CCM",
        "cdt_s12_blocked_example": '💬 *"Hey — bloqueado/a en [problema]. Contactando a [nombre] para no perder SLA. Te actualizo."*',
        "cdt_s12_error_cta": "📌 **Slack DM → CCM inmediatamente**\n\n*En el momento que lo encuentres. No esperes.*",
        "cdt_s12_request_flow": "**Luego →** Escríbele al CCM antes de cumplir\n\n💬 Al solicitante: *\"Recibido — déjame sincronizar con [CCM].\"*\n\n💬 Al CCM: *\"[Nombre] pidió [solicitud]. ¿Puedo proceder?\"*",
        "cdt_s3_question_cta": "📌 **Usa tu criterio primero**\n\n*Ya has visto esto antes. Revisa tus notas, luego actúa.*\n\nSi realmente no estás seguro/a → Slack CCM",
        "cdt_s3_question_example": '💬 *"Pregunta rápida — [pregunta]. Me inclino hacia [enfoque]. ¿Puedo proceder o estoy pasando algo por alto?"*',
        "cdt_s3_blocked_escalation": "📌 **Escala al equipo especialista**\n+ aviso al CCM después",
        "cdt_s3_blocked_example": '💬 *"Bloqueado/a en [problema] — escalé a [equipo]. Te aviso para visibilidad."*',
        "cdt_s3_error_cta": "📌 **Evalúa impacto → Slack CCM**\n\n*Pre-PTS: corrígelo, anótalo. Post-PTS: señala inmediatamente.*",
        "cdt_s3_request_flow": "**Manéjalo →** Haz el trabajo, luego avisa al CCM\n\n💬 Al solicitante: *\"En eso — te lo envío pronto.\"*\n\n💬 Al CCM (después): *\"FYI — [Nombre] pidió [solicitud]. Lo manejé y envié.\"*",
        "cdt_escalation_title": "### 🔺 Ruta de Escalación",
        "cdt_s12_esc1": "**Paso 1 → CCM**\n\nTu CCM es siempre el primer contacto si no entiendes algo. Si no responde en el canal del equipo, entonces Slack DM y señala urgencia.",
        "cdt_s12_esc2": "**Paso 2 → Escalación**\n\nSi tu CCM no está disponible después de 15 minutos y el problema es urgente, escala al equipo especialista o recurso apropiado. Avisa a tu CCM que escalaste.",
        "cdt_s12_esc3": "**Paso 3 → Líder del Account Team**\n\nSolo si tu CCM y los recursos especialistas no están disponibles y hay riesgo inmediato para el cliente o incumplimiento de SLA.",
        "cdt_s3_esc1": "**Paso 1 → Evalúa y Actúa**\n\nTú manejas tus workflows. Para preguntas dentro de tu alcance, usa tu criterio y actúa. Para cualquier cosa fuera de tu área o con impacto al cliente, consulta primero con tu CCM.",
        "cdt_s3_esc2": "**Paso 2 → Equipo Especialista o CCM**\n\nSi el problema requiere experiencia fuera de tu conocimiento, escala al equipo especialista apropiado. Dale visibilidad a tu CCM.",
        "cdt_s3_esc3": "**Paso 3 → Líder del Account Team**\n\nSolo si los recursos especialistas no están disponibles y hay riesgo inmediato para el cliente o incumplimiento de SLA. Raramente deberías necesitar esta ruta en Stage 3.",
        "cdt_urgency_title": "### 🚨 Señales de Urgencia a Reconocer",
        "cdt_urgency_emoji": "**Señales de emoji:**\n- :alert: o :boom: = acción inmediata\n- ✅ 👀 🫡 = confirmación estándar",
        "cdt_urgency_time": "**Anclas de tiempo:**\n- \"sale en vivo esta noche\"\n- \"lanzamiento en 8 días\"\n- \"ASAP hoy\" / \"para EOD\"",
        "cdt_urgency_doubt": "**Si tienes dudas:**\n- Pregunta → ¿es urgente o informativo?\n- Revisa timing del SLA\n- Por defecto: proactivo sobre silencioso",
        # -- Prioritization Framework --
        "pf_title": "Marco de Priorización",
        "pf_subtitle": "Cinco principios para decidir en qué trabajar cuando todo se siente urgente.",
        "pf_note": "No hay una lista de prioridades universal. El contexto lo cambia todo. Estos principios te ayudan a razonar la decisión — no la toman por ti.",
        "pf_principles": [
            {
                "title": "1. Campañas en vivo antes que campañas futuras",
                "body": "Si algo está en vivo y tiene un problema, tiene prioridad sobre algo que aún no se ha lanzado. Un tracking pixel que no funciona en una campaña activa importa más que un trafficking assignment con fecha de mañana."
            },
            {
                "title": "2. Riesgo para el cliente antes que deadlines internos",
                "body": "Si un problema podría resultar en que el cliente vea algo incorrecto — creative equivocado, fechas incorrectas, entrega errónea — sube en la cola. Los trackers internos y reportes pueden esperar; la confianza del cliente no."
            },
            {
                "title": "3. El trabajo bloqueado se comunica, no se entierra",
                "body": "Si estás bloqueado/a, no pases silenciosamente a la siguiente tarea esperando que el bloqueo se resuelva solo. Repórtalo. Dile a tu CCM. Luego trabaja en lo que puedas mientras esperas. Bloqueado no significa pausado — significa paralelo."
            },
            {
                "title": "4. La proximidad del SLA determina la urgencia, no el orden de llegada",
                "body": "Una tarea con fecha límite en 4 horas importa más que una con fecha en 3 días, aunque la de 3 días haya llegado primero. Revisa tus SLAs cada mañana y reorganiza tu cola."
            },
            {
                "title": "5. Cuando dos cosas son igual de urgentes, elige la que tiene más dependencias",
                "body": "Si tu trafficking assignment desbloquea al equipo de creative, QA, y la actualización del CCM al cliente — haz esa primero. Desbloquear a otros multiplica tu impacto."
            }
        ],
        # -- Scenario Practice --
        "sp_title": "Práctica de Escenarios",
        "sp_card_progress": "Tarjeta {} de {}",
        "sp_shuffle_btn": "🔀 Mezclar",
        "sp_category_label": "Categoría:",
        "sp_think_prompt": "💭 **Piénsalo primero** — ¿Qué harías? ¿Cómo te comunicarías? ¿A quién involucrarías? ¿Qué le presentarías a tu CCM antes de actuar?",
        "sp_reveal_btn": "🔍 Revelar Enfoque Sugerido",
        "sp_prev_btn": "⬅️ Anterior",
        "sp_next_btn": "Siguiente ➡️",
        "sp_footer": "Estos escenarios están basados en situaciones reales de alianza CM/CCM. No hay una sola respuesta 'correcta' — los enfoques sugeridos muestran una manera de navegar cada situación con claridad y profesionalismo.",
        # -- Confidence Check --
        "cc_title": "Control de Confianza",
        "cc_subtitle": "Califícate honestamente. Esto es para ti — nadie más lo ve a menos que elijas compartirlo.",
        "cc_instruction": "Selecciona tu stage actual y califica cada área del 1 (nada seguro/a) al 5 (totalmente seguro/a).",
        "cc_stage_label": "¿En qué stage estás?",
        "cc_stages": ["Stage 1 — Construyendo Confianza", "Stage 2 — Ganando Independencia", "Stage 3 — Alianza Completa"],
        "cc_date_label": "Fecha del check-in",
        "cc_dimensions": [
            {"key": "trafficking", "label": "Trafficking — Puedo abrir, ejecutar y enviar assignments en Salesforce/Rodeo con precisión"},
            {"key": "optimizations", "label": "Optimizations — Puedo ejecutar assignments de optimización con el contexto adecuado"},
            {"key": "communication", "label": "Comunicación — Sé a quién contactar, cuándo y cómo (normas de Slack, syncs diarios, escalación)"},
            {"key": "prioritization", "label": "Priorización — Puedo razonar entre prioridades usando proximidad de SLA y dependencias"},
            {"key": "navigation", "label": "Navegación — Sé cuándo Preguntar, Intentar o Escalar"},
            {"key": "ambiguity", "label": "Ambigüedad — Puedo avanzar cuando las instrucciones son poco claras o incompletas"},
            {"key": "partnership", "label": "Alianza — Estoy construyendo una relación de trabajo real con mi CCM y Account Team"},
            {"key": "independence", "label": "Independencia — Estoy aportando valor, no solo completando tareas"}
        ],
        "cc_reflection_label": "Reflexión — ¿Qué quieres que tu CCM sepa?",
        "cc_reflection_placeholder": "Opcional: qué apoyo necesitas, qué va bien, qué sigue siendo difícil...",
        "cc_save_btn": "Guardar Control de Confianza",
        "cc_saved_msg": "✅ ¡Guardado! Fecha: {}",
        "cc_history_title": "📈 Tu Tendencia de Confianza",
        "cc_no_history": "No hay controles anteriores guardados. Completa tu primero arriba.",
        "cc_report_title": "📋 Reporte de Progreso para 1:1s",
        "cc_report_desc": "Descarga un resumen de tu tendencia de confianza para llevar a **conversaciones 1:1** con tu CCM, M1, o facilitador de training. Úsalo para fundamentar la conversación en datos específicos — dónde te sientes fuerte, dónde quieres apoyo, y cómo ha cambiado tu confianza.",
        "cc_report_btn": "📥 Descargar Reporte de Progreso",
        "cc_report_preview": "👁️ Vista previa del reporte antes de descargar",
        # -- My Notes --
        "notes_title": "Mi Cuaderno",
        "notes_subtitle": "Tu espacio para notas, preparación de 1:1s, y seguimiento de tu progreso. Todo se guarda localmente en tu máquina.",
        "notes_placeholder": "Empieza a escribir tus notas aquí...",
        "notes_save_btn": "💾 Guardar Notas",
        "notes_saved_msg": "✅ Notas guardadas.",
        "notes_download_btn": "📥 Descargar como Archivo de Texto",
        # -- Reference Documents --
        "docs_title": "Documentos de Referencia",
        "docs_subtitle": "Ve documentos directamente o descarga para uso offline. Coloca archivos .docx, .txt, o .md en la subcarpeta `materials/`.",
        "docs_no_files": "No se encontraron documentos de referencia en la carpeta de materiales. Coloca archivos .docx, .pptx, .txt, o .md en la subcarpeta `materials/`.",
        "docs_view_btn": "📖 Ver",
        "docs_download_btn": "📥 Descargar",
    }
}


def t(key):
    """Get translated string for current language."""
    lang = st.session_state.get("language", "en")
    return LANG.get(lang, LANG["en"]).get(key, LANG["en"].get(key, key))


# ============================================================
# NAVIGATION HELPER
# ============================================================

def navigate_to(page_key):
    """Set navigation state and rerun."""
    st.session_state["current_page"] = page_key


# ============================================================
# DATA PERSISTENCE HELPERS
# ============================================================

def get_user_dir():
    """Get or create user-specific data directory."""
    alias = st.session_state.get("alias", "anonymous")
    user_dir = DATA_DIR / alias
    user_dir.mkdir(exist_ok=True)
    return user_dir


def save_confidence_check(scores, stage, check_date, reflection=""):
    """Save confidence check scores as JSON with stage and date."""
    user_dir = get_user_dir()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    data = {
        "timestamp": timestamp,
        "date_display": datetime.now().strftime("%b %d, %Y %I:%M %p"),
        "check_date": check_date,
        "stage": stage,
        "scores": scores,
        "reflection": reflection
    }
    filepath = user_dir / f"confidence_{timestamp}.json"
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    return data["date_display"]


def load_confidence_history():
    """Load all confidence checks for current user."""
    user_dir = get_user_dir()
    history = []
    for filepath in sorted(user_dir.glob("confidence_*.json")):
        with open(filepath) as f:
            history.append(json.load(f))
    return history


def save_notes(text):
    """Save notes to local file."""
    user_dir = get_user_dir()
    filepath = user_dir / "notes.txt"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)


def load_notes():
    """Load notes from local file."""
    user_dir = get_user_dir()
    filepath = user_dir / "notes.txt"
    if filepath.exists():
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    return ""


def save_scenario_viewed(card_index):
    """Track which scenario cards have been viewed/flipped."""
    user_dir = get_user_dir()
    filepath = user_dir / "scenarios_viewed.json"
    viewed = set()
    if filepath.exists():
        with open(filepath) as f:
            viewed = set(json.load(f))
    viewed.add(card_index)
    with open(filepath, "w") as f:
        json.dump(sorted(viewed), f)


def load_scenarios_viewed():
    """Load set of viewed scenario card indices."""
    user_dir = get_user_dir()
    filepath = user_dir / "scenarios_viewed.json"
    if filepath.exists():
        with open(filepath) as f:
            return set(json.load(f))
    return set()


def save_oneone_topics(text):
    """Save 1:1 discussion topics to local file."""
    user_dir = get_user_dir()
    filepath = user_dir / "oneone_topics.txt"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)


def load_oneone_topics():
    """Load 1:1 discussion topics from local file."""
    user_dir = get_user_dir()
    filepath = user_dir / "oneone_topics.txt"
    if filepath.exists():
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    return ""


def generate_progress_report(history, alias):
    """Generate a comprehensive progress report pulling from all data sources."""
    # Gather all data
    notes_text = load_notes()
    oneone_topics = load_oneone_topics()
    scenarios_viewed = load_scenarios_viewed()
    total_scenarios = 6

    # Load checklist state
    user_dir = get_user_dir()
    checklist_file = user_dir / "alignment_checklist.json"
    if checklist_file.exists():
        with open(checklist_file, "r", encoding="utf-8") as f:
            checklist_state = json.load(f)
    else:
        checklist_state = {}

    # Read integration stage
    global_stage = st.session_state.get("global_stage", "Stage 1 — Building Trust")
    if "Stage 1" in global_stage:
        stage_num = 1
    elif "Stage 2" in global_stage:
        stage_num = 2
    else:
        stage_num = 3

    lines = []
    lines.append("=" * 60)
    lines.append("CM PROGRESS REPORT — FOR 1:1 CONVERSATIONS")
    lines.append("=" * 60)
    lines.append(f"CM Alias:       {alias}")
    lines.append(f"Generated:      {datetime.now().strftime('%B %d, %Y at %I:%M %p')}")
    lines.append(f"Integration:    {global_stage} (Stage {stage_num} of 3)")
    lines.append(f"Total Check-ins: {len(history)}")
    if history:
        lines.append(f"First Check-in: {history[0].get('check_date', history[0].get('date_display', '—'))}")
        lines.append(f"Latest Check-in: {history[-1].get('check_date', history[-1].get('date_display', '—'))}")
    lines.append("=" * 60)
    lines.append("")
    lines.append("HOW TO USE THIS REPORT")
    lines.append("-" * 40)
    lines.append("This report is designed for 1:1 conversations with your CCM,")
    lines.append("M1, or training facilitator. It shows your integration stage,")
    lines.append("checklist progress, and how your self-assessed confidence has")
    lines.append("changed over time across 8 dimensions.")
    lines.append("")
    lines.append("Suggested conversation starters:")
    lines.append("  • \"Here's where I feel strongest / most uncertain right now.\"")
    lines.append("  • \"This area improved since last time — here's what helped.\"")
    lines.append("  • \"I'm still working on this — what would help me grow here?\"")
    lines.append("")

    # ---- INTEGRATION STAGE & CHECKLIST ----
    lines.append("")
    lines.append("INTEGRATION STAGE & ALIGNMENT CHECKLIST")
    lines.append("-" * 40)
    lines.append(f"  Current Stage: {global_stage}")
    lines.append("")

    all_stage_items = {
        "Stage 1 — Building Trust": [
            ("s1_intro_call", "Introduction call with CCM"),
            ("s1_daily_cadence", "Daily sync cadence established"),
            ("s1_slack_channels", "Added to Slack channels"),
            ("s1_weekly_syncs", "Added to weekly syncs"),
            ("s1_email_distro", "Added to email distribution list"),
            ("s1_sf_access", "Salesforce access confirmed"),
            ("s1_regular_syncs", "Regular syncs established or scheduled"),
        ],
        "Stage 2 — Becoming Independent": [
            ("s2_open_independently", "Completed assignment independently"),
            ("s2_ccm_qa_only", "CCM transitioned to QA-only"),
            ("s2_team_call_updates", "Providing updates in team meetings"),
            ("s2_project_brainstorm", "Identified project/initiative with CCM"),
        ],
        "Stage 3 — Full Integration": [
            ("s3_self_qa", "Self-QA'ing all assignments"),
            ("s3_full_ownership", "Full workflow ownership"),
            ("s3_proactive_tracking", "Proactively tracking launches"),
            ("s3_coaching", "Coaching teammates"),
        ],
    }

    for stage_name, items in all_stage_items.items():
        completed = sum(1 for key, _ in items if checklist_state.get(key, False))
        total = len(items)
        lines.append(f"  {stage_name}  ({completed}/{total})")
        for key, label in items:
            status = "✓" if checklist_state.get(key, False) else "○"
            lines.append(f"    {status}  {label}")
        lines.append("")

    if not history:
        lines.append("")
        lines.append("No confidence checks recorded yet.")
        return "\n".join(lines)

    # Dimension labels for readable output
    dim_labels = {
        "trafficking": "Trafficking",
        "optimizations": "Optimizations",
        "communication": "Communication",
        "prioritization": "Prioritization",
        "navigation": "Navigation",
        "ambiguity": "Ambiguity",
        "partnership": "Partnership",
        "independence": "Independence",
    }

    # Latest snapshot
    lines.append("")
    lines.append("LATEST CONFIDENCE SNAPSHOT")
    lines.append("-" * 40)
    latest = history[-1]
    lines.append(f"Date:  {latest.get('check_date', '—')}")
    lines.append(f"Stage: {latest.get('stage', '—')}")
    lines.append("")

    avg = sum(latest["scores"].values()) / len(latest["scores"])
    lines.append(f"Overall Average: {avg:.1f} / 5.0")
    lines.append("")

    # Sort dimensions: highest first
    sorted_dims = sorted(latest["scores"].items(), key=lambda x: x[1], reverse=True)
    for key, val in sorted_dims:
        bar = "█" * val + "░" * (5 - val)
        label = dim_labels.get(key, key.capitalize())
        lines.append(f"  {bar}  {val}/5  {label}")

    lines.append("")

    # Strengths and growth areas
    top = [dim_labels.get(k, k) for k, v in sorted_dims if v >= 4]
    growth = [dim_labels.get(k, k) for k, v in sorted_dims if v <= 2]
    if top:
        lines.append(f"  Strengths (4-5):     {', '.join(top)}")
    if growth:
        lines.append(f"  Growth areas (1-2):  {', '.join(growth)}")

    if latest.get("reflection"):
        lines.append("")
        lines.append(f"  Reflection: \"{latest['reflection']}\"")

    # Full timeline
    if len(history) > 1:
        lines.append("")
        lines.append("")
        lines.append("FULL TIMELINE")
        lines.append("-" * 40)

        for i, entry in enumerate(history):
            check_dt = entry.get("check_date", entry.get("date_display", "—"))
            stage = entry.get("stage", "—")
            avg = sum(entry["scores"].values()) / len(entry["scores"])
            lines.append("")
            lines.append(f"  Check-in #{i + 1}  |  {check_dt}  |  {stage}  |  Avg: {avg:.1f}/5.0")

            for key, val in entry["scores"].items():
                bar = "█" * val + "░" * (5 - val)
                label = dim_labels.get(key, key.capitalize())
                lines.append(f"    {bar}  {val}/5  {label}")

            if entry.get("reflection"):
                lines.append(f"    Reflection: \"{entry['reflection']}\"")

        # Trend analysis — compare first vs latest
        lines.append("")
        lines.append("")
        lines.append("GROWTH SUMMARY (First → Latest)")
        lines.append("-" * 40)

        first = history[0]
        for key in latest["scores"]:
            first_val = first["scores"].get(key, 0)
            latest_val = latest["scores"].get(key, 0)
            diff = latest_val - first_val
            label = dim_labels.get(key, key.capitalize())
            if diff > 0:
                arrow = f"+{diff} ▲"
            elif diff < 0:
                arrow = f"{diff} ▼"
            else:
                arrow = "  —"
            lines.append(f"  {label:<20s}  {first_val} → {latest_val}  {arrow}")

        overall_first = sum(first["scores"].values()) / len(first["scores"])
        overall_latest = sum(latest["scores"].values()) / len(latest["scores"])
        overall_diff = overall_latest - overall_first
        if overall_diff > 0:
            arrow = f"+{overall_diff:.1f} ▲"
        elif overall_diff < 0:
            arrow = f"{overall_diff:.1f} ▼"
        else:
            arrow = "  —"
        lines.append(f"  {'Overall Average':<20s}  {overall_first:.1f} → {overall_latest:.1f}  {arrow}")

    # ---- 1:1 TOPICS ----
    lines.append("")
    lines.append("")
    lines.append("TOPICS FOR MY 1:1")
    lines.append("-" * 40)
    if oneone_topics and oneone_topics.strip():
        for line in oneone_topics.strip().splitlines():
            lines.append(f"  • {line.strip()}" if line.strip() else "")
    else:
        lines.append("  (No topics saved — add them in My Notebook)")

    # ---- SCENARIO PRACTICE ----
    lines.append("")
    lines.append("")
    lines.append("SCENARIO PRACTICE")
    lines.append("-" * 40)
    lines.append(f"  Scenarios practiced: {len(scenarios_viewed)} of {total_scenarios}")

    scenario_titles = [
        "First Assignment from Your CCM",
        "CCM and M1 Give Conflicting Direction",
        "AE Asks You for Something Directly",
        "You Trafficked the Wrong Flight Dates",
        "A Teammate Asks You to Cover",
        "Your Stage 1 Integration Is Not Happening"
    ]
    for i, title in enumerate(scenario_titles):
        status = "✓" if i in scenarios_viewed else "○"
        lines.append(f"  {status}  {title}")

    # ---- NOTES (excerpt) ----
    lines.append("")
    lines.append("")
    lines.append("NOTES (excerpt)")
    lines.append("-" * 40)
    if notes_text and notes_text.strip():
        note_lines = notes_text.strip().splitlines()[:20]
        for line in note_lines:
            lines.append(f"  {line}")
        if len(notes_text.strip().splitlines()) > 20:
            lines.append(f"  ... ({len(notes_text.strip().splitlines()) - 20} more lines)")
    else:
        lines.append("  (No notes saved yet)")

    lines.append("")
    lines.append("=" * 60)
    lines.append("Generated by CM Integration Hub | Model 2 | Stage 1 → Stage 3")
    lines.append("=" * 60)

    return "\n".join(lines)



def extract_docx_text(filepath):
    """Extract text from a .docx file using basic zip/XML parsing (no python-docx needed)."""
    import zipfile
    import xml.etree.ElementTree as ET
    try:
        with zipfile.ZipFile(filepath, "r") as z:
            with z.open("word/document.xml") as f:
                tree = ET.parse(f)
                root = tree.getroot()
                ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
                paragraphs = []
                for p in root.iter(f"{{{ns['w']}}}p"):
                    texts = []
                    for t_elem in p.iter(f"{{{ns['w']}}}t"):
                        if t_elem.text:
                            texts.append(t_elem.text)
                    if texts:
                        paragraphs.append("".join(texts))
                return "\n\n".join(paragraphs)
    except Exception as e:
        return f"Could not read document: {e}"


# ============================================================
# PAGE RENDERERS
# ============================================================

def render_home():
    # ============================================================
    # DASHBOARD — personalized, stage-aware, dynamic
    # ============================================================
    alias = st.session_state.get("alias", "")
    history = load_confidence_history()
    scenarios_viewed = load_scenarios_viewed()
    oneone_topics = load_oneone_topics()
    total_scenarios = 6

    # Determine stage and stats
    current_stage = history[-1].get("stage", "Stage 1 — Building Trust") if history else "Stage 1 — Building Trust"
    stage_num = 1
    if "Stage 2" in current_stage:
        stage_num = 2
    elif "Stage 3" in current_stage:
        stage_num = 3

    # ---- HEADER ----
    st.title("CM Integration Hub")

    # ---- HOSTED vs LOCAL BANNER ----
    if IS_HOSTED:
        st.warning(
            "🌐 **You're viewing the hosted preview.** Browse freely — but notes, confidence checks, "
            "and checklist progress **will not save** between sessions.\n\n"
            "To get the full experience with persistent local storage, "
            "[set up your own copy →](https://github.com/ajamithos/CM-integration-hub#quick-start---local-install)"
        )

    if not alias:
        st.markdown("")
        st.markdown("### 👋 Welcome to the CM Integration Hub")
        st.markdown("")
        st.markdown(
            "A self-contained integration and reference tool built for **Campaign Managers in Model 2**. "
            "Everything you need to work with clarity, consistency, and confidence — "
            "from **Stage 1** through **Stage 3**."
        )
        st.markdown("")
        st.markdown("**What's inside:**")
        st.markdown(
            "- ✅ **Campaign Navigation** — when to Ask, Attempt, or Escalate\n"
            "- ✅ **Communication Decision Tree** — who to contact, what channel, what to say\n"
            "- ✅ **Prioritization Framework** — five principles for competing priorities\n"
            "- ✅ **Scenario Practice** — real CM/CCM situations with suggested approaches\n"
            "- ✅ **Confidence Check** — track your growth across 8 dimensions\n"
            "- ✅ **My Notebook** — notes, 1:1 prep, and downloadable progress reports"
        )
        st.markdown("")
        st.info(
            "🔒 **Your data stays on your machine.** Notes, confidence scores, and progress — "
            "all saved locally in a folder on your laptop. Nothing is uploaded, shared, or visible "
            "to anyone until you share it."
        )
        st.markdown("")
        st.warning(
            "👈 **To get started:** Enter your Amazon alias in the sidebar. "
            "Your dashboard will personalize with your stage, progress, and recommended next steps."
        )
        st.divider()

    if alias:
        st.markdown(f"**Welcome back, {alias}.** &nbsp; `{current_stage}`")

    # ============================================================
    # WHERE YOU ARE — progress bar + summary stats
    # ============================================================
    stage_short = {1: "Building Trust", 2: "Becoming Independent", 3: "Full Integration"}
    st.markdown(f"### 📍 Where You Are — Stage {stage_num}: {stage_short[stage_num]}")

    # Stage progress bar
    progress_pct = (stage_num - 1) / 2.0  # 0.0 for Stage 1, 0.5 for Stage 2, 1.0 for Stage 3
    col_bar, col_labels = st.columns([4, 1])
    with col_bar:
        st.progress(progress_pct)
    with col_labels:
        st.caption(f"Stage {stage_num} of 3")

    # Summary stat row
    latest_avg = 0.0
    avg_trend = ""
    if history:
        latest_avg = sum(history[-1]["scores"].values()) / len(history[-1]["scores"])
        if len(history) >= 2:
            prev_avg = sum(history[-2]["scores"].values()) / len(history[-2]["scores"])
            diff = latest_avg - prev_avg
            if diff > 0:
                avg_trend = f"▲ +{diff:.1f} since last"
            elif diff < 0:
                avg_trend = f"▼ {diff:.1f} since last"
            else:
                avg_trend = "— no change"

    stat1, stat2, stat3, stat4 = st.columns(4)
    with stat1:
        st.metric("Confidence Avg", f"{latest_avg:.1f} / 5" if history else "—", delta=avg_trend if avg_trend else None)
    with stat2:
        st.metric("Check-ins", str(len(history)) if history else "0")
    with stat3:
        st.metric("Scenarios Practiced", f"{len(scenarios_viewed)} / {total_scenarios}")
    with stat4:
        days_label = "—"
        if history:
            last_date_str = history[-1].get("check_date", "")
            if last_date_str:
                try:
                    from datetime import date as dt_date
                    last_date = dt_date.fromisoformat(last_date_str)
                    days_ago = (date.today() - last_date).days
                    days_label = f"{days_ago}d ago" if days_ago > 0 else "Today"
                except (ValueError, TypeError):
                    days_label = "—"
        st.metric("Last Check-in", days_label)

    st.divider()

    # ============================================================
    # SUGGESTED NEXT STEP — smart, context-aware recommendation
    # ============================================================
    st.markdown("### 🎯 Suggested Next Step")

    # Determine the best recommendation based on current state
    if not history and not scenarios_viewed:
        # Brand new — linear onboarding
        st.info(
            "**New here? Here's your path:**\n\n"
            "1️⃣ Start with **Campaign Navigation** — learn when to Ask, Attempt, or Escalate\n\n"
            "2️⃣ Review the **Communication Tree** — know who to contact and how\n\n"
            "3️⃣ Try your first **Scenario** — practice before the real thing\n\n"
            "4️⃣ Do your first **Confidence Check** — set your baseline"
        )
        col_a, col_b = st.columns(2)
        with col_a:
            st.button("📋 Start with Campaign Navigation →", key="dash_start_campaign",
                       on_click=navigate_to, args=("campaign",))
        with col_b:
            st.button("🎯 Jump to Scenario Practice →", key="dash_start_scenarios",
                       on_click=navigate_to, args=("scenarios",))

    elif not history and scenarios_viewed:
        # Has practiced scenarios but no confidence check yet
        st.warning(
            "👋 **You've practiced scenarios but haven't done a Confidence Check yet.** "
            "Take 2 minutes to set your baseline — it helps you and your CCM track growth over time."
        )
        st.button("📊 Do Your First Confidence Check →", key="dash_first_cc",
                   on_click=navigate_to, args=("confidence",))

    else:
        # Has data — give a targeted recommendation
        latest_scores = history[-1]["scores"] if history else {}
        # Find lowest confidence dimension
        if latest_scores:
            lowest_dim = min(latest_scores, key=latest_scores.get)
            lowest_val = latest_scores[lowest_dim]
            dim_labels = {
                "trafficking": "Trafficking", "optimizations": "Optimizations",
                "communication": "Communication", "prioritization": "Prioritization",
                "navigation": "Navigation", "ambiguity": "Ambiguity",
                "partnership": "Partnership", "independence": "Independence",
            }
            # Map dimensions to relevant scenarios
            dim_to_scenario = {
                "trafficking": (0, "First Assignment from Your CCM"),
                "optimizations": (0, "First Assignment from Your CCM"),
                "communication": (5, "Your Stage 1 Integration Is Not Happening"),
                "prioritization": (1, "CCM and M1 Give Conflicting Direction"),
                "navigation": (2, "AE Asks You for Something Directly"),
                "ambiguity": (1, "CCM and M1 Give Conflicting Direction"),
                "partnership": (5, "Your Stage 1 Integration Is Not Happening"),
                "independence": (4, "A Teammate Asks You to Cover"),
            }

            # Find unpracticed scenarios
            unpracticed = [i for i in range(total_scenarios) if i not in scenarios_viewed]

            if lowest_val <= 3 and lowest_dim in dim_to_scenario:
                rec_idx, rec_title = dim_to_scenario[lowest_dim]
                practiced_tag = "✓ already practiced" if rec_idx in scenarios_viewed else "not yet practiced"

                st.info(
                    f"**Your lowest confidence area: {dim_labels.get(lowest_dim, lowest_dim)} ({lowest_val}/5)**\n\n"
                    f"→ Try scenario: **\"{rec_title}\"** ({practiced_tag}) — it directly exercises "
                    f"{dim_labels.get(lowest_dim, lowest_dim).lower()} skills."
                )
                st.button("🎯 Go to Scenario Practice →", key="dash_rec_scenario",
                           on_click=navigate_to, args=("scenarios",))

            elif unpracticed:
                scenario_titles = [
                    "First Assignment from Your CCM",
                    "CCM and M1 Give Conflicting Direction",
                    "AE Asks You for Something Directly",
                    "You Trafficked the Wrong Flight Dates",
                    "A Teammate Asks You to Cover",
                    "Your Stage 1 Integration Is Not Happening"
                ]
                next_title = scenario_titles[unpracticed[0]]
                st.info(
                    f"**{len(unpracticed)} scenario(s) remaining.** "
                    f"Next up: **\"{next_title}\"**"
                )
                st.button("🎯 Continue Scenario Practice →", key="dash_continue_scenario",
                           on_click=navigate_to, args=("scenarios",))

            elif len(history) == 1:
                st.success(
                    "**All scenarios practiced. Nice work.** "
                    "Do another Confidence Check in a few days to track how your confidence changes with experience."
                )
                st.button("📊 Confidence Check →", key="dash_next_cc",
                           on_click=navigate_to, args=("confidence",))
            else:
                last_check_str = history[-1].get("check_date", "")
                try:
                    last_dt = date.fromisoformat(last_check_str)
                    days_since = (date.today() - last_dt).days
                except (ValueError, TypeError):
                    days_since = 999

                if days_since >= 7:
                    st.warning(
                        f"**It's been {days_since} days since your last Confidence Check.** "
                        "Regular check-ins help you and your CCM track real progress."
                    )
                    st.button("📊 Do a Confidence Check →", key="dash_overdue_cc",
                               on_click=navigate_to, args=("confidence",))
                else:
                    st.success(
                        "**You're on track.** All scenarios practiced. Confidence check is current. "
                        "Keep building reps — review scenarios again, prep for your next 1:1, or explore reference docs."
                    )

    st.divider()

    # ============================================================
    # QUICK SNAPSHOT — 3 live metric cards
    # ============================================================
    st.markdown("### 📊 Quick Snapshot")

    snap1, snap2, snap3 = st.columns(3)

    with snap1:
        st.markdown("**📊 Confidence**")
        if history:
            latest = history[-1]
            avg = sum(latest["scores"].values()) / len(latest["scores"])
            # Mini dimension bars
            sorted_dims = sorted(latest["scores"].items(), key=lambda x: x[1], reverse=True)
            for key, val in sorted_dims[:4]:  # Top 4 only for compactness
                bar = "●" * val + "○" * (5 - val)
                st.caption(f"{key.capitalize()}: {bar}")
            if len(sorted_dims) > 4:
                st.caption(f"*+{len(sorted_dims) - 4} more dimensions*")
        else:
            st.caption("No check-ins yet")
        st.button("Open Confidence Check →", key="dash_snap_cc",
                   on_click=navigate_to, args=("confidence",))

    with snap2:
        st.markdown("**🎯 Scenarios**")
        if scenarios_viewed:
            scenario_titles = [
                "First Assignment", "Conflicting Direction",
                "AE Direct Ask", "Wrong Flight Dates",
                "Cover a Teammate", "Stage 1 Integration"
            ]
            for i, title in enumerate(scenario_titles):
                status = "✅" if i in scenarios_viewed else "⬜"
                st.caption(f"{status} {title}")

            # All cards complete — offer reset
            if len(scenarios_viewed) >= total_scenarios:
                st.markdown("")
                st.success("🎉 All scenarios completed!")
                if st.button("🔄 Reset & Retry", key="dash_reset_scenarios"):
                    user_dir = get_user_dir()
                    viewed_file = user_dir / "scenarios_viewed.json"
                    if viewed_file.exists():
                        viewed_file.unlink()
                    st.rerun()
        else:
            st.caption("No scenarios practiced yet")
        st.button("Open Scenario Practice →", key="dash_snap_sc",
                   on_click=navigate_to, args=("scenarios",))
    with snap3:
        st.markdown("**📝 1:1 Prep**")
        topic_count = len([l for l in oneone_topics.strip().splitlines() if l.strip()]) if oneone_topics else 0
        if topic_count:
            st.caption(f"{topic_count} topic(s) saved")
            # Show first 3 topics
            for line in oneone_topics.strip().splitlines()[:3]:
                if line.strip():
                    st.caption(f"• {line.strip()[:50]}{'...' if len(line.strip()) > 50 else ''}")
        else:
            st.caption("No 1:1 topics saved yet")
        notes_text = load_notes()
        if notes_text:
            st.caption(f"📝 {len(notes_text.strip().splitlines())} lines of notes")
        st.button("Open My Notebook →", key="dash_snap_notes",
                   on_click=navigate_to, args=("notes",))

    st.divider()

    # ============================================================
    # ACTION NEEDED — contextual nudges
    # ============================================================
    actions = []

    if not history:
        actions.append(("📊", "Complete your first **Confidence Check** to set a baseline and unlock your Progress Report.", "confidence"))

    if history and len(history) >= 1:
        last_check_str = history[-1].get("check_date", "")
        try:
            last_dt = date.fromisoformat(last_check_str)
            days_since = (date.today() - last_dt).days
            if days_since >= 7:
                actions.append(("📊", f"Your last Confidence Check was **{days_since} days ago**. Time for a refresh.", "confidence"))
        except (ValueError, TypeError):
            pass

    if len(scenarios_viewed) < total_scenarios:
        remaining = total_scenarios - len(scenarios_viewed)
        actions.append(("🎯", f"**{remaining} scenario(s)** remaining. Practice builds muscle memory.", "scenarios"))

    if not oneone_topics or not oneone_topics.strip():
        actions.append(("📝", "Add **1:1 topics** to your notebook before your next sync with your CCM or M1.", "notes"))

    if actions:
        st.markdown("### ⚡ Action Needed")
        for icon, msg, page_key in actions:
            col_msg, col_btn = st.columns([4, 1])
            with col_msg:
                st.markdown(f"{icon} {msg}")
            with col_btn:
                st.button("Go →", key=f"dash_action_{page_key}_{msg[:20]}", on_click=navigate_to, args=(page_key,))
        st.divider()

    # ============================================================
    # QUICK REFERENCE — deep links to high-value content
    # ============================================================
    st.markdown("### 💡 Quick Reference")
    ref1, ref2, ref3, ref4, ref5 = st.columns(5)
    with ref1:
        st.button("⏱️ 15-Minute Rule", key="dash_ref_15min", on_click=navigate_to, args=("campaign",))
    with ref2:
        st.button("🔺 Escalation Path", key="dash_ref_escalation", on_click=navigate_to, args=("comms",))
    with ref3:
        st.button("⚡ Prioritization", key="dash_ref_priority", on_click=navigate_to, args=("priority",))
    with ref4:
        st.button("📄 Reference Docs", key="dash_ref_docs", on_click=navigate_to, args=("docs",))
    with ref5:
        st.link_button("📋 Workflow SOP ↗", "https://w.amazon.com/bin/view/Users/ajamitho/CM-UAT-Test/")


def render_campaign_navigation():
    st.title(t("cn_title"))
    st.markdown(t("cn_subtitle"))
    st.divider()

    # ============================================================
    # STAGE SELECTOR AT TOP — drives everything below
    # ============================================================
    global_stage = st.session_state.get("global_stage", "Stage 1 — Building Trust")
    if "Stage 1" in global_stage:
        stage_num = 1
        stage_label = "Stage 1 — Building Trust"
        stage_focus = t("cn_stage1_focus")
    elif "Stage 2" in global_stage:
        stage_num = 2
        stage_label = "Stage 2 — Becoming Independent"
        stage_focus = t("cn_stage2_focus")
    else:
        stage_num = 3
        stage_label = "Stage 3 — Full Integration"
        stage_focus = t("cn_stage3_focus")

    st.markdown(f"### {t('cn_stage_header').format(stage_label)}")
    st.caption(stage_focus + " — " + t("cn_stage_change"))
    st.markdown("")

    # ============================================================
    # ASK / ATTEMPT / ESCALATE — stage-aware content
    # ============================================================
    col1, col2, col3 = st.columns(3)

    # --- STAGE-SPECIFIC ASK ITEMS ---
    stage_suffix = f"s{stage_num}"
    ask_items = t(f"cn_ask_items_{stage_suffix}")
    ask_who = t(f"cn_ask_who_{stage_suffix}")

    # --- STAGE-SPECIFIC ATTEMPT ITEMS ---
    attempt_items = t(f"cn_attempt_items_{stage_suffix}")
    attempt_who = t(f"cn_attempt_who_{stage_suffix}")

    # --- STAGE-SPECIFIC ESCALATE ITEMS ---
    escalate_items = t(f"cn_escalate_items_{stage_suffix}")
    escalate_who = t(f"cn_escalate_who_{stage_suffix}")

    with col1:
        st.markdown(f"### {t('cn_ask_title')}")
        st.markdown(t("cn_ask_when"))
        for item in ask_items:
            st.markdown(f"- {item}")
        st.info(ask_who)

    with col2:
        st.markdown(f"### {t('cn_attempt_title')}")
        st.markdown(t("cn_attempt_when"))
        for item in attempt_items:
            st.markdown(f"- {item}")
        st.success(attempt_who)

    with col3:
        st.markdown(f"### {t('cn_escalate_title')}")
        st.markdown(t("cn_escalate_when"))
        for item in escalate_items:
            st.markdown(f"- {item}")
        st.error(escalate_who)

    st.divider()

    st.markdown(f"### {t('cn_15min_title')}")
    st.warning(t("cn_15min_body"))

    st.divider()

    st.markdown(f"### {t('cn_guardrails_title')}")
    if stage_num <= 2:
        for item in t("cn_guardrails_items"):
            st.markdown(f"🚫 {item}")
    else:
        for item in t("cn_guardrails_s3"):
            st.markdown(f"🚫 {item}")

    st.divider()

    # ============================================================
    # SOP BY STAGE — Stage-specific responsibilities from the Workflow SOP
    # ============================================================
    st.markdown(f"### {t('cn_sop_title')}")
    st.caption(t("cn_sop_source"))

    if stage_num == 1:
        st.markdown(t("cn_sop_duration"))
        st.markdown(t("cn_sop_s1_focus"))
        st.markdown("")

        ccm_col, cm_col = st.columns(2)
        with ccm_col:
            st.markdown(t("cn_sop_ccm_title"))
            st.markdown(t("cn_sop_s1_ccm"))
        with cm_col:
            st.markdown(t("cn_sop_cm_title"))
            st.markdown(t("cn_sop_s1_cm"))

    elif stage_num == 2:
        st.markdown(t("cn_sop_duration"))
        st.markdown(t("cn_sop_s2_focus"))
        st.markdown("")

        ccm_col, cm_col = st.columns(2)
        with ccm_col:
            st.markdown(t("cn_sop_ccm_title"))
            st.markdown(t("cn_sop_s2_ccm"))
        with cm_col:
            st.markdown(t("cn_sop_cm_title"))
            st.markdown(t("cn_sop_s2_cm"))

    else:  # Stage 3
        st.markdown(t("cn_sop_duration"))
        st.markdown(t("cn_sop_s3_focus"))
        st.info(t("cn_sop_s3_note"))
        st.markdown("")

        # Stage 3: single unified column — it's a partnership, not a split
        st.markdown(t("cn_sop_s3_practice_title"))
        st.markdown(t("cn_sop_s3_practice"))

        st.markdown("")
        with st.expander(t("cn_sop_client_facing_title")):
            st.markdown(t("cn_sop_client_facing"))

    st.divider()

    # ============================================================
    # CCM-CM ALIGNMENT CHECKLIST — stage-specific (not cumulative)
    # ============================================================
    st.markdown(t("cn_checklist_title"))
    st.caption(t("cn_checklist_caption").format(stage_label))

    # Load/save checklist state
    user_dir = get_user_dir()
    checklist_file = user_dir / "alignment_checklist.json"
    if checklist_file.exists():
        with open(checklist_file, "r", encoding="utf-8") as f:
            checklist_state = json.load(f)
    else:
        checklist_state = {}

    # Stage-specific checklist items — pull labels from translation dict
    checklist_keys_s1 = ["s1_intro_call", "s1_daily_cadence", "s1_slack_channels", "s1_weekly_syncs", "s1_email_distro", "s1_sf_access", "s1_regular_syncs"]
    checklist_keys_s2 = ["s2_open_independently", "s2_ccm_qa_only", "s2_team_call_updates", "s2_project_brainstorm"]
    checklist_keys_s3 = ["s3_self_qa", "s3_full_ownership", "s3_proactive_tracking", "s3_coaching"]

    if stage_num == 1:
        checklist_keys = checklist_keys_s1
        checklist_labels = t("cn_checklist_s1")
    elif stage_num == 2:
        checklist_keys = checklist_keys_s2
        checklist_labels = t("cn_checklist_s2")
    else:
        checklist_keys = checklist_keys_s3
        checklist_labels = t("cn_checklist_s3")

    items_to_show = list(zip(checklist_keys, checklist_labels))

    changed = False
    for key, label in items_to_show:
        current_val = checklist_state.get(key, False)
        new_val = st.checkbox(label, value=current_val, key=f"checklist_{key}")
        if new_val != current_val:
            checklist_state[key] = new_val
            changed = True

    if changed:
        with open(checklist_file, "w", encoding="utf-8") as f:
            json.dump(checklist_state, f, indent=2)
        st.rerun()

    # Progress summary for current stage
    completed = sum(1 for key, _ in items_to_show if checklist_state.get(key, False))
    total = len(items_to_show)
    st.progress(completed / total if total > 0 else 0)
    st.caption(t("cn_checklist_complete").format(completed, total, stage_label))


def render_communication_tree():
    # Force scroll to top when navigating to this page
    st.markdown('<div id="cdt-top"></div>', unsafe_allow_html=True)
    st.title(t("cdt_title"))
    st.markdown(t("cdt_subtitle"))

    # Read global stage
    global_stage = st.session_state.get("global_stage", "Stage 1 — Building Trust")
    if "Stage 1" in global_stage:
        stage_num = 1
    elif "Stage 2" in global_stage:
        stage_num = 2
    else:
        stage_num = 3

    st.caption(t("cdt_stage_caption").format(global_stage))
    st.divider()

    # ============================================================
    # VISUAL DECISION TREE — boxed columns, stage-aware
    # ============================================================

    st.markdown(t("cdt_what_happening"))
    st.markdown("")

    # Stage-aware language maps
    if stage_num <= 2:
        question_cta = t("cdt_s12_question_cta")
        question_example = t("cdt_s12_question_example")
        blocked_escalation = t("cdt_s2_blocked_escalation") if stage_num == 2 else t("cdt_s1_blocked_escalation")
        blocked_example = t("cdt_s12_blocked_example")
        error_cta = t("cdt_s12_error_cta")
        request_flow = t("cdt_s12_request_flow")
    else:  # Stage 3
        question_cta = t("cdt_s3_question_cta")
        question_example = t("cdt_s3_question_example")
        blocked_escalation = t("cdt_s3_blocked_escalation")
        blocked_example = t("cdt_s3_blocked_example")
        error_cta = t("cdt_s3_error_cta")
        request_flow = t("cdt_s3_request_flow")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.container(border=True).markdown(f"""
{t("cdt_box_question")}

⬇

{question_cta}

{question_example}
""")

    with col2:
        st.container(border=True).markdown(f"""
{t("cdt_box_blocked")}

⬇

{t("cdt_blocked_responded")}

{t("cdt_blocked_yes")}

{t("cdt_blocked_no_15")}
{blocked_escalation}

{blocked_example}
""")

    with col3:
        st.container(border=True).markdown(f"""
{t("cdt_box_error")}

⬇

{error_cta}

{t("cdt_error_example")}
""")

    with col4:
        st.container(border=True).markdown(f"""
{t("cdt_box_request")}

⬇

{t("cdt_request_acknowledge")}

{request_flow}
""")

    with col5:
        st.container(border=True).markdown(f"""
{t("cdt_box_update")}

⬇

{t("cdt_update_who")}

{t("cdt_update_ccm_only")}

{t("cdt_update_full_team")}

{t("cdt_update_example")}
""")

    st.divider()

    # -- ESCALATION PATH — stage-aware --
    st.markdown(t("cdt_escalation_title"))
    st.markdown("")

    esc1, esc2, esc3 = st.columns(3)

    if stage_num <= 2:
        with esc1:
            st.info(t("cdt_s12_esc1"))
        with esc2:
            st.warning(t("cdt_s12_esc2"))
        with esc3:
            st.error(t("cdt_s12_esc3"))
    else:  # Stage 3
        with esc1:
            st.info(t("cdt_s3_esc1"))
        with esc2:
            st.warning(t("cdt_s3_esc2"))
        with esc3:
            st.error(t("cdt_s3_esc3"))

    st.divider()

    # -- CHANNEL GUIDE TABLE --
    st.markdown(f"### {t('cdt_channel_title')}")
    headers = t("cdt_channel_headers")
    rows = t("cdt_channel_rows")

    table_md = f"| {' | '.join(headers)} |\n| {' | '.join(['---'] * len(headers))} |\n"
    for row in rows:
        table_md += f"| {' | '.join(row)} |\n"
    st.markdown(table_md)

    st.divider()

    # -- URGENCY SIGNALS --
    st.markdown(t("cdt_urgency_title"))
    sig1, sig2, sig3 = st.columns(3)
    with sig1:
        st.container(border=True).markdown(t("cdt_urgency_emoji"))
    with sig2:
        st.container(border=True).markdown(t("cdt_urgency_time"))
    with sig3:
        st.container(border=True).markdown(t("cdt_urgency_doubt"))

def render_prioritization():
    st.title(t("pf_title"))
    st.markdown(t("pf_subtitle"))
    st.info(t("pf_note"))
    st.divider()

    for principle in t("pf_principles"):
        st.markdown(f"### {principle['title']}")
        st.markdown(principle["body"])
        st.markdown("---")


def render_scenarios():
    st.title(t("sp_title"))
    st.divider()

    if "current_card_index" not in st.session_state:
        st.session_state.current_card_index = 0
    if "card_order" not in st.session_state:
        st.session_state.card_order = list(range(6))

    # ============================================================
    # SCENARIO CARDS — Grounded in CCM Language & Operations Brief
    # ============================================================
    scenario_cards = [
        {
            "category": "Relationship Building",
            "title": "First Assignment from Your CCM",
            "scenario": """Your CCM Slacks you: "Hey! Just opened the Tron FR CM Task — SF link is here. Statics are in, videos still pending from the agency. Let me know if you have questions, I'm in a sync til 11 but free after."

You open the Salesforce assignment. The FR has a static creative ready, but the video asset is not in the folder yet. The notes say "video pending from [agency], expected today." SLA is 1 business day.

It is 10:15 AM. **What do you do?**""",
            "approach": """**One way to handle this:**

1. **Acknowledge receipt immediately** — Slack your CCM back: *"Got it — I'll start trafficking what I can in Rodeo and check back this afternoon on the video. Let me know if anything changes."* A ✅ or 👀 emoji also works for initial receipt — full sentences are not required for acknowledgment.

2. **Work on what you can** — Open Rodeo and begin trafficking the static placement. Do not wait for the video to start making progress. Blocked does not mean paused — it means parallel. *(See Prioritization Principle #3: Blocked work gets communicated, not buried.)*

3. **Set a check-in time** — If the video creative has not arrived by 3 PM, Slack your CCM: *"Checking in on the [product] [placement] video — still pending in the folder. Want me to follow up with anyone, or are you tracking it?"*

4. **If it still has not arrived by EOD**, flag the status: *"Putting the [product] [placement] on Pending Advertiser — video from [agency] still outstanding. Static placement is trafficked and ready. Will recheck tomorrow AM."*

**Why this works:**
- You referenced the assignment by its actual name, not "a DSP trafficking assignment"
- You acknowledged in Slack immediately, respecting your CCM's sync schedule
- You made progress on what was available instead of waiting
- You communicated the blocker proactively without over-escalating
- You used Pending Advertiser status correctly — the blocker is external (agency creative)""",
            "principles": []
        },
        {
            "category": "Navigating Ambiguity",
            "title": "Your CCM and M1 Give Conflicting Direction",
            "scenario": """Your CCM Slacks you: ":alert: Can you prioritize the [product] [placement]? Goes live tonight, needs to be trafficked and pushed to Rodeo ASAP."

Thirty minutes later, your M1 pings you on Slack: "The QBR deck needs your input by EOD — top priority."

Both are legitimate asks. The [placement] is time-sensitive (goes live tonight). The QBR is an M1 directive with an EOD deadline. You cannot do both well in the time remaining.

**What do you do?**""",
            "approach": """**One way to handle this:**

1. **Do not choose in silence** — Both requests came from people with legitimate authority over your work. Choosing one without communicating puts you in a no-win position.

2. **Bring the conflict to your CCM first** — Slack your CCM: *"Quick heads up — [M1] just asked me to prioritize QBR input by EOD. I know the [product] [placement] goes live tonight and needs to be trafficked. Can you send this one to the queue, or should I flag [M1] of the conflict? I want to make sure I'm prioritizing correctly."*

3. **Apply your prioritization framework** — The [placement] is a live-tonight, client-facing risk (Prioritization Principle #1: live campaigns before future campaigns, and Principle #2: client-facing risk before internal deadlines). The QBR deck is an internal deadline. Your framework says client-facing risk comes first — but the CCM and M1 need to align on that together.

4. **Give your CCM the option to resolve it** — They may know context you don't (e.g., the launch can be delayed, or the QBR is actually non-negotiable). Or they may choose to escalate to [M1] themselves.

5. **Once aligned**, confirm back: *"Got it — focusing on the [product] [placement] first, will push to Rodeo by [time]. Will pick up QBR input after. Let me know if anything changes."*

**Why this works:**
- You recognized the urgency signals (":alert:", "goes live tonight", "ASAP")
- You did not ghost either request
- You gave your CCM a clear either/or — not a vague "what should I do?"
- You gave your CCM the information they needed to make the call with [M1]
- You demonstrated that partnership means shared decision-making, not unilateral task execution""",
            "principles": [1, 2]
        },
        {
            "category": "Communication Boundaries",
            "title": "The AE Asks You for Something Directly",
            "scenario": """Your AE ([AE name]) Slacks you directly: "Hey — can you send me the trafficking confirmation for the [product] [placement]? The client wants to verify flight dates before launch."

Your CCM has not mentioned this to you. You know where the assignment lives in Salesforce, and you can pull the confirmation from Rodeo. This request is going to the client.

**What do you do?**""",
            "approach": """**One way to handle this:**

**Stage 1–2: Do the work, then validate before sending.**

1. **Acknowledge the AE immediately** — Respond in the same Slack channel: *"Got it, [AE name] — pulling that now. Give me a few minutes."*

2. **Do the work** — Pull the trafficking confirmation from Rodeo. Verify the flight dates match the assignment. Get it ready to send.

3. **Validate with your CCM before sending** — Slack your CCM: *"[AE name] asked for the trafficking confirmation on the [product] [placement] — client wants to verify flight dates. I've pulled it from Rodeo. Good to send to [AE name]?"*

4. **Once confirmed, send it** — Respond to the AE with the confirmation. You did the work; your CCM signed off on the last mile.

**Stage 3: Handle it end-to-end.**

1. Pull the confirmation from Rodeo, verify the details, and send it directly to [AE name].
2. Give your CCM a heads-up after the fact: *"FYI — [AE name] asked for the [product] [placement] trafficking confirmation for the client. Pulled it and sent it over. Flight dates confirmed."*

**Why this works:**
- You responded promptly to the AE without freezing or deflecting
- In Stage 1–2, you did the actual work — you didn't just relay a message. You validated before sending because client-facing communication flows through the CCM.
- In Stage 3, you handled it independently and kept your CCM informed
- You referenced the campaign by name, not "the assignment"
- You understood that AEs communicate directly with the pod constantly — that is normal""",
            "principles": []
        },
        {
            "category": "Trust and Accountability",
            "title": "You Trafficked the Wrong Flight Dates",
            "scenario": """You submitted the [product] [placement] trafficking assignment yesterday. This morning, you are reviewing your work and realize the flight start date is one day early — September 18 instead of September 19. The campaign is not PTS yet, so nothing is live.

Your CCM has not mentioned it. Nobody has noticed yet.

**What do you do?**""",
            "approach": """**One way to handle this:**

**If it is NOT PTS (not live) — just fix it.**

1. **Amend the assignment** — Open Rodeo, correct the flight start date from 9/18 to 9/19, and resubmit.

2. **Note the correction** — You can add a note on the assignment (*"Corrected flight start from 9/18 to 9/19"*) or give your CCM a quick heads-up: *"FYI — caught a date error on the [product] [placement], corrected it in Rodeo. 9/18 → 9/19. Nothing went live."* This is not mandatory — use your judgment on whether your CCM needs to know.

3. **Move on** — The assignment was not PTS. No ads served. No client impact. Fix it, note it, keep working.

**If it IS live (post-PTS) — that is a different situation.**

1. **Notify your CCM immediately** — Slack your CCM: *"Heads up — the [product] [placement] went live with the wrong flight start. Should have been 9/19 but it's been serving since 9/18. I'm looking at the delivery impact now. What do you want me to do?"*

2. **Assess the impact** — Check delivery numbers. Is the spend material? Is the client going to notice? This determines the severity of the response.

3. **Follow your CCM's lead on remediation** — They will decide whether the client needs to be informed, whether a make-good is needed, or whether the variance is immaterial.

**Why this works:**
- Pre-PTS: You caught it, fixed it, moved on. That is how quality control works — catch errors before they become client issues.
- Post-PTS: You escalated immediately because a live error has client impact. You gave your CCM the information they need to decide next steps.
- You understood PTS as the critical dividing line between "fix it quietly" and "escalate now"
- You referenced the campaign by name and the specific error (flight dates)""",
            "principles": []
        },
        {
            "category": "Boundaries and Prioritization",
            "title": "A Teammate Asks You to Cover Their Assignment",
            "scenario": """Another CM on an adjacent account Slacks you: "I'm slammed — can you jump into the [product] [placement] in Salesforce and submit the trafficking? It's straightforward, just needs to go out today."

You are not on that account. You have not seen the order in OMS, the MPT, or the SF opp. You do not know the client's preferences or the CCM's communication style on that account. But the ask seems small and you want to be helpful.

**What do you do?**""",
            "approach": """**One way to handle this:**

**Stage 1–2: Check with your CCM first.**

1. **Do not say yes immediately** — Even if it seems straightforward, you do not have context on that account. You do not know the advertiser's history, the CCM's preferences, or whether "straightforward" actually means straightforward. You also do not know if their CCM is aware of this request.

2. **Check with your CCM** — Slack your CCM: *"[CM name] asked if I can help submit the [product] [placement] trafficking on [their account]. They're slammed and said it's straightforward. Do you want me to help, or should I stay focused on our work?"*

3. **If your CCM says yes**, Slack the other CM: *"I can help — but I'll need you to walk me through the specifics since I'm not on your account. Can you send me the SF link and MPT? And is your CCM aware? I don't want to submit something without their visibility."*

4. **If your CCM says no**, Slack the other CM: *"I wish I could help, but I'm at capacity on [account name]. Have you flagged this with your CCM or [M1]? They might have other options."*

**Stage 3: You own your bandwidth.**

1. **Make the call yourself** — You know your workload, your priorities, and your SLA commitments. If you have the bandwidth and the other CM's CCM is aware, you can say yes.

2. **If you help**, get the SF link, MPT, and any account-specific context from the other CM. Ensure their CCM has visibility before you submit.

3. **If you decline**, be direct: *"Can't take it on today — I've got [reason]. Have you flagged [M1] or your CCM?"*

5. **Never mix products in a single trafficking assignment** — If you do help, make sure you understand the scope. Each product gets its own assignment.

**Why this works:**
- In Stage 1–2, you did not create a commitment your CCM does not know about
- In Stage 3, you exercised independent judgment on your own bandwidth
- You ensured the other account's CCM has visibility before you touch their work
- You referenced the campaign correctly and asked for the right artifacts (SF link, MPT)
- You demonstrated that "being helpful" means being thoughtful, not saying yes to everything""",
            "principles": [4, 5]
        },
        {
            "category": "Integration & Onboarding",
            "title": "Your Stage 1 Integration Is Not Happening",
            "scenario": """You have been on the account for two weeks. Your CCM is friendly and responsive when you reach out, but the structural integration has not happened. You are not CC'd on account emails. You were not added to the account pod's internal calls. Assignments arrive in your queue without context — no heads-up, no Slack, no link to the related SF opp.

You are not being excluded intentionally — your CCM is just used to doing everything themselves. They have been running this account solo for a long time, and the habit of working with a CM partner has not formed yet.

You need the integration to happen so you can actually do your job. But you do not want to come across as demanding or critical.

**What do you do?**""",
            "approach": """**One way to handle this:**

1. **Name the gap directly, but frame it as operational** — Bring it up in your daily sync or Slack your CCM: *"Hey — I want to make sure I'm set up to support you fully. Right now I'm not on the account email distribution or the pod call invite, so I'm missing context on what's coming in. Can we get those set up this week?"*

2. **Make specific, low-lift asks** — Do not say "loop me in more." Give your CCM a concrete checklist:
   - *"Add me to the [account name] email distribution list"*
   - *"Put me on the weekly pod call invite"*
   - *"Tag me on Slack when AE requests come in so I can see them in real time"*
   - *"Send me the SF link when you open assignments so I can start building context"*

3. **Frame it as your SOP** — The Stage 1 integration framework says the CM should be embedded in the account's communication channels from Week 1. You are not asking for a favor — you are asking for the baseline setup that the model requires. *"I know the SOP has a Stage 1 integration checklist — can we run through it together to make sure I'm not missing anything?"*

4. **Follow up if it does not happen** — One conversation will not change years of muscle memory. If you are still not CC'd on emails after a week, follow up: *"Hey — I'm still not seeing the account emails come through. Can you check if I was added to the distribution? Want to make sure it didn't get lost."*

5. **If it persists, involve your [M1]** — If structural integration has not happened after two follow-ups, bring it to your [M1] in your next 1:1. Frame it factually: *"I've asked [CCM] twice about getting added to account emails and pod calls. It hasn't happened yet. Can you help unblock this?"*

**Why this works:**
- You framed the issue as structural (setup that needs to happen) not interpersonal (CCM excluding you)
- You gave specific, actionable asks — not vague "include me more"
- You referenced the SOP integration framework — you are advocating for the model, not just for yourself
- You had a clear escalation path: ask CCM → follow up → involve [M1]
- You demonstrated that advocacy and professionalism are not in conflict""",
            "principles": []
        }
    ]
    current_index = st.session_state.card_order[st.session_state.current_card_index]
    current_card = scenario_cards[current_index]
    total_cards = len(scenario_cards)

    # Prioritization principles — used for inline dropdowns on cards that reference them
    prioritization_principles = {
        1: ("Live campaigns before future campaigns",
            "If something is live and broken, it takes priority over something that has not launched yet. A tracking pixel that is not firing on a live campaign matters more than a trafficking assignment due tomorrow."),
        2: ("Client-facing risk before internal deadlines",
            "If an issue could result in the client seeing something wrong — wrong creative, wrong dates, wrong delivery — it jumps the queue. Internal trackers and reports can wait; client trust cannot."),
        3: ("Blocked work gets communicated, not buried",
            "If you are blocked, do not silently move to the next task and hope the blocker resolves itself. Flag it. Tell your CCM. Then work on what you can while you wait. Blocked does not mean paused — it means parallel."),
        4: ("SLA proximity drives urgency, not assignment order",
            "A task due in 4 hours matters more than a task due in 3 days, even if the 3-day task arrived first. Check your SLAs every morning and re-sort your queue accordingly."),
        5: ("When two things are equally urgent, choose the one with the most dependencies",
            "If your trafficking assignment unblocks the creative team, QA, and the CCM's client update — do that one first. Unblocking other people multiplies your impact."),
    }

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"**{t('sp_card_progress').format(st.session_state.current_card_index + 1, total_cards)}**")
    with col2:
        if st.button(t("sp_shuffle_btn"), key="shuffle_btn"):
            import random
            st.session_state.card_order = list(range(total_cards))
            random.shuffle(st.session_state.card_order)
            st.session_state.current_card_index = 0
            st.rerun()

    st.divider()

    st.markdown(f"**{t('sp_category_label')}** `{current_card['category']}`")
    st.markdown("")
    st.markdown(f"### {current_card['title']}")
    st.markdown("")
    st.markdown(current_card['scenario'])
    st.markdown("")
    st.info(t("sp_think_prompt"))
    st.markdown("")

    # Unique key per card forces Streamlit to reset expander state on card flip
    card_key = f"reveal_{current_index}_{st.session_state.current_card_index}"

    with st.expander(t("sp_reveal_btn"), expanded=False, key=f"approach_{card_key}"):
        st.markdown(current_card['approach'])
        # Track that this card was viewed/flipped
        save_scenario_viewed(current_index)

    # Show referenced Prioritization Principles as a dropdown below the approach
    card_principles = current_card.get("principles", [])
    if card_principles:
        with st.expander(f"⚡ Prioritization Principles Referenced (#{', #'.join(str(p) for p in card_principles)})", key=f"principles_{card_key}"):
            for p_num in card_principles:
                p_title, p_body = prioritization_principles.get(p_num, ("", ""))
                st.markdown(f"**Principle #{p_num}: {p_title}**")
                st.markdown(p_body)
                st.markdown("")

    st.divider()

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button(t("sp_prev_btn"), disabled=(st.session_state.current_card_index == 0), key="prev_btn"):
            st.session_state.current_card_index -= 1
            st.rerun()
    with col3:
        if st.button(t("sp_next_btn"), disabled=(st.session_state.current_card_index >= total_cards - 1), key="next_btn"):
            st.session_state.current_card_index += 1
            st.rerun()

    st.markdown("")
    st.caption(t("sp_footer"))


def render_confidence_check():
    # Force scroll to top when navigating to this page
    st.markdown('<div id="cc-top"></div>', unsafe_allow_html=True)
    st.title(t("cc_title"))
    st.markdown(t("cc_subtitle"))
    st.info("📋 **Not sure what stage you're in?** Review the [Integration SOP](https://w.amazon.com/bin/view/Users/ajamitho/CM-UAT-Test/) — it defines each stage, duration, and what's expected of you and your CCM.")
    st.markdown(t("cc_instruction"))
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        stage_options = t("cc_stages")
        # Pre-select based on global stage
        global_stage = st.session_state.get("global_stage", stage_options[0])
        default_idx = 0
        for i, opt in enumerate(stage_options):
            if global_stage and any(kw in opt for kw in global_stage.split("—")[0].strip().split()):
                default_idx = i
                break
        selected_stage = st.selectbox(
            t("cc_stage_label"),
            options=stage_options,
            index=default_idx,
            key="cc_stage_select"
        )
    with col2:
        check_date = st.date_input(
            t("cc_date_label"),
            value=date.today(),
            key="cc_date_input"
        )

    st.divider()

    dimensions = t("cc_dimensions")
    scores = {}

    for dim in dimensions:
        scores[dim["key"]] = st.slider(
            dim["label"],
            min_value=1,
            max_value=5,
            value=3,
            key=f"cc_{dim['key']}"
        )

    st.divider()

    reflection = st.text_area(
        t("cc_reflection_label"),
        placeholder=t("cc_reflection_placeholder"),
        height=100,
        key="cc_reflection"
    )

    st.divider()

    if st.button(t("cc_save_btn"), type="primary"):
        date_display = save_confidence_check(
            scores,
            selected_stage,
            str(check_date),
            reflection
        )
        st.success(t("cc_saved_msg").format(date_display))

    st.divider()
    st.markdown(f"### {t('cc_history_title')}")

    history = load_confidence_history()
    if history:
        for entry in reversed(history[-10:]):
            avg = sum(entry["scores"].values()) / len(entry["scores"])
            bar = "█" * int(avg) + "░" * (5 - int(avg))
            stage_label = entry.get("stage", "—")
            check_dt = entry.get("check_date", entry.get("date_display", "—"))
            with st.expander(f"**{check_dt}** — {stage_label} — {bar} {avg:.1f}/5.0"):
                for key, val in entry["scores"].items():
                    score_bar = "●" * val + "○" * (5 - val)
                    st.markdown(f"  {key.capitalize()}: {score_bar} ({val}/5)")
                if entry.get("reflection"):
                    st.markdown(f"\n**Reflection:** {entry['reflection']}")

    else:
        st.caption(t("cc_no_history"))

    # ============================================================
    # EXPORT CONFIDENCE HISTORY AS CSV
    # ============================================================
    if history:
        st.divider()
        st.markdown("### 📥 Export Confidence Data")
        st.caption("Download your full confidence check history as a CSV file to share with your CCM, M1, or facilitator.")

        # Build CSV content
        dim_keys = ["trafficking", "optimizations", "communication", "prioritization", "navigation", "ambiguity", "partnership", "independence"]
        csv_lines = ["Date,Stage," + ",".join([k.capitalize() for k in dim_keys]) + ",Average,Reflection"]
        for entry in history:
            check_dt = entry.get("check_date", entry.get("date_display", ""))
            stage = entry.get("stage", "").replace(",", " ")
            scores_vals = [str(entry["scores"].get(k, "")) for k in dim_keys]
            avg = sum(entry["scores"].values()) / len(entry["scores"])
            reflection = entry.get("reflection", "").replace(",", " ").replace("\n", " ")
            csv_lines.append(f"{check_dt},{stage},{','.join(scores_vals)},{avg:.1f},{reflection}")
        csv_text = "\n".join(csv_lines)

        alias = st.session_state.get("alias", "anonymous")
        st.download_button(
            label="📊 Download Confidence History (.csv)",
            data=csv_text,
            file_name=f"confidence_history_{alias}_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            key="download_confidence_csv"
        )


def render_notes():
    st.title(t("notes_title"))
    st.markdown(t("notes_subtitle"))
    st.divider()

    # ============================================================
    # GENERAL NOTES
    # ============================================================
    st.markdown("### 📝 General Notes")
    st.markdown("Observations, questions, things to follow up on.")

    existing_notes = load_notes()

    notes_text = st.text_area(
        label="Notes",
        value=existing_notes,
        height=300,
        placeholder=t("notes_placeholder"),
        label_visibility="collapsed"
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button(t("notes_save_btn"), type="primary"):
            save_notes(notes_text)
            st.success(t("notes_saved_msg"))
    with col2:
        if notes_text:
            st.download_button(
                label=t("notes_download_btn"),
                data=notes_text,
                file_name=f"cm_notes_{st.session_state.get('alias', 'anonymous')}_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain"
            )

    # ============================================================
    # 1:1 TOPICS
    # ============================================================
    st.divider()
    st.markdown("### 📌 Topics for My 1:1")
    st.markdown(
        "Use this space to prep for conversations with your CCM, M1, or facilitator. "
        "These topics get included in your Progress Report when you download it."
    )

    existing_topics = load_oneone_topics()
    oneone_text = st.text_area(
        label="1:1 Topics",
        value=existing_topics,
        height=150,
        placeholder="What do I want to discuss?\nWhat support do I need?\nWhat went well this week?\nWhat's still unclear?",
        label_visibility="collapsed",
        key="oneone_topics_input"
    )

    if st.button("💾 Save 1:1 Topics", key="save_oneone_topics"):
        save_oneone_topics(oneone_text)
        st.success("✅ 1:1 topics saved.")

    # ============================================================
    # SYNC AGENDA GENERATOR
    # ============================================================
    st.divider()
    st.markdown("### 📋 Sync Agenda Generator")
    st.caption("Auto-generate a ready-to-paste agenda based on your progress, topics, and confidence data.")

    agenda_type = st.radio(
        "Generate agenda for:",
        ["CCM / 1:1 Sync", "Account Team Sync"],
        horizontal=True,
        key="agenda_type_radio"
    )

    if st.button("⚡ Generate Agenda", key="generate_agenda_btn"):
        history = load_confidence_history()
        oneone_topics_text = load_oneone_topics()
        scenarios_viewed_set = load_scenarios_viewed()
        alias_val = st.session_state.get("alias", "anonymous")
        today_str = date.today().strftime("%B %d, %Y")

        agenda_lines = []

        if agenda_type == "CCM / 1:1 Sync":
            agenda_lines.append(f"📋 CM 1:1 SYNC AGENDA — {today_str}")
            agenda_lines.append(f"CM: {alias_val}")
            agenda_lines.append("=" * 40)

            # Confidence snapshot
            if history:
                latest = history[-1]
                avg = sum(latest["scores"].values()) / len(latest["scores"])
                stage = latest.get("stage", "—")
                agenda_lines.append(f"\n📊 Current Stage: {stage}")
                agenda_lines.append(f"Confidence Avg: {avg:.1f} / 5.0")

                dim_labels = {
                    "trafficking": "Trafficking", "optimizations": "Optimizations",
                    "communication": "Communication", "prioritization": "Prioritization",
                    "navigation": "Navigation", "ambiguity": "Ambiguity",
                    "partnership": "Partnership", "independence": "Independence"
                }
                sorted_dims = sorted(latest["scores"].items(), key=lambda x: x[1])
                growth_areas = [(dim_labels.get(k, k), v) for k, v in sorted_dims if v <= 3]
                if growth_areas:
                    agenda_lines.append("\n🔍 Areas I'd like support on:")
                    for dim, val in growth_areas:
                        agenda_lines.append(f"  • {dim} ({val}/5)")

                if latest.get("reflection"):
                    agenda_lines.append(f"\n💭 Reflection: {latest['reflection']}")
            else:
                agenda_lines.append("\n📊 No confidence check completed yet")

            # 1:1 topics
            if oneone_topics_text and oneone_topics_text.strip():
                agenda_lines.append("\n📌 Discussion Topics:")
                for line in oneone_topics_text.strip().splitlines():
                    if line.strip():
                        agenda_lines.append(f"  • {line.strip()}")
            else:
                agenda_lines.append("\n📌 Discussion Topics: (none saved)")

            # Scenarios
            total_sc = 6
            remaining = total_sc - len(scenarios_viewed_set)
            agenda_lines.append(f"\n🎯 Scenarios Practiced: {len(scenarios_viewed_set)}/{total_sc}")
            if remaining > 0:
                agenda_lines.append(f"  → {remaining} remaining")

            # Days since last check
            if history:
                last_check = history[-1].get("check_date", "")
                if last_check:
                    try:
                        days_since = (date.today() - date.fromisoformat(last_check)).days
                        agenda_lines.append(f"\n📅 Last Confidence Check: {days_since} day(s) ago")
                    except ValueError:
                        pass

        else:  # Account Team Sync
            agenda_lines.append(f"📋 ACCOUNT TEAM SYNC NOTES — {today_str}")
            agenda_lines.append(f"CM: {alias_val}")
            agenda_lines.append("=" * 40)

            if history:
                stage = history[-1].get("stage", "—")
                agenda_lines.append(f"\n📊 Integration Stage: {stage}")

            agenda_lines.append("\n📌 Updates / Status:")
            agenda_lines.append("  • [assignments in progress]")
            agenda_lines.append("  • [blockers or pending items]")
            agenda_lines.append("  • [upcoming launches / SLA deadlines]")

            agenda_lines.append("\n❓ Questions for the Team:")
            agenda_lines.append("  • [add your questions here]")

            agenda_lines.append("\n🔄 Action Items / Follow-ups:")
            agenda_lines.append("  • [capture during the sync]")

            # Pull 1:1 topics if relevant
            if oneone_topics_text and oneone_topics_text.strip():
                agenda_lines.append("\n📝 From My Notebook:")
                for line in oneone_topics_text.strip().splitlines()[:5]:
                    if line.strip():
                        agenda_lines.append(f"  • {line.strip()}")

        agenda_text = "\n".join(agenda_lines)

        st.text_area("Generated Agenda", value=agenda_text, height=300, key="generated_agenda_output")

        col_copy, col_dl = st.columns(2)
        with col_copy:
            st.caption("📋 Select all → copy → paste into Slack or Calendar")
        with col_dl:
            st.download_button(
                label="📥 Download as .txt",
                data=agenda_text,
                file_name=f"sync_agenda_{alias_val}_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain",
                key="download_sync_agenda"
            )


def render_progress_report():
    """Dedicated Progress Report page — integration stage, checklist, confidence, scenarios, notes."""
    st.title("📈 Progress Report")
    st.markdown(
        "A comprehensive view of your integration journey. "
        "Use this for **1:1 conversations** with your CCM, M1, or training facilitator."
    )
    st.divider()

    alias = st.session_state.get("alias", "anonymous")
    history = load_confidence_history()
    scenarios_viewed = load_scenarios_viewed()
    oneone_topics = load_oneone_topics()
    total_scenarios = 6

    # ---- INTEGRATION STAGE ----
    global_stage = st.session_state.get("global_stage", "Stage 1 — Building Trust")
    if "Stage 1" in global_stage:
        stage_num = 1
    elif "Stage 2" in global_stage:
        stage_num = 2
    else:
        stage_num = 3

    st.markdown("### 📍 Integration Stage")
    progress_pct = (stage_num - 1) / 2.0
    col_bar, col_label = st.columns([4, 1])
    with col_bar:
        st.progress(progress_pct)
    with col_label:
        st.caption(f"Stage {stage_num} of 3")
    st.markdown(f"**Current stage:** {global_stage}")
    st.markdown("")

    # ---- ALIGNMENT CHECKLIST STATUS ----
    st.markdown("### ✅ Alignment Checklist")

    user_dir = get_user_dir()
    checklist_file = user_dir / "alignment_checklist.json"
    if checklist_file.exists():
        with open(checklist_file, "r", encoding="utf-8") as f:
            checklist_state = json.load(f)
    else:
        checklist_state = {}

    # All stage items for summary
    all_stage_items = {
        "Stage 1": [
            ("s1_intro_call", "Introduction call with CCM"),
            ("s1_daily_cadence", "Daily sync cadence established"),
            ("s1_slack_channels", "Added to account team Slack channels"),
            ("s1_weekly_syncs", "Added to weekly syncs / pod calls"),
            ("s1_email_distro", "Added to email distribution list"),
            ("s1_sf_access", "Salesforce access confirmed"),
            ("s1_regular_syncs", "Regular syncs established or scheduled"),
        ],
        "Stage 2": [
            ("s2_open_independently", "Completed assignment independently"),
            ("s2_ccm_qa_only", "CCM transitioned to QA-only"),
            ("s2_team_call_updates", "Providing updates in team meetings"),
            ("s2_project_brainstorm", "Identified project/initiative with CCM"),
        ],
        "Stage 3": [
            ("s3_self_qa", "Self-QA'ing all assignments"),
            ("s3_full_ownership", "Full workflow ownership"),
            ("s3_proactive_tracking", "Proactively tracking launches"),
            ("s3_coaching", "Coaching teammates"),
        ],
    }

    for stage_name, items in all_stage_items.items():
        completed = sum(1 for key, _ in items if checklist_state.get(key, False))
        total = len(items)
        pct = completed / total if total > 0 else 0

        is_current = (stage_name == "Stage 1" and stage_num == 1) or \
                     (stage_name == "Stage 2" and stage_num == 2) or \
                     (stage_name == "Stage 3" and stage_num == 3)

        marker = " ← You are here" if is_current else ""
        st.markdown(f"**{stage_name}**{marker} — {completed}/{total} complete")
        st.progress(pct)

        # Show individual items
        for key, label in items:
            status = "✅" if checklist_state.get(key, False) else "⬜"
            st.caption(f"  {status} {label}")

    st.divider()

    # ---- CONFIDENCE SNAPSHOT ----
    st.markdown("### 📊 Confidence Snapshot")

    if history:
        dim_labels = {
            "trafficking": "Trafficking",
            "optimizations": "Optimizations",
            "communication": "Communication",
            "prioritization": "Prioritization",
            "navigation": "Navigation",
            "ambiguity": "Ambiguity",
            "partnership": "Partnership",
            "independence": "Independence",
        }

        latest = history[-1]
        avg = sum(latest["scores"].values()) / len(latest["scores"])

        stat1, stat2, stat3 = st.columns(3)
        with stat1:
            st.metric("Overall Average", f"{avg:.1f} / 5")
        with stat2:
            st.metric("Check-ins", str(len(history)))
        with stat3:
            st.metric("Scenarios Practiced", f"{len(scenarios_viewed)} / {total_scenarios}")

        st.markdown("")
        sorted_dims = sorted(latest["scores"].items(), key=lambda x: x[1], reverse=True)
        for key, val in sorted_dims:
            label = dim_labels.get(key, key.capitalize())
            st.markdown(f"{'█' * val}{'░' * (5 - val)}  **{val}/5**  {label}")

        # Growth trend if multiple check-ins
        if len(history) > 1:
            st.markdown("")
            st.markdown("**Growth Summary (First → Latest):**")
            first = history[0]
            for key in latest["scores"]:
                first_val = first["scores"].get(key, 0)
                latest_val = latest["scores"].get(key, 0)
                diff = latest_val - first_val
                label = dim_labels.get(key, key.capitalize())
                if diff > 0:
                    arrow = f"+{diff} ▲"
                elif diff < 0:
                    arrow = f"{diff} ▼"
                else:
                    arrow = "—"
                st.caption(f"  {label}: {first_val} → {latest_val}  {arrow}")

        if latest.get("reflection"):
            st.markdown("")
            st.info(f"💭 Latest reflection: *\"{latest['reflection']}\"*")
    else:
        st.info("📊 Complete your first **Confidence Check** to see your snapshot here.")

    st.divider()

    # ---- SCENARIO PRACTICE ----
    st.markdown("### 🎯 Scenario Practice")
    st.markdown(f"**{len(scenarios_viewed)} of {total_scenarios}** scenarios practiced")
    scenario_titles = [
        "First Assignment from Your CCM",
        "CCM and M1 Give Conflicting Direction",
        "AE Asks You for Something Directly",
        "You Trafficked the Wrong Flight Dates",
        "A Teammate Asks You to Cover",
        "Your Stage 1 Integration Is Not Happening"
    ]
    for i, title in enumerate(scenario_titles):
        status = "✅" if i in scenarios_viewed else "⬜"
        st.caption(f"  {status}  {title}")

    st.divider()

    # ---- 1:1 TOPICS ----
    st.markdown("### 💬 Topics for My 1:1")
    if oneone_topics and oneone_topics.strip():
        for line in oneone_topics.strip().splitlines():
            if line.strip():
                st.markdown(f"- {line.strip()}")
    else:
        st.caption("No topics saved yet — add them in My Notebook.")

    st.divider()

    # ---- DOWNLOAD ----
    st.markdown("### 📥 Download Full Report")

    if history:
        report_text = generate_progress_report(history, alias)

        col1, col2 = st.columns([1, 2])
        with col1:
            st.download_button(
                label="📥 Download Progress Report",
                data=report_text,
                file_name=f"cm_progress_report_{alias}_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain",
                key="download_progress_report",
                type="primary"
            )
        with col2:
            st.caption(
                "Includes: integration stage • checklist status • confidence trend • 1:1 topics • scenario practice • notes excerpt"
            )

        with st.expander("👁️ Preview report before downloading"):
            st.code(report_text, language=None)
    else:
        st.info(
            "📊 Complete your first **Confidence Check** to unlock the downloadable report. "
            "Your checklist, 1:1 topics, and notes will be included automatically."
        )


def render_zoyla():
    """Ask Zoyla — embedded QuickSight AI agent."""
    import streamlit.components.v1 as components

    st.title("💬 Ask Zoyla")
    st.markdown(
        "Your AI training assistant — grounded in CCM/AdOps operations. "
        "Ask about assignments, systems, workflows, or how to handle a situation."
    )
    st.divider()

    st.info(
        "💡 **Tip:** Ask naturally — e.g. *'Where do I find the MPT?'* or "
        "*'What do I do if a campaign is not PTS?'* or *'How do I escalate a blocker?'*"
    )

    # Embed the QuickSight Q chat agent as a full-height iframe
    zoyla_iframe = f"""
    <iframe
        width="100%"
        height="800"
        allow="clipboard-read https://us-east-1.quicksight.aws.amazon.com; clipboard-write https://us-east-1.quicksight.aws.amazon.com"
        src="{ASK_ZOYLA_URL}"
        style="border: 1px solid rgba(255,255,255,0.1); border-radius: 8px;">
    </iframe>
    """
    components.html(zoyla_iframe, height=820, scrolling=False)

    st.caption(
        "Zoyla is powered by Amazon QuickSight Q. "
        "If you see a sign-in screen, authenticate with your Amazon credentials — "
        "the session will persist for the rest of your browser session."
    )


def render_reference_docs():
    st.title(t("docs_title"))
    st.markdown(t("docs_subtitle"))
    st.divider()

    # ============================================================
    # QUICK LINKS
    # ============================================================
    st.markdown("### 🔗 Quick Links")
    link1, link2 = st.columns(2)
    with link1:
        st.link_button("📋 Workflow SOP (Wiki) ↗", "https://w.amazon.com/bin/view/Users/ajamitho/CM-UAT-Test/")
        st.caption("Stage definitions, responsibilities, best practices, FAQ")
    with link2:
        st.link_button("🏠 CM Integration Hub (this app) ↗", "http://localhost:8501")
        st.caption("Bookmark this link to open the hub anytime")

    st.divider()

    # ============================================================
    # CM REFERENCE DOCUMENTS — curated from materials/ folder
    # ============================================================
    st.markdown("### 📄 CM Reference Documents")
    materials_dir = Path(__file__).parent / "materials"
    materials_dir.mkdir(exist_ok=True)

    viewable_extensions = {".txt", ".md", ".docx"}
    all_extensions = {".docx", ".pptx", ".pdf", ".xlsx", ".txt", ".md"}
    # Exclude archive folder, temp files (~$), and non-CM docs
    excluded_files = {"SME Prep Guide.docx", "How_to_Edit_This_Hub.md"}
    files = [f for f in materials_dir.iterdir()
             if f.suffix.lower() in all_extensions
             and not f.name.startswith("~$")
             and f.name not in excluded_files
             and f.is_file()]

    if files:
        for filepath in sorted(files):
            is_viewable = filepath.suffix.lower() in viewable_extensions

            col1, col2 = st.columns([3, 1])
            with col1:
                icon = "📄" if filepath.suffix.lower() in {".docx", ".pptx"} else "📋" if filepath.suffix.lower() in {".txt", ".md"} else "📊"
                st.markdown(f"{icon} **{filepath.name}**")
            with col2:
                with open(filepath, "rb") as f:
                    file_bytes = f.read()
                st.download_button(
                    label=t("docs_download_btn"),
                    data=file_bytes,
                    file_name=filepath.name,
                    key=f"dl_{filepath.name}"
                )

            if is_viewable:
                with st.expander(f"{t('docs_view_btn')} {filepath.name}", expanded=False):
                    if filepath.suffix.lower() in {".txt", ".md"}:
                        try:
                            content = filepath.read_text(encoding="utf-8")
                        except UnicodeDecodeError:
                            content = filepath.read_text(encoding="latin-1")
                        if filepath.suffix.lower() == ".md":
                            st.markdown(content)
                        else:
                            st.text(content)
                    elif filepath.suffix.lower() == ".docx":
                        content = extract_docx_text(filepath)
                        st.markdown(content)

            st.markdown("---")
    else:
        st.caption(t("docs_no_files"))

    # ============================================================
    # TRAINING CONTENT — placeholders for upcoming materials
    # ============================================================
    st.divider()
    st.markdown("### 🎓 Training Content")
    st.caption("These resources are in development. Check back as your integration progresses.")

    training_items = [
        ("🎓", "Rodeo Trafficking Walkthrough", "Step-by-step guide to DSP trafficking in Rodeo — from assignment to PTS."),
        ("🎓", "Salesforce Assignment Workflow", "How assignments are created, managed, and tracked in SF — the CM perspective."),
        ("🎓", "OMS Booking Reference", "When and how to interact with OMS — booking, verifying inventory, common pitfalls."),
        ("🎓", "CSU End-to-End Process", "Full Campaign Setup flow — from AE request to live campaign."),
    ]

    for icon, title, desc in training_items:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"{icon} **{title}**")
            st.caption(desc)
        with col2:
            st.button("Coming Soon", key=f"soon_{title}", disabled=True)
        st.markdown("---")


def main():
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon=APP_ICON,
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # -- Custom CSS — works on both light and dark Streamlit themes --
    st.markdown("""
    <style>
        .block-container { padding-top: 2rem; }
        [data-testid="stSidebar"] { min-width: 260px; }

        /* Sidebar nav buttons — high contrast on any background */
        [data-testid="stSidebar"] .stButton > button {
            width: 100%;
            text-align: left;
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.25);
            border-radius: 6px;
            padding: 0.5rem 0.75rem;
            font-size: 0.92rem;
            font-weight: 500;
            color: inherit;
            cursor: pointer;
            transition: all 0.15s;
        }
        [data-testid="stSidebar"] .stButton > button:hover {
            background: rgba(255, 255, 255, 0.18);
            border-color: rgba(255, 255, 255, 0.5);
        }

        /* Active page marker — bright white-on-blue pill */
        .nav-active {
            background-color: #FF9900;
            color: #000000 !important;
            padding: 0.5rem 0.75rem;
            border-radius: 6px;
            font-size: 0.92rem;
            font-weight: 700;
            margin-bottom: 0.35rem;
            margin-top: 0.1rem;
        }
        .nav-active p {
            color: #000000 !important;
            margin: 0;
        }
    </style>
    """, unsafe_allow_html=True)

    # Initialize navigation state
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "home"
    # ============================================================
    # "ASK ZOYLA" — dedicated nav page with embedded iframe
    # The FAB button navigates to the Ask Zoyla page in the sidebar.
    # The page renders the QuickSight agent via st.components.v1.iframe
    # which is the only reliable way to embed external content in Streamlit.
    # ============================================================
    st.markdown(f"""
    <style>
        .zoyla-fab {{
            position: fixed;
            bottom: 28px;
            right: 28px;
            z-index: 9999;
            background: linear-gradient(135deg, #FF9900 0%, #E88600 100%);
            color: #000000 !important;
            border: none;
            border-radius: 50px;
            padding: 14px 24px;
            font-size: 1rem;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 4px 16px rgba(0,0,0,0.3);
            transition: all 0.2s;
            text-decoration: none !important;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }}
        .zoyla-fab:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 24px rgba(0,0,0,0.4);
            background: linear-gradient(135deg, #FFa820 0%, #FF9900 100%);
            color: #000000 !important;
            text-decoration: none !important;
        }}
    </style>
    <a class="zoyla-fab" href="?page=zoyla" target="_self">
        💬 Ask Zoyla
    </a>
    """, unsafe_allow_html=True)

    # Handle ?page=zoyla query param — navigate to Zoyla page
    params = st.query_params
    if params.get("page") == "zoyla":
        st.session_state["current_page"] = "zoyla"
        st.query_params.clear()
        st.rerun()



    # -- Sidebar --
    with st.sidebar:
        # Language toggle
        lang_options = {"English": "en", "Español": "es"}
        selected_lang = st.radio(
            t("sidebar_language"),
            options=list(lang_options.keys()),
            index=0 if st.session_state.get("language", "en") == "en" else 1,
            horizontal=True
        )
        st.session_state["language"] = lang_options[selected_lang]

        st.divider()

        # Alias input
        alias = st.text_input(
            t("sidebar_alias_label"),
            value=st.session_state.get("alias", ""),
            help=t("sidebar_alias_help"),
            key="alias_input"
        )
        if alias:
            st.session_state["alias"] = alias.strip().lower()
            st.markdown(t("sidebar_welcome").format(alias))

        # Global stage selector — persists across all tabs
        stage_options_sidebar = t("cc_stages")
        current_global_stage = st.session_state.get("global_stage", stage_options_sidebar[0])
        if current_global_stage not in stage_options_sidebar:
            current_global_stage = stage_options_sidebar[0]
        selected_global_stage = st.selectbox(
            "📊 Your Current Stage",
            options=stage_options_sidebar,
            index=stage_options_sidebar.index(current_global_stage),
            key="sidebar_stage_select"
        )
        st.session_state["global_stage"] = selected_global_stage

        st.divider()
        lang = st.session_state.get("language", "en")
        current = st.session_state.get("current_page", "home")

        # -- Navigation --
        for page_key, icon, en_label, es_label in NAV_PAGES:
            label = es_label if lang == "es" else en_label

            if page_key == current:
                # Active page — dark pill with white text
                st.markdown(f'<div class="nav-active">{icon}  {label}</div>', unsafe_allow_html=True)
            else:
                # Inactive pages — visible bordered buttons
                st.button(f"{icon}  {label}", key=f"nav_{page_key}", on_click=navigate_to, args=(page_key,))

    # -- Route to page --
    current_page = st.session_state.get("current_page", "home")

    if current_page == "home":
        render_home()
    elif current_page == "campaign":
        render_campaign_navigation()
    elif current_page == "comms":
        render_communication_tree()
    elif current_page == "priority":
        render_prioritization()
    elif current_page == "scenarios":
        render_scenarios()
    elif current_page == "confidence":
        render_confidence_check()
    elif current_page == "progress":
        render_progress_report()
    elif current_page == "notes":
        render_notes()
    elif current_page == "docs":
        render_reference_docs()
    elif current_page == "zoyla":
        render_zoyla()


if __name__ == "__main__":
    main()
