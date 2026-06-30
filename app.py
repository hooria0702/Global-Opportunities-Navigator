"""
app.py — Flask routes. Thin layer: read → call module → render template.
"""
from flask import (Flask, render_template, request, redirect,
                   url_for, session, flash, jsonify)
from datetime import date, datetime
import database as db
import eligibility as elig
import scoring as sc
import os

app = Flask(__name__)
app.secret_key = os.environ.get(
    "SECRET_KEY",
    "local-development-key"
)

with app.app_context():
    db.init_db()

OPP_TYPES = ["Scholarship", "Exchange", "Internship", "Summer School",
             "Research Program", "Fellowship", "Competition"]
REGIONS    = ["Europe", "Asia Pacific", "North America", "Middle East & Central Asia",
              "Global", "Africa", "Latin America"]

ALL_COUNTRIES = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola",
    "Antigua and Barbuda", "Argentine", "Armenia", "Australia", "Austria",
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus",
    "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina",
    "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
    "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Republic",
    "Chad", "Chile", "China", "Colombia", "Comoros", "Republic of Congo",
    "Democratic Republic of the Congo", "Cook Islands", "Costa Rica",
    "Côte d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic",
    "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador",
    "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
    "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia",
    "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea",
    "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hong Kong", "Hungary",
    "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
    "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati",
    "South Korea", "Kosovo", "Kuwait", "Kyrgyz Republic", "Laos", "Latvia",
    "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania",
    "Luxembourg", "Macao", "Madagascar", "Malawi", "Malaysia", "Maldives",
    "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico",
    "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
    "Mozambique", "Multiple", "Myanmar", "Namibia", "Nauru", "Nepal",
    "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue",
    "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau",
    "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru",
    "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia",
    "Rwanda", "Saint Christopher and Nevis", "Saint Lucia", "Saint Vincent",
    "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia",
    "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan",
    "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
    "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste",
    "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey",
    "Turkmenistan", "Tuvalu", "UAE", "Uganda", "Ukraine",
    "United Arab Emirates", "United Kingdom", "United States", "Uruguay",
    "Uzbekistan", "Vanuatu", "Vatican", "Venezuela", "Viet Nam", "Yemen",
    "Zambia", "Zimbabwe",
]

@app.context_processor
def inject_globals():
    return {"today": date.today(), "current_year": date.today().year,
            "opp_types": OPP_TYPES}

# ── Home ────────────────────────────────────────────────────────────
@app.route("/")
def index():
    q = request.args.get("q", "").strip()
    if q:
        return redirect(url_for('search', q=q))
    opportunities = db.get_all_opportunities()
    stats = {t: 0 for t in OPP_TYPES}
    for opp in opportunities:
        stats[opp["type"]] = stats.get(opp["type"], 0) + 1
    upcoming = []
    for opp in opportunities:
        dl = opp["deadline"]
        if dl and dl.lower() != "rolling":
            try:
                dl_date = datetime.strptime(dl, "%Y-%m-%d").date()
                days_left = (dl_date - date.today()).days
                if 0 <= days_left <= 90:
                    upcoming.append({"opp": opp, "days_left": days_left})
            except ValueError:
                pass
    upcoming.sort(key=lambda x: x["days_left"])

    # Build display labels for the homepage stat strip — show the 4 largest
    # categories by count so it stays accurate as opportunity types grow,
    # rather than hardcoding specific type names.
    TYPE_LABELS = {
        "Scholarship":      "Scholarships",
        "Exchange":         "Exchanges",
        "University":       "Universities",
        "Internship":       "Internships",
        "Research Program": "Research Programs",
        "Fellowship":       "Fellowships",
        "Summer School":    "Summer Schools",
        "Competition":      "Competitions",
    }
    sorted_types = sorted(stats.items(), key=lambda kv: kv[1], reverse=True)
    top_stats = [
        (TYPE_LABELS.get(t, t), n, t) for t, n in sorted_types if n > 0
    ]

    return render_template("index.html", stats=stats, upcoming=upcoming[:6],
                           total=len(opportunities), regions=REGIONS,
                           top_stats=top_stats)

