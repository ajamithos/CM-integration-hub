# How to Edit the CM Integration Hub

Everything lives in **one file**: `cm_training_hub.py`

Open it in any text editor — VS Code, Notepad++, or even Notepad.

---

## Quick Reference: What to Edit and Where

### Scenario Cards

Search for: `scenario_cards = [`

Each card is a dictionary:
```python
{
    "category": "Relationship Building",
    "title": "First Assignment from Your CCM",
    "scenario": """Your CCM Slacks you...""",
    "approach": """**One way to handle..."""
}
```

- **Change wording:** Edit text inside triple quotes (`"""`)
- **Add a card:** Copy a card block, paste after the last `}` before `]`, add comma between cards. Update `list(range(6))` to `list(range(7))` (or your new total)
- **Remove a card:** Delete from `{` to `},`. Update the `range()` number

### Confidence Check Dimensions

Search for: `"cc_dimensions":`

Each dimension: `{"key": "trafficking", "label": "Trafficking — I can open..."}`

Edit `"label"` text. Update **both** `"en"` and `"es"` sections.

### Campaign Navigation (Ask / Attempt / Escalate)

Search for: `"cn_ask_items":` or `"cn_attempt_items":` or `"cn_escalate_items":`

Simple lists of strings — add, remove, or edit items.

### Communication Decision Tree

Search for: `def render_communication_tree():`

The tree uses `st.columns()` and markdown. Each column is one decision path. Edit the markdown text inside each `with colN:` block.

### Prioritization Framework

Search for: `"pf_principles":`

Each principle: `{"title": "1. Live campaigns...", "body": "If something is live..."}`

### Home Page

Search for: `"home_tagline":` and `"home_footer":`

### Navigation Menu

Search for: `NAV_PAGES = [`

Each entry: `("page_key", "icon", "English Label", "Spanish Label")`

### Reference Documents

Drop files into the `materials/` subfolder:
- `.md` and `.txt` → viewable as formatted text
- `.docx` → viewable as extracted text + downloadable
- `.pptx`, `.pdf`, `.xlsx` → download only

No code changes needed.

---

## Bilingual Content

Every text string exists twice — under `"en":` and `"es":`.

Search for the English key (e.g., `"cn_ask_items":`) — it appears twice. First = English, second = Spanish.

---

## After Editing

1. Save the file
2. If Streamlit is running → click **Rerun** in the browser (or it auto-detects)
3. If not running → `streamlit run cm_training_hub.py`

---

## Tips

- **Triple-quoted strings** (`"""text"""`) can span multiple lines
- **Indentation matters** — use spaces, not tabs. Keep existing indentation.
- **Commas matter** — each list item needs a comma after it (except the last)
- If you break something, the app shows an error with the line number
- For structural changes (new pages, new features) → bring it to Orcha
