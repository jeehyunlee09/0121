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
            ("🧬 데이터 사이언티스트", "가설을 세우고 검증하며 인사이트를 만들어요.", ["💻 IT/데이터"]),
            ("📚 학술 연구자", "이론을 만들고 비판적으로 확장해요.", ["🧪 연구/과학"]),
        ],
    },
    "ENTJ": {
        "summary": "🚀 지휘관 · 목표 달성 · 조직을 움직이고 판을 키워요.",
        "strengths": ["🎯 결단", "📈 성과", "🧭 리더십", "🗺️ 전략"],
        "jobs": [
            ("🧩 프로덕트 매니저(PM)", "비전·우선순위·실행을 총괄해요.", ["📈 비즈/기획", "💻 IT/데이터"]),
            ("🏢 사업개발(BD)", "시장과 파트너십을 개척해요.", ["📈 비즈/기획"]),
            ("🗣️ 조직/전략 리더", "조직 설계와 운영으로 임팩트를 내요.", ["📈 비즈/기획"]),
            ("📣 캠페인 디렉터", "메시지·자원·사람을 묶어 변화를 만들어요.", ["📣 미디어/커뮤니케이션", "⚖️ 공공/정책"]),
        ],
    },
    "ENTP": {
        "summary": "⚡ 아이디어 스파커 · 토론/혁신 · 가능성을 연결해요.",
        "strengths": ["💡 발상", "🧩 연결", "🗣️ 설득", "🧪 실험"],
        "jobs": [
            ("🚀 스타트업 창업/기획", "새로운 문제를 정의하고 제품을 만들어요.", ["📈 비즈/기획"]),
            ("🧠 UX 리서처", "사람의 행동을 분석해 개선점을 찾어요.", ["🎨 창의/콘텐츠", "📈 비즈/기획"]),
            ("📣 마케팅 전략가", "메시지·채널·브랜딩을 설계해요.", ["📣 미디어/커뮤니케이션", "📈 비즈/기획"]),
            ("🎤 커뮤니케이션/PR", "이슈를 설계하고 여론을 관리해요.", ["📣 미디어/커뮤니케이션"]),
        ],
    },

    # Diplomats / advocates
    "INFJ": {
        "summary": "🌿 통찰형 조력자 · 가치/의미 · 사람과 구조를 함께 봐요.",
        "strengths": ["🧭 가치지향", "🫶 공감", "🔎 통찰", "🧩 서사화"],
        "jobs": [
            ("🕊️ 사회정책/NGO 기획", "취약성·정의를 중심으로 프로젝트를 설계해요.", ["⚖️ 공공/정책", "📈 비즈/기획"]),
            ("🧑‍🏫 진로/학습 코치", "목표 설정과 성장 경로를 돕습니다.", ["🤝 교육/상담"]),
            ("🧠 상담/임상심리 분야", "심리적 회복을 돕고 개입을 설계해요.", ["🤝 교육/상담", "🩺 보건/돌봄"]),
            ("✍️ 에디터/작가", "사람과 사회를 깊이 있게 해석해요.", ["🎨 창의/콘텐츠", "📣 미디어/커뮤니케이션"]),
        ],
    },
    "INFP": {
        "summary": "🎨 이상주의 창작자 · 진정성 · 의미 있는 이야기를 만들어요.",
        "strengths": ["💛 진정성", "🎭 표현", "🫶 공감", "🌈 가치"],
        "jobs": [
            ("✍️ 콘텐츠 크리에이터/작가", "감정과 의미를 담은 콘텐츠를 만들어요.", ["🎨 창의/콘텐츠", "📣 미디어/커뮤니케이션"]),
            ("🎨 브랜드 디자이너", "가치와 정체성을 시각화해요.", ["🎨 창의/콘텐츠"]),
            ("🧑‍🏫 교육 콘텐츠 개발", "학습을 더 ‘사람답게’ 설계해요.", ["🤝 교육/상담", "🎨 창의/콘텐츠"]),
            ("🕊️ 인권/시민단체 활동가", "가치 기반으로 변화를 조직해요.", ["⚖️ 공공/정책"]),
        ],
    },
    "ENFJ": {
        "summary": "🌟 사람을 이끄는 조율자 · 팀/관계 · 동기를 끌어올려요.",
        "strengths": ["🧭 리더십", "🫶 공감", "🗣️ 소통", "🤝 조정"],
        "jobs": [
            ("🧑‍🏫 교사/교육기획자", "사람의 성장을 설계하고 실행해요.", ["🤝 교육/상담"]),
            ("🤝 HR/조직문화", "조직의 관계와 동기를 설계해요.", ["📈 비즈/기획"]),
            ("📣 대외협력/커뮤니티 매니저", "사람과 기관을 연결해요.", ["📣 미디어/커뮤니케이션", "⚖️ 공공/정책"]),
            ("🕊️ 국제협력/프로젝트 코디네이터", "현장·기관·자원을 연결해요.", ["⚖️ 공공/정책", "📈 비즈/기획"]),
        ],
    },
    "ENFP": {
        "summary": "🎉 에너지 메이커 · 사람/아이디어 · 분위기와 가능성을 키워요.",
        "strengths": ["🌈 창의", "🗣️ 소통", "🤝 네트워킹", "🔥 동기부여"],
        "jobs": [
            ("🎤 크리에이터/방송/진행", "사람들과 에너지를 공유해요.", ["🎨 창의/콘텐츠", "📣 미디어/커뮤니케이션"]),
            ("📣 마케팅/브랜딩", "매력적인 스토리로 사람을 모아요.", ["📣 미디어/커뮤니케이션", "📈 비즈/기획"]),
            ("🧑‍🏫 교육/워크숍 퍼실리테이터", "참여형 수업/행사를 만들어요.", ["🤝 교육/상담"]),
            ("🌍 국제교류/행사기획", "다양한 사람을 연결해요.", ["⚖️ 공공/정책", "📣 미디어/커뮤니케이션"]),
        ],
    },

    # Guardians / doers
    "ISTJ": {
        "summary": "🧱 신뢰형 관리자 · 규칙/책임 · 안정적으로 완수해요.",
        "strengths": ["✅ 성실", "🧾 정확", "🧠 현실감각", "🛠️ 실행력"],
        "jobs": [
            ("📑 회계/재무", "정확한 기준으로 숫자를 관리해요.", ["📈 비즈/기획"]),
            ("🏛️ 행정/공무", "규정과 절차로 공공서비스를 운영해요.", ["⚖️ 공공/정책"]),
            ("🧪 품질관리(QA/QC)", "제품/프로세스의 품질을 지켜요.", ["🏗️ 공학/현장", "🧪 연구/과학"]),
            ("🗂️ 운영/PMO", "프로젝트를 일정·리스크로 관리해요.", ["📈 비즈/기획"]),
        ],
    },
    "ISFJ": {
        "summary": "🧸 배려형 지원자 · 돌봄/책임 · 꾸준히 지켜줘요.",
        "strengths": ["🫶 배려", "🧭 책임", "🧩 섬세함", "🤝 협업"],
        "jobs": [
            ("🩺 간호/보건", "돌봄과 안전을 책임져요.", ["🩺 보건/돌봄"]),
            ("🧑‍🏫 학급/생활지도 분야", "학생의 일상을 지지해요.", ["🤝 교육/상담"]),
            ("🏥 병원 코디네이터/행정", "의료 현장을 안정적으로 운영해요.", ["🩺 보건/돌봄", "📈 비즈/기획"]),
            ("🤝 사회복지", "일상의 회복을 돕습니다.", ["🩺 보건/돌봄", "⚖️ 공공/정책"]),
        ],
    },
    "ESTJ": {
        "summary": "📣 실행형 리더 · 조직/규율 · 성과를 ‘끝까지’ 만들어내요.",
        "strengths": ["📌 추진", "🧭 리더십", "🧾 체계", "✅ 책임"],
        "jobs": [
            ("🏗️ 현장/프로젝트 매니저", "현장을 안전·일정·품질로 관리해요.", ["🏗️ 공학/현장", "📈 비즈/기획"]),
            ("🏛️ 공공행정/관리", "제도와 운영으로 성과를 만듭니다.", ["⚖️ 공공/정책"]),
            ("📦 운영/물류", "프로세스를 최적화해요.", ["📈 비즈/기획"]),
            ("👮 조직관리/리더", "규칙과 기준으로 팀을 이끕니다.", ["📈 비즈/기획"]),
        ],
    },
    "ESFJ": {
        "summary": "💞 관계형 조정자 · 소통/돌봄 · 함께 잘 되게 만들어요.",
        "strengths": ["🤝 관계", "🗣️ 소통", "🧩 조율", "🫶 배려"],
        "jobs": [
            ("🧑‍🏫 교사/학원 강사", "관계와 동기로 학습을 이끌어요.", ["🤝 교육/상담"]),
            ("🤝 HR/채용/교육", "사람과 조직을 연결해요.", ["📈 비즈/기획"]),
            ("🏥 의료/복지 코디네이터", "사람 중심으로 서비스를 설계해요.", ["🩺 보건/돌봄"]),
            ("🎪 행사/커뮤니티 운영", "사람들이 모이고 성장하는 장을 만들어요.", ["📣 미디어/커뮤니케이션", "📈 비즈/기획"]),
        ],
    },

    # Explorers
    "ISTP": {
        "summary": "🛠️ 실전형 메이커 · 손으로 해결 · 빠르게 고쳐요.",
        "strengths": ["🔧 문제해결", "⚙️ 도구 활용", "🧠 냉정", "🏃 즉흥 대응"],
        "jobs": [
            ("🧰 엔지니어(기계/전기)", "현장의 문제를 기술로 해결해요.", ["🏗️ 공학/현장"]),
            ("🔍 디버거/테스터", "문제를 잡아내고 원인을 찾습니다.", ["💻 IT/데이터"]),
            ("🧪 실험/분석 테크니션", "정확한 실험과 측정에 강해요.", ["🧪 연구/과학"]),
            ("🚑 응급/구조 분야", "현장에서 빠르게 판단하고 대응해요.", ["🩺 보건/돌봄"]),
        ],
    },
    "ISFP": {
        "summary": "🌸 감각형 아티스트 · 취향/미감 · 섬세하게 표현해요.",
        "strengths": ["🎨 미감", "🫶 공감", "🌿 감수성", "🧩 디테일"],
        "jobs": [
            ("🎨 그래픽/영상 디자이너", "감각적으로 메시지를 전달해요.", ["🎨 창의/콘텐츠", "📣 미디어/커뮤니케이션"]),
            ("📷 포토/영상 크리에이터", "일상을 아름답게 기록해요.", ["🎨 창의/콘텐츠"]),
            ("🧑‍🍳 푸드/공예 분야", "손으로 만드는 직업에 잘 맞아요.", ["🎨 창의/콘텐츠"]),
            ("🩺 작업치료/재활 보조", "섬세한 관찰과 손기술이 중요해요.", ["🩺 보건/돌봄"]),
        ],
    },
    "ESTP": {
        "summary": "⚡ 액션형 도전가 · 현장/승부 · 빠르게 기회를 잡아요.",
        "strengths": ["🚀 실행", "🗣️ 설득", "🎯 승부", "🧭 대처"],
        "jobs": [
            ("💼 세일즈/영업", "사람을 만나 기회를 만들어요.", ["📈 비즈/기획"]),
            ("🎬 현장 프로듀서/AD", "현장을 컨트롤하며 결과를 내요.", ["🎨 창의/콘텐츠", "📈 비즈/기획"]),
            ("🚒 안전/현장 관리", "순간 판단과 대응이 중요해요.", ["🏗️ 공학/현장"]),
            ("📣 이벤트/프로모션", "즉각적 실행이 강점이에요.", ["📣 미디어/커뮤니케이션"]),
        ],
    },
    "ESFP": {
        "summary": "🎈 분위기 메이커 · 체험/공연 · 사람과 즐거움을 나눠요.",
        "strengths": ["🌟 표현", "🤝 친화", "🎭 무대감", "💛 공감"],
        "jobs": [
            ("🎤 공연/MC/아나운서", "무대에서 에너지를 전달해요.", ["🎨 창의/콘텐츠", "📣 미디어/커뮤니케이션"]),
            ("🧑‍🏫 체험형 교육 강사", "재미있게 배우게 만드는 재능!", ["🤝 교육/상담"]),
            ("🤝 서비스/호스피탈리티", "사람 중심의 서비스에 강해요.", ["📈 비즈/기획"]),
            ("📣 홍보/콘텐츠 운영", "사람을 모으는 메시지를 만들어요.", ["📣 미디어/커뮤니케이션"]),
        ],
    },
}