# ── Profile ─────────────────────────────────────────────────────────
@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        # Use .get() for everything — never let a missing/empty field crash the server
        name         = request.form.get("name", "").strip()
        nationality  = request.form.get("nationality", "Pakistani").strip()
        country      = request.form.get("country", "Pakistan").strip()
        degree_level = request.form.get("degree_level", "").strip()
        major        = request.form.get("major", "").strip()
        cgpa_raw     = request.form.get("cgpa", "").strip()
        budget       = request.form.get("budget", "").strip()

        # Server-side validation — catches what browser 'required' might miss
        errors = []
        if not name:
            errors.append("Please enter your name.")
        if not degree_level:
            errors.append("Please select a degree level.")
        if not major:
            errors.append("Please enter your major / field of study.")
        if not budget:
            errors.append("Please select a funding preference.")
        try:
            cgpa = float(cgpa_raw)
            if not (0.0 <= cgpa <= 4.0):
                errors.append("CGPA must be between 0.0 and 4.0.")
        except (ValueError, TypeError):
            errors.append("Please enter a valid CGPA (e.g. 3.2).")
            cgpa = 0.0

        if errors:
            for e in errors:
                flash(e, "warning")
            return render_template("profile.html")

        preferred_raw = request.form.get("preferred_countries", "")
        preferred_clean = ",".join(
            c.strip() for c in preferred_raw.replace("\n", ",").split(",") if c.strip()
        )

        data = {
            "name":                name,
            "nationality":         nationality or "Pakistani",
            "country":             country or "Pakistan",
            "degree_level":        degree_level,
            "major":               major,
            "cgpa":                cgpa,
            "has_ielts":           1 if request.form.get("has_ielts") else 0,
            "ielts_score":         request.form.get("ielts_score") or None,
            "has_toefl":           1 if request.form.get("has_toefl") else 0,
            "toefl_score":         request.form.get("toefl_score") or None,
            "budget":              budget,
            "preferred_countries": preferred_clean,
        }
        student_id = db.save_student(data)
        session["student_id"] = student_id
        flash("Profile saved!", "success")
        return redirect(url_for("results"))
    return render_template("profile.html")

# ── Results ─────────────────────────────────────────────────────────
@app.route("/results")
def results():
    student_id = session.get("student_id")
    if not student_id:
        flash("Please fill in your profile first.", "warning")
        return redirect(url_for("profile"))
    student = db.get_student_by_id(student_id)
    opportunities = db.get_all_opportunities()
    buckets = elig.check_all(student, opportunities)
    for bucket_key in buckets:
        for item in buckets[bucket_key]:
            item["score_result"] = sc.compute_score(student, item["opportunity"])
    buckets["eligible"].sort(key=lambda x: x["score_result"]["score"], reverse=True)
    buckets["potentially"].sort(key=lambda x: x["score_result"]["score"], reverse=True)
    return render_template("results.html", student=student, buckets=buckets,
                           eligible_count=len(buckets["eligible"]),
                           potential_count=len(buckets["potentially"]),
                           not_count=len(buckets["not_eligible"]))

# ── Search ──────────────────────────────────────────────────────────
@app.route("/search")
def search():
    filters = {
        "q":             request.args.get("q", "").strip(),
        "country":       request.args.get("country", "").strip(),
        "region":        request.args.get("region", "").strip(),
        "funding_type":  request.args.get("funding_type", "").strip(),
        "opp_type":      request.args.get("opp_type", "").strip(),
        "degree_level":  request.args.get("degree_level", "").strip(),
        "field":         request.args.get("field", "").strip(),
        "deadline_month":request.args.get("deadline_month", "").strip(),
    }
    any_filter = any(filters.values())
    opportunities = db.search_opportunities(filters) if any_filter else db.get_all_opportunities()
    enriched = []
    for opp in opportunities:
        enriched.append({"opp": opp, "days_left": _days_left(opp["deadline"], opp["application_status"] if opp["application_status"] else None)})
    countries = ALL_COUNTRIES
    all_opps = db.get_all_opportunities()
    fields_list = sorted({
        f.strip() for o in all_opps
        for f in o["fields"].split(",") if f.strip().lower() != "all"
    })
    return render_template("search.html", results=enriched, filters=filters,
                           countries=countries, fields_list=fields_list,
                           regions=REGIONS, opp_types=OPP_TYPES,
                           result_count=len(enriched))

