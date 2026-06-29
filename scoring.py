"""
scoring.py
----------
Transparent, explainable match score between a student and an opportunity.
No machine learning.  Every point is traceable to a specific rule.

Max score: 100 points across 5 weighted factors.

Factor              Weight   Max pts
──────────────────────────────────────
GPA headroom           25      25
Language readiness     25      25
Degree level match     20      20
Country preference     15      15
Funding alignment      15      15
──────────────────────────────────────
Total                 100     100
"""


def compute_score(student: dict, opportunity: dict) -> dict:
    """
    Returns
    -------
    {
        "score":    int   (0-100),
        "grade":    str   ("Excellent" | "Good" | "Fair" | "Low"),
        "factors":  [ { "label", "points", "max", "note" }, ... ]
    }
    """
    # Normalise sqlite3.Row → plain dict so .get() works
    if not isinstance(student, dict):
        student = dict(student)
    if not isinstance(opportunity, dict):
        opportunity = dict(opportunity)

    factors = []

    # ── 1. GPA headroom (25 pts) ──────────────────────────────────── #
    cgpa    = float(student["cgpa"])
    min_gpa = float(opportunity["min_gpa"] or 0)

    if min_gpa == 0:
        gpa_pts = 25
        gpa_note = "No GPA requirement — full points awarded"
    else:
        headroom = cgpa - min_gpa
        if headroom >= 0.5:
            gpa_pts  = 25
            gpa_note = f"Strong GPA headroom (+{headroom:.2f} above minimum)"
        elif headroom >= 0.2:
            gpa_pts  = 18
            gpa_note = f"Comfortable GPA headroom (+{headroom:.2f})"
        elif headroom >= 0:
            gpa_pts  = 10
            gpa_note = f"GPA just meets the minimum (+{headroom:.2f})"
        elif headroom >= -0.2:
            gpa_pts  = 4
            gpa_note = f"GPA slightly below minimum ({headroom:.2f})"
        else:
            gpa_pts  = 0
            gpa_note = f"GPA significantly below minimum ({headroom:.2f})"

    factors.append({"label": "GPA", "points": gpa_pts, "max": 25, "note": gpa_note})

    # ── 2. Language readiness (25 pts) ────────────────────────────── #
    ielts_req  = bool(int(opportunity["ielts_required"] or 0))
    toefl_req  = bool(int(opportunity["toefl_required"] or 0))
    has_ielts  = bool(int(student["has_ielts"] or 0))
    has_toefl  = bool(int(student["has_toefl"] or 0))
    ielts_score = student.get("ielts_score")
    toefl_score = student.get("toefl_score")
    min_ielts   = opportunity.get("min_ielts")
    min_toefl   = opportunity.get("min_toefl")

    if not ielts_req and not toefl_req:
        lang_pts  = 25
        lang_note = "No language test required"
    elif ielts_req and has_ielts:
        if min_ielts and ielts_score:
            gap = float(ielts_score) - float(min_ielts)
            if gap >= 0.5:
                lang_pts  = 25
                lang_note = f"IELTS {ielts_score} — well above minimum {min_ielts}"
            elif gap >= 0:
                lang_pts  = 18
                lang_note = f"IELTS {ielts_score} meets requirement (min {min_ielts})"
            else:
                lang_pts  = 5
                lang_note = f"IELTS {ielts_score} below minimum {min_ielts}"
        else:
            lang_pts  = 20
            lang_note = "IELTS available — no minimum specified"
    elif toefl_req and has_toefl:
        if min_toefl and toefl_score:
            gap = int(toefl_score) - int(min_toefl)
            if gap >= 10:
                lang_pts  = 25
                lang_note = f"TOEFL {toefl_score} — well above minimum {min_toefl}"
            elif gap >= 0:
                lang_pts  = 18
                lang_note = f"TOEFL {toefl_score} meets requirement (min {min_toefl})"
            else:
                lang_pts  = 5
                lang_note = f"TOEFL {toefl_score} below required {min_toefl}"
        else:
            lang_pts  = 20
            lang_note = "TOEFL available — no minimum specified"
    else:
        lang_pts  = 0
        lang_note = "Required language test not taken"

    factors.append({"label": "Language", "points": lang_pts, "max": 25, "note": lang_note})

    # ── 3. Degree level match (20 pts) ────────────────────────────── #
    degree_levels  = [d.strip() for d in opportunity["degree_levels"].split(",")]
    student_degree = student["degree_level"].strip()

    if student_degree in degree_levels:
        deg_pts  = 20
        deg_note = f"{student_degree} is an accepted degree level"
    else:
        deg_pts  = 0
        deg_note = f"Programme does not accept {student_degree} students"

    factors.append({"label": "Degree Level", "points": deg_pts, "max": 20, "note": deg_note})

    # ── 4. Country preference (15 pts) ────────────────────────────── #
    preferred_raw = student.get("preferred_countries", "") or ""
    preferred     = [c.strip().lower() for c in preferred_raw.split(",") if c.strip()]
    opp_country   = opportunity["country"].lower()

    europe_group = {
        "germany", "france", "hungary", "netherlands",
        "finland", "italy", "europe", "austria", "sweden",
        "norway", "denmark", "belgium", "spain"
    }

    if not preferred:
        country_pts  = 10
        country_note = "No preference set — neutral score"
    elif opp_country in preferred:
        country_pts  = 15
        country_note = f"{opportunity['country']} is in your preferred list"
    elif "europe" in preferred and opp_country in europe_group:
        country_pts  = 12
        country_note = f"{opportunity['country']} is in Europe (your preferred region)"
    else:
        country_pts  = 3
        country_note = f"{opportunity['country']} is not in your preferred list"

    factors.append({"label": "Country Preference", "points": country_pts, "max": 15, "note": country_note})

    # ── 5. Funding alignment (15 pts) ─────────────────────────────── #
    funding_type   = opportunity["funding_type"].lower()
    student_budget = student["budget"].lower()

    if "fully" in funding_type:
        fund_pts  = 15
        fund_note = "Fully funded — best match for any budget preference"
    elif student_budget == "partial" and "partial" in funding_type:
        fund_pts  = 12
        fund_note = "Partial funding matches your preference"
    elif student_budget == "self":
        fund_pts  = 15
        fund_note = "Self-funded preference — any programme qualifies"
    elif "varies" in funding_type:
        fund_pts  = 8
        fund_note = "Funding varies — aid availability uncertain"
    else:
        fund_pts  = 3
        fund_note = f"Funding type ({opportunity['funding_type']}) doesn't align with your preference"

    factors.append({"label": "Funding", "points": fund_pts, "max": 15, "note": fund_note})

    # ── Final score ───────────────────────────────────────────────── #
    total = sum(f["points"] for f in factors)

    if total >= 85:
        grade = "Excellent"
    elif total >= 65:
        grade = "Good"
    elif total >= 40:
        grade = "Fair"
    else:
        grade = "Low"

    return {
        "score":   total,
        "grade":   grade,
        "factors": factors,
    }


