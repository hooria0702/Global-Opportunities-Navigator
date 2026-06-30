# Global Opportunities Navigator

A web platform that helps Pakistani students discover scholarships, exchange programmes,
and universities that match their academic profile — and understand exactly why they
qualify or don't.

Built with Flask, SQLite, and Bootstrap. No frameworks. No machine learning.
Everything is explainable.

View the WebApp live at:
https://oppsnav.pythonanywhere.com/

---

## Table of Contents

- [Motivation](#motivation)
- [Problem Statement](#problem-statement)
- [Features](#features)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Database Design](#database-design)
- [Eligibility Logic](#eligibility-logic)
- [Match Scoring](#match-scoring)
- [Installation](#installation)
- [Usage](#usage)
- [Opportunities in the Database](#opportunities-in-the-database)
- [Future Improvements](#future-improvements)

---

## Motivation

I started building this project after spending weeks trying to figure out which
international scholarships I was actually eligible for. Information was scattered
across dozens of websites, eligibility criteria were buried in PDFs, and every
time I found a programme I liked, I'd discover I missed a requirement — or worse,
the deadline had already passed.

I wanted one place where a student could enter their academic profile and
immediately see which programmes they qualify for, what's missing, and how much
time they have left to apply.

---

## Problem Statement

Pakistani students searching for international opportunities face several real barriers:

- Information scattered across government websites, university portals, and PDF brochures
- Complex eligibility requirements that are hard to cross-reference with your own profile
- No way to know which programmes you qualify for without reading each one individually
- Deadlines that are easy to miss when tracking ten programmes across different countries
- No personalised guidance — just generic lists

This platform centralises opportunities and runs a transparent eligibility check
against each student's academic profile.

---

## Features

### Profile Setup
Enter your name, country, degree level, major, CGPA (0–4.0), IELTS/TOEFL scores,
funding preference, and preferred countries. Your profile is stored in SQLite and
used for all eligibility checks.

### Eligibility Checker
The system checks your profile against every programme in the database across
eight criteria: GPA, degree level, field of study, IELTS, TOEFL, country preference,
funding alignment, and deadline. Each programme is classified as:

- **Eligible** — you meet all hard requirements
- **Potentially Eligible** — you meet core requirements but have minor soft gaps
- **Not Eligible** — you fail one or more hard requirements

### Missing Requirements Analysis
For each programme, a detailed breakdown shows which requirements you meet,
which are soft gaps, and which are hard failures — with plain-English explanations.

### Opportunity Search
Filter the full catalogue by country, type (Scholarship / Exchange / University),
funding type, degree level, and field of study. Results display in Bootstrap cards
with colour-coded deadline badges.

### Deadline Tracker
Every opportunity shows days remaining. Badges turn red under 14 days, amber under
45 days, and green beyond that. Expired deadlines are clearly marked as closed.

### Match Score (0–100)
Each programme gets a transparent 100-point match score based on five weighted
factors: GPA headroom (25 pts), language readiness (25 pts), degree level (20 pts),
country preference (15 pts), and funding alignment (15 pts).

### Dashboard
A summary view showing eligible/potentially/not-eligible counts, your top three
matches by score, upcoming deadlines, and an insight panel explaining what's
blocking you from the programmes you don't currently qualify for.

### Saved Opportunities
Bookmark programmes and review them later with deadline and match score visible
at a glance.

---

## Screenshots
<img width="835" height="412" alt="image" src="https://github.com/user-attachments/assets/589a2e21-3135-4f7b-83ef-6defeffd1928" />
<img width="532" height="335" alt="image" src="https://github.com/user-attachments/assets/2644f209-b5e7-4b9d-8d0d-37d2ff02bd14" />
<img width="833" height="413" alt="image" src="https://github.com/user-attachments/assets/600f2bb9-cdc9-4347-b64b-e14f8d834fee" />
<img width="835" height="412" alt="image" src="https://github.com/user-attachments/assets/6e125b8d-df07-4bf3-a34b-7b7b422e847c" />
<img width="839" height="406" alt="image" src="https://github.com/user-attachments/assets/7278f870-8552-4bf0-a80c-2bb5c4e857e2" />
<img width="814" height="413" alt="image" src="https://github.com/user-attachments/assets/93e8cd3c-4426-41be-9645-bf487e36e96e" />
<img width="833" height="413" alt="image" src="https://github.com/user-attachments/assets/5d051a3a-512a-4445-bd8f-267d6e287347" />

---

## Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Backend    | Python 3, Flask                   |
| Templating | Jinja2                            |
| Frontend   | Bootstrap 5, Bootstrap Icons      |
| Database   | SQLite (via Python `sqlite3`)     |
| Fonts      | Poppins + Inter (Google Fonts)    |
| Data       | Pandas (available for extensions) |

**Not used:** React, TypeScript, Docker, Redis, Django, any ORM, any ML library.

Everything is readable by a second-year CS student.

---

## Project Structure

```
Global-Opportunities-Navigator/
│
├── app.py              # Flask routes — thin layer, delegates to modules below
├── database.py         # SQLite schema, init, and query helpers
├── eligibility.py      # Rule-based eligibility engine (pure Python, no Flask)
├── scoring.py          # Match score algorithm (pure Python, no Flask)
├── seed_data.py        # Loads sample opportunity data into the database
│
├── requirements.txt    # flask, pandas
├── README.md
├── opportunities.db    # Auto-created on first run (gitignored)
│
├── templates/
│   ├── base.html       # Shared layout: navbar, footer, CSS variables
│   ├── index.html      # Home page with hero, stats, upcoming deadlines
│   ├── profile.html    # Student profile form
│   ├── results.html    # Eligibility results grouped by status
│   ├── search.html     # Filterable opportunity catalogue
│   ├── detail.html     # Single opportunity with eligibility breakdown
│   ├── dashboard.html  # Student dashboard with insights
│   ├── saved.html      # Saved/bookmarked opportunities
│   └── about.html      # About page
│
└── static/
    ├── css/
    │   └── style.css   # Custom overrides (most CSS lives in base.html)
    └── js/
        └── main.js     # Optional JS utilities
```

---

## Database Design

Three tables. No ORM — plain SQL so the schema is completely transparent.

### `students`
Stores one profile per session. No login system required.

| Column               | Type    | Notes                              |
|---------------------|---------|------------------------------------|
| id                  | INTEGER | Primary key, autoincrement         |
| name                | TEXT    | Student's full name                |
| country             | TEXT    | e.g. "Pakistan"                    |
| degree_level        | TEXT    | Bachelors / Masters / PhD          |
| major               | TEXT    | e.g. "Computer Science"            |
| cgpa                | REAL    | 0.0 – 4.0                         |
| has_ielts           | INTEGER | 1 = yes, 0 = no                    |
| ielts_score         | REAL    | Band score, NULL if not taken      |
| has_toefl           | INTEGER | 1 = yes, 0 = no                    |
| toefl_score         | INTEGER | iBT score, NULL if not taken       |
| budget              | TEXT    | Fully Funded / Partial / Self      |
| preferred_countries | TEXT    | Comma-separated: "Germany,Japan"   |
| created_at          | TEXT    | datetime('now')                    |

### `opportunities`
Central catalogue. All eligibility constraints live here so the engine
has no hardcoded rules.

| Column         | Type    | Notes                                     |
|----------------|---------|-------------------------------------------|
| id             | INTEGER | Primary key                               |
| name           | TEXT    | Programme name                            |
| country        | TEXT    | Host country                              |
| type           | TEXT    | Scholarship / Exchange / University       |
| degree_levels  | TEXT    | Comma-separated: "Bachelors,Masters,PhD"  |
| fields         | TEXT    | "All" or "Engineering,CS,Medicine"        |
| min_gpa        | REAL    | Minimum CGPA required                     |
| ielts_required | INTEGER | 1 = required                              |
| min_ielts      | REAL    | Minimum band, NULL if not specified       |
| toefl_required | INTEGER | 1 = required                              |
| min_toefl      | INTEGER | Minimum score, NULL if not specified      |
| funding_type   | TEXT    | Fully Funded / Partially Funded / Varies  |
| deadline       | TEXT    | "YYYY-MM-DD" or "Rolling"                 |
| description    | TEXT    | Programme description                     |
| official_link  | TEXT    | Official programme URL                    |

### `saved_opportunities`
Junction table linking students to bookmarked programmes.

| Column         | Type    | Notes                             |
|----------------|---------|-----------------------------------|
| id             | INTEGER | Primary key                       |
| student_id     | INTEGER | FK → students.id                  |
| opportunity_id | INTEGER | FK → opportunities.id             |
| saved_at       | TEXT    | datetime('now')                   |

A `UNIQUE(student_id, opportunity_id)` constraint prevents duplicate bookmarks.
`INSERT OR IGNORE` handles the case where a student saves the same programme twice.

---

## Eligibility Logic

`eligibility.py` contains pure Python functions — no Flask imports, no database
calls. This makes it independently testable.

The core function `check_eligibility(student, opportunity)` runs eight checks
in order:

```
1. GPA           Hard if more than 0.2 below minimum. Soft if within 0.2.
2. Degree Level  Hard. Student must be in the programme's accepted levels.
3. Field         Soft. Field mismatch is flagged but not a hard disqualifier.
4. IELTS         Hard if required but not taken, or score below minimum.
5. TOEFL         Hard if required but not taken, or score below minimum.
6. Country       Soft. If student has preferences and programme doesn't match.
7. Funding       Soft. Mismatch between student preference and programme type.
8. Deadline      Hard if deadline has passed.
```

**Hard failures** (one or more) → `not_eligible`
**Soft gaps only** → `potentially`
**All clear** → `eligible`

Each check returns a `{ label, met, note }` dict. `met` is `True`, `False`,
or `"partial"` — this is what drives the green/amber/red display in the UI.

The `check_all(student, opportunities)` function runs this against every
programme and returns three sorted buckets.

---

## Match Scoring

`scoring.py` computes a 0–100 score for each student–opportunity pair.
No machine learning. Every point is traceable to a specific rule.

| Factor            | Max Points | Logic                                               |
|-------------------|-----------|-----------------------------------------------------|
| GPA Headroom      | 25        | Full points if 0.5+ above minimum                  |
| Language          | 25        | Full points if test taken and score meets/exceeds   |
| Degree Level      | 20        | Binary — 20 if match, 0 if not                     |
| Country Preference| 15        | 15 if in preferred list, 12 if in preferred region  |
| Funding Alignment | 15        | 15 for fully funded, scales down for partial/varies |

**Grades:** 85–100 = Excellent, 65–84 = Good, 40–64 = Fair, 0–39 = Low

The score is independent of eligibility. A `not_eligible` programme can still
score 90/100 — meaning "this is a perfect fit, but you're missing IELTS."
That distinction helps students prioritise what to work on.

---

## Installation

**Requirements:** Python 3.8+

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/global-opportunities-navigator.git
cd global-opportunities-navigator

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Seed the database with sample opportunities
python seed_data.py

# 5. Run the development server
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

The database file `opportunities.db` is created automatically on first run.
To reset the data, delete `opportunities.db` and re-run `python seed_data.py`.

---

## Usage

1. **Home page** — overview of available programmes and upcoming deadlines
2. **Check My Chances** — fill in your academic profile (takes ~2 minutes)
3. **Results** — see which programmes you're eligible for, with match scores and requirement breakdowns
4. **Browse** — search and filter the full catalogue independently of your profile
5. **Dashboard** — summary of your eligibility, top matches, and what's blocking you
6. **Save** — bookmark programmes to review later

---

## Opportunities in the Database

| Programme                        | Country        | Type         | Funding       |
|----------------------------------|----------------|--------------|---------------|
| Stipendium Hungaricum            | Hungary        | Scholarship  | Fully Funded  |
| CSC Scholarship                  | China          | Scholarship  | Fully Funded  |
| Türkiye Bursları                 | Turkey         | Scholarship  | Fully Funded  |
| MEXT Scholarship                 | Japan          | Scholarship  | Fully Funded  |
| Commonwealth Scholarship         | United Kingdom | Scholarship  | Fully Funded  |
| DAAD Scholarship                 | Germany        | Scholarship  | Fully Funded  |
| ARICE Scholarship                | Italy          | Scholarship  | Fully Funded  |
| Korean Government Scholarship    | South Korea    | Scholarship  | Fully Funded  |
| Erasmus+ Exchange                | Europe         | Exchange     | Partial       |
| DAAD RISE Germany                | Germany        | Exchange     | Fully Funded  |
| University of Toronto            | Canada         | University   | Varies        |
| TU Delft                         | Netherlands    | University   | Varies        |
| University of Helsinki           | Finland        | University   | Varies        |

All data sourced from official programme websites. Deadlines change each cycle —
always verify before applying.

---

## Future Improvements

These are the next logical steps if I continue developing this project:

**Short term**
- Add a `.gitignore` and environment-based `SECRET_KEY` via `.env`
- Add more opportunities — HEC scholarships, Australia Awards, Fulbright
- Allow students to delete their profile and start over within the same session
- Add a "What should I do next?" rule-based guidance panel per programme

**Medium term**
- AI-powered explanation: user clicks "Why am I not eligible?" and gets a
  personalised improvement plan from Claude or GPT-4 via API call
- Deadline email reminders (Flask-Mail + a simple cron job)
- Allow operators to add new opportunities via an admin form without touching `seed_data.py`
- Pandas-powered analytics page: show which requirement blocks the most students

**Longer term**
- User accounts with proper authentication (Flask-Login)
- Community notes: students share tips about specific programmes
- Application tracker: mark programmes as "Applied", "Interview", "Accepted"
- Scraper that pulls live deadline data from official programme pages

---

## Notes for Interviewers

The eligibility engine (`eligibility.py`) and scoring algorithm (`scoring.py`) are
completely independent of Flask and SQLite. They take plain Python dicts and return
plain Python dicts. This means they can be unit tested in isolation, reused in a
different framework, or extended without touching the web layer.

The route handlers in `app.py` are intentionally thin — each one reads data,
calls a function, and passes the result to a template. Business logic lives in
the modules, not the routes.

---

*Built as a portfolio project. Data is for demonstration purposes only.*
*Always verify programme requirements and deadlines on official websites.*