# ── Detail ──────────────────────────────────────────────────────────
@app.route("/opportunity/<int:opp_id>")
def opportunity_detail(opp_id):
    opp = db.get_opportunity_by_id(opp_id)
    if not opp:
        flash("Opportunity not found.", "danger")
        return redirect(url_for("search"))
    days_left = _days_left(opp["deadline"], opp["application_status"] if opp["application_status"] else None)
    elig_result = score_result = roadmap_steps = None
    student_id = session.get("student_id")
    if student_id:
        student = db.get_student_by_id(student_id)
        elig_result = elig.check_eligibility(student, dict(opp))
        score_result = sc.compute_score(student, dict(opp))
        roadmap_steps = elig.generate_roadmap(student, dict(opp))
    return render_template("detail.html", opp=opp, days_left=days_left,
                           elig_result=elig_result, score_result=score_result,
                           roadmap_steps=roadmap_steps)

# ── Save / unsave ────────────────────────────────────────────────────
@app.route("/save/<int:opp_id>", methods=["POST"])
def save_opportunity(opp_id):
    student_id = session.get("student_id")
    if not student_id:
        flash("Set up your profile first.", "warning")
        return redirect(url_for("profile"))
    db.save_bookmark(student_id, opp_id)
    flash("Saved to your list.", "success")
    return redirect(request.referrer or url_for("search"))

@app.route("/unsave/<int:opp_id>", methods=["POST"])
def unsave_opportunity(opp_id):
    student_id = session.get("student_id")
    if student_id:
        db.remove_bookmark(student_id, opp_id)
        flash("Removed from saved list.", "success")
    return redirect(request.referrer or url_for("saved"))

# ── Saved ────────────────────────────────────────────────────────────
@app.route("/saved")
def saved():
    student_id = session.get("student_id")
    if not student_id:
        flash("Set up your profile first.", "warning")
        return redirect(url_for("profile"))
    student = db.get_student_by_id(student_id)
    opps = db.get_saved_opportunities(student_id)
    enriched = []
    for opp in opps:
        enriched.append({"opp": opp, "days_left": _days_left(opp["deadline"]),
                         "score_result": sc.compute_score(student, dict(opp))})
    return render_template("saved.html", student=student, saved=enriched)

# ── Dashboard ────────────────────────────────────────────────────────
@app.route("/dashboard")
def dashboard():
    student_id = session.get("student_id")
    if not student_id:
        flash("Set up your profile to see your dashboard.", "warning")
        return redirect(url_for("profile"))
    student = db.get_student_by_id(student_id)
    opportunities = db.get_all_opportunities()
    buckets = elig.check_all(student, opportunities)
    scored = sc.score_all(student, [i["opportunity"] for i in buckets["eligible"]])
    top_matches = scored[:3]
    deadlines = []
    for item in buckets["eligible"] + buckets["potentially"]:
        opp = item["opportunity"]
        dl = _days_left(opp["deadline"])
        if dl is not None and 0 <= dl <= 120:
            deadlines.append({"opp": opp, "days_left": dl})
    deadlines.sort(key=lambda x: x["days_left"])
    saved_count = len(db.get_saved_opportunities(student_id))
    return render_template("dashboard.html", student=student, buckets=buckets,
                           eligible_count=len(buckets["eligible"]),
                           potential_count=len(buckets["potentially"]),
                           not_count=len(buckets["not_eligible"]),
                           top_matches=top_matches, deadlines=deadlines[:6],
                           saved_count=saved_count)

# ── About ─────────────────────────────────────────────────────────
@app.route("/about")
def about():
    return render_template("about.html")

# ══════════════════════════════════════════════════════════════════
# ADMIN PANEL
# ══════════════════════════════════════════════════════════════════

def admin_required():
    return session.get("admin_logged_in")

@app.route("/admin")
def admin():
    if not admin_required():
        return redirect(url_for("admin_login"))
    opps = db.get_all_opportunities()
    stats = {t: 0 for t in OPP_TYPES}
    for o in opps:
        stats[o["type"]] = stats.get(o["type"], 0) + 1
    submissions = db.get_submissions()
    return render_template("admin/index.html", opportunities=opps, stats=stats,
                           total=len(opps), submissions=submissions)

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if db.verify_admin(username, password):
            session["admin_logged_in"] = True
            flash("Logged in.", "success")
            return redirect(url_for("admin"))
        flash("Invalid credentials.", "danger")
    return render_template("admin/login.html")

