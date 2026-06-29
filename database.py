import sqlite3
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "opportunities.db")


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            name                TEXT    NOT NULL,
            nationality         TEXT    NOT NULL DEFAULT 'Pakistani',
            country             TEXT    NOT NULL DEFAULT 'Pakistan',
            degree_level        TEXT    NOT NULL,
            major               TEXT    NOT NULL,
            cgpa                REAL    NOT NULL,
            has_ielts           INTEGER NOT NULL DEFAULT 0,
            ielts_score         REAL,
            has_toefl           INTEGER NOT NULL DEFAULT 0,
            toefl_score         INTEGER,
            budget              TEXT    NOT NULL,
            preferred_countries TEXT,
            created_at          TEXT    DEFAULT (datetime('now'))
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS opportunities (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            name            TEXT    NOT NULL,
            country         TEXT    NOT NULL,
            region          TEXT    NOT NULL DEFAULT 'Global',
            type            TEXT    NOT NULL,
            degree_levels   TEXT    NOT NULL,
            fields          TEXT    NOT NULL DEFAULT 'All',
            min_gpa         REAL    NOT NULL DEFAULT 0.0,
            ielts_required  INTEGER NOT NULL DEFAULT 0,
            min_ielts       REAL,
            toefl_required  INTEGER NOT NULL DEFAULT 0,
            min_toefl       INTEGER,
            funding_type    TEXT    NOT NULL,
            deadline        TEXT,
            opening_date    TEXT,
            application_status TEXT NOT NULL DEFAULT 'Open',
            description     TEXT,
            official_link   TEXT,
            roadmap                 TEXT,
            eligible_nationalities  TEXT    DEFAULT '',
            created_at              TEXT    DEFAULT (datetime('now'))
        )
    """)

    # Migrate existing DBs that don't have newer columns
    for migration in [
        "ALTER TABLE opportunities ADD COLUMN region TEXT NOT NULL DEFAULT 'Global'",
        "ALTER TABLE opportunities ADD COLUMN roadmap TEXT",
        "ALTER TABLE opportunities ADD COLUMN eligible_nationalities TEXT DEFAULT ''",
        "ALTER TABLE students ADD COLUMN nationality TEXT NOT NULL DEFAULT 'Pakistani'",
        "ALTER TABLE opportunities ADD COLUMN opening_date TEXT",
        "ALTER TABLE opportunities ADD COLUMN application_status TEXT NOT NULL DEFAULT 'Open'",
    ]:
        try:
            c.execute(migration)
        except Exception:
            pass

    c.execute("""
        CREATE TABLE IF NOT EXISTS saved_opportunities (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id      INTEGER NOT NULL,
            opportunity_id  INTEGER NOT NULL,
            saved_at        TEXT    DEFAULT (datetime('now')),
            FOREIGN KEY (student_id)     REFERENCES students(id),
            FOREIGN KEY (opportunity_id) REFERENCES opportunities(id),
            UNIQUE (student_id, opportunity_id)
        )
    """)

    # Admin users table (simple, no hashing needed for portfolio)
    c.execute("""
        CREATE TABLE IF NOT EXISTS admin_users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT    UNIQUE NOT NULL,
            password TEXT    NOT NULL
        )
    """)
    # Default admin credentials (change in production)
    c.execute("INSERT OR IGNORE INTO admin_users (username, password) VALUES ('admin', 'Opps_Nav#2026')")

    conn.commit()
    conn.close()


# ── Query helpers ───────────────────────────────────────────────────

def get_all_opportunities():
    conn = get_db()
    rows = conn.execute("SELECT * FROM opportunities ORDER BY deadline ASC").fetchall()
    conn.close()
    return rows


def get_opportunity_by_id(opp_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM opportunities WHERE id = ?", (opp_id,)).fetchone()
    conn.close()
    return row


def save_student(data):
    conn = get_db()
    cur = conn.execute("""
        INSERT INTO students
            (name, country, degree_level, major, cgpa,
             has_ielts, ielts_score, has_toefl, toefl_score,
             budget, preferred_countries)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["name"], data["country"], data["degree_level"],
        data["major"], float(data["cgpa"]),
        int(data.get("has_ielts", 0)), data.get("ielts_score") or None,
        int(data.get("has_toefl", 0)), data.get("toefl_score") or None,
        data["budget"], data.get("preferred_countries", ""),
    ))
    student_id = cur.lastrowid
    conn.commit()
    conn.close()
    return student_id


