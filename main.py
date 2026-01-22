import streamlit as st
import random

# =========================
# Page config
# =========================
st.set_page_config(
    page_title="🌈 MBTI 진로 추천 스튜디오",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================
# Fancy CSS
# =========================
st.markdown(
    """
<style>
/* Base */
html, body, [class*="css"]  {
    font-family: "Pretendard", "Apple SD Gothic Neo", "Noto Sans KR", sans-serif;
}

/* Background gradient */
.stApp {
    background: radial-gradient(1200px 600px at 10% 10%, rgba(255, 0, 180, 0.18), transparent 50%),
                radial-gradient(1000px 700px at 90% 20%, rgba(0, 200, 255, 0.18), transparent 52%),
                radial-gradient(900px 600px at 40% 90%, rgba(0, 255, 170, 0.16), transparent 52%),
                linear-gradient(135deg, #0b0f19 0%, #0b1220 35%, #0b0f19 100%);
    color: #eaf0ff;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Title glow */
.glow-title {
    font-size: 2.6rem;
    font-weight: 900;
    line-height: 1.15;
    margin-bottom: 0.25rem;
    background: linear-gradient(90deg, #ff4fd8, #6ee7ff, #7CFF6B);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 18px rgba(255, 79, 216, 0.28), 0 0 22px rgba(110, 231, 255, 0.18);
}
.subtle {
    color: rgba(234,240,255,0.8);
    font-size: 1.05rem;
    margin-bottom: 1.25rem;
}

/* Pills */
.pill {
    display:inline-block;
    padding: 0.35rem 0.65rem;
    border-radius: 999px;
    margin-right: 0.4rem;
    margin-bottom: 0.4rem;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    color: rgba(234,240,255,0.92);
    font-size: 0.95rem;
}

/* Card */
.card {
    background: linear-gradient(180deg, rgba(255,255,255,0.09), rgba(255,255,255,0.04));
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 22px;
    padding: 18px 18px 16px 18px;
    box-shadow: 0 10px 35px rgba(0,0,0,0.35);
    position: relative;
    overflow: hidden;
    min-height: 180px;
}
.card::before {
    content:"";
    position:absolute;
    inset:-2px;
    background: radial-gradient(400px 200px at 20% 10%, rgba(255,79,216,0.22), transparent 60%),
                radial-gradient(400px 220px at 80% 20%, rgba(110,231,255,0.18), transparent 60%),
                radial-gradient(400px 220px at 60% 90%, rgba(124,255,107,0.14), transparent 60%);
    filter: blur(0px);
    z-index: 0;
}
.card > * { position: relative; z-index: 1; }

.card-title {
    font-weight: 900;
    font-size: 1.2rem;
    margin-bottom: 0.3rem;
}
.card-desc {
    color: rgba(234,240,255,0.82);
    font-size: 0.98rem;
    margin-bottom: 0.7rem;
}
.badges span {
    display:inline-block;
    font-size: 0.85rem;
    padding: 0.28rem 0.55rem;
    border-radius: 999px;
    margin-right: 0.35rem;
    margin-bottom: 0.35rem;
    border: 1px solid rgba(255,255,255,0.14);
    background: rgba(0,0,0,0.18);
}

/* Big hero box */
.hero {
    background: linear-gradient(180deg, rgba(255,255,255,0.11), rgba(255,255,255,0.05));
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 26px;
    padding: 18px 22px;
    box-shadow: 0 14px 60px rgba(0,0,0,0.36);
    position: relative;
    overflow: hidden;
}
.hero::after {
    content:"";
    position:absolute;
    width: 520px;
    height: 520px;
    right: -240px;
    top: -240px;
    background: radial-gradient(circle at 30% 30%, rgba(255,79,216,0.25), transparent 55%),
                radial-gradient(circle at 70% 70%, rgba(110,231,255,0.22), transparent 55%);
    filter: blur(0px);
    z-index: 0;
}
.hero > * { position: relative; z-index: 1; }

/* Smaller info box */
.info {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 18px;
    padding: 14px 16px;
}

/* Button tweaks */
.stButton button {
    border-radius: 14px !important;
    padding: 0.6rem 1.0rem !important;
    font-weight: 800 !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    background: linear-gradient(90deg, rgba(255,79,216,0.24), rgba(110,231,255,0.22), rgba(124,255,107,0.18)) !important;
    color: #eaf0ff !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.30);
}
.stButton button:hover {
    transform: translateY(-1px);
}

/* Selectbox / multiselect */
div[data-baseweb="select"] > div {
    border-radius: 14px !important;
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
}

/* Footer */
.footer {
    opacity: 0.72;
    font-size: 0.9rem;
    padding-top: 0.6rem;
}
</style>
""",
    unsafe_allow_html=True,
)

# =========================
# Data (MBTI -> traits + jobs)
# =========================
CATEGORIES = ["🎨 창의/콘텐츠", "💻 IT/데이터", "🧪 연구/과학", "📈 비즈/기획", "🤝 교육/상담", "🩺 보건/돌봄", "⚖️ 공공/정책", "🏗️ 공학/현장", "🧑‍⚖️ 법/윤리", "📣 미디어/커뮤니케이션"]

JOB_DB = {
    # Analysts / strategists
    "INTJ": {
        "summary": "🧠 전략 설계자 · 장기 목표 · 시스템 최적화에 강해요.",
        "strengths": ["📌 큰 그림", "🧩 구조화", "🧠 분석", "🧭 독립적 추진"],
        "jobs": [
            ("📊 데이터 전략가", "데이터로 문제를 정의하고 해결책을 설계해요.", ["💻 IT/데이터", "📈 비즈/기획"]),
            ("🧩 정책/전략 컨설턴트", "복잡한 이해관계를 구조화해 전략을 만들어요.", ["⚖️ 공공/정책", "📈 비즈/기획"]),
            ("🧪 연구기획자(R&D PM)", "연구 로드맵과 자원 배분을 설계해요.", ["🧪 연구/과학", "📈 비즈/기획"]),
            ("🏛️ 공공정책 분석가", "정책의 효과·형평성·부작용을 분석해요.", ["⚖️ 공공/정책"]),
        ],
    },
    "INTP": {
        "summary": "🧪 아이디어 실험가 · 개념/논리 탐구 · ‘왜?’에 집착해요.",
        "strengths": ["🧠 논리", "🔍 탐구", "💡 발상", "🧰 문제해결"],
        "jobs": [
            ("🧠 AI/ML 연구원", "모델을 설계하고 실험하며 개선해요.", ["💻 IT/데이터", "🧪 연구/과학"]),
            ("🔐 보안 연구원", "시스템 취약점을 찾고 방어 전략을 세워요.", ["💻 IT/데이터"]),
            ("🧬 데이터 사이언티스트", "가