@app.route("/admin/logout")
def admin_logout():
    session.pop("admin_logged_in", None)
    flash("Logged out.", "success")
    return redirect(url_for("admin_login"))

@app.route("/admin/add", methods=["GET", "POST"])
def admin_add():
    if not admin_required():
        return redirect(url_for("admin_login"))
    if request.method == "POST":
        data = _form_to_opp_dict(request.form)
        db.admin_add_opportunity(data)
        flash(f"'{data['name']}' added successfully.", "success")
        return redirect(url_for("admin"))
    return render_template("admin/form.html", opp=None, action="Add",
                           opp_types=OPP_TYPES, regions=REGIONS)

@app.route("/admin/edit/<int:opp_id>", methods=["GET", "POST"])
def admin_edit(opp_id):
    if not admin_required():
        return redirect(url_for("admin_login"))
    opp = db.get_opportunity_by_id(opp_id)
    if not opp:
        flash("Opportunity not found.", "danger")
        return redirect(url_for("admin"))
    if request.method == "POST":
        data = _form_to_opp_dict(request.form)
        db.admin_update_opportunity(opp_id, data)
        flash(f"'{data['name']}' updated.", "success")
        return redirect(url_for("admin"))
    return render_template("admin/form.html", opp=dict(opp), action="Edit",
                           opp_types=OPP_TYPES, regions=REGIONS)

@app.route("/admin/delete/<int:opp_id>", methods=["POST"])
def admin_delete(opp_id):
    if not admin_required():
        return redirect(url_for("admin_login"))
    opp = db.get_opportunity_by_id(opp_id)
    if opp:
        name = opp["name"]
        db.admin_delete_opportunity(opp_id)
        flash(f"'{name}' deleted.", "success")
    return redirect(url_for("admin"))

# ── Helpers ──────────────────────────────────────────────────────────
def _days_left(deadline_str, app_status=None):
    """Return days until deadline. Returns None for rolling/invalid. Negative if past."""
    if app_status and app_status.lower() == "closed":
        return -1  # treat as closed regardless of date
    if not deadline_str or deadline_str.lower() == "rolling":
        return None
    try:
        return (datetime.strptime(deadline_str, "%Y-%m-%d").date() - date.today()).days
    except ValueError:
        return None

def _form_to_opp_dict(form):
    return {
        "name":           form.get("name","").strip(),
        "country":        form.get("country","").strip(),
        "region":         form.get("region","Global"),
        "type":           form.get("type","Scholarship"),
        "degree_levels":  ",".join(form.getlist("degree_levels")),
        "fields":         form.get("fields","All").strip(),
        "min_gpa":        form.get("min_gpa",0) or 0,
        "ielts_required": 1 if form.get("ielts_required") else 0,
        "min_ielts":      form.get("min_ielts") or None,
        "toefl_required": 1 if form.get("toefl_required") else 0,
        "min_toefl":      form.get("min_toefl") or None,
        "funding_type":        form.get("funding_type","Varies"),
        "deadline":            form.get("deadline") or None,
        "opening_date":        form.get("opening_date") or None,
        "application_status":  form.get("application_status","Open"),
        "description":         form.get("description","").strip(),
        "official_link":  form.get("official_link","").strip(),
        "roadmap":        form.get("roadmap","").strip(),
    }


# ── Opportunity Submission ────────────────────────────────────────
@app.route("/submit", methods=["GET", "POST"])
def submit_opportunity():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if not name:
            flash("Please provide the programme name.", "warning")
            return render_template("submit.html")
        data = {
            "name":        name,
            "type":        request.form.get("type", "").strip(),
            "country":     request.form.get("country", "").strip(),
            "link":        request.form.get("link", "").strip(),
            "description": request.form.get("description", "").strip(),
            "submitter":   request.form.get("submitter", "").strip(),
        }
        db.save_submission(data)
        flash("Thank you! Your suggestion has been submitted for review.", "success")
        return redirect(url_for("submit_opportunity"))
    return render_template("submit.html")

if __name__ == "__main__":
    app.run()
