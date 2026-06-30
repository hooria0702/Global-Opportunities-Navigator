# 🌍 Opportunities Navigator

A web platform that helps students discover scholarships, internships, exchange programmes, fellowships, research programmes, and universities that match their academic profile.

Students can explore opportunities, check eligibility, receive match scores, track deadlines, and save programmes in one place.

🔗 **Live Demo:** https://oppsnav.pythonanywhere.com/

---

## ✨ Features

### 🎯 Profile-Based Matching
Create a student profile including:
- Degree level
- Major
- CGPA
- IELTS/TOEFL scores
- Funding preference
- Preferred countries

### 🔍 Smart Opportunity Search
Filter opportunities by:
- Country
- Region
- Programme Type
- Funding Type
- Degree Level
- Application Month

### ✅ Eligibility Analysis
Automatically determines whether a student is:
- Eligible
- Potentially Eligible
- Not Eligible

### 📊 Match Scoring
Generates a transparent score out of 100 based on:
- Academic fit
- Language readiness
- Degree compatibility
- Country preference
- Funding alignment

### ⏰ Deadline Tracking
Displays:
- Days remaining
- Upcoming deadlines
- Expired opportunities

### ⭐ Saved Opportunities
Bookmark opportunities for later review.

---

## 📸 Screenshots

### Home Page
<img src="https://github.com/user-attachments/assets/589a2e21-3135-4f7b-83ef-6defeffd1928" />

### Profile Setup
<img src="https://github.com/user-attachments/assets/2644f209-b5e7-4b9d-8d0d-37d2ff02bd14" />

### Eligibility Results
<img src="https://github.com/user-attachments/assets/600f2bb9-cdc9-4347-b64b-e14f8d834fee" />

### Opportunity Search
<img src="https://github.com/user-attachments/assets/6e125b8d-df07-4bf3-a34b-7b7b422e847c" />

### Opportunity Details
<img src="https://github.com/user-attachments/assets/7278f870-8552-4bf0-a80c-2bb5c4e857e2" />

### Dashboard
<img src="https://github.com/user-attachments/assets/93e8cd3c-4426-41be-9645-bf487e36e96e" />

### Saved Opportunities
<img src="https://github.com/user-attachments/assets/5d051a3a-512a-4445-bd8f-267d6e287347" />

---

## 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Backend | Python, Flask |
| Frontend | HTML, CSS, Bootstrap 5 |
| Database | SQLite |
| Templates | Jinja2 |
| Icons | Bootstrap Icons |

---

## 🏗 Project Structure

```text
Global-Opportunities-Navigator/
│
├── app.py
├── database.py
├── eligibility.py
├── scoring.py
├── seed_data.py
│
├── requirements.txt
├── README.md
├── opportunities.db
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── profile.html
│   ├── results.html
│   ├── search.html
│   ├── detail.html
│   ├── dashboard.html
│   ├── saved.html
│   ├── about.html
│   │
│   └── admin/
│       ├── form.html
│       ├── login.html
│       └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── main.js```
```
---

## ⚙ Eligibility Engine

The eligibility system evaluates:

1. GPA
2. Degree Level
3. Field of Study
4. IELTS
5. TOEFL
6. Country Preference
7. Funding Preference
8. Deadline Status

Results are classified as:

- Eligible
- Potentially Eligible
- Not Eligible

---

## 📈 Match Score Algorithm

| Factor | Weight |
|----------|----------|
| GPA | 25 |
| Language Requirements | 25 |
| Degree Level | 20 |
| Country Preference | 15 |
| Funding Alignment | 15 |

Total Score: **100**

---

## 🚀 Installation

```bash
git clone https://github.com/hooria0702/Global-Opportunities-Navigator.git

cd global-opportunities-navigator

pip install -r requirements.txt

python seed_data.py

python app.py
```

---

## 🎯 Motivation

Finding international opportunities is difficult because information is scattered across university websites, scholarship portals, and government platforms.

Opportunities Navigator centralises these opportunities and provides personalised eligibility analysis so students can quickly identify programmes that fit their profile.

---

## 🔮 Future Improvements

- More scholarships and internships
- Admin dashboard for adding opportunities
- Email deadline reminders
- AI-powered eligibility explanations
- User authentication
- Application tracker
- Live opportunity scraping

---

## 📄 Note

This project was built as a portfolio project to demonstrate:
- Full-stack web development
- Database design
- Search and filtering systems
- Rule-based recommendation logic
- Flask application architecture

Always verify programme requirements and deadlines through official sources before applying.