def score_all(student: dict, opportunities: list) -> list:
    """
    Score a student against every opportunity.
    Returns a list of dicts sorted by score descending.
    """
    scored = []
    for opp in opportunities:
        opp_dict = dict(opp)
        result   = compute_score(student, opp_dict)
        scored.append({"opportunity": opp_dict, "score_result": result})

    scored.sort(key=lambda x: x["score_result"]["score"], reverse=True)
    return scored


# ------------------------------------------------------------------ #
# Smoke-test — run:  python scoring.py                                #
# ------------------------------------------------------------------ #

if __name__ == "__main__":
    sample_student = {
        "name": "Ali Hassan",
        "degree_level": "Bachelors",
        "major": "Computer Science",
        "cgpa": 3.4,
        "has_ielts": 0,
        "ielts_score": None,
        "has_toefl": 0,
        "toefl_score": None,
        "budget": "Fully Funded",
        "preferred_countries": "Germany,Hungary,Turkey",
    }
    opps = [
        {
            "name": "Stipendium Hungaricum", "country": "Hungary",
            "degree_levels": "Bachelors,Masters,PhD", "fields": "All",
            "min_gpa": 3.0, "ielts_required": 0, "min_ielts": None,
            "toefl_required": 0, "min_toefl": None, "funding_type": "Fully Funded",
        },
        {
            "name": "DAAD Scholarship", "country": "Germany",
            "degree_levels": "Masters,PhD", "fields": "All",
            "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.0,
            "toefl_required": 0, "min_toefl": 80, "funding_type": "Fully Funded",
        },
    ]
    for item in opps:
        r = compute_score(sample_student, item)
        print(f"\n{'='*52}")
        print(f"  {item['name']}")
        print(f"  Score : {r['score']}/100  ({r['grade']})")
        for f in r["factors"]:
            bar = "█" * (f["points"] * 10 // f["max"]) if f["max"] else ""
            print(f"    {f['label']:20s} {f['points']:2d}/{f['max']}  {bar}  {f['note']}")
