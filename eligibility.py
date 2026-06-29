"""
eligibility.py — Pure Python eligibility engine.
No Flask, no SQLite. Fully unit-testable.
"""
from datetime import date, datetime


def check_eligibility(student, opportunity):
    if not isinstance(student, dict):
        student = dict(student)
    if not isinstance(opportunity, dict):
        opportunity = dict(opportunity)

    requirements = []
    hard_failures = 0
    soft_gaps = 0

    # 1. GPA
    min_gpa = float(opportunity.get("min_gpa") or 0)
    cgpa = float(student.get("cgpa") or 0)
    if min_gpa == 0:
        requirements.append({"label": "GPA", "met": True, "note": "No GPA requirement"})
    elif cgpa >= min_gpa:
        requirements.append({"label": "GPA", "met": True, "note": f"Your CGPA {cgpa:.2f} meets the minimum {min_gpa:.2f}"})
    elif min_gpa - cgpa <= 0.2:
        soft_gaps += 1
        requirements.append({"label": "GPA", "met": "partial", "note": f"CGPA {cgpa:.2f} is slightly below {min_gpa:.2f} — some programmes consider upward trends"})
    else:
        hard_failures += 1
        requirements.append({"label": "GPA", "met": False, "note": f"CGPA {cgpa:.2f} is below the minimum {min_gpa:.2f}"})

    # 2. Nationality eligibility
    eligible_nat_raw = (opportunity.get("eligible_nationalities") or "").strip()
    if eligible_nat_raw:
        allowed = [n.strip().lower() for n in eligible_nat_raw.split(",") if n.strip()]
        student_nat = (student.get("nationality") or student.get("country") or "Pakistani").strip().lower()
        # match if student nationality or common variants appear in the allowed list
        nat_variants = {student_nat}
        # handle "Pakistani" ↔ "Pakistan" etc
        if student_nat.endswith("i"):
            nat_variants.add(student_nat[:-1])   # Pakistani → Pakistan
        if not student_nat.endswith("i"):
            nat_variants.add(student_nat + "i")
        nat_match = any(v in allowed for v in nat_variants)
        if nat_match:
            requirements.append({"label": "Nationality", "met": True,
                "note": f"Open to {student.get('nationality', 'Pakistani')} students"})
        else:
            hard_failures += 1
            requirements.append({"label": "Nationality", "met": False,
                "note": f"This programme is restricted to: {eligible_nat_raw}. Pakistani students are not currently eligible."})
    # else: no nationality restriction — skip the check entirely (don't add a row)

    # 3. Degree Level
    degree_levels = [d.strip() for d in (opportunity.get("degree_levels") or "").split(",")]
    student_degree = (student.get("degree_level") or "").strip()
    if student_degree in degree_levels:
        requirements.append({"label": "Degree Level", "met": True, "note": f"Programme accepts {student_degree} students"})
    else:
        hard_failures += 1
        requirements.append({"label": "Degree Level", "met": False, "note": f"Programme is for {', '.join(degree_levels)} only"})

    # 4. Field
    opp_fields = (opportunity.get("fields") or "All").strip()
    if opp_fields.lower() == "all":
        requirements.append({"label": "Field of Study", "met": True, "note": "Open to all fields"})
    else:
        accepted = [f.strip().lower() for f in opp_fields.split(",")]
        major = (student.get("major") or "").strip().lower()
        if any(f in major or major in f for f in accepted):
            requirements.append({"label": "Field of Study", "met": True, "note": f"Your major matches: {opp_fields}"})
        else:
            soft_gaps += 1
            requirements.append({"label": "Field of Study", "met": "partial", "note": f"Programme targets {opp_fields}. Your major '{student.get('major')}' may not qualify — verify on the official site."})

    # 5. IELTS
    ielts_req = bool(int(opportunity.get("ielts_required") or 0))
    min_ielts = opportunity.get("min_ielts")
    if not ielts_req:
        requirements.append({"label": "IELTS", "met": True, "note": "No IELTS required"})
    else:
        has_ielts = bool(int(student.get("has_ielts") or 0))
        score = student.get("ielts_score")
        if not has_ielts:
            hard_failures += 1
            requirements.append({"label": "IELTS", "met": False, "note": f"IELTS required{f' (minimum {min_ielts})' if min_ielts else ''} but you haven't taken it"})
        elif min_ielts and score and float(score) < float(min_ielts):
            hard_failures += 1
            requirements.append({"label": "IELTS", "met": False, "note": f"Your IELTS {score} is below the required {min_ielts}"})
        else:
            requirements.append({"label": "IELTS", "met": True, "note": f"IELTS satisfied{f' (score {score})' if score else ''}"})

    # 6. TOEFL
    toefl_req = bool(int(opportunity.get("toefl_required") or 0))
    min_toefl = opportunity.get("min_toefl")
    if not toefl_req:
        requirements.append({"label": "TOEFL", "met": True, "note": "No TOEFL required"})
    else:
        has_toefl = bool(int(student.get("has_toefl") or 0))
        score = student.get("toefl_score")
        if not has_toefl:
            hard_failures += 1
            requirements.append({"label": "TOEFL", "met": False, "note": f"TOEFL required{f' (minimum {min_toefl})' if min_toefl else ''} but you haven't taken it"})
        elif min_toefl and score and int(score) < int(min_toefl):
            hard_failures += 1
            requirements.append({"label": "TOEFL", "met": False, "note": f"Your TOEFL {score} is below the required {min_toefl}"})
        else:
            requirements.append({"label": "TOEFL", "met": True, "note": f"TOEFL satisfied{f' (score {score})' if score else ''}"})

    # 7. Country preference
    preferred_raw = student.get("preferred_countries") or ""
    preferred = [c.strip().lower() for c in preferred_raw.split(",") if c.strip()]
    opp_country = (opportunity.get("country") or "").lower()
    opp_region = (opportunity.get("region") or "").lower()
    europe = {"germany","france","hungary","netherlands","finland","italy","europe","austria","sweden","norway","denmark","belgium","spain","switzerland","uk","united kingdom","portugal","ireland"}
    if not preferred:
        requirements.append({"label": "Country Preference", "met": True, "note": "No preference set"})
    elif opp_country in preferred or opp_region.lower() in [p.lower() for p in preferred]:
        requirements.append({"label": "Country Preference", "met": True, "note": f"{opportunity.get('country')} matches your preferences"})
    elif "europe" in preferred and opp_country in europe:
        requirements.append({"label": "Country Preference", "met": True, "note": f"{opportunity.get('country')} is in Europe (your preferred region)"})
    else:
        soft_gaps += 1
        requirements.append({"label": "Country Preference", "met": "partial", "note": f"{opportunity.get('country')} is not in your preferred list, but you can still apply"})

    # 8. Funding
    funding = (opportunity.get("funding_type") or "").lower()
    budget = (student.get("budget") or "").lower()
    if "fully" in funding:
        requirements.append({"label": "Funding", "met": True, "note": "Fully funded — matches any preference"})
    elif budget == "partial" and ("partial" in funding or "varies" in funding):
        requirements.append({"label": "Funding", "met": True, "note": "Partial funding matches your preference"})
    elif budget == "self":
        requirements.append({"label": "Funding", "met": True, "note": "Self-funded preference — any programme qualifies"})
    else:
        soft_gaps += 1
        requirements.append({"label": "Funding", "met": "partial", "note": f"Programme is {opportunity.get('funding_type')} — check if this fits your situation"})

    # 9. Application status, opening date, and deadline
    app_status = (opportunity.get("application_status") or "Open").strip()
    opening_raw = opportunity.get("opening_date")
    dl = opportunity.get("deadline")
    today = date.today()

    # Closed by explicit status
    if app_status.lower() == "closed":
        hard_failures += 1
        requirements.append({"label": "Application Status", "met": False,
            "note": "Applications are currently closed for this cycle."})

    # Not yet open
    elif opening_raw:
        try:
            open_date = datetime.strptime(opening_raw, "%Y-%m-%d").date()
            if open_date > today:
                days_until = (open_date - today).days
                requirements.append({"label": "Application Status", "met": "partial",
                    "note": f"Applications open in {days_until} days ({opening_raw}) — bookmark this now."})
                soft_gaps += 1
            else:
                # Open — check deadline
                if not dl or dl.lower() == "rolling":
                    requirements.append({"label": "Deadline", "met": True, "note": "Rolling deadline — apply any time"})
                else:
                    try:
                        dl_date = datetime.strptime(dl, "%Y-%m-%d").date()
                        days_left = (dl_date - today).days
                        if days_left < 0:
                            hard_failures += 1
                            requirements.append({"label": "Deadline", "met": False, "note": f"Deadline passed ({dl})"})
                        else:
                            requirements.append({"label": "Deadline", "met": True, "note": f"{days_left} days remaining (deadline: {dl})"})
                    except ValueError:
                        requirements.append({"label": "Deadline", "met": True, "note": f"Deadline: {dl}"})
        except ValueError:
            requirements.append({"label": "Application Status", "met": True, "note": f"Opens: {opening_raw}"})

    # No opening date — just check deadline
    elif not dl or dl.lower() == "rolling":
        requirements.append({"label": "Deadline", "met": True, "note": "Rolling deadline — apply any time"})
    else:
        try:
            dl_date = datetime.strptime(dl, "%Y-%m-%d").date()
            days_left = (dl_date - today).days
            if days_left < 0:
                hard_failures += 1
                requirements.append({"label": "Deadline", "met": False, "note": f"Deadline passed ({dl}) — check for next cycle"})
            else:
                requirements.append({"label": "Deadline", "met": True, "note": f"{days_left} days remaining (deadline: {dl})"})
        except ValueError:
            requirements.append({"label": "Deadline", "met": True, "note": f"Deadline: {dl}"})

    met_count = sum(1 for r in requirements if r["met"] is True)
    total_count = len(requirements)

    if hard_failures == 0 and soft_gaps == 0:
        status = "eligible"
        summary = "You meet all requirements."
    elif hard_failures == 0:
        status = "potentially"
        summary = f"You meet core requirements but have {soft_gaps} soft gap(s)."
    else:
        status = "not_eligible"
        summary = f"{hard_failures} hard requirement(s) not met."

    return {
        "status": status,
        "requirements": requirements,
        "met_count": met_count,
        "total_count": total_count,
        "summary": summary,
        "hard_failures": hard_failures,
        "soft_gaps": soft_gaps,
    }


