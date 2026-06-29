"""
seed_data.py — Run once to populate the opportunities table.
python seed_data.py
"""
from database import get_db, init_db

OPPORTUNITIES = [

    # ════════════════════════════════════════════════════════════════
    # SCHOLARSHIPS
    # ════════════════════════════════════════════════════════════════
    {
        "name": "Stipendium Hungaricum", "country": "Hungary", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Bachelors,Masters,PhD", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-01-16",
        "description": "Hungarian government scholarship open to Pakistani students. Covers tuition, accommodation, monthly stipend, and medical insurance. No IELTS required — universities conduct their own language assessment.",
        "official_link": "https://stipendiumhungaricum.hu",
        "roadmap": "1. Check HEC's partner university list\n2. Select up to 5 programmes at Hungarian universities\n3. Prepare academic transcripts (attested by HEC)\n4. Write a strong motivation letter\n5. Submit via the Stipendium Hungaricum online portal\n6. Shortlisted candidates attend an interview",
    },
    {
        "name": "Türkiye Bursları (Turkey Scholarships)", "country": "Turkey", "region": "Middle East & Central Asia",
        "type": "Scholarship", "degree_levels": "Bachelors,Masters,PhD", "fields": "All",
        "min_gpa": 3.2, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-02-20",
        "description": "Turkish government scholarship covering tuition, accommodation, health insurance, Turkish language course, and monthly stipend. Recipients complete a one-year Turkish language course before their main programme.",
        "official_link": "https://www.turkiyeburslari.gov.tr",
        "roadmap": "1. Register at turkiyeburslari.gov.tr\n2. Upload CGPA transcript (minimum 3.2)\n3. Write motivation letter and research plan (for Masters/PhD)\n4. Submit by February deadline\n5. Attend interview if shortlisted\n6. Complete one-year Turkish language course upon arrival",
    },
    {
        "name": "DAAD EPOS Scholarship", "country": "Germany", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Masters,PhD", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": 80,
        "funding_type": "Fully Funded", "deadline": "2025-10-15",
        "description": "DAAD's Development-Related Postgraduate Courses scholarship for students from developing countries. Covers monthly stipend, health insurance, travel, and study allowance for Masters and PhD degrees in Germany.",
        "official_link": "https://www.daad.de/en/study-and-research-in-germany/scholarships/epos",
        "roadmap": "1. Identify a DAAD-partnered EPOS programme in your field\n2. Obtain IELTS 6.0+ or TOEFL 80+\n3. Request a letter of recommendation from a professor\n4. Write a development-impact statement\n5. Apply through the DAAD portal by October\n6. If accepted, apply separately to the German university",
    },
    {
        "name": "Erasmus Mundus Joint Masters", "country": "Europe", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Masters", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": 90,
        "funding_type": "Fully Funded", "deadline": "2026-02-15",
        "description": "EU-funded joint Masters degrees delivered across 2-3 European universities. Covers tuition, travel, accommodation, and a monthly allowance of €1,000. Students study in multiple European countries.",
        "official_link": "https://www.eacea.ec.europa.eu/scholarships/emjm_en",
        "roadmap": "1. Browse the Erasmus Mundus catalogue for your field\n2. Check each consortium's specific requirements\n3. Obtain IELTS 6.5+\n4. Prepare a strong academic CV and motivation letter\n5. Apply directly to the consortium (each has its own portal)\n6. Deadlines vary by programme — most are Jan-Feb",
    },
    {
        "name": "CSC Scholarship (China)", "country": "China", "region": "Asia Pacific",
        "type": "Scholarship", "degree_levels": "Bachelors,Masters,PhD", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-03-15",
        "description": "Chinese Government Scholarship via China Scholarship Council (CSC). Covers tuition, accommodation, and monthly stipend. Pakistani students apply through HEC. One of the most accessible fully-funded options available.",
        "official_link": "https://www.csc.edu.cn/studyinchina",
        "roadmap": "1. Register on HEC's scholarship portal\n2. Select up to 3 Chinese universities\n3. Prepare academic documents (attested)\n4. Obtain a pre-admission letter from a Chinese university (recommended)\n5. Submit through HEC by March\n6. Medical examination required after acceptance",
    },
    {
        "name": "Global Korea Scholarship (GKS)", "country": "South Korea", "region": "Asia Pacific",
        "type": "Scholarship", "degree_levels": "Bachelors,Masters,PhD", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-03-01",
        "description": "Korean government scholarship (NIIED). Covers tuition, Korean language training, monthly stipend, accommodation, and health insurance. Recipients complete one year of Korean language before their degree.",
        "official_link": "https://www.niied.go.kr",
        "roadmap": "1. Apply via the Korean embassy in Pakistan (embassy track) or directly to a Korean university (university track)\n2. CGPA must be 3.0+\n3. No Korean language required at application stage\n4. Prepare two recommendation letters\n5. Write a study plan\n6. Complete one year of Korean language training on arrival",
    },
    {
        "name": "MEXT Scholarship (Japan)", "country": "Japan", "region": "Asia Pacific",
        "type": "Scholarship", "degree_levels": "Bachelors,Masters,PhD", "fields": "All",
        "min_gpa": 3.2, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-05-30",
        "description": "Japanese Ministry of Education scholarship. Covers tuition, accommodation, and monthly stipend. A preliminary Japanese language course is included. Apply through the Japanese embassy in Islamabad.",
        "official_link": "https://www.mext.go.jp/en",
        "roadmap": "1. Contact the Japanese Embassy in Islamabad in April-May\n2. Fill the MEXT application form\n3. Pass the written exam (English, Math/Science)\n4. Attend an embassy interview\n5. Embassy nominates candidates to Japanese universities\n6. University placement is confirmed by the Ministry",
    },
    {
        "name": "Eiffel Excellence Scholarship (France)", "country": "France", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Masters,PhD", "fields": "All",
        "min_gpa": 3.3, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": 90,
        "funding_type": "Fully Funded", "deadline": "2026-01-12",
        "description": "French Ministry of Foreign Affairs scholarship for outstanding international students at Masters and PhD level. Covers monthly allowance, accommodation, return flight, health insurance, and cultural activities.",
        "official_link": "https://www.campusfrance.org/en/eiffel-scholarship-program-of-excellence",
        "roadmap": "1. Apply to a French university programme first (you must be admitted)\n2. Ask the French university to nominate you for Eiffel — you cannot apply directly\n3. University must submit the nomination by January\n4. Maintain a strong academic record (most recipients are top of their class)\n5. IELTS 6.5+ or equivalent required",
    },
    {
        "name": "Chevening Scholarship (UK)", "country": "United Kingdom", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Masters", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2025-11-04",
        "description": "UK government's global scholarship and fellowship programme. Covers tuition, monthly stipend, return flights, and visa fee for a one-year Masters at any UK university. Requires 2 years of work experience.",
        "official_link": "https://www.chevening.org",
        "roadmap": "1. Must have 2+ years of full-time work experience\n2. Apply online at chevening.org — opens August each year\n3. Write four 500-word essays on leadership, networking, studying in UK, and career goals\n4. November deadline; shortlisted candidates interview in Feb-Mar\n5. Apply to three UK universities simultaneously\n6. Conditional offer from a UK university required before final award",
    },
    {
        "name": "Fulbright Scholarship (USA)", "country": "United States", "region": "North America",
        "type": "Scholarship", "degree_levels": "Masters,PhD", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 7.0, "toefl_required": 0, "min_toefl": 100,
        "funding_type": "Fully Funded", "deadline": "2026-02-15",
        "description": "US government's flagship international educational exchange programme. Fully funded Masters and PhD at US universities. Highly competitive — requires strong academic record, leadership experience, and a compelling statement of purpose.",
        "official_link": "https://www.usefpakistan.org",
        "roadmap": "1. Apply through USEFP (US Educational Foundation in Pakistan)\n2. Must have IELTS 7.0+ or TOEFL 100+\n3. GRE not mandatory but strongly recommended\n4. Write a detailed study objective\n5. Applications open December, close February\n6. Interview process: written test → panel interview → final selection",
    },
    {
        "name": "Australia Awards Scholarship", "country": "Australia", "region": "Asia Pacific",
        "type": "Scholarship", "degree_levels": "Masters,PhD", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-04-30",
        "description": "Australian government scholarship for students from developing countries. Fully funded Masters and PhD at Australian universities. Emphasises development impact — applicants must demonstrate how their studies benefit Pakistan.",
        "official_link": "https://www.australiaawards.gov.au",
        "roadmap": "1. Applications open January each year\n2. IELTS 6.5+ required (no TOEFL alternative)\n3. Write a development-impact statement specific to Pakistan\n4. Two professional reference letters required\n5. Shortlisted candidates attend an interview\n6. Successful candidates must return to Pakistan for 2 years after graduating",
    },
    {
        "name": "Aga Khan Foundation Scholarship", "eligible_nationalities": "", "country": "Multiple", "region": "Global",
        "type": "Scholarship", "degree_levels": "Masters", "fields": "All",
        "min_gpa": 3.2, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-03-31",
        "description": "Competitive scholarship for exceptional students from developing countries pursuing postgraduate study. Targets areas including health, education, and rural development. Repayable as a grant — no payback required.",
        "official_link": "https://www.akdn.org/our-agencies/aga-khan-foundation/scholarships",
        "roadmap": "1. Apply at akfed.org — opens January each year\n2. Must demonstrate financial need alongside academic merit\n3. IELTS 6.5+ required\n4. Targets Masters in areas with development impact (health, education, environment)\n5. Panel interview conducted in Pakistan\n6. Award covers full tuition and living costs",
    },
    {
        "name": "Commonwealth Scholarship (UK)", "eligible_nationalities": "Pakistani,Indian,Bangladeshi,Kenyan,Ghanaian,Nigerian,South African,Sri Lankan,Ugandan,Tanzanian,Zambian,Zimbabwean,Jamaican", "country": "United Kingdom", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Masters,PhD", "fields": "All",
        "min_gpa": 3.5, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2025-12-05",
        "description": "UK government scholarship for Commonwealth nations. Covers tuition, flights, accommodation allowance, and living stipend. Focus on development impact — applicants must demonstrate how studies benefit Pakistan.",
        "official_link": "https://cscuk.fcdo.gov.uk",
        "roadmap": "1. Apply via the Commonwealth Scholarship Commission portal\n2. Strong CGPA required (most successful applicants have 3.5+)\n3. IELTS 6.5+ required\n4. Write a development impact statement\n5. Shortlisted candidates nominated by Pakistani government\n6. Final selection by CSC in the UK",
    },
    {
        "name": "DAAD Scholarship (Germany)", "country": "Germany", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Masters,PhD", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": 80,
        "funding_type": "Fully Funded", "deadline": "2025-11-15",
        "description": "German Academic Exchange Service scholarship for postgraduate studies. Covers monthly stipend, health insurance, travel, and study allowance. Research-oriented applicants (PhD) have strong prospects.",
        "official_link": "https://www.daad.de/en",
        "roadmap": "1. Browse DAAD programmes at daad.de matching your field\n2. Obtain IELTS 6.0+ or TOEFL 80+\n3. Contact a German professor for research collaboration (especially for PhD)\n4. Prepare a research proposal\n5. Apply through the DAAD portal\n6. Applications typically reviewed Nov-Jan",
    },

    # ════════════════════════════════════════════════════════════════
    # EXCHANGES
    # ════════════════════════════════════════════════════════════════
    {
        "name": "UGRAD Exchange Program (USA)", "eligible_nationalities": "Pakistani", "country": "United States", "region": "North America",
        "type": "Exchange", "degree_levels": "Bachelors", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2025-11-30",
        "description": "US State Department-funded one-semester exchange for undergraduate students. Fully funded placement at a US university including tuition, housing, and a monthly allowance. Students in years 1-3 of their Bachelor's are eligible.",
        "official_link": "https://exchanges.state.gov/non-us/program/undergraduate-exchange-program-ugrad",
        "roadmap": "1. Apply through USEFP Pakistan — opens October\n2. Must be in Year 1, 2 or 3 of a Bachelor's programme\n3. CGPA 3.0+ required\n4. No IELTS needed — USEFP conducts its own English test\n5. Two-stage selection: written application → interview\n6. Placement at a US university for one semester",
    },
    {
        "name": "Erasmus+ Exchange", "country": "Europe", "region": "Europe",
        "type": "Exchange", "degree_levels": "Bachelors,Masters,PhD", "fields": "All",
        "min_gpa": 2.8, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Partially Funded", "deadline": "Rolling",
        "description": "EU exchange programme for students from partner institutions. Monthly grant and tuition waiver at the host university for 3–12 months. Apply through your home university — NUST, LUMS, and several Pakistani universities have active agreements.",
        "official_link": "https://erasmus-plus.ec.europa.eu",
        "roadmap": "1. Check if your university has an Erasmus+ bilateral agreement\n2. Contact your international office — internal deadline is usually 3-4 months before departure\n3. Apply through your university's Erasmus coordinator\n4. Language requirements set by the host university\n5. Monthly grant covers living costs partially\n6. Tuition is waived at the host university",
    },
    {
        "name": "JENESYS (Japan)", "country": "Japan", "region": "Asia Pacific",
        "type": "Exchange", "degree_levels": "Bachelors,Masters", "fields": "All",
        "min_gpa": 2.8, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": "Japan-East Asia Network of Exchange for Students and Youths. Short-term exchange (7-30 days) to Japan. Covers flights, accommodation, and local expenses. Applied through the Japanese Embassy in Islamabad.",
        "official_link": "https://www.mofa.go.jp/fp/pp/page23e_000029.html",
        "roadmap": "1. Watch for announcements from the Japanese Embassy Pakistan\n2. Submit nomination through your university\n3. Must be enrolled in a degree programme\n4. No Japanese language required\n5. Programme includes campus visits, cultural immersion, and industry tours",
    },
    {
        "name": "KAUST Exchange (Saudi Arabia)", "country": "Saudi Arabia", "region": "Middle East & Central Asia",
        "type": "Exchange", "degree_levels": "Masters,PhD", "fields": "Engineering,Computer Science,Natural Sciences",
        "min_gpa": 3.3, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": 90,
        "funding_type": "Fully Funded", "deadline": "2026-01-15",
        "description": "King Abdullah University of Science and Technology short-term research exchange for Masters and PhD students. Covers accommodation and a research allowance at one of the world's best-funded research universities.",
        "official_link": "https://www.kaust.edu.sa/en/study/vsrp",
        "roadmap": "1. Identify a KAUST faculty member working in your research area\n2. Email them directly with your CV and research interest\n3. CGPA 3.3+ required\n4. IELTS 6.5+ or TOEFL 90+\n5. Apply online with a faculty sponsor's agreement\n6. Programme runs 3-4 months",
    },

    # ════════════════════════════════════════════════════════════════
    # INTERNSHIPS
    # ════════════════════════════════════════════════════════════════
    {
        "name": "CERN Technical Internship", "country": "Switzerland", "region": "Europe",
        "type": "Internship", "degree_levels": "Bachelors,Masters", "fields": "Engineering,Computer Science,Physics,Mathematics",
        "min_gpa": 3.2, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": "Work at the world's largest particle physics laboratory in Geneva. Technical Student and Summer Student programmes available. Covers monthly allowance, travel, and accommodation contribution. Duration 2-12 months.",
        "official_link": "https://careers.cern/students",
        "roadmap": "1. Create a CERN careers account at careers.cern\n2. Browse open technical student positions\n3. Apply with CV, motivation letter, and transcript\n4. Must be enrolled in a university at time of application\n5. IELTS 6.0+ recommended (working language is English/French)\n6. Positions open year-round — apply early, competition is intense",
    },
    {
        "name": "OIST Research Internship (Japan)", "country": "Japan", "region": "Asia Pacific",
        "type": "Internship", "degree_levels": "Bachelors,Masters", "fields": "Natural Sciences,Engineering,Computer Science",
        "min_gpa": 3.2, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": "Okinawa Institute of Science and Technology research internship. Covers round-trip flights, accommodation on the OIST campus, and a monthly stipend. Work directly with a research unit for 2-3 months in a world-class interdisciplinary environment.",
        "official_link": "https://admissions.oist.jp/oist-research-internship-program-orip",
        "roadmap": "1. Browse OIST research units at groups.oist.jp\n2. Email a faculty member whose research interests you\n3. If they agree, apply online with their support\n4. Applications are reviewed on a rolling basis\n5. Accommodation in OIST village is provided\n6. Deadlines: March for summer, August for winter intake",
    },
    {
        "name": "KAUST VSRP Internship", "country": "Saudi Arabia", "region": "Middle East & Central Asia",
        "type": "Internship", "degree_levels": "Bachelors,Masters", "fields": "Engineering,Computer Science,Natural Sciences",
        "min_gpa": 3.3, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": "KAUST's Visiting Student Research Program. Covers accommodation, a research stipend, and partial flights. Work on cutting-edge research in science and engineering at a fully funded university in Saudi Arabia.",
        "official_link": "https://vsrp.kaust.edu.sa",
        "roadmap": "1. Browse KAUST faculty at kaust.edu.sa\n2. Email a supervisor directly with your CV and a tailored research statement\n3. CGPA 3.3+ required\n4. IELTS 6.0+\n5. Apply on the VSRP portal once a supervisor agrees\n6. Intakes in January and June each year",
    },
    {
        "name": "DESY Summer Internship (Germany)", "country": "Germany", "region": "Europe",
        "type": "Internship", "degree_levels": "Bachelors,Masters", "fields": "Physics,Engineering,Computer Science,Mathematics",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-01-31",
        "description": "Summer internship at DESY, one of the world's leading accelerator centres in Hamburg and Zeuthen. Covers stipend, accommodation, and travel. Students work alongside world-class researchers for 8-10 weeks.",
        "official_link": "https://www.desy.de/research/student_programmes/summer_students",
        "roadmap": "1. Apply via the DESY summer students portal — opens November\n2. Select up to 3 research groups from the programme list\n3. IELTS 6.0+ or equivalent\n4. Transcripts and CV required\n5. Deadline is end of January for July-September placement\n6. Stipend and shared accommodation provided",
    },
    {
        "name": "RIPS REU Internship (USA)", "eligible_nationalities": "US Citizen,US Permanent Resident", "country": "United States", "region": "North America",
        "type": "Internship", "degree_levels": "Bachelors", "fields": "Mathematics,Computer Science,Engineering",
        "min_gpa": 3.3, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-02-14",
        "description": "Research in Industrial Projects for Students at UCLA's IPAM. Industry-sponsored mathematical research experience. Covers stipend, housing, and travel. Teams of 4 students solve real problems for companies including Google and NSA.",
        "official_link": "https://www.ipam.ucla.edu/programs/student-research-programs/research-in-industrial-projects-for-students",
        "roadmap": "1. Apply at ipam.ucla.edu — deadline February each year\n2. Must be an undergraduate with strong maths/CS background\n3. No IELTS requirement but excellent English needed\n4. Two recommendation letters from professors\n5. Teams of 4 work on one industry project for 8 weeks\n6. Results presented to the sponsoring company",
    },
    {
        "name": "IST Austria Internship", "country": "Austria", "region": "Europe",
        "type": "Internship", "degree_levels": "Bachelors,Masters", "fields": "Natural Sciences,Computer Science,Mathematics",
        "min_gpa": 3.2, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-01-31",
        "description": "Research internship at IST Austria, a world-class research institute near Vienna. ISTernship programme covers round-trip travel, on-campus accommodation, and a monthly stipend. Work directly with a research group for 8-12 weeks.",
        "official_link": "https://ist.ac.at/en/education/internships",
        "roadmap": "1. Apply at ist.ac.at/internships — deadline January 31\n2. Browse research groups and select 3 preferences\n3. CGPA 3.2+ expected\n4. Submit transcript, CV, and a motivation letter\n5. Short online interview if shortlisted\n6. Accommodation provided on-campus in the ISTernship dormitory",
    },

    # ════════════════════════════════════════════════════════════════
    # SUMMER SCHOOLS
    # ════════════════════════════════════════════════════════════════
    {
        "name": "EPFL Summer Research Program", "country": "Switzerland", "region": "Europe",
        "type": "Summer School", "degree_levels": "Bachelors,Masters", "fields": "Engineering,Computer Science,Natural Sciences,Life Sciences",
        "min_gpa": 3.3, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-01-08",
        "description": "10-week summer research at École Polytechnique Fédérale de Lausanne, one of Europe's top engineering universities. Covers return flights, accommodation, and monthly CHF 1,100 stipend. Highly competitive.",
        "official_link": "https://bachelor.epfl.ch/summer-research",
        "roadmap": "1. Apply at summer.epfl.ch — deadline early January\n2. CGPA must be in the top 10% of your class\n3. Strong research background required (prior lab experience helps)\n4. Two academic recommendation letters\n5. Write a research statement matching EPFL faculty interests\n6. Results announced March-April",
    },
    {
        "name": "ETH Zurich Summer Research Fellowship", "country": "Switzerland", "region": "Europe",
        "type": "Summer School", "degree_levels": "Bachelors,Masters", "fields": "Engineering,Computer Science,Natural Sciences",
        "min_gpa": 3.3, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-12-15",
        "description": "10-week summer research at ETH Zurich, ranked #7 globally. Covers accommodation, flights, and a monthly stipend. Work directly in a research group on a specific project. Applications open November.",
        "official_link": "https://www.inf.ethz.ch/studies/summer-research-fellowship.html",
        "roadmap": "1. Identify an ETH professor in your research area\n2. Contact them directly by email before the deadline\n3. Apply via the online portal — deadline December 15\n4. CV, transcript, and a strong motivation letter required\n5. Two letters of recommendation needed\n6. Results announced February-March",
    },
    {
        "name": "MBZUAI Summer School (UAE)", "country": "UAE", "region": "Middle East & Central Asia",
        "type": "Summer School", "degree_levels": "Bachelors,Masters", "fields": "Computer Science,Artificial Intelligence,Data Science",
        "min_gpa": 3.0, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-03-31",
        "description": "Mohamed bin Zayed University of AI summer programme focused on AI, machine learning, and data science. Covers accommodation in Abu Dhabi, meals, and a modest stipend. Ideal for students building a portfolio in AI.",
        "official_link": "https://mbzuai.ac.ae/study/summer-programme",
        "roadmap": "1. Apply online at mbzuai.ac.ae — deadline March\n2. Background in maths, programming, or ML preferred\n3. No IELTS required — English is the medium of instruction\n4. CV and motivation letter required\n5. Programme runs 2-4 weeks in June or July\n6. Certificate of completion awarded",
    },
    {
        "name": "HKUST Summer Research Program", "country": "Hong Kong", "region": "Asia Pacific",
        "type": "Summer School", "degree_levels": "Bachelors,Masters", "fields": "Engineering,Computer Science,Natural Sciences,Business",
        "min_gpa": 3.2, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-02-28",
        "description": "Hong Kong University of Science and Technology research programme for outstanding undergraduate and postgraduate students. Covers accommodation, a monthly stipend, and visa support. Duration 6-8 weeks.",
        "official_link": "https://pg.ust.hk/prospective-students/activities/ug-overseas-research-opportunities",
        "roadmap": "1. Apply at pg.ust.hk — deadline February\n2. CGPA 3.2+ recommended\n3. IELTS 6.0+ required\n4. Select research groups aligned to your interests\n5. Two faculty recommendation letters required\n6. Accommodation in HKUST student halls provided",
    },
    {
        "name": "NTU Summer Programme (Singapore)", "country": "Singapore", "region": "Asia Pacific",
        "type": "Summer School", "degree_levels": "Bachelors", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Partially Funded", "deadline": "2026-02-15",
        "description": "Nanyang Technological University's summer programme. Partial scholarships available for outstanding students. Take university-level courses, conduct research, and experience Singapore. Duration 4-6 weeks.",
        "official_link": "https://www.ntu.edu.sg/admissions/global-experience/summer",
        "roadmap": "1. Apply via NTU's global experience portal\n2. CGPA 3.0+ required\n3. IELTS 6.0+\n4. Apply for the NTU Global Travel Award for partial funding\n5. Submit by February deadline\n6. Course credits may be transferable to your home university",
    },

    # ════════════════════════════════════════════════════════════════
    # RESEARCH PROGRAMS
    # ════════════════════════════════════════════════════════════════
    {
        "name": "MITACS Globalink Research (Canada)", "country": "Canada", "region": "North America",
        "type": "Research Program", "degree_levels": "Bachelors", "fields": "Engineering,Computer Science,Natural Sciences,Mathematics",
        "min_gpa": 3.2, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2025-10-15",
        "description": "12-week research internship at a Canadian university. Covers round-trip flights, accommodation, and a CAD 10,000 stipend. Students work under a Canadian professor. One of the best research opportunities for Pakistani undergraduates.",
        "official_link": "https://www.mitacs.ca/globalink",
        "roadmap": "1. Apply at mitacs.ca — deadline mid-October\n2. Must be an undergraduate in penultimate or final year\n3. CGPA 3.2+ required\n4. Apply to up to 7 faculty projects across Canadian universities\n5. No IELTS required\n6. Strong CV, transcript, and two recommendation letters needed\n7. Results announced January-February",
    },
    {
        "name": "DAAD RISE Germany (Research)", "country": "Germany", "region": "Europe",
        "type": "Research Program", "degree_levels": "Bachelors", "fields": "Engineering,Computer Science,Natural Sciences,Medicine",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": 80,
        "funding_type": "Fully Funded", "deadline": "2025-12-15",
        "description": "DAAD research internship for undergraduate STEM students. 2-3 months at a German university or research institute. Includes monthly stipend and travel grant. Outstanding academic record expected.",
        "official_link": "https://www.daad.de/rise/en",
        "roadmap": "1. Register on the DAAD RISE portal — opens November\n2. Browse available research projects\n3. Send a personalised application to each project supervisor\n4. IELTS 6.0+ or TOEFL 80+\n5. Deadline December 15 — supervisors select students by March\n6. Stipend: approx. €800/month",
    },
    {
        "name": "Amgen Scholars Program", "country": "Multiple", "region": "Global",
        "type": "Research Program", "degree_levels": "Bachelors", "fields": "Natural Sciences,Medicine,Engineering",
        "min_gpa": 3.2, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-02-01",
        "description": "Prestigious research programme for undergraduates in biosciences, chemistry, and bioengineering. Partner universities in USA, Europe, Japan, and Australia. Covers accommodation, a stipend, and an exclusive Amgen Scholars symposium.",
        "official_link": "https://amgenscholars.com",
        "roadmap": "1. Choose a host institution (MIT, Cambridge, Tokyo, etc.)\n2. Apply directly via the Amgen Scholars website\n3. CGPA 3.2+ required\n4. IELTS 6.5+ for non-native speakers\n5. Transcripts and two recommendation letters required\n6. Research proposal or statement of interest required",
    },
    {
        "name": "Charité Summer Research (Germany)", "country": "Germany", "region": "Europe",
        "type": "Research Program", "degree_levels": "Bachelors,Masters", "fields": "Medicine,Natural Sciences,Biomedical Engineering",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Partially Funded", "deadline": "2026-02-28",
        "description": "Research internship at Charité – Europe's largest university hospital in Berlin. Students work in clinical research labs for 8-12 weeks. Partial stipend provided. Excellent for medical and biomedical students.",
        "official_link": "https://charite.de/en/research/career/students",
        "roadmap": "1. Browse Charité research groups at charite.de\n2. Email a principal investigator directly\n3. IELTS 6.0+ required\n4. Medical/biomedical background strongly preferred\n5. Letter of motivation and CV required\n6. Partial funding — check department-specific awards for top-up",
    },
    {
        "name": "IAESTE Technical Traineeship", "country": "Multiple", "region": "Global",
        "type": "Research Program", "degree_levels": "Bachelors,Masters", "fields": "Engineering,Computer Science,Natural Sciences",
        "min_gpa": 2.8, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": "International Association for the Exchange of Students for Technical Experience. Paid technical traineeships in 80+ countries. Apply through IAESTE Pakistan. Duration 6 weeks to 12 months. Covers accommodation and local wages.",
        "official_link": "https://iaeste.org",
        "roadmap": "1. Register with IAESTE Pakistan (check iaeste.pk)\n2. Browse available traineeships in your field\n3. Submit application to IAESTE Pakistan\n4. IAESTE matches you with a host company abroad\n5. Host country IAESTE handles accommodation\n6. Compensation matches local rates for engineers/scientists",
    },

    # ════════════════════════════════════════════════════════════════
    # FELLOWSHIPS
    # ════════════════════════════════════════════════════════════════
    {
        "name": "Obama Foundation Scholars", "country": "United States", "region": "North America",
        "type": "Fellowship", "degree_levels": "Masters", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 7.0, "toefl_required": 0, "min_toefl": 100,
        "funding_type": "Fully Funded", "deadline": "2026-01-16",
        "description": "One-year leadership fellowship at Columbia University. Fully funded Masters with a focus on civic leadership and public service. For emerging leaders with a track record of community impact.",
        "official_link": "https://www.obama.org/scholars",
        "roadmap": "1. Must demonstrate significant community leadership experience\n2. IELTS 7.0+ or TOEFL 100+\n3. Apply at obama.org/scholars — deadline January\n4. Short-list interviews conducted virtually\n5. One-year Masters at Columbia's School of International and Public Affairs\n6. Access to Obama Foundation global network",
    },
    {
        "name": "Schwarzman Scholars (China)", "country": "China", "region": "Asia Pacific",
        "type": "Fellowship", "degree_levels": "Masters", "fields": "All",
        "min_gpa": 3.5, "ielts_required": 1, "min_ielts": 7.0, "toefl_required": 0, "min_toefl": 100,
        "funding_type": "Fully Funded", "deadline": "2025-09-18",
        "description": "One-year Masters at Tsinghua University focused on global leadership. Fully funded including tuition, housing, travel, Mandarin instruction, and a monthly stipend. Extremely competitive — comparable to Rhodes Scholarship.",
        "official_link": "https://www.schwarzmanscholars.org",
        "roadmap": "1. Apply by mid-September each year\n2. CGPA must be exceptional (most successful scholars have 3.7+)\n3. IELTS 7.0+ or TOEFL 100+\n4. Demonstrate significant leadership impact\n5. Two-stage: written application → selection weekend\n6. Programme begins August each year at Tsinghua, Beijing",
    },
    {
        "name": "ATLAS Fellowship", "country": "United Kingdom", "region": "Europe",
        "type": "Fellowship", "degree_levels": "Bachelors", "fields": "All",
        "min_gpa": 3.5, "ielts_required": 1, "min_ielts": 7.0, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-04-01",
        "description": "Intensive 10-day fellowship at Cambridge for high-potential undergraduates aged 18-21. Covers all costs. Focuses on global challenges, critical thinking, and intellectual growth. Small cohort of 60 students worldwide.",
        "official_link": "https://www.atlasfellowship.org",
        "roadmap": "1. Must be 18-21 and currently in undergraduate study\n2. Apply with a 500-word essay on a global challenge\n3. IELTS 7.0+ recommended\n4. Strong academic record expected\n5. Short-list stage: a phone/video call\n6. Programme runs in Cambridge during summer",
    },

    # ════════════════════════════════════════════════════════════════
    # COMPETITIONS
    # ════════════════════════════════════════════════════════════════
    {
        "name": "Google Summer of Code", "country": "Global", "region": "Global",
        "type": "Competition", "degree_levels": "Bachelors,Masters", "fields": "Computer Science,Engineering",
        "min_gpa": 0.0, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-04-02",
        "description": "Google's annual programme for students to contribute to open-source projects. Stipend of USD 1,500–6,600 depending on country. Work remotely with a mentor from a real open-source organisation for 12-22 weeks.",
        "official_link": "https://summerofcode.withgoogle.com",
        "roadmap": "1. Browse participating organisations at summerofcode.withgoogle.com\n2. Contribute to your chosen project's codebase before the deadline\n3. Write a detailed project proposal\n4. Submit by April — applications open in March\n5. No CGPA requirement — coding skills are everything\n6. Mentors select students; Google pays the stipend",
    },
    {
        "name": "ICPC (International Collegiate Programming Contest)", "country": "Global", "region": "Global",
        "type": "Competition", "degree_levels": "Bachelors,Masters", "fields": "Computer Science,Mathematics",
        "min_gpa": 0.0, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Varies", "deadline": "Rolling",
        "description": "World's largest competitive programming contest. Teams of 3 from universities worldwide compete through regional to world finals. Winners gain direct recognition from top tech companies. Participation is free and open.",
        "official_link": "https://icpc.global",
        "roadmap": "1. Form a team of 3 students from your university\n2. Register through your university's ICPC coach\n3. Compete in the Asia Regional contest (held in Pakistan)\n4. Top teams qualify for the ICPC World Finals\n5. Practice on Codeforces, LeetCode, and past ICPC problems\n6. Regional contests held October-December each year",
    },
    {
        "name": "Microsoft Imagine Cup", "country": "Global", "region": "Global",
        "type": "Competition", "degree_levels": "Bachelors,Masters", "fields": "Computer Science,Engineering,Business",
        "min_gpa": 0.0, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Varies", "deadline": "2026-03-01",
        "description": "Microsoft's global student technology competition. Teams build AI-powered solutions to real-world problems. World finalist teams receive USD 85,000, Azure credits, and mentorship from Microsoft executives.",
        "official_link": "https://imaginecup.microsoft.com",
        "roadmap": "1. Form a team of 1-3 students\n2. Build a technology solution using Azure/AI tools\n3. Register and submit your project by March\n4. Compete through national → regional → world finals\n5. No CGPA or language test required\n6. Finalist teams invited to a global event at Microsoft HQ",
    },

    # ════════════════════════════════════════════════════════════════
    # UNIVERSITIES
    # ════════════════════════════════════════════════════════════════
    {
        "name": "Harvard University (Need-Blind Aid)", "country": "United States", "region": "North America",
        "type": "University", "degree_levels": "Bachelors", "fields": "All",
        "min_gpa": 3.7, "ielts_required": 1, "min_ielts": 7.0, "toefl_required": 0, "min_toefl": 100,
        "funding_type": "Fully Funded", "deadline": "2027-01-01",
        "description": (
            "Harvard is need-blind for all applicants worldwide — your ability to pay has zero impact on admission. "
            "It meets 100% of demonstrated financial need for all admitted students. Families earning under "
            "~$200,000/year typically pay nothing. For the 2026–27 year, total cost of attendance is ~$91,634, "
            "but the average aid package means most international students pay far less. Harvard is the most "
            "financially accessible Ivy League school for students who cannot afford tuition."
        ),
        "official_link": "https://college.harvard.edu/financial-aid",
        "roadmap": "1. Build an exceptional academic record — most admitted students are in the top 1% of their class\n2. Prepare for SAT/ACT (no longer required but recommended)\n3. Get IELTS 7.0+ or TOEFL 100+\n4. Write standout application essays — Harvard values uniqueness, not just achievements\n5. Apply via the Common App — deadline January 1 (Regular Decision)\n6. Submit the CSS Profile and ISFAA for financial aid simultaneously\n7. Financial aid decisions come with admission decisions in late March",
    },
    {
        "name": "MIT (Need-Blind Aid)", "country": "United States", "region": "North America",
        "type": "University", "degree_levels": "Bachelors", "fields": "Engineering,Computer Science,Natural Sciences,Mathematics",
        "min_gpa": 3.7, "ielts_required": 1, "min_ielts": 7.0, "toefl_required": 0, "min_toefl": 100,
        "funding_type": "Fully Funded", "deadline": "2027-01-01",
        "description": (
            "MIT is need-blind for all applicants and meets 100% of demonstrated need. The median annual "
            "cost paid by scholarship recipients in 2024–25 was just $10,268. Over 60% of undergraduates "
            "receive need-based aid. MIT's financial aid includes no loans — only grants. One of the few "
            "STEM-focused institutions in the world offering full financial coverage to international students."
        ),
        "official_link": "https://web.mit.edu/fnaid/",
        "roadmap": "1. Build a stellar maths and science background — top-percentile grades required\n2. Demonstrate genuine intellectual passion, not just grades (MIT values curiosity)\n3. TOEFL 100+ or IELTS 7.0+\n4. Apply via the MIT application portal — deadline January 1\n5. Submit CSS Profile for financial aid\n6. Strong recommendation letters from maths/science teachers are critical\n7. No alumni interview process — essays carry significant weight",
    },
    {
        "name": "Princeton University (Need-Blind Aid)", "country": "United States", "region": "North America",
        "type": "University", "degree_levels": "Bachelors", "fields": "All",
        "min_gpa": 3.7, "ielts_required": 1, "min_ielts": 7.0, "toefl_required": 0, "min_toefl": 100,
        "funding_type": "Fully Funded", "deadline": "2027-01-01",
        "description": (
            "Princeton was the first US university to replace all student loans with grant aid. It is "
            "need-blind for international students and meets 100% of demonstrated need. 89% of recent seniors "
            "graduated debt-free. Total cost of attendance is ~$86,680/year but aid packages mean middle-income "
            "families pay little to nothing. Princeton's no-loan policy is unique among US universities."
        ),
        "official_link": "https://financialaid.princeton.edu",
        "roadmap": "1. Princeton is one of the most selective universities in the world — aim for the top of your class\n2. TOEFL 100+ or IELTS 7.0+\n3. Apply via Common App — January 1 deadline (Regular Decision)\n4. Submit CSS Profile and ISFAA for financial aid\n5. Write compelling essays — Princeton asks about intellectual interests in detail\n6. No standardized test requirement (SAT/ACT optional since 2021, but strong scores help)\n7. Aid decisions are released alongside admission decisions",
    },
    {
        "name": "Yale University (Need-Blind Aid)", "country": "United States", "region": "North America",
        "type": "University", "degree_levels": "Bachelors", "fields": "All",
        "min_gpa": 3.7, "ielts_required": 1, "min_ielts": 7.0, "toefl_required": 0, "min_toefl": 100,
        "funding_type": "Fully Funded", "deadline": "2027-01-02",
        "description": (
            "Yale is need-blind and meets 100% of demonstrated need with grants, not loans. Over half of "
            "undergraduates receive need-based aid. Total cost of attendance for 2026–27 is ~$97,985/year "
            "but the aid programme ensures that admitted students can afford to attend regardless of background. "
            "Yale is known for its residential college system and exceptional liberal arts education."
        ),
        "official_link": "https://finaid.yale.edu",
        "roadmap": "1. Excel academically — Yale admits fewer than 5% of applicants\n2. Build leadership and community involvement outside class\n3. TOEFL 100+ or IELTS 7.0+\n4. Apply via Common App — January 2 deadline\n5. Submit CSS Profile for financial aid consideration\n6. Participate in alumni interview if offered (virtual option available for international applicants)\n7. Yale values intellectual diversity — essay authenticity is key",
    },
    {
        "name": "Amherst College (Need-Blind Aid)", "country": "United States", "region": "North America",
        "type": "University", "degree_levels": "Bachelors", "fields": "All",
        "min_gpa": 3.5, "ielts_required": 1, "min_ielts": 7.0, "toefl_required": 0, "min_toefl": 100,
        "funding_type": "Fully Funded", "deadline": "2027-01-05",
        "description": (
            "Amherst College is need-blind for all students including international applicants, and meets "
            "100% of demonstrated financial need with no loan requirement. Estimated cost of attendance "
            "2026–27 is ~$96,360 but the aid package covers the gap completely. One of the most generous "
            "liberal arts colleges in the world. Smaller and more accessible than Ivy League schools, but "
            "with equivalent financial generosity."
        ),
        "official_link": "https://www.amherst.edu/offices/financial_aid",
        "roadmap": "1. Amherst is highly selective but slightly more accessible than Ivies — still aim for the top 5% of your class\n2. TOEFL 100+ or IELTS 7.0+\n3. Apply via Common App — deadline January 5\n4. Submit CSS Profile for financial aid\n5. Amherst values intellectual curiosity and community engagement\n6. Application essays are closely reviewed — be genuine and specific\n7. Alumni interviews available for international students",
    },
    {
        "name": "Lester B. Pearson Scholarship (U of Toronto)", "country": "Canada", "region": "North America",
        "type": "University", "degree_levels": "Bachelors", "fields": "All",
        "min_gpa": 3.7, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": 100,
        "funding_type": "Fully Funded", "deadline": "2026-11-01",
        "description": (
            "The University of Toronto's most prestigious international undergraduate scholarship. Covers "
            "full tuition, student fees, and living costs for four years. Open to international students "
            "who demonstrate exceptional academic achievement and are nominated by their secondary school. "
            "Only students nominated by their school can apply — you cannot self-nominate. Approximately "
            "37 scholars are selected annually from around the world."
        ),
        "official_link": "https://future.utoronto.ca/pearson/",
        "roadmap": "1. Ask your school principal or head teacher to nominate you — self-nominations are not accepted\n2. School nomination deadline is November 1 each year\n3. Once nominated, you submit a full application including essays and a video\n4. IELTS 6.5+ or TOEFL 100+\n5. Must have outstanding grades — aim for the top 1% of your school\n6. Demonstrate leadership, community impact, and curiosity\n7. Final selection interviews held in February; award announced March",
    },
    {
        "name": "TU Munich (Free Tuition)", "country": "Germany", "region": "Europe",
        "type": "University", "degree_levels": "Bachelors,Masters", "fields": "Engineering,Computer Science,Natural Sciences,Mathematics",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": 88,
        "funding_type": "Varies", "deadline": "2026-05-31",
        "description": (
            "Technical University of Munich is one of Europe's top engineering and technology universities "
            "(QS Rank ~30 globally). Public German universities charge no tuition for any student, including "
            "international students — only a semester fee of ~€150. TUM has numerous English-taught Masters "
            "programmes. Living costs ~€900–1,200/month in Munich. The DAAD scholarship can fund living expenses."
        ),
        "official_link": "https://www.tum.de/en/studies/application",
        "roadmap": "1. Check TUM's English-taught programmes for your field\n2. Apply via TUM's online portal — most deadlines are May 31 (winter) or November 30 (summer)\n3. IELTS 6.5+ or TOEFL 88+ required for English-taught programmes\n4. Prepare HEC-attested transcripts and degree certificates\n5. Some programmes require GRE or other subject tests — check per programme\n6. Apply separately to DAAD for a living-expense scholarship\n7. No tuition fees — just a ~€150 semester admin fee",
    },
    {
        "name": "RWTH Aachen University (Free Tuition)", "country": "Germany", "region": "Europe",
        "type": "University", "degree_levels": "Bachelors,Masters", "fields": "Engineering,Computer Science,Natural Sciences",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": 83,
        "funding_type": "Varies", "deadline": "2026-06-30",
        "description": (
            "RWTH Aachen is Germany's largest technical university and one of Europe's most respected "
            "engineering schools. Tuition-free for all students under Germany's public university system. "
            "Semester fee only ~€300. Many Master's programmes offered in English. Strong industry links "
            "with automotive and manufacturing sectors. Located in western Germany near Belgium and Netherlands."
        ),
        "official_link": "https://www.rwth-aachen.de/cms/root/studium/vor-dem-studium/bewerbung/~obl/international-applicants/",
        "roadmap": "1. Browse RWTH's English-taught programmes on their website\n2. Apply via uni-assist (Germany's international admissions platform)\n3. IELTS 6.0+ or TOEFL 83+ for English-taught programmes\n4. German-taught programmes require TestDaF or DSH German language certificate\n5. HEC-attested transcripts required — allow 6–8 weeks for attestation\n6. Deadline: June 30 for winter semester (October start)\n7. Zero tuition fees — living costs ~€800–1,000/month in Aachen",
    },
    {
        "name": "University of Manchester (Global Futures Scholarship)", "eligible_nationalities": "Pakistani,Indian,Bangladeshi,Sri Lankan,Nepali", "country": "United Kingdom", "region": "Europe",
        "type": "University", "degree_levels": "Bachelors", "fields": "All",
        "min_gpa": 3.3, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Partially Funded", "deadline": "2026-05-25",
        "description": (
            "The University of Manchester's Global Futures Scholarship for South Asia is specifically open "
            "to Pakistani students. Awards £10,000 per year for three years (£30,000 total) as a tuition "
            "fee discount. Over 100 merit-based undergraduate scholarships available annually. Manchester is "
            "a Russell Group university ranked in the top 30 globally. Apply after receiving a conditional "
            "or unconditional offer."
        ),
        "official_link": "https://www.manchester.ac.uk/study/international/country-specific-information/pakistan/scholarships/",
        "roadmap": "1. Apply to your chosen Manchester undergraduate programme via UCAS\n2. Receive a conditional or unconditional offer\n3. The scholarship application link is emailed to you automatically after your offer\n4. A-levels, IB, or FSc qualifications are accepted\n5. Must select Manchester as your Firm UCAS choice by May 25\n6. IELTS 6.5+\n7. Award announced by June 1 — conditional on final exam results",
    },
    {
        "name": "University of British Columbia (International Major Entrance Scholarship)", "country": "Canada", "region": "North America",
        "type": "University", "degree_levels": "Bachelors", "fields": "All",
        "min_gpa": 3.5, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": 90,
        "funding_type": "Partially Funded", "deadline": "2026-12-01",
        "description": (
            "UBC's International Major Entrance Scholarships (IMES) are awarded automatically to the top "
            "international applicants with outstanding academic records. Awards range from CAD $10,000 to "
            "$40,000 over four years. UBC is ranked top 40 globally with strong Engineering, CS, and "
            "Sciences programmes. Vancouver has a large Pakistani community. Additional bursaries and "
            "work-study options are available."
        ),
        "official_link": "https://you.ubc.ca/financial-planning/scholarships-awards/international-major-entrance-scholarship/",
        "roadmap": "1. Apply to UBC via the UBC online application — December 1 deadline for most programmes\n2. No separate scholarship application needed — you are automatically considered based on your application\n3. IELTS 6.5+ or TOEFL 90+\n4. Attain the highest possible A-level or FSc grades\n5. Scholarship awarded to top ~200 international applicants each year\n6. Include a personal profile section — extracurriculars and community work matter\n7. Apply for additional need-based bursaries through UBC's financial aid portal",
    },

    # ════════════════════════════════════════════════════════════════
    # ADDITIONAL SCHOLARSHIPS
    # ════════════════════════════════════════════════════════════════
    {
        "name": "Knight-Hennessy Scholars (Stanford)", "country": "United States", "region": "North America",
        "type": "Scholarship", "degree_levels": "Masters,PhD", "fields": "All",
        "min_gpa": 3.5, "ielts_required": 0, "min_ielts": None, "toefl_required": 1, "min_toefl": 100,
        "funding_type": "Fully Funded", "deadline": "2026-10-06",
        "description": (
            "One of the world's most prestigious graduate scholarships. Funds up to 3 years at any Stanford "
            "graduate programme — Masters, MBA, JD, MD, or PhD. Covers tuition, living stipend, travel, and "
            "relocation. 100 scholars selected globally each year. No minimum GPA requirement for the "
            "scholarship itself — selection is based on independence of thought, purposeful leadership, and "
            "generosity of spirit. You must also apply to a Stanford graduate programme simultaneously."
        ),
        "official_link": "https://knight-hennessy.stanford.edu",
        "roadmap": "1. Identify a Stanford graduate programme in your field and apply concurrently\n2. TOEFL 100+ required for most Stanford graduate programmes\n3. No minimum GPA — leadership and intellectual impact matter more than grades\n4. Submit two recommendation letters focused on leadership\n5. Complete written responses and a 2-minute video\n6. Deadline: October 6, 2026 (1pm Pacific)\n7. Finalists attend a selection weekend in February; decisions in March",
    },
    {
        "name": "Rhodes Scholarship (Oxford)", "eligible_nationalities": "Pakistani", "country": "United Kingdom", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Masters,PhD", "fields": "All",
        "min_gpa": 3.7, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-08-01",
        "description": (
            "The world's oldest and most prestigious international scholarship. Funds postgraduate study at "
            "Oxford University. Covers full tuition, living stipend, airfare, and health insurance. "
            "Pakistan has a dedicated Rhodes constituency — approximately 2 scholarships are awarded to "
            "Pakistani students annually. Requires outstanding academics and demonstrated leadership, "
            "community service, and moral character. Exceptionally competitive."
        ),
        "official_link": "https://www.rhodeshouse.ox.ac.uk/scholarships/the-rhodes-scholarship/",
        "roadmap": "1. Must be a Pakistani citizen aged 19–25 at time of application\n2. Demonstrate exceptional academic achievement — most scholars have near-perfect GPAs\n3. Show significant leadership and community impact in Pakistan\n4. Apply through the Pakistan Rhodes Scholarship committee — application opens April\n5. District-level selection leads to a national selection committee interview\n6. Short-listed candidates attend an interview in Pakistan (typically October)\n7. Final selection for Oxford entry the following October",
    },
    {
        "name": "Gates Cambridge Scholarship", "country": "United Kingdom", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Masters,PhD", "fields": "All",
        "min_gpa": 3.7, "ielts_required": 1, "min_ielts": 7.5, "toefl_required": 0, "min_toefl": 110,
        "funding_type": "Fully Funded", "deadline": "2025-10-15",
        "description": (
            "The Bill & Melinda Gates Foundation scholarship for postgraduate study at the University of "
            "Cambridge. Covers full fees, maintenance allowance, return airfare, and visa costs. "
            "Approximately 90 scholars selected globally each year. Selection criteria include: outstanding "
            "academic achievement, a commitment to improving lives of others, leadership potential, and a "
            "fit with the aims of the Gates Cambridge Trust."
        ),
        "official_link": "https://www.gatescambridge.org",
        "roadmap": "1. Apply for admission to Cambridge via GRADSAF — deadline is usually October/November\n2. Tick the Gates Cambridge box within the Cambridge application\n3. IELTS 7.5+ or TOEFL 110+\n4. Write a strong statement on how your studies will benefit others\n5. Shortlisted candidates are interviewed (virtually) by the Gates Cambridge Trust\n6. Most Gates scholars are research-focused — prior research experience is a strong advantage",
    },
    {
        "name": "Hubert Humphrey Fellowship (USA)", "eligible_nationalities": "", "country": "United States", "region": "North America",
        "type": "Fellowship", "degree_levels": "Masters", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": 92,
        "funding_type": "Fully Funded", "deadline": "2026-10-01",
        "description": (
            "US State Department fellowship for mid-career professionals from developing countries. "
            "10-month non-degree programme at a US university. Covers tuition, living allowance, health "
            "insurance, and flights. Focuses on leadership development in areas including education, "
            "environment, public health, law, and economic development. Requires 5+ years of work "
            "experience. Apply through USEFP Pakistan."
        ),
        "official_link": "https://www.humphreyfellowship.org",
        "roadmap": "1. Must have at least 5 years of full-time professional work experience\n2. Apply through USEFP (US Educational Foundation in Pakistan) — applications open July\n3. IELTS 6.5+ or TOEFL 92+\n4. Write a clear professional development statement\n5. Deadline typically October 1 each year\n6. USEFP interviews shortlisted candidates in Pakistan\n7. Fellows placed at US universities from August the following year",
    },
    {
        "name": "VLIR-UOS Scholarship (Belgium)", "country": "Belgium", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Masters", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-02-01",
        "description": (
            "Belgian government scholarship for students from developing countries to pursue Masters degrees "
            "at Flemish universities. Covers tuition, living allowance, health insurance, and travel. "
            "Pakistan is an eligible country. Programmes span development-related fields — agriculture, "
            "health, environment, engineering, and social sciences. Apply directly through individual "
            "Belgian universities participating in VLIR-UOS."
        ),
        "official_link": "https://www.vliruos.be/en/scholarships",
        "roadmap": "1. Browse the VLIR-UOS scholarship programmes at vliruos.be\n2. Each programme has its own application portal and deadline (typically February)\n3. IELTS 6.0+ required\n4. Write a motivation letter explaining development relevance to Pakistan\n5. Some programmes require a medical certificate\n6. Scholarship is linked to specific programmes — you cannot apply generally",
    },
    {
        "name": "Swedish Institute Scholarship", "country": "Sweden", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Masters", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": 90,
        "funding_type": "Fully Funded", "deadline": "2026-02-10",
        "description": (
            "Swedish government scholarship covering tuition, living expenses, travel, and insurance for "
            "Masters study at Swedish universities. Pakistan is an eligible country. Approximately 350 "
            "scholarships awarded annually from a pool of 10,000+ applicants globally. Focus on sustainable "
            "development. Swedish universities offer a wide range of English-taught Masters programmes. "
            "Studying in Sweden means no tuition fees + a stipend for living costs."
        ),
        "official_link": "https://si.se/en/apply/scholarships/swedish-institute-scholarships-for-global-professionals/",
        "roadmap": "1. Register at si.se — applications open November each year\n2. Must apply to a Swedish university Masters programme at the same time\n3. IELTS 6.5+\n4. Must have at least 3,000 hours (~18 months) of work experience post-graduation\n5. Demonstrate leadership experience and civic engagement\n6. February 10 deadline — decisions announced May\n7. Note: work experience is a strict requirement — this is for professionals returning to study",
    },
    {
        "name": "ADB-Japan Scholarship", "country": "Multiple", "region": "Asia Pacific",
        "type": "Scholarship", "degree_levels": "Masters", "fields": "Engineering,Economics,Business,Social Sciences",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": 80,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": (
            "Asian Development Bank–Japan Scholarship Programme for citizens of ADB's developing member "
            "countries, including Pakistan. Fully funded Masters at designated Asian universities including "
            "IIT Delhi, Asian Institute of Technology, and others. Covers tuition, travel, living allowance, "
            "and health insurance. Requires 2+ years of work experience and commitment to return to Pakistan."
        ),
        "official_link": "https://www.adb.org/site/careers/japan-scholarship-program",
        "roadmap": "1. Check the list of ADB-JSP designated universities at adb.org\n2. Apply to a designated university's Masters programme directly\n3. Submit an ADB-JSP scholarship application via the university\n4. Must have 2+ years of professional work experience after first degree\n5. IELTS 6.0+ or TOEFL 80+\n6. Must be a citizen of an ADB developing member country (Pakistan qualifies)\n7. Must return to Pakistan for at least 2 years after completing the degree",
    },
    {
        "name": "Heinrich Böll Foundation Scholarship (Germany)", "country": "Germany", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Bachelors,Masters,PhD", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-03-01",
        "description": (
            "Political foundation scholarship linked to the German Green Party. Supports students with "
            "excellent academic records who are committed to ecology, sustainability, democracy, and human "
            "rights. Covers €934/month living costs + €300 study allowance for Bachelors/Masters, or "
            "€1,350/month for PhD. Open to international students studying in Germany. Strong social or "
            "political engagement is a key selection criterion."
        ),
        "official_link": "https://www.boell.de/en/scholarships",
        "roadmap": "1. Must be enrolled or accepted at a German university — this is not a study-abroad placement scholarship\n2. Must demonstrate exceptional academic achievement\n3. Show significant engagement with ecology, sustainability, democracy or human rights\n4. Apply at boell.de — deadline is typically March 1 and September 1\n5. Two rounds of selection: written application → interview workshop\n6. Political and civic engagement is weighted as heavily as academic achievement",
    },

    # ════════════════════════════════════════════════════════════════
    # ADDITIONAL INTERNSHIPS & RESEARCH
    # ════════════════════════════════════════════════════════════════
    {
        "name": "Max Planck Research Internship (Germany)", "country": "Germany", "region": "Europe",
        "type": "Internship", "degree_levels": "Bachelors,Masters", "fields": "Natural Sciences,Engineering,Computer Science,Mathematics",
        "min_gpa": 3.3, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": (
            "Research internship at Max Planck Institutes — Germany's world-leading basic research "
            "organisation with 80+ institutes across the country. Covers monthly stipend and travel. "
            "No centralised portal — students contact group leaders directly. Interns work alongside "
            "Nobel Prize–level researchers. Duration typically 6–12 weeks. Summer and winter placements "
            "available year-round."
        ),
        "official_link": "https://www.mpg.de/en/research",
        "roadmap": "1. Browse Max Planck Institute research groups at mpg.de matching your field\n2. Email group leaders directly with a targeted application — generic emails are ignored\n3. Attach your CV, transcript, and a one-page research statement\n4. IELTS 6.0+ recommended (English is the working language)\n5. Apply 4–6 months in advance — responses can take weeks\n6. Stipend provided (~€1,000–1,500/month); accommodation not always guaranteed",
    },
    {
        "name": "Smithsonian Institution Fellowship (USA)", "country": "United States", "region": "North America",
        "type": "Research Program", "degree_levels": "Masters,PhD", "fields": "Natural Sciences,Social Sciences,Engineering",
        "min_gpa": 3.2, "ielts_required": 1, "min_ielts": 7.0, "toefl_required": 0, "min_toefl": 100,
        "funding_type": "Fully Funded", "deadline": "2026-11-01",
        "description": (
            "Research fellowship at the Smithsonian Institution, the world's largest museum and research "
            "complex. Graduate Research Fellowships and Predoctoral Fellowships available. Covers stipend, "
            "research allowance, and travel. Work alongside curators and researchers at facilities including "
            "the National Museum of Natural History and the Smithsonian Tropical Research Institute."
        ),
        "official_link": "https://fellowship.si.edu",
        "roadmap": "1. Browse Smithsonian research units at si.edu to find a match for your research\n2. Identify a Smithsonian researcher as a potential adviser\n3. Contact them by email before applying — informal agreement helps the application\n4. Apply at fellowship.si.edu — deadline November 1 each year\n5. IELTS 7.0+ or TOEFL 100+\n6. Submit a detailed research proposal (3–5 pages)\n7. Letters of recommendation from supervisors required",
    },
    {
        "name": "NUST-JICA Japanese Internship", "country": "Japan", "region": "Asia Pacific",
        "type": "Internship", "degree_levels": "Bachelors,Masters", "fields": "Engineering,Computer Science,Natural Sciences",
        "min_gpa": 3.0, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": (
            "Japan International Cooperation Agency internship programme coordinated through Pakistani "
            "universities including NUST, UET, and COMSATS. Short-term technical traineeships in Japan "
            "covering engineering, manufacturing, agriculture, and IT. Covers flights, accommodation, "
            "and a daily allowance. Applications submitted through your university's international office."
        ),
        "official_link": "https://www.jica.go.jp/pakistan/english/activities/index.html",
        "roadmap": "1. Check with your university's international or industry liaison office for the current JICA cycle\n2. Must be nominated by your university — not an open application\n3. CGPA 3.0+ typically required by the nominating university\n4. Basic English communication required — no formal test\n5. Application requires a personal statement and faculty endorsement\n6. Placement is in Japan for 3–6 months in a technical organisation",
    },
    {
        "name": "Alibaba Global E-Commerce Talent Program", "country": "China", "region": "Asia Pacific",
        "type": "Internship", "degree_levels": "Bachelors,Masters", "fields": "Computer Science,Business,Engineering",
        "min_gpa": 3.0, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": (
            "Alibaba Group's international internship and talent programme for students in tech and business. "
            "Covers accommodation, daily allowance, and flights. Interns rotate through Alibaba's Hangzhou "
            "campus working on real product and business challenges. Strong focus on AI, e-commerce, and "
            "cloud technology. Particularly accessible for Pakistani students given strong China–Pakistan "
            "economic ties."
        ),
        "official_link": "https://talent.alibaba.com",
        "roadmap": "1. Apply at talent.alibaba.com — positions open throughout the year\n2. Filter for 'International Intern' positions\n3. Submit resume and a cover letter in English\n4. Coding test required for technical roles\n5. Interview rounds: HR → technical → manager\n6. Accommodation in Alibaba's campus housing is provided\n7. Strong English skills required; Mandarin is a plus but not mandatory",
    },
    {
        "name": "Google STEP Internship", "country": "Multiple", "region": "Global",
        "type": "Internship", "degree_levels": "Bachelors", "fields": "Computer Science,Engineering",
        "min_gpa": 0.0, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": (
            "Google's Student Training in Engineering Program for first- and second-year undergraduates. "
            "Paid internship (~USD 1,200/week) at Google offices worldwide. Covers relocation and housing. "
            "Designed for students from underrepresented backgrounds in tech. Work on real engineering "
            "projects with a Google engineer mentor. Strong pipeline to full software engineering internship "
            "in later years."
        ),
        "official_link": "https://careers.google.com/students/",
        "roadmap": "1. Apply at careers.google.com — positions open September-November for following summer\n2. Must be in 1st or 2nd year of a Computer Science or related degree\n3. No CGPA minimum — coding skills and problem-solving are what matter\n4. Strong background in data structures and algorithms is essential\n5. Online coding assessment followed by 2 technical interviews\n6. Visa sponsorship available — Google handles the process\n7. Competitive but accessible — focus on competitive programming to prepare",
    },

    # ════════════════════════════════════════════════════════════════
    # BATCH 2 — 25 NEW OPPORTUNITIES
    # ════════════════════════════════════════════════════════════════
    {
        "name": "Brunei Darussalam Government Scholarship",
        "country": "Brunei", "region": "Asia Pacific",
        "type": "Scholarship", "degree_levels": "Bachelors,Masters", "fields": "All",
        "min_gpa": 0.0, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": "Government-funded scholarship for international students to pursue undergraduate and postgraduate studies in Brunei. Covers tuition, accommodation, stipend, and medical expenses. Pakistan has an active bilateral agreement with Brunei — Pakistani students are among the eligible nationalities.",
        "official_link": "https://www.mfa.gov.bn",
        "eligible_nationalities": "",
        "roadmap": "1. Check the Ministry of Foreign Affairs Brunei website for the current intake cycle\n2. Create account on the scholarship portal\n3. Upload academic transcripts and attested documents\n4. Write a statement of purpose\n5. Submit application before the advertised deadline",
    },
    {
        "name": "Romanian Government Scholarship",
        "country": "Romania", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Bachelors,Masters,PhD", "fields": "All",
        "min_gpa": 0.0, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": "Scholarships funded by the Romanian government for international students across multiple disciplines. Covers tuition, accommodation, and a monthly stipend. Romanian language instruction provided in the first year. Pakistan is among eligible countries. No language test required at the application stage.",
        "official_link": "https://studyinromania.gov.ro",
        "eligible_nationalities": "",
        "roadmap": "1. Browse available programmes at studyinromania.gov.ro\n2. Select programme and confirm Pakistan is an eligible country for the current cycle\n3. Prepare academic documents — HEC attestation required\n4. Submit online application\n5. Successful applicants complete a Romanian language preparatory year",
    },
    {
        "name": "Joint Japan World Bank Scholarship",
        "country": "Japan", "region": "Asia Pacific",
        "type": "Scholarship", "degree_levels": "Masters", "fields": "Economics,Development Studies,Public Policy,Engineering",
        "min_gpa": 0.0, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": "Jointly administered by the Japanese government and World Bank for students from developing countries pursuing development-related Master's degrees. Covers tuition, living allowance, travel, and health insurance. Focus is on economic development, public policy, and infrastructure — Pakistani students working in development sectors are strong candidates.",
        "official_link": "https://www.worldbank.org/en/programs/scholarships/jjwbsp",
        "eligible_nationalities": "",
        "roadmap": "1. Must be a citizen of a World Bank member country and have 2+ years of development-related work experience\n2. Apply to a participating university programme first and obtain admission\n3. Submit the JJWBSP scholarship application with proof of admission\n4. Deadline varies by university — check the World Bank programme page\n5. Must commit to returning to Pakistan to work in development for at least 3 years",
    },
    {
        "name": "Orange Knowledge Programme (Netherlands)",
        "country": "Netherlands", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Masters", "fields": "Agriculture,Engineering,Health Sciences,Water Management",
        "min_gpa": 0.0, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": "Dutch government-funded scholarship (formerly NFP) supporting mid-career professionals from developing countries including Pakistan. Covers tuition, travel, living allowance, and health insurance for short courses or full Master's degrees at Dutch institutions. Focus on food security, water, and health sectors.",
        "official_link": "https://www.nuffic.nl/en/subjects/orange-knowledge-programme",
        "eligible_nationalities": "",
        "roadmap": "1. Must be a mid-career professional with at least 2 years of relevant work experience\n2. Check the OKP scholarship page to confirm Pakistan is in the eligible country list for the current cycle\n3. Apply for admission to an OKP-eligible programme at a Dutch institution\n4. Submit the Nuffic OKP scholarship application alongside your admissions application\n5. IELTS 6.0+ required for most programmes",
    },
    {
        "name": "Leiden University Excellence Scholarship",
        "country": "Netherlands", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Masters", "fields": "Law,Science,Medicine,Humanities",
        "min_gpa": 3.2, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": 90,
        "funding_type": "Partially Funded", "deadline": "2026-02-01",
        "description": "Merit-based scholarship for outstanding non-EU international Master's students at Leiden University, one of Europe's oldest universities. Awards of €10,000, €15,000, or full tuition waiver depending on merit. Available across most Master's programmes in law, science, social sciences, and humanities.",
        "official_link": "https://www.universiteitleiden.nl/en/scholarships/sea/leiden-university-excellence-scholarship",
        "eligible_nationalities": "",
        "roadmap": "1. Apply for a Master's programme at Leiden University — deadline typically February 1\n2. Tick the LExS scholarship box in your admissions application\n3. IELTS 6.5+ or TOEFL 90+\n4. Top applicants are automatically considered — no separate scholarship application\n5. Results announced with admission decision in April",
    },
    {
        "name": "Radboud Scholarship Programme",
        "country": "Netherlands", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Masters", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": 90,
        "funding_type": "Partially Funded", "deadline": "2026-02-01",
        "description": "Radboud University scholarship reducing tuition fees to the EU rate for talented non-EU international Master's students. Saves approximately €8,000–12,000 per year. Open to all Master's programmes at Radboud. Must be an excellent student — top of your class. Nijmegen is one of the most affordable Dutch cities.",
        "official_link": "https://www.ru.nl/scholarships/radboud-scholarship-programme",
        "eligible_nationalities": "",
        "roadmap": "1. Apply for a Radboud Master's programme by February 1\n2. Indicate scholarship interest in the admissions application\n3. IELTS 6.5+ or TOEFL 90+\n4. Upload academic transcripts showing excellent grades\n5. Scholarship decision comes with the admission decision",
    },
    {
        "name": "Swiss Government Excellence Scholarship",
        "country": "Switzerland", "region": "Europe",
        "type": "Scholarship", "degree_levels": "PhD", "fields": "All",
        "min_gpa": 3.3, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-11-15",
        "description": "Federal Commission for Scholarships (FCS) scholarship for foreign researchers and artists. Covers full living costs, tuition waiver, health insurance, and travel for PhD study or postdoctoral research at Swiss universities including ETH Zurich and EPFL. Pakistan is an eligible country. Highly competitive — strong research track record expected.",
        "official_link": "https://www.sbfi.admin.ch/sbfi/en/home/education/scholarships-and-grants/swiss-government-excellence-scholarships.html",
        "eligible_nationalities": "",
        "roadmap": "1. Identify a Swiss professor willing to supervise your research — email approach strongly recommended\n2. Apply through the Swiss Embassy in Pakistan — deadline typically November each year\n3. Prepare a detailed research proposal (4–5 pages)\n4. Two academic recommendation letters required\n5. No language test required but prior knowledge of the language of instruction helps\n6. Decisions announced by March of the following year",
    },
    {
        "name": "Vanier Canada Graduate Scholarship",
        "country": "Canada", "region": "North America",
        "type": "Scholarship", "degree_levels": "PhD", "fields": "Health Sciences,Engineering,Natural Sciences,Social Sciences",
        "min_gpa": 3.5, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-11-01",
        "description": "Prestigious Canadian doctoral scholarship worth CAD $50,000/year for 3 years. Awarded to exceptional researchers demonstrating leadership, academic excellence, and research potential. Open to Canadian and international students enrolled at Canadian universities. Highly competitive — less than 10% acceptance rate.",
        "official_link": "https://vanier.gc.ca/en/home-accueil.html",
        "eligible_nationalities": "",
        "roadmap": "1. Must be nominated by a Canadian university — you cannot apply directly\n2. Secure a supervisor at a Canadian university willing to nominate you\n3. Demonstrate outstanding academic record and leadership\n4. Nomination deadline is typically November 1\n5. Minimum A-equivalent average (3.5+ GPA) in last 2 years of full-time study required\n6. Results announced the following spring",
    },
    {
        "name": "Singapore International Graduate Award (SINGA)",
        "country": "Singapore", "region": "Asia Pacific",
        "type": "Research Program", "degree_levels": "PhD", "fields": "Engineering,Biomedical Sciences,Computing,Physical Sciences",
        "min_gpa": 3.2, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-06-01",
        "description": "International PhD research award jointly offered by A*STAR, NTU, NUS, and SUTD. Covers full tuition, monthly stipend of SGD $2,000–2,500, one-time airfare grant, and conference funding. Research conducted at Singapore's world-class research labs. Excellent for students with strong STEM research backgrounds.",
        "official_link": "https://www.a-star.edu.sg/Scholarships/for-graduate-studies/singapore-international-graduate-award-singa",
        "eligible_nationalities": "",
        "roadmap": "1. Apply at the SINGA portal — two intakes per year (January and June)\n2. Select up to 5 research projects from the SINGA project list\n3. Strong academic record in STEM required\n4. Research experience and publications are an advantage\n5. Shortlisted candidates attend an online interview\n6. Programme lasts 4 years",
    },
    {
        "name": "Hong Kong PhD Fellowship Scheme",
        "country": "Hong Kong", "region": "Asia Pacific",
        "type": "Fellowship", "degree_levels": "PhD", "fields": "All",
        "min_gpa": 3.5, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-12-01",
        "description": "Highly competitive fellowship supporting outstanding doctoral students at Hong Kong's eight universities including HKU, HKUST, and CUHK. Provides HKD $27,600/month stipend, conference grants, and travel allowance. One of the best-funded PhD fellowships in Asia — approximately 300 awarded globally each year.",
        "official_link": "https://cerg1.ugc.edu.hk/hkpfs/index.html",
        "eligible_nationalities": "",
        "roadmap": "1. Identify a supervisor at a participating Hong Kong university\n2. Apply online through the HKPFS portal — deadline December 1\n3. Simultaneously apply for PhD admission at the target university\n4. Submit 2 academic recommendation letters\n5. Write a compelling research proposal\n6. Shortlisted candidates may be invited for an interview",
    },
    {
        "name": "Research Training Program (Australia)",
        "country": "Australia", "region": "Asia Pacific",
        "type": "Scholarship", "degree_levels": "Masters,PhD", "fields": "All",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": "Australian government-funded scholarship supporting postgraduate research at Australian universities. Covers full tuition fees and a living allowance (approximately AUD $32,000/year). International students compete with domestic students for a limited number of international RTP places. Strong research proposal and supervisor support are critical.",
        "official_link": "https://www.education.gov.au/research-training-program",
        "eligible_nationalities": "",
        "roadmap": "1. Identify a potential supervisor at an Australian university\n2. Contact the supervisor by email — prior agreement significantly improves success\n3. Apply for PhD or Research Masters admission through the university\n4. Indicate RTP scholarship interest in the application\n5. IELTS 6.5+ required\n6. Competitive — academic excellence and a clear research plan are essential",
    },
    {
        "name": "University of Padua Excellence Scholarship",
        "country": "Italy", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Bachelors,Masters", "fields": "Engineering,Science,Medicine,Agriculture",
        "min_gpa": 3.2, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-04-30",
        "description": "Merit scholarship for talented international students at the University of Padua, one of Europe's oldest universities (est. 1222). Covers full tuition and a monthly living allowance for Bachelor's and Master's students in science, engineering, medicine, and agriculture. Italy has no tuition fee for some programmes even without the scholarship.",
        "official_link": "https://www.unipd.it/en/scholarships-international-students",
        "eligible_nationalities": "",
        "roadmap": "1. Apply for a degree programme at the University of Padua\n2. Browse the DSU (regional authority) scholarship alongside the university scholarship\n3. IELTS 6.0+ for English-taught programmes\n4. Submit academic transcripts showing excellent grades\n5. Scholarship application deadline is typically April/May — confirm on the official site",
    },
    {
        "name": "Bocconi Merit Award",
        "country": "Italy", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Bachelors,Masters", "fields": "Business,Economics,Finance",
        "min_gpa": 3.3, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": 90,
        "funding_type": "Partially Funded", "deadline": "2026-04-01",
        "description": "Merit-based award at Bocconi University, Europe's top business school. Covers 10–50% tuition reduction. Also offers need-based grants that can cover up to full costs for students with demonstrated financial need. Bocconi is consistently ranked among the world's top 10 for Economics and Business. Milan has a large international student community.",
        "official_link": "https://www.unibocconi.eu/scholarships",
        "eligible_nationalities": "",
        "roadmap": "1. Apply for admission to a Bocconi programme — deadline April 1 for scholarships\n2. Submit academic transcripts and test scores\n3. IELTS 6.5+ or TOEFL 90+ for English-taught programmes\n4. Scholarship is automatically considered based on academic records\n5. Need-based grants require additional financial documentation\n6. Strong performance in Bocconi's language assessment test is important",
    },
    {
        "name": "National Taiwan University Scholarship",
        "country": "Taiwan", "region": "Asia Pacific",
        "type": "Scholarship", "degree_levels": "Masters,PhD", "fields": "Engineering,Medicine,Agriculture,Science",
        "min_gpa": 3.2, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-03-31",
        "description": "NTU is Asia's top 20 university. International graduate scholarships cover monthly stipend (TWD 10,000–34,000), full or partial tuition waiver, and research allowance. English-taught programmes available across engineering, CS, and sciences. Taiwan is increasingly popular among Pakistani students for its affordability, safety, and research quality.",
        "official_link": "https://www.ntu.edu.tw/english/admissions/scholarship.html",
        "eligible_nationalities": "",
        "roadmap": "1. Browse English-taught graduate programmes at NTU\n2. Contact a potential supervisor before applying\n3. Apply online — deadline typically March 31\n4. IELTS 6.0+ or equivalent required for English programmes\n5. Submit research plan and recommendation letters\n6. Taiwan Ministry of Education (MOE) Scholarship can be applied alongside NTU scholarship",
    },
    {
        "name": "President's Scholarship NTUST (Taiwan)",
        "country": "Taiwan", "region": "Asia Pacific",
        "type": "Scholarship", "degree_levels": "Masters,PhD", "fields": "Engineering,Computer Science,Management",
        "min_gpa": 3.3, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Fully Funded", "deadline": "2026-04-30",
        "description": "Graduate scholarship at National Taiwan University of Science and Technology (NTUST), a top engineering university in Asia. Covers full tuition waiver and monthly stipend. English-taught programmes in engineering, CS, and management. Taiwan offers a safe, affordable, and internationally connected study environment.",
        "official_link": "https://www.ntust.edu.tw/home.php",
        "eligible_nationalities": "",
        "roadmap": "1. Apply to NTUST's English-taught graduate programme online\n2. Email a potential supervisor before the deadline — supervisor agreement significantly helps\n3. No IELTS required for many programmes (internal English assessment)\n4. Strong academic record in engineering or CS required\n5. Submit transcripts, CV, and statement of purpose\n6. Results announced within 6–8 weeks of application",
    },
    {
        "name": "Khalifa University Graduate Scholarship",
        "country": "UAE", "region": "Middle East & Central Asia",
        "type": "Scholarship", "degree_levels": "Masters,PhD", "fields": "Electrical Engineering,Mechanical Engineering,Chemical Engineering,Petroleum Engineering",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": 79,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": "Comprehensive graduate scholarship at Khalifa University, Abu Dhabi — one of the Arab world's top STEM universities (QS Rank ~271). Covers full tuition, monthly stipend (AED 4,000–7,000), and accommodation support. Strong focus on energy, aerospace, nuclear, and computer engineering. Very accessible for Pakistani students given proximity and cultural familiarity.",
        "official_link": "https://www.ku.ac.ae/graduate-admissions",
        "eligible_nationalities": "",
        "roadmap": "1. Browse Khalifa University graduate programmes at ku.ac.ae\n2. Apply online — rolling admissions, apply early\n3. IELTS 6.0+ or TOEFL 79+ required\n4. Submit transcripts, CV, and statement of purpose\n5. Strong GRE scores are an advantage but not always mandatory\n6. Scholarship included in admission package for qualifying students",
    },
    {
        "name": "University of Debrecen Scholarship (Hungary)",
        "country": "Hungary", "region": "Europe",
        "type": "University", "degree_levels": "Bachelors,Masters,PhD", "fields": "Medicine,Pharmacy,Dentistry,Engineering",
        "min_gpa": 2.8, "ielts_required": 0, "min_ielts": None, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Partially Funded", "deadline": "Rolling",
        "description": "University of Debrecen offers institutional scholarships and Stipendium Hungaricum placements. Particularly strong in Medicine, Pharmacy, and Dentistry — these programmes are taught in English and attract many Pakistani students. Tuition fees are lower than Western Europe. The Stipendium Hungaricum scholarship separately covers full costs.",
        "official_link": "https://www.unideb.hu/en/international-students",
        "eligible_nationalities": "",
        "roadmap": "1. Apply for Stipendium Hungaricum first — if accepted, costs are fully covered\n2. Alternatively, apply directly for English-taught Medicine, Pharmacy, or Dentistry programmes\n3. No IELTS required — the university conducts its own English assessment\n4. Submit secondary school or bachelor's transcripts\n5. Entrance interview or exam may be required for Medicine\n6. Institutional partial scholarships available for outstanding applicants",
    },
    {
        "name": "Bilkent University Graduate Scholarship",
        "country": "Turkey", "region": "Middle East & Central Asia",
        "type": "Scholarship", "degree_levels": "Masters,PhD", "fields": "Engineering,Science,Economics",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": 79,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": "Bilkent University, Turkey's first private university, offers full graduate funding packages including tuition waiver, monthly stipend, and accommodation for outstanding Masters and PhD students. Strong in engineering, computer science, and economics. English-taught programmes available. Turkish culture and proximity make it an accessible option for Pakistani students.",
        "official_link": "https://w3.bilkent.edu.tr/bilkent/graduate-admissions",
        "eligible_nationalities": "",
        "roadmap": "1. Browse Bilkent's English-taught graduate programmes at bilkent.edu.tr\n2. Contact a potential supervisor by email\n3. Apply online — rolling admissions\n4. IELTS 6.0+ or TOEFL 79+\n5. Submit academic transcripts and a research/study plan\n6. Fully funded package awarded to competitive applicants at admission",
    },
    {
        "name": "University of Auckland International Excellence Scholarship",
        "country": "New Zealand", "region": "Asia Pacific",
        "type": "Scholarship", "degree_levels": "Bachelors,Masters", "fields": "All",
        "min_gpa": 3.3, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": 90,
        "funding_type": "Partially Funded", "deadline": "2026-10-01",
        "description": "Merit scholarship for high-achieving international students at the University of Auckland, New Zealand's top-ranked university (QS Rank ~68). Awards up to NZD $10,000 for one year of study. New Zealand offers a welcoming environment, world-class research, and post-study work visa options of up to 3 years.",
        "official_link": "https://www.auckland.ac.nz/en/study/scholarships-and-awards/scholarship-types/international-student-scholarships.html",
        "eligible_nationalities": "",
        "roadmap": "1. Apply for admission to the University of Auckland\n2. Submit scholarship application — deadline October 1 for Semester 1 entry\n3. IELTS 6.5+ or TOEFL 90+\n4. Strong academic record required — GPA equivalent to A/A-\n5. Scholarship automatically considered based on your academic record\n6. Results announced with admission decision",
    },
    {
        "name": "Monash International Merit Scholarship",
        "country": "Australia", "region": "Asia Pacific",
        "type": "Scholarship", "degree_levels": "Bachelors,Masters", "fields": "All",
        "min_gpa": 3.3, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": 79,
        "funding_type": "Partially Funded", "deadline": "Rolling",
        "description": "Scholarship recognising excellent academic achievement for international students at Monash University (QS Rank ~37). Awards AUD $10,000 per year, automatically applied as a tuition reduction. Open to all undergraduate and postgraduate coursework programmes. Monash is particularly strong in Engineering, Medicine, Law, and Business.",
        "official_link": "https://www.monash.edu/study/fees-scholarships/scholarships/find-a-scholarship/monash-international-merit-scholarship",
        "eligible_nationalities": "",
        "roadmap": "1. Apply for admission to Monash University — scholarship automatically considered\n2. No separate scholarship application required\n3. IELTS 6.5+ or TOEFL 79+\n4. Must achieve the equivalent of a high distinction average\n5. Award applied directly to your tuition invoice\n6. Rolling applications — apply early for best results",
    },
    {
        "name": "University of Adelaide Global Academic Excellence Scholarship",
        "country": "Australia", "region": "Asia Pacific",
        "type": "Scholarship", "degree_levels": "Bachelors,Masters", "fields": "All",
        "min_gpa": 3.3, "ielts_required": 1, "min_ielts": 6.5, "toefl_required": 0, "min_toefl": 79,
        "funding_type": "Partially Funded", "deadline": "Rolling",
        "description": "25% tuition reduction scholarship for high-performing international students at the University of Adelaide, a Group of Eight research university. Automatically awarded to students meeting the academic threshold — no separate application needed. Adelaide is one of Australia's most affordable capital cities for international students.",
        "official_link": "https://www.adelaide.edu.au/scholarships/undergraduate/all-faculties/global-academic-excellence-scholarship",
        "eligible_nationalities": "",
        "roadmap": "1. Apply for admission to University of Adelaide — scholarship automatically assessed\n2. IELTS 6.5+ or TOEFL 79+\n3. Must meet the academic excellence threshold (high distinction equivalent)\n4. No separate scholarship form needed\n5. Award appears as a 25% tuition reduction in your offer letter",
    },
    {
        "name": "University of Malta Scholarship",
        "country": "Malta", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Masters", "fields": "Engineering,Health Sciences,Arts,Business",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": None,
        "funding_type": "Partially Funded", "deadline": "Rolling",
        "description": "Funding opportunities for international postgraduate students at the University of Malta, the smallest EU country's national university. Malta is English-speaking, EU-member, Mediterranean island — unique combination of culture and academic quality. Partial scholarships and assistantships available. Good option for students interested in European study at lower cost than Western Europe.",
        "official_link": "https://www.um.edu.mt/scholarships",
        "eligible_nationalities": "",
        "roadmap": "1. Browse postgraduate programmes at um.edu.mt\n2. Apply for a programme and indicate scholarship interest\n3. IELTS 6.0+ (Malta is English-speaking so requirements are accessible)\n4. Upload academic transcripts and CV\n5. Contact the relevant department for assistantship opportunities\n6. Malta's tuition fees are among the lowest in the EU",
    },
    {
        "name": "Skoltech Graduate Scholarship (Russia)",
        "country": "Russia", "region": "Europe",
        "type": "Scholarship", "degree_levels": "Masters,PhD", "fields": "Data Science,Artificial Intelligence,Engineering,Biotechnology",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": 75,
        "funding_type": "Fully Funded", "deadline": "2026-04-30",
        "description": "Skolkovo Institute of Science and Technology (Skoltech) offers fully funded graduate education in a unique partnership with MIT. Covers full tuition, monthly stipend, and accommodation in Moscow. Programmes entirely in English. Focus on AI, data science, energy, biomedicine, and space technology. Includes a semester at MIT as part of the curriculum.",
        "official_link": "https://www.skoltech.ru/en/admissions",
        "eligible_nationalities": "",
        "roadmap": "1. Apply at Skoltech's online portal — deadline April 30\n2. Select a Masters or PhD programme in your area\n3. IELTS 6.0+ or TOEFL 75+ required\n4. Submit academic transcripts and a statement of purpose\n5. Online interview conducted for shortlisted candidates\n6. Scholarship covers full costs including accommodation",
    },
    {
        "name": "Chulalongkorn University Graduate Scholarship",
        "country": "Thailand", "region": "Asia Pacific",
        "type": "Scholarship", "degree_levels": "Masters,PhD", "fields": "Engineering,Medicine,Public Health,Science",
        "min_gpa": 3.0, "ielts_required": 1, "min_ielts": 6.0, "toefl_required": 0, "min_toefl": 79,
        "funding_type": "Fully Funded", "deadline": "Rolling",
        "description": "Graduate scholarship at Chulalongkorn University, Thailand's most prestigious university and one of Southeast Asia's top research institutions. Covers full tuition, monthly stipend, accommodation, and health insurance. English-taught programmes available in engineering, public health, and sciences. Bangkok is affordable and culturally vibrant.",
        "official_link": "https://www.chula.ac.th/en/admissions/international-students",
        "eligible_nationalities": "",
        "roadmap": "1. Browse English-taught graduate programmes at Chulalongkorn\n2. Contact a faculty member in your research area\n3. Apply for admission online — rolling deadlines\n4. IELTS 6.0+ or TOEFL 79+ required\n5. Submit research proposal, transcripts, and CV\n6. Thailand also offers a separate government scholarship for Pakistani students — check the Thai Embassy",
    },
]


