# CM Integration Hub

A self-contained integration and reference tool for Campaign Managers in Model 2 — from Stage 1 through Stage 3.

Runs on your laptop. No servers. No accounts. No installs beyond Python and Streamlit.

---

## Quick Start

### 1. Install Python (one-time)

Download from [python.org](https://www.python.org/downloads/) — check **"Add Python to PATH"** during install.

### 2. Clone this repo

Open Command Prompt (Windows) or Terminal (Mac) and run:

```
git clone https://github.com/ajamithos/CM-integration-hub.git
cd CM-integration-hub
```

### 3. Install Streamlit (one-time)

```
pip install streamlit
```

If `pip` doesn't work, try: `python -m pip install streamlit`

### 4. Launch

```
streamlit run cm_training_hub.py
```

Your browser opens to `http://localhost:8501`. Enter your alias in the sidebar and go.

### 5. Stop the app

Press `Ctrl+C` in the terminal.

---

## What's Inside

| Page | What It Does |
|---|---|
| 🏠 **Dashboard** | Your progress at a glance — stage, confidence avg, scenarios practiced, next steps |
| 📋 **Campaign Navigation** | Stage-aware Ask / Attempt / Escalate framework, SOP by stage, alignment checklist |
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

## Your Data is 100% Local

Everything you enter (notes, confidence scores, checklist progress) is saved in `data/{your_alias}/` on your laptop. Nothing is uploaded, shared, or visible to anyone until you share it.

---

## For Testers — How to Give Feedback

We're crowdsourcing fine-detail edits before rolling this out to all CMs. Here's how to help:

### Claim a Section

Open the **Feedback Tracker** (shared separately) → go to **Tester Assignments** tab → claim an unclaimed section by adding your name.

### Test Your Section

- Try everything — buttons, links, toggles
- Switch English ↔ Español
- Change stages in the sidebar — does the content update?
- Save data, close the app, reopen — does it persist?

### Log Findings

In the **Feedback Log** tab, one row per finding:

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

## Get Latest Updates

After Jamie pushes fixes based on your feedback:

```
cd CM-integration-hub
git pull
```

That's it — you now have the latest version. Relaunch with `streamlit run cm_training_hub.py`.

---

## Common Issues

| Problem | Fix |
|---|---|
| `python` not recognized | Reinstall Python, check "Add to PATH" |
| `pip` not recognized | Use: `python -m pip install streamlit` |
| Page is blank | Paste `http://localhost:8501` directly in browser |
| `ModuleNotFoundError` | Run: `pip install streamlit` |
| Want to stop the app | Press `Ctrl+C` in terminal |

**Still stuck?** Slack **@ajamitho** (Jamie Thomas) with a screenshot.

---

Built for CMs in Model 2. Your reference from Stage 1 through Stage 3.
