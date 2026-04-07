import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Лиманский Лев · CV", page_icon="📄", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; background-color: #F5F0E8; color: #1A1A1A; }
.stApp { background-color: #F5F0E8; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 1.5rem 5rem; max-width: 780px; }


.me-label { font-size: 0.72rem; font-weight: 500; letter-spacing: 0.18em; text-transform: uppercase; color: #888; margin-bottom: 0.5rem; }
.me-name { font-family: 'Playfair Display', serif; font-size: clamp(2.4rem, 6vw, 3.8rem); font-weight: 900; line-height: 1.05; margin: 0 0 0.6rem; letter-spacing: -0.02em; }
.me-title { font-size: 1.05rem; font-weight: 300; color: #555; margin-bottom: 1.4rem; }
.me-contacts { display: flex; flex-wrap: wrap; gap: 0.5rem 1.5rem; font-size: 0.85rem; color: #444; }
.me-contacts a { color: #444; text-decoration: none; border-bottom: 1px solid #ccc; }
.me-contacts a:hover { color: #1A1A1A; border-color: #1A1A1A; }
.dl-btn { display: inline-block; margin-top: 1.2rem; padding: 0.55rem 1.4rem; background: #1A1A1A; color: #F5F0E8 !important; font-size: 0.78rem; font-weight: 500; letter-spacing: 0.12em; text-transform: uppercase; text-decoration: none !important; cursor: pointer; transition: background 0.2s; }
.dl-btn:hover { background: #333; }

.section-header { display: flex; align-items: baseline; gap: 1rem; margin: 2.5rem 0 1.2rem; }
.section-title { font-family: 'Playfair Display', serif; font-size: 1.35rem; font-weight: 700; letter-spacing: -0.01em; white-space: nowrap; }
.section-line { flex: 1; height: 1px; background: #1A1A1A; opacity: 0.25; }

.summary-text { font-size: 0.96rem; line-height: 1.8; color: #333; max-width: 660px; }
.summary-text p { margin: 0 0 0.75rem; }
.summary-text p:last-child { margin-bottom: 0; }

.exp-item { display: grid; grid-template-columns: 120px 1fr; gap: 0 1.5rem; margin-bottom: 1.8rem; padding-bottom: 1.8rem; border-bottom: 1px solid rgba(26,26,26,0.1); }
.exp-item:last-child { border-bottom: none; }
.exp-period { font-size: 0.78rem; font-weight: 500; color: #888; letter-spacing: 0.05em; padding-top: 0.15rem; line-height: 1.4; }
.exp-company { font-family: 'Playfair Display', serif; font-size: 1.02rem; font-weight: 700; margin-bottom: 0.15rem; }
.exp-role { font-size: 0.82rem; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase; color: #777; margin-bottom: 0.4rem; }
.exp-desc { font-size: 0.9rem; line-height: 1.65; color: #444; }

.edu-item { margin-bottom: 1.6rem; padding-bottom: 1.6rem; border-bottom: 1px solid rgba(26,26,26,0.1); }
.edu-item:last-child { border-bottom: none; }
.edu-year { font-size: 0.75rem; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; color: #888; margin-bottom: 0.25rem; }
.edu-school { font-family: 'Playfair Display', serif; font-size: 1.02rem; font-weight: 700; margin-bottom: 0.15rem; }
.edu-detail { font-size: 0.88rem; color: #555; line-height: 1.6; }
.edu-gpa { display: inline-block; margin-top: 0.3rem; padding: 0.15rem 0.55rem; background: #1A1A1A; color: #F5F0E8; font-size: 0.72rem; font-weight: 500; letter-spacing: 0.08em; }
.edu-papers { margin-top: 0.5rem; padding-left: 1rem; border-left: 2px solid rgba(26,26,26,0.15); }
.edu-paper { font-size: 0.83rem; color: #555; margin-bottom: 0.25rem; font-style: italic; }

.lang-row { display: flex; align-items: center; gap: 1rem; margin-bottom: 0.7rem; }
.lang-name { font-size: 0.9rem; font-weight: 500; width: 110px; }
.lang-bar-bg { flex: 1; height: 3px; background: rgba(26,26,26,0.12); }
.lang-bar-fill { height: 100%; background: #1A1A1A; }
.lang-level { font-size: 0.75rem; color: #888; width: 120px; text-align: right; }

.interests { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.5rem; }
.interest-tag { padding: 0.3rem 0.9rem; border: 1px solid rgba(26,26,26,0.2); font-size: 0.82rem; color: #555; font-style: italic; }

.activity-row { display: flex; gap: 1rem; margin-bottom: 0.7rem; font-size: 0.9rem; }
.act-year { color: #888; font-size: 0.8rem; width: 80px; flex-shrink: 0; padding-top: 0.05rem; }
.act-desc { color: #333; line-height: 1.5; }
            
@media print {
        html, body, .stApp, .block-container { 
            background-color: #FFFFFF !important; 
            color: #000000 !important;
            width: 100% !important;
            max-width: 100% !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        /* Скрываем всё лишнее: кнопку скачивания и элементы Streamlit */
        .no-print, header, footer, #MainMenu, .stDeployButton, [data-testid="stRadio"], iframe, [data-testid="stHtml"] {
            display: none !important;
        }

        .main .block-container {
            padding-top: 1rem !important;
        }

        /* Чтобы карточки опыта и учебы не разрывались между страницами */
        .exp-item, .edu-item {
            page-break-inside: avoid;
        }

        /* Текст контактов и ссылок делаем черным для четкости */
        .me-contacts a, .me-contacts span {
            color: #000 !important;
            border-color: #000 !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# ── Info ──────────────────────────────────────────────────────────
st.markdown(f"""
<div class="no-print" style="margin-bottom:2rem;padding-bottom:1rem;border-bottom:1px solid rgba(26,26,26,0.15);
     display:flex;justify-content:space-between;align-items:center;font-size:0.85rem;color:#666;">
    <div style="display:flex; gap:15px;">
        <a href="https://github.com/levlimanskiy" target="_blank" style="color:#666; text-decoration:none;">GitHub</a>
        <a href="https://t.me/levlimanskiy" target="_blank" style="color:#666; text-decoration:none;">Telegram</a>
    </div>
</div>""", unsafe_allow_html=True)

def section(en, ru):
    title = ru if RU else en
    st.markdown(f"""
    <div class="section-header">
        <span class="section-title">{title}</span>
        <div class="section-line"></div>
    </div>""", unsafe_allow_html=True)

def t(en, ru):
    return ru if RU else en

# ── Language toggle ───────────────────────────────────────────────────────────
if "lang" not in st.session_state:
    st.session_state.lang = "RU"

st.radio(
    "",
    ["EN", "RU"],
    key="lang",
    horizontal=True
)

RU = st.session_state.lang == "RU"

# ── ME ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="me">
    <div class="me-label">{t("Curriculum Vitae", "Резюме")}</div>
    <div class="me-name">{t("Lev Limanskiy", "Лиманский Лев Романович")}</div>
    <div class="me-title">{t("Economist · ML Engineer · Data Analyst", "Экономист · ML-инженер · Аналитик данных")}</div>
    <div class="me-contacts">
        <span>{t("📍 Moscow, Russia", "📍 Москва, Россия")}</span>
        <a href="mailto:lrlimanskiy@edu.hse.ru">lrlimanskiy@edu.hse.ru</a>
        <a href="tel:+79044773971">+7 904 477 39 71</a>
    </div>
    <br/>
</div>
""", unsafe_allow_html=True)
components.html(f"""
    <style>
        .dl-btn {{
            display: inline-block;
            padding: 0.55rem 1.4rem;
            background: #1A1A1A;
            color: #F5F0E8 !important;
            font-family: 'DM Sans', sans-serif;
            font-size: 0.78rem;
            font-weight: 500;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            text-decoration: none !important;
            cursor: pointer;
            border: none;
        }}
        .dl-btn:hover {{ background: #333; }}
    </style>
<button class="dl-btn" onclick="window.parent.print()">
    {t("↓ Download PDF", "↓ Скачать PDF")}
</button>
""", height=40)
# ── SUMMARY ───────────────────────────────────────────────────────────────────
section("Summary", "О себе")

summary_en = """
<div class="summary-text">
<p>
Economist and data scientist with a dual background that is genuinely rare: a rigorous quantitative
degree from HSE ICEF — one of Russia's most demanding economics programmes — combined with
hands-on machine learning engineering experience developed through academic research, professional
courses, and competitive hackathons.
</p>
<p>
On the finance side, my track record spans financial modelling at a construction firm,
real-estate advisory at KEPT, and transactional accounting at a federal government institution.
On the technical side, I have applied ML to crypto markets and real-estate pricing,
completed Karpov.Courses' intensive ML programme, and am currently pursuing an MSc in Data Science
(Machine Learning Engineering track) at HSE — GPA 4.99.
</p>
<p>
I am equally comfortable writing production Python pipelines and presenting results to a non-technical
audience. My goal is to work at the intersection of quantitative finance and data science —
building models that translate into real economic decisions.
</p>
</div>
"""

summary_ru = """
<div class="summary-text">
<p>
Экономист и специалист по данным с редким сочетанием двух дисциплин: строгая количественная
подготовка на программе МИЭФ ВШЭ — одной из самых сложных экономических программ страны —
и практический опыт в машинном обучении, накопленный через академические исследования,
профессиональные курсы и участие в хакатонах.
</p>
<p>
В области финансов: финансовое моделирование в строительной компании, стажировка в
консалтинге по недвижимости (КЭПТ) и работа в бухгалтерии федерального государственного учреждения.
В области технологий: применение ML для анализа крипторынков и оценки недвижимости. Для последнего даже
доплнил существующую модель <a href="https://www.hse.ru/ba/icef/students/diplomas/1054700208" target="_blank" style="color:inherit; text-decoration:underline;"> GWANN (geographically weighted artificial neural network) и добился улучшения
её работы</a>. К тому же, прошёл интенсивный курс Karpov.Courses по машинному обучению, а также продолжил обучение
в магистратуре ВШЭ по направлению «Науки о данных» (трек ML Engineer) — GPA 4.99.
</p>
<p>
Одинаково уверенно чувствую себя как при написании production Python-пайплайнов,
так и при презентации результатов нетехнической аудитории. Стремлюсь работать на стыке
количественных финансов и науки о данных — строить модели, которые влияют на реальные
экономические решения.
</p>
</div>
"""

st.markdown(summary_ru if RU else summary_en, unsafe_allow_html=True)

# ── EXPERIENCE ────────────────────────────────────────────────────────────────
section("Experience", "Опыт работы")

experience = [
    {
        "period":  ("2021–2023", "2021–2023"),
        "company": ("OOO SeverStroyTorg", "ООО «СеверСтройТорг»"),
        "role":    ("Economist", "Экономист"),
        "desc":    (
            "Economic analysis, financial modelling, and reporting for a construction and trade company. "
            "Contributed to budget planning and cost control processes.",
            "Экономический анализ, финансовое моделирование и отчётность для строительно-торговой компании. "
            "Участие в бюджетном планировании и контроле затрат.",
        ),
    },
    {
        "period":  ("Aug 2023", "Авг. 2023"),
        "company": ("KEPT — Real Estate Dept.", "ООО «Кэпт», Департамент недвижимости"),
        "role":    ("Intern", "Стажёр"),
        "desc":    (
            "Internship in the real estate advisory practice of a leading professional services firm. "
            "Gained hands-on exposure to property valuation methodologies and deal structuring.",
            "Стажировка в практике консультирования по недвижимости ведущей консалтинговой компании. "
            "Изучение методологий оценки объектов недвижимости и структурирования сделок.",
        ),
    },
    {
        "period":  ("Sep 2024\n– present", "Сент. 2024\n– н.в."),
        "company": (
            "Presidential Affairs Directorate of Russia — FSBI",
            "ФГБУ «Управление по эксплуатации зданий высших органов власти» УД Президента РФ",
        ),
        "role":    (
            "Senior Accountant · Banking Operations Group",
            "Ведущий бухгалтер · Группа по операциям с банковскими счетами",
        ),
        "desc":    (
            "Responsible for bank account operations within the central accounting department. "
            "Day-to-day transactional accounting, reconciliation, and financial reporting for a federal government body.",
            "Ведение операций по банковским счетам в центральной бухгалтерии учреждения. "
            "Ежедневный учёт транзакций, сверка и финансовая отчётность в федеральном органе государственной власти.",
        ),
    },
]

i = 1 if RU else 0
for exp in experience:
    st.markdown(f"""
    <div class="exp-item">
        <div class="exp-period">{exp['period'][i].replace(chr(10), '<br>')}</div>
        <div>
            <div class="exp-company">{exp['company'][i]}</div>
            <div class="exp-role">{exp['role'][i]}</div>
            <div class="exp-desc">{exp['desc'][i]}</div>
        </div>
    </div>""", unsafe_allow_html=True)

# ── EDUCATION ─────────────────────────────────────────────────────────────────
section("Education", "Образование")

if RU:
    st.markdown("""
    <div class="edu-item">
        <div class="edu-year">2020</div>
        <div class="edu-school">Программа Международного бакалавриата (IB)</div>
        <div class="edu-detail">Предметы: Английский язык, Немецкий язык, История</div>
        <span class="edu-gpa">GPA 5 / 5</span>
    </div>
    <div class="edu-item">
        <div class="edu-year">2020 – 2025</div>
        <div class="edu-school">НИУ «Высшая школа экономики»</div>
        <div class="edu-detail">Международный институт экономики и финансов (МИЭФ) · Бакалавриат: математика и экономика</div>
        <span class="edu-gpa">GPA 4.01 / 5</span>
        <div class="edu-papers">
            <div class="edu-paper">2022 · «Машинное обучение на рынке криптовалют» — 8/10</div>
            <div class="edu-paper">2023 · «Влияние социальных сетей на уровень цен: методы машинного анализа» — 5/10</div>
            <div class="edu-paper">2025 · <a href="https://www.hse.ru/ba/icef/students/diplomas/1054700208" target="_blank" style="color:inherit; text-decoration:underline;">ВКР: «Анализ ценообразования на рынке недвижимости»</a> — 7/10 </div>
        </div>
    </div>
    <div class="edu-item">
        <div class="edu-year">2021</div>
        <div class="edu-school">Coursera — Калифорнийский университет, Сан-Диего</div>
        <div class="edu-detail">Введение в анализ больших данных (Introduction to Big Data Analytics)</div>
    </div>
    <div class="edu-item">
        <div class="edu-year">2025</div>
        <div class="edu-school">Karpov.Courses</div>
        <div class="edu-detail">Машинное обучение: полный курс — продвинутые методы ML, работа с реальными данными, проектная практика</div>
    </div>
    <div class="edu-item">
        <div class="edu-year">2025 – н.в.</div>
        <div class="edu-school">НИУ «Высшая школа экономики»</div>
        <div class="edu-detail">Магистратура · Науки о данных (МНАД) · Трек: Machine Learning Engineer</div>
        <span class="edu-gpa">GPA 4.99 / 5</span>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="edu-item">
        <div class="edu-year">2020</div>
        <div class="edu-school">IB Certificate Programme</div>
        <div class="edu-detail">Subjects: English Language, German Language, History</div>
        <span class="edu-gpa">GPA 5 / 5</span>
    </div>
    <div class="edu-item">
        <div class="edu-year">2020 – 2025</div>
        <div class="edu-school">HSE — Higher School of Economics</div>
        <div class="edu-detail">International College of Economics and Finance (ICEF) · BSc Mathematics &amp; Economics</div>
        <span class="edu-gpa">GPA 4.01 / 5</span>
        <div class="edu-papers">
            <div class="edu-paper">2022 · "Machine Learning on Crypto Markets" — 8/10</div>
            <div class="edu-paper">2023 · "The Influence of Social Networks on Price Level: ML Techniques" — 5/10</div>
            <div class="edu-paper">2025 · Thesis: "Pricing and Valuation in the Real Estate Market" — 7/10</div>
        </div>
    </div>
    <div class="edu-item">
        <div class="edu-year">2021</div>
        <div class="edu-school">Coursera — UC San Diego</div>
        <div class="edu-detail">Introduction to Big Data Analytics</div>
    </div>
    <div class="edu-item">
        <div class="edu-year">2025</div>
        <div class="edu-school">Karpov.Courses</div>
        <div class="edu-detail">Machine Learning: Full Course — advanced ML methods, real-world datasets, end-to-end project work</div>
    </div>
    <div class="edu-item">
        <div class="edu-year">2025 – present</div>
        <div class="edu-school">HSE — Higher School of Economics</div>
        <div class="edu-detail">MSc Data Science (MNAD) · Machine Learning Engineer track</div>
        <span class="edu-gpa">GPA 4.99 / 5</span>
    </div>
    """, unsafe_allow_html=True)

# ── SKILLS ────────────────────────────────────────────────────────────────────
section("Skills & Tools", "Навыки и инструменты")

skill_rows = [
    (t("Programming",        "Программирование"),
     t("Python, VBA, C++",   "Python, VBA, C++")),
    (t("ML & Data Science", "ML и Data Science"),
     t("Scikit-learn, Pandas, NumPy, GeoPandas, PyTorch (ANN), Matplotlib, Time-Series, Big Data",
       "Scikit-learn, Pandas, NumPy, GeoPandas, PyTorch (ANN), Matplotlib, временные ряды, Big Data")),
    (t("Databases & SQL", "Базы данных"),
     t("PostgreSQL, SQL Server, Database Design, DBeaver, Pyodbc",
       "PostgreSQL, SQL Server, проектирование БД, DBeaver, Pyodbc")),
    (t("Finance & Analysis", "Финансы и анализ"),
     t("Financial Modelling, Accounting, Real Estate Valuation, Budgeting",
       "Финансовое моделирование, бухучёт, оценка недвижимости, бюджетирование")),
    (t("Dev Tools", "Инструменты"),
     t("VS Code, PyCharm, Jupyter Notebook, Git / GitHub, Streamlit, Excel / VBA, Power BI, 1C",
       "VS Code, PyCharm, Jupyter Notebook, Git / GitHub, Streamlit, Excel / VBA, Power BI, 1С")),
    (t("Operating Systems", "Операционные системы"),
     t("Linux (Ubuntu), Windows", "Linux (Ubuntu), Windows")),
]

cat_s = "font-size:0.72rem;letter-spacing:0.12em;text-transform:uppercase;color:#888;font-weight:500;padding-top:0.15rem"
val_s = "font-size:0.9rem;color:#333;line-height:1.75"

rows_html = "".join(
    f'<span style="{cat_s}">{cat}</span><span style="{val_s}">{val}</span>'
    for cat, val in skill_rows
)

st.markdown(f"""
<div style="display:grid;grid-template-columns:165px 1fr;gap:0.9rem 1.5rem;align-items:start;">
  {rows_html}
</div>
""", unsafe_allow_html=True)

# ── LANGUAGES ─────────────────────────────────────────────────────────────────
section("Languages", "Языки")

languages = [
    (t("Russian",  "Русский"),     1.0,  t("Native",          "Родной")),
    (t("English",  "Английский"),  0.85, "IELTS 7.5 · C1"),
    (t("German",   "Немецкий"),    0.55, t("Intermediate · B1", "Средний · B1")),
]
for name, pct, label in languages:
    st.markdown(f"""
    <div class="lang-row">
        <span class="lang-name">{name}</span>
        <div class="lang-bar-bg"><div class="lang-bar-fill" style="width:{int(pct*100)}%"></div></div>
        <span class="lang-level">{label}</span>
    </div>""", unsafe_allow_html=True)

# ── ACTIVITIES ────────────────────────────────────────────────────────────────
section("Activities & Volunteering", "Деятельность и волонтёрство")

activities = [
    ("2021–2023",
     t("Member, HSE Case Club — case competitions in strategy, finance, and operations.",
       "Участник кейс-клуба ВШЭ — кейс-чемпионаты по стратегии, финансам и операционному менеджменту.")),
    ("2021",
     t("Academic Tutor for Freshman students at HSE ICEF.",
       "Академический тьютор для первокурсников МИЭФ ВШЭ.")),
    ("2026",
     t("ML Hackathon participant — built and deployed an ML solution under time pressure as part of a team.",
       'Участник <a href="https://cups.online/ru/workareas/hse/1670/3007" target="_blank" style="color:inherit; text-decoration:underline;">хакатона по ML</a> — разработка и деплой ML-решения в условиях ограниченного времени, командная работа.')),
]

for year, desc in activities:
    st.markdown(f"""
    <div class="activity-row">
        <div class="act-year">{year}</div>
        <div class="act-desc">{desc}</div>
    </div>""", unsafe_allow_html=True)

# ── INTERESTS ─────────────────────────────────────────────────────────────────
section("Interests", "Интересы")

interests = [
    t("History",                "История"),
    t("Philosophy",             "Философия"),
    t("Political Science",      "Политология"),
    t("Machine Learning",       "Машинное обучение"),
    t("Real Estate Markets",    "Рынок недвижимости"),
]
tags = "".join(f'<span class="interest-tag">{i}</span>' for i in interests)
st.markdown(f'<div class="interests">{tags}</div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="no-print" style="margin-top:4rem;padding-top:1.5rem;border-top:1px solid rgba(26,26,26,0.15);
    <div>
        <span>{t("Lev Limanskiy · CV", "Лиманский Лев Романович · Резюме")}</span>
        <span style="margin-left: 10px;">
            <a href="https://github.com/levlimanskiy" target="_blank" style="color:#aaa; text-decoration:none;">GitHub</a> · 
            <a href="https://t.me/levlimanskiy" target="_blank" style="color:#aaa; text-decoration:none;">Telegram</a>
        </span>
    </div>
</div>""", unsafe_allow_html=True)