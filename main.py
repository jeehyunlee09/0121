import streamlit as st

# 1. 페이지 설정 (가장 상단에 위치해야 합니다)
st.set_page_config(
    page_title="✨ 내 미래를 찾아줘! MBTI 진로 탐색 ✨",
    page_icon="🚀",
    layout="wide"
)

# 2. 커스텀 스타일 (CSS로 폰트와 배경색 살짝 꾸미기)
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
    }
    .mbti-card {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 데이터 정의 (MBTI별 특징 및 추천 직업)
mbti_data = {
    "ISTJ": {"emoji": "📏", "desc": "청렴결백한 논리주의자", "jobs": ["회계사", "공무원", "데이터 분석가", "사서"]},
    "ISFJ": {"emoji": "🛡️", "desc": "용감한 수호자", "jobs": ["간호사", "초등교사", "사회복지사", "인사 담당자"]},
    "INFJ": {"emoji": "🔮", "desc": "선의의 옹호자", "jobs": ["상담심리사", "작가", "환경 운동가", "예술가"]},
    "INTJ": {"emoji": "🧠", "desc": "용의주도한 전략가", "jobs": ["소프트웨어 개발자", "과학자", "경영 컨설턴트", "건축가"]},
    "ISTP": {"emoji": "🛠️", "desc": "만능 재주꾼", "jobs": ["엔지니어", "파일럿", "응급구조사", "카레이서"]},
    "ISFP": {"emoji": "🎨", "desc": "호기심 많은 예술가", "jobs": ["디자이너", "작곡가", "수의사", "플로리스트"]},
    "INFP": {"emoji": "🧚", "desc": "열정적인 중재자", "jobs": ["에디터", "상담가", "인권 운동가", "일러스트레이터"]},
    "INTP": {"emoji": "🧪", "desc": "논리적인 사색가", "jobs": ["철학자", "프로그래머", "수학자", "전략기획자"]},
    "ESTP": {"emoji": "⚡", "desc": "모험을 즐기는 사업가", "jobs": ["기업가", "마케터", "스포츠 에이전트", "기자"]},
    "ESFP": {"emoji": "🎉", "desc": "자유로운 영혼의 연예인", "jobs": ["연예인", "이벤트 플래너", "승무원", "홍보 전문가"]},
    "ENFP": {"emoji": "🌈", "desc": "재기발랄한 활동가", "jobs": ["광고 제작자", "유튜버", "심리치료사", "카피라이터"]},
    "ENTP": {"emoji": "💡", "desc": "뜨거운 논쟁을 즐기는 변론가", "jobs": ["변호사", "광고 기획자", "정치인", "스타트업 창업자"]},
    "ESTJ": {"emoji": "📋", "desc": "엄격한 관리자", "jobs": ["경영자", "은행원", "프로젝트 매니저", "군교관"]},
    "ESFJ": {"emoji": "🤝", "desc": "사교적인 외교관", "jobs": ["호텔리어", "승무원", "홍보부서", "의료 코디네이터"]},
    "ENFJ": {"emoji": "🌟", "desc": "정의로운 사회운동가", "jobs": ["비영리단체 리더", "코치", "아나운서", "정치학자"]},
    "ENTJ": {"emoji": "👑", "desc": "대담한 통솔자", "jobs": ["CEO", "변호사", "대학 교수", "경제 분석가"]},
}

# 4. 사이드바 구성
with st.sidebar:
    st.title("⚙️ 설정 및 메뉴")
    st.info("당신의 MBTI를 선택하고 어울리는 직업의 세계를 탐험해보세요!")
    st.divider()
    st.write("📌 **진로 상담 문의:** help@mbti-edu.com")

# 5. 메인 화면 구성
st.title("🌈 내 MBTI에 딱 맞는 직업은?")
st.subheader("흥미로운 성격 유형별 진로 탐색 가이드 🚀")
st.write("---")

# 드롭다운 선택
option = st.selectbox(
    "나의 MBTI를 선택해주세요 👇",
    list(mbti_data.keys()),
    index=None,
    placeholder="선택하기..."
)

# 결과 표시 섹션
if option:
    data = mbti_data[option]
    
    # 두 개의 컬럼으로 나누기
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"<h1 style='text-align: center; font-size: 100px;'>{data['emoji']}</h1>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center;'>{option}</h2>", unsafe_allow_html=True)
    
    with col2:
        st.success(f"### **{data['desc']}**")
        st.write("당신의 성격과 가치관에 비추어 보았을 때, 다음과 같은 직업군에서 큰 보람을 느낄 가능성이 높아요!")
        
        # 추천 직업 리스트 출력
        st.write("#### 🎯 추천 직업 리스트:")
        for job in data['jobs']:
            st.write(f"- {job}")

    st.divider()
    
    # 추가 교육 메시지
    st.info(f"💡 **팁:** {option} 유형은 주로 {data['desc']}라는 특징이 있어요. 하지만 MBTI는 참고용일 뿐, 여러분의 열정이 가장 중요합니다!")
    
    # 풍선 효과! (화려함 추가)
    st.balloons()

else:
    st.warning("위의 드롭다운에서 MBTI를 선택하면 화려한 결과가 나타납니다! ✨")

# 6. 하단 푸터
st.markdown("---")
st.caption("© 2026 MBTI Career Education Center. All rights reserved.")
