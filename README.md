# CM Training Hub

A self-contained reference and development tool for Campaign Managers in their first 30 days on-account under Model 2.

## Features

### ✅ Completed Sections

1. **🏠 Home** - Overview and quick navigation
2. **📋 Campaign Navigation** - Ask → Attempt → Escalate framework with 15-Minute Rule
3. **💬 Communication Decision Tree** - Situation-based routing for who/when/how to communicate
4. **⚡ Prioritization Framework** - Five principles for managing competing priorities
5. **🎯 Scenario Practice** - 6 interactive flashcard scenarios with:
   - Real CM/CCM partnership situations
   - Category tags (Relationship Building, Navigating Ambiguity, Communication Boundaries, etc.)
   - "Think about it first" prompts
   - Expandable "Reveal Suggested Approach" sections
   - Previous/Next navigation
   - Shuffle functionality
   - Progress indicator
6. **📊 Confidence Check** - Self-assessment tool with 8 dimensions and trend tracking
7. **📝 My Notes** - Personal notepad with local storage and download
8. **📄 Reference Documents** - Downloadable materials section

### 🌐 Bilingual Support

- Full English / Español translations
- Toggle in sidebar
- All content and UI elements localized

## How to Run

### Requirements

- Python 3.8+
- Streamlit

### Installation

```bash
# Navigate to the app directory
cd "C:\Users\ajamitho\Desktop\CM Training Program\CM_Training_Hub"

# Install dependencies (first time only)
pip install streamlit

# Run the app
streamlit run cm_training_hub.py
```

The app will open in your default browser at `http://localhost:8501`

### First-Time Setup

1. **Enter your alias** in the sidebar (e.g., "dcampos")
2. **Select your language** (English or Español)
3. **Navigate** using the sidebar menu

## Data Storage

All user data is stored **locally** in the `data/` folder:

- Confidence checks saved as JSON files
- Notes saved as text files
- Organized by user alias

**No external servers. No databases. Each CM runs their own copy.**

## Scenario Flashcards

The Scenario Practice section contains 6 cards covering:

1. **First Assignment from Your CCM** (Relationship Building)
2. **Your CCM and M1 Give Conflicting Direction** (Navigating Ambiguity)
3. **The Client Asks You Something Directly on a Call** (Communication Boundaries)
4. **You Trafficked the Wrong Flight Dates** (Trust and Accountability)
5. **A Teammate Asks You to Cover Their Assignment** (Boundaries and Prioritization)
6. **Your CCM Is Not Looping You In** (Advocating for Yourself)

### How to Use Scenario Cards

1. **Read the scenario** - Understand the situation
2. **Think about it first** - Consider your response before revealing the approach
3. **Click "Reveal Suggested Approach"** - See one way to handle the situation
4. **Navigate** - Use Previous/Next buttons or Shuffle to randomize order

**No scoring. No right/wrong answers.** The suggested approaches are framed as "one way to handle this" — designed to build judgment, not test knowledge.

## Adding Reference Documents

To add downloadable reference materials:

1. Create a `materials/` folder in the app directory (if it doesn't exist)
2. Add `.docx`, `.pptx`, `.pdf`, or `.xlsx` files
3. They will automatically appear in the Reference Documents section

## Customization

All content is in the `LANG` dictionary at the top of `cm_training_hub.py`. To modify:

- **English content**: Edit entries under `"en"`
- **Spanish content**: Edit entries under `"es"`
- **Scenario cards**: Edit the `scenario_cards` list in `render_scenarios()`

## Architecture

- **Framework**: Streamlit (single-page app)
- **Data persistence**: Local JSON and text files
- **Styling**: Custom CSS for Amazon branding
- **Navigation**: Radio button sidebar with 8 sections
- **State management**: Streamlit session state for card navigation

## Support

Built for the SJO AdOps → CM transition under Model 2. For questions or updates, contact Jamie Thomas (ajamitho@).

---

**Version**: 1.0  
**Last Updated**: March 9, 2026  
**Built by**: Jamie Thomas (ajamitho@)