MBTI_LIST = list(JOB_DB.keys())
MBTI_LIST.sort()

def pick_jobs(mbti: str, categories_filter: list[str], k: int, shuffle: bool):
    jobs = JOB_DB[mbti]["jobs"]
    if categories_filter:
        jobs = [j for j in jobs if any(cat in j[2] for cat in categories_filter)]
    jobs = jobs[:]
    if shuffle:
        random.shuffle(jobs)
    return jobs[:k]

# =========================
# Header
# =========================
st.markdown('<div class="glow-title">🌈 MBTI 진로 추천 스튜디오 🧭</div>', unsafe_allow_html=True)
st.markdown('<div class="subtle">MBTI를 선택하면 ✨ 성향 요약 + 직업 추천 + 학습 포인트를 화려한 카드로 보여주는 진로 교육용 웹앱 🎓💼</div>', unsafe_allow_html=True)

# =========================
# Sidebar controls
# =========================
with st.sidebar:
    st.markdown("## 🧩 설정 패널")
    mbti = st.selectbox("🧬 MBTI 선택", MBTI_LIST, index=MBTI_LIST.index("ENFP") if "ENFP" in MBTI_LIST else 0)
    st.markdown("### 🎯 추천 필터")
    categories = st.multiselect("관심 분야(선택)", CATEGORIES, default=[])
    top_k = st.slider("추천 개수", 3, 12, 8)
    shuffle = st.toggle("🔀 추천 섞기", value=True)

    st.markdown("---")
    st.markdown("### 🧠 학습 팁")
    st.info("이 추천은 **참고용**이에요! 🤍\n\n✅ 흥미(Interest) + 강점(Strength) + 가치(Value) + 환경(Fit)을 함께 고려해보세요. 🌱")