def seed():
    init_db()
    conn = get_db()
    existing = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    if existing > 0:
        print(f"Clearing {existing} existing opportunities...")
        conn.execute("DELETE FROM opportunities")
        conn.commit()

    for opp in OPPORTUNITIES:
        conn.execute("""
            INSERT INTO opportunities
                (name, country, region, type, degree_levels, fields, min_gpa,
                 ielts_required, min_ielts, toefl_required, min_toefl,
                 funding_type, deadline, opening_date, application_status,
                 description, official_link, roadmap, eligible_nationalities)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            opp["name"], opp["country"], opp.get("region", "Global"),
            opp["type"], opp["degree_levels"], opp.get("fields", "All"),
            opp["min_gpa"], opp["ielts_required"], opp.get("min_ielts"),
            opp["toefl_required"], opp.get("min_toefl"),
            opp["funding_type"], opp.get("deadline"),
            opp.get("opening_date"), opp.get("application_status", "Open"),
            opp.get("description", ""), opp.get("official_link", ""),
            opp.get("roadmap", ""), opp.get("eligible_nationalities", ""),
        ))

    conn.commit()
    count = conn.execute("SELECT COUNT(*) FROM opportunities").fetchone()[0]
    conn.close()
    print(f"Seeded {count} opportunities.")
    # Print type summary
    conn2 = get_db()
    for row in conn2.execute("SELECT type, COUNT(*) as n FROM opportunities GROUP BY type ORDER BY n DESC"):
        print(f"  {row['type']:20s} {row['n']}")
    conn2.close()


if __name__ == "__main__":
    seed()
