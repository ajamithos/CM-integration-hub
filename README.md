# CM Integration Hub

A self-contained integration and reference tool for Campaign Managers in Model 2 — from Stage 1 through Stage 3.

---

## 🔗 Open the Hub

**[Launch CM Integration Hub →](https://cm-integration.streamlit.app/)**

No install needed. Click the link, enter your alias, and explore.

> ⚠️ **Note:** The hosted version is a **preview for browsing and testing**. Notes, confidence checks, and checklist progress will not save between sessions. For persistent data, set up a local copy below.

---

## For Testers — How to Give Feedback

We're crowdsourcing fine-detail edits before rolling this out to all CMs.

### 1. Open the Hub using the link above

### 2. Claim a Section
Open the **Feedback Tracker** (shared separately) → go to **Tester Assignments** tab → claim an unclaimed section by adding your name.

### 3. Test Your Section
- Try everything — buttons, links, toggles
- Switch English ↔ Español
- Change stages in the sidebar — does the content update?
- Try saving data (notes, confidence check) — it works within a session

### 4. Log Findings
In the **Feedback Log** tab of the tracker, one row per finding:
- **Which page/feature?** (be specific)
- **What's wrong or confusing?**
- **What should it say/do instead?**
- **Priority**: P1 (blocker) → P4 (nice-to-have)

### What to Look For

| Find These | Also Valuable |
|---|---|
| ❌ Bugs — broken, crashed, error | 😕 UX — confusing flow |
| 📝 Content — wrong or outdated text | 🤷 Missing — expected but not there |
| 🇪🇸 Translation — ES labels wrong | ✨ Ideas — "it would be great if..." |
| 💾 Data — doesn't save or load | 👍 Wins — things you liked! |

---

## What's Inside

| Page | What It Does |
|---|---|
| 🏠 **Dashboard** | Your progress at a glance — stage, confidence avg, scenarios practiced, next steps |
| 📋 **Navigating Campaign R&Rs** | Stage-aware Ask / Attempt / Escalate framework, SOP by stage, alignment checklist |
| 💬 **Communication Tree** | Decision tree for who to contact, what channel, what to say — adapts to your stage |
| ⚡ **Prioritization** | Five principles for competing priorities |
| 🎯 **Scenario Practice** | 6 real CM/CCM situations with suggested approaches |
| 📊 **Confidence Check** | Self-assessment across 8 dimensions with trend tracking |
| 📈 **Progress Report** | Full integration summary — stage, checklist, confidence, scenarios, 1:1 topics |
| 📝 **My Notebook** | Notes, 1:1 prep, sync agenda generator |
| 📄 **Reference Documents** | CM-curated docs and quick links |
| 🤖 **Ask Zoyla** | AI assistant for campaign questions |

🌐 **Bilingual** — toggle English / Español in the sidebar.

---

## Quick Start — Local Install

For the full experience with persistent data (notes, confidence history, checklist progress saved permanently):

### 1. Install Python (one-time)
Download from [python.org](https://www.python.org/downloads/) — check **"Add Python to PATH"** during install.

### 2. Install Git (one-time)
Download from [git-scm.com](https://git-scm.com/download/win) — click Next through everything with defaults.

### 3. Clone and run

```
git clone https://github.com/ajamithos/CM-integration-hub.git
cd CM-integration-hub
pip install streamlit
streamlit run cm_training_hub.py
```

Browser opens to `http://localhost:8501`. Enter your alias and go.

### 4. Get latest updates

```
cd CM-integration-hub
git pull
```

Then relaunch with `streamlit run cm_training_hub.py`.

---

## Your Data (Local Version)

Everything you enter is saved in `data/{your_alias}/` on your laptop. Nothing is uploaded, shared, or visible to anyone until you share it.

---

## Common Issues

| Problem | Fix |
|---|---|
| `python` not recognized | Reinstall Python, check "Add to PATH" |
| `pip` not recognized | Use: `python -m pip install streamlit` |
| Page is blank | Paste `http://localhost:8501` directly in browser |
| `ModuleNotFoundError` | Run: `pip install streamlit` |
| Stop the app | Press `Ctrl+C` in terminal |

**Still stuck?** Slack **@ajamitho** (Jamie Thomas) with a screenshot.

---

Built for CMs in Model 2. Your reference from Stage 1 through Stage 3.