# =========================
# Main layout
# =========================
left, right = st.columns([1.15, 0.85], gap="large")

with left:
    info = JOB_DB[mbti]
    st.markdown(
        f"""
        <div class="hero">
            <div style="display:flex; align-items:center; gap:14px; flex-wrap:wrap;">
                <div style="font-size:2.2rem;">🧬</div>
                <div>
                    <div style="font-weight:900; font-size:1.7rem;">{mbti} 타입 추천</div>
                    <div style="opacity:0.86; font-size:1.05rem; margin-top:2px;">{info["summary"]}</div>
                </div>
            </div>
            <div style="margin-top:14px;">
                {"".join([f'<span class="pill">{s}</span>' for s in info["strengths"]])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🧭 추천 직업 리스트 💼✨")
    jobs = pick_jobs(mbti, categories, top_k, shuffle)

    if not jobs:
        st.warning("😵 선택한 분야 필터에 맞는 추천이 없어요. 사이드바에서 필터를 조금 완화해봐요! ✨")
    else:
        cols = st.columns(2, gap="large")
        for idx, (title, desc, tags) in enumerate(jobs):
            with cols[idx % 2]:
                badges = "".join([f"<span>🏷️ {t}</span>" for t in tags])
                st.markdown(
                    f"""
                    <div class="card">
                        <div class="card-title">{title}</div>
                        <div class="card-desc">{desc}</div>
                        <div class="badges">{badges}</div>
                        <div style="margin-top:10px; opacity:0.78; font-size:0.92rem;">
                            ✅ <b>다음 행동</b>: 관련 직무 1개를 골라 <b>업무 3가지</b> + <b>필요 역량 3가지</b>를 적어보세요 ✍️
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

with right:
    st.markdown("### 🎒 진로 탐색 미션 🔥")
    st.markdown(
        """
        <div class="info">
            <div style="font-weight:900; font-size:1.1rem;">📌 오늘의 미션 (10분)</div>
            <ul style="margin-top:10px; line-height:1.7;">
                <li>🗺️ 추천 직업 중 <b>가장 끌리는 1개</b>를 고르기</li>
                <li>🔎 그 직업의 <b>실제 하는 일 3개</b> 찾아 적기</li>
                <li>🧠 필요한 <b>역량 3개</b>와 내가 가진 <b>근거 1개</b> 쓰기</li>
                <li>🧪 이번 주에 할 수 있는 <b>작은 실험 1개</b> 정하기</li>
            </ul>
            <div style="opacity:0.8; font-size:0.95rem;">
                🌟 팁: “작은 실험”은 예를 들어 <b>직무 인터뷰 영상 1개 보기</b>, <b>관련 책 10쪽 읽기</b>, <b>미니 프로젝트 1개 만들기</b> 같은 거예요!
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🧩 나만의 진로 키워드 생성기 ✨")
    colA, colB = st.columns(2)
    with colA:
        vibe = st.selectbox("🌈 분위기", ["차분한", "도전적인", "따뜻한", "논리적인", "창의적인", "담대한", "섬세한", "에너지 넘치는"])
    with colB:
        theme = st.selectbox("🧭 관심 테마", ["사람", "데이터", "정책", "기술", "예술", "교육", "환경", "의료", "커뮤니티", "국제"])
    key = f"🔑 {mbti} · {vibe} · {theme}"
    st.success(key)

    st.markdown("### 🎇 추천 문장 (자기소개/포스터용)")
    lines = [
        f"🚀 저는 {mbti} 성향을 바탕으로 **{theme}** 분야에서 **{vibe}** 방식으로 문제를 해결하고 싶어요!",
        f"🧩 제가 좋아하는 건 ‘{theme}’이고, 저는 {mbti}답게 **강점을 구조화해서 실행**하는 편이에요.",
        f"🌱 저는 {mbti}로서 **{vibe}** 태도로 배우고, 작은 실험을 통해 진로를 구체화하고 있어요!"
    ]
    st.write(random.choice(lines))

    st.markdown("### 🧷 주의(교육용 안내)")
    st.caption("⚠️ MBTI는 성향 참고 도구예요. 개인의 경험·가치·환경·역량이 더 중요합니다. 💙")

st.markdown('<div class="footer">✨ Made with Streamlit · 진로 교육용 MBTI 추천 데모 · 이모지 파티 🎉🧠💼</div>', unsafe_allow_html=True)