def check_all(student, opportunities):
    buckets = {"eligible": [], "potentially": [], "not_eligible": []}
    for opp in opportunities:
        result = check_eligibility(student, opp)
        buckets[result["status"]].append({"opportunity": dict(opp), "result": result})
    for key in buckets:
        buckets[key].sort(key=lambda x: x["result"]["met_count"], reverse=True)
    return buckets


def generate_roadmap(student, opportunity):
    """
    Generate a personalised step-by-step roadmap based on missing requirements.
    Combines the programme's stored roadmap with personalised gap advice.
    """
    if not isinstance(student, dict):
        student = dict(student)
    if not isinstance(opportunity, dict):
        opportunity = dict(opportunity)

    result = check_eligibility(student, opportunity)
    steps = []

    # Add personalised gap steps first
    for req in result["requirements"]:
        if req["met"] is False or req["met"] == "partial":
            label = req["label"]
            if "IELTS" in label and req["met"] is False:
                min_ielts = opportunity.get("min_ielts")
                score_needed = min_ielts if min_ielts else 6.5
                steps.append(f"Register for IELTS and achieve a band score of {score_needed}+")
            elif "GPA" in label and req["met"] is False:
                steps.append(f"Improve your CGPA to at least {opportunity.get('min_gpa', 3.0):.1f} — focus on upcoming semester grades")
            elif "GPA" in label and req["met"] == "partial":
                steps.append(f"Your CGPA is close — maintain or improve it above {opportunity.get('min_gpa', 3.0):.1f} this semester")
            elif "Field" in label:
                steps.append(f"Verify that your major qualifies for this programme's field requirements ({opportunity.get('fields')})")
            elif "Deadline" in label:
                steps.append("Note: this cycle's deadline has passed — bookmark it for next year's intake")

    # Then add the programme's official roadmap steps, skipping near-duplicates of gap steps already added
    roadmap_text = opportunity.get("roadmap") or ""
    if roadmap_text:
        import re
        gap_keywords = []
        if any("IELTS" in s for s in steps):
            gap_keywords.append("ielts")
        if any("CGPA" in s for s in steps):
            gap_keywords.append("gpa")

        for line in roadmap_text.strip().split("\n"):
            line = line.strip()
            if not line:
                continue
            clean = re.sub(r"^\d+\.\s*", "", line)
            clean_lower = clean.lower()
            # skip programme steps that just restate a gap we already flagged
            is_duplicate_gap = any(
                kw in clean_lower and ("required" in clean_lower or "recommended" in clean_lower or "minimum" in clean_lower or "register for" in clean_lower)
                for kw in gap_keywords
            )
            if clean and not is_duplicate_gap and clean not in steps:
                steps.append(clean)

    return steps