def get_student_by_id(student_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM students WHERE id = ?", (student_id,)).fetchone()
    conn.close()
    return row


def save_bookmark(student_id, opp_id):
    conn = get_db()
    conn.execute("INSERT OR IGNORE INTO saved_opportunities (student_id, opportunity_id) VALUES (?, ?)", (student_id, opp_id))
    conn.commit()
    conn.close()


def remove_bookmark(student_id, opp_id):
    conn = get_db()
    conn.execute("DELETE FROM saved_opportunities WHERE student_id=? AND opportunity_id=?", (student_id, opp_id))
    conn.commit()
    conn.close()


def get_saved_opportunities(student_id):
    conn = get_db()
    rows = conn.execute("""
        SELECT o.* FROM opportunities o
        JOIN saved_opportunities s ON o.id = s.opportunity_id
        WHERE s.student_id = ? ORDER BY o.deadline ASC
    """, (student_id,)).fetchall()
    conn.close()
    return rows


def search_opportunities(filters):
    query = "SELECT * FROM opportunities WHERE 1=1"
    params = []

    if filters.get("q"):
        q = f"%{filters['q']}%"
        query += " AND (name LIKE ? OR description LIKE ? OR country LIKE ? OR fields LIKE ?)"
        params.extend([q, q, q, q])

    if filters.get("country"):
        query += " AND (LOWER(country) = LOWER(?) OR LOWER(country) IN ('global', 'multiple'))"
        params.append(filters["country"])

    if filters.get("region"):
        query += " AND LOWER(region) = LOWER(?)"
        params.append(filters["region"])

    if filters.get("funding_type"):
        query += " AND LOWER(funding_type) = LOWER(?)"
        params.append(filters["funding_type"])

    if filters.get("opp_type"):
        query += " AND LOWER(type) = LOWER(?)"
        params.append(filters["opp_type"])

    if filters.get("degree_level"):
        query += " AND degree_levels LIKE ?"
        params.append(f"%{filters['degree_level']}%")

    if filters.get("field"):
        query += " AND (fields = 'All' OR LOWER(fields) LIKE ?)"
        params.append(f"%{filters['field'].lower()}%")

    if filters.get("deadline_month"):
        query += " AND deadline LIKE ?"
        params.append(f"%-{filters['deadline_month'].zfill(2)}-%")

    query += " ORDER BY deadline ASC"
    conn = get_db()
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return rows


def get_distinct_countries():
    conn = get_db()
    rows = conn.execute("SELECT DISTINCT country FROM opportunities ORDER BY country").fetchall()
    conn.close()
    return [r[0] for r in rows]


def get_distinct_regions():
    conn = get_db()
    rows = conn.execute("SELECT DISTINCT region FROM opportunities ORDER BY region").fetchall()
    conn.close()
    return [r[0] for r in rows]


# ── Admin CRUD ──────────────────────────────────────────────────────

def admin_add_opportunity(data):
    conn = get_db()
    conn.execute("""
        INSERT INTO opportunities
            (name, country, region, type, degree_levels, fields, min_gpa,
             ielts_required, min_ielts, toefl_required, min_toefl,
             funding_type, deadline, opening_date, application_status,
             description, official_link, roadmap, eligible_nationalities)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        data["name"], data["country"], data.get("region","Global"),
        data["type"], data["degree_levels"], data.get("fields","All"),
        float(data.get("min_gpa",0) or 0),
        int(data.get("ielts_required",0) or 0),
        data.get("min_ielts") or None,
        int(data.get("toefl_required",0) or 0),
        data.get("min_toefl") or None,
        data["funding_type"], data.get("deadline") or None,
        data.get("opening_date") or None, data.get("application_status","Open"),
        data.get("description",""), data.get("official_link",""),
        data.get("roadmap",""), data.get("eligible_nationalities",""),
    ))
    conn.commit()
    conn.close()


def admin_update_opportunity(opp_id, data):
    conn = get_db()
    conn.execute("""
        UPDATE opportunities SET
            name=?, country=?, region=?, type=?, degree_levels=?, fields=?,
            min_gpa=?, ielts_required=?, min_ielts=?, toefl_required=?,
            min_toefl=?, funding_type=?, deadline=?, opening_date=?,
            application_status=?, description=?, official_link=?, roadmap=?
        WHERE id=?
    """, (
        data["name"], data["country"], data.get("region","Global"),
        data["type"], data["degree_levels"], data.get("fields","All"),
        float(data.get("min_gpa",0) or 0),
        int(data.get("ielts_required",0) or 0),
        data.get("min_ielts") or None,
        int(data.get("toefl_required",0) or 0),
        data.get("min_toefl") or None,
        data["funding_type"], data.get("deadline") or None,
        data.get("opening_date") or None, data.get("application_status","Open"),
        data.get("description",""), data.get("official_link",""),
        data.get("roadmap",""), opp_id,
    ))
    conn.commit()
    conn.close()


def admin_delete_opportunity(opp_id):
    conn = get_db()
    conn.execute("DELETE FROM opportunities WHERE id=?", (opp_id,))
    conn.execute("DELETE FROM saved_opportunities WHERE opportunity_id=?", (opp_id,))
    conn.commit()
    conn.close()


def save_submission(data):
    """Save a user-submitted opportunity request."""
    conn = get_db()
    conn.execute("""
        INSERT INTO submission_requests (name, type, country, link, description, submitter)
        VALUES (?,?,?,?,?,?)
    """, (data.get("name",""), data.get("type",""), data.get("country",""),
          data.get("link",""), data.get("description",""), data.get("submitter","")))
    conn.commit()
    conn.close()


def get_submissions():
    conn = get_db()
    try:
        rows = conn.execute("SELECT * FROM submission_requests ORDER BY submitted_at DESC").fetchall()
    except Exception:
        rows = []
    conn.close()
    return rows


def verify_admin(username, password):
    conn = get_db()
    row = conn.execute(
        "SELECT id FROM admin_users WHERE username=? AND password=?",
        (username, password)
    ).fetchone()
    conn.close()
    return row is not None


if __name__ == "__main__":
    init_db()
    print("DB initialised.")