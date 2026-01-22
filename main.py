import streamlit as st
import requests
from streamlit_lottie import st_lottie

# 페이지 설정
st.set_page_config(page_title="내 꿈을 찾아줘! MBTI 진로 탐색", page_icon="🚀", layout="wide")

# Lottie 애니메이션 로드 함수
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_career = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_u8o7blal.json") # 커리어 관련 애니메이션

# --- 데이터베이스 ---
mbti_careers = {
    "ISTJ": {"job": "회계사, 공무원, 사서", "desc": "신중하고 철저하며 책임감이 강해요!", "emoji": "📋"},
    "ISFJ": {"job": "간호사, 초등교사, 사회복지사", "desc": "차분하고 헌신적이며 타인을 잘 도와요!", "emoji": "🏥"},
    "INFJ": {"job": "상담심리사, 작가, 예술가", "desc": "통찰력이 뛰어나고 사람들에게 영감을 줘요!", "emoji": "🔮"},
    "INTJ": {"job": "데이터 과학자, 전략가, 건축가", "desc": "논리적이고 독립적이며 분석 능력이 탁월해요!", "emoji": "🧠"},
    "ISTP": {"job": "엔지니어, 파일럿, 운동선수", "desc": "객관적이고 합리적이며 도구 사용에 능숙해요!", "emoji": "🛠️"},
    "ISFP": {"job": "디자이너, 작곡가, 사진작가", "desc": "예술적 감각이 뛰어나고 현재의 삶을 즐겨요!", "emoji": "🎨"},
    "INFP": {"job": "소설가, 시인, 정신건강 상담사", "desc": "이상주의적이며 자신만의 가치관이 뚜렷해요!", "emoji": "🌈"},
    "INTP": {"job": "철학자, 프로그래머, 연구원", "desc": "지적 호기심이 많고 문제 해결을 즐겨요!", "emoji": "💻"},
    "ESTP": {"job": "사업가, 소방관, 경찰관", "desc": "활동적이고 에너지가 넘치며 현장형 타입이에요!", "emoji": "🔥"},
    "ESFP": {"job": "배우, 연예인, 이벤트 기획자", "desc": "사교적이고 낙천적이며 분위기 메이커예요!", "emoji": "✨"},
    "ENFP": {"job": "마케터, 광고 기획자, 크리에이터", "desc": "상상력이 풍부하고 열정적으로 새로운 일을 시작해요!", "emoji": "🎡"},
    "ENTP": {"job": "변호사, 정치인, 발명가", "desc": "다재다능하고 토론을 즐기며 혁신적이에요!", "emoji": "💡"},
    "ESTJ": {"job": "경영인, 프로젝트 매니저, 군인", "desc": "조직적이고 실무적이며 추진력이 대단해요!", "emoji": "📢"},
    "ESFJ": {"job": "호텔리어, 승무원, 영업사원", "desc": "친절하고 동료애가 깊으며 협동을 잘해요!", "emoji": "🤝"},
    "ENFJ": {"job": "교사, 외교관, 사회운동가", "desc": "카리스마가 있고 타인의 성장을 돕는 리더예요!", "emoji": "🌟"},
    "ENTJ": {"job": "CEO, 정치 리더, 경영 컨설턴트", "desc": "비전이 뚜렷하고 목표를 달성하는 능력이 커요!", "emoji": "🎯"},
}

# --- 메인 화면 구성 ---
st.markdown("<h1 style='text-align: center; color: #6C63FF;'>✨ 내 꿈을 찾는 MBTI 여행 ✨</h1>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([1, 1])

with col1:
    st_lottie(lottie_career, height=300, key="coding")

with col2:
    st.subheader("나의 MBTI는 무엇인가요? 🤔")
    selected_mbti = st.selectbox(
        "아래에서 선택해 주세요 👇",
        list(mbti_careers.keys())
    )
    
    btn_clicked = st.button("🚀 추천 직업 확인하기!")

# --- 결과 섹션 ---
if btn_clicked:
    data = mbti_careers[selected_mbti]
    
    st.balloons() # 풍선 효과
    
    st.markdown(f"""
    <div style="background-color: #F0F2F6; padding: 30px; border-radius: 20px; border: 2px solid #6C63FF;">
        <h2 style="color: #6C63FF; text-align: center;">{data['emoji']} 당신은 멋진 {selected_mbti} 타입!</h2>
        <h4 style="text-align: center; color: #31333F;">"{data['desc']}"</h4>
        <hr>
        <h3 style="text-align: center;">추천하는 직업 리스트 🏆</h3>
        <p style="text-align: center; font-size: 24px; font-weight: bold;">{data['job']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info(f"💡 {selected_mbti} 친구들은 주로 이런 환경에서 능력을 잘 발휘한답니다! 여러분의 꿈을 응원해요!")

# 사이드바
st.sidebar.header("🧭 진로 탐색 가이드")
st.sidebar.write("1. 자신의 MBTI를 선택하세요.")
st.sidebar.write("2. 추천 직업을 확인하세요.")
st.sidebar.write("3. 해당 직업이 나에게 맞는지 고민해보세요!")
st.sidebar.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-1.2.1&auto=format&fit=crop&w=300&q=80")
