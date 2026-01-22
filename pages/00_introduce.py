import streamlit as st
from PIL import Image

# 1. 페이지 설정
st.set_page_config(page_title="내 자기소개 페이지", page_icon="👋", layout="centered")

# 2. 사이드바 구성 (연락처 등)
with st.sidebar:
    st.header("Contact Me")
    st.write("📧 Email: your_email@example.com")
    st.write("🔗 [GitHub](https://github.com/yourid)")
    st.write("📝 [Blog](https://yourblog.com)")

# 3. 메인 섹션 - 인사말 및 사진
col1, col2 = st.columns([1, 2], gap="medium")

with col1:
    # 본인의 사진 파일 경로를 넣으세요. (예: 'profile.jpg')
    # 파일이 없다면 샘플 이미지가 표시됩니다.
    try:
        image = Image.open('profile.jpg')
        st.image(image, use_container_width=True)
    except:
        st.image("https://via.placeholder.com/150", caption="내 사진")

with col2:
    st.title("안녕하세요, 홍길동입니다! 👋")
    st.write("""
    데이터를 통해 세상의 문제를 해결하고 싶은 **데이터 분석가/개발자**입니다. 
    새로운 기술을 배우는 것을 즐기며, 협업과 공유의 가치를 소중히 여깁니다.
    """)
    st.button("이력서 다운로드")

st.divider()

# 4. 상세 정보 섹션 (Tabs 활용)
tab1, tab2, tab3 = st.tabs(["💻 기술 스택", "📊 프로젝트", "🎓 학력/경력"])

with tab1:
    st.subheader("Technical Skills")
    st.write("**Languages:** Python, SQL, JavaScript")
    st.write("**Frameworks:** Streamlit, FastAPI, React")
    st.write("**Tools:** Docker, Git, AWS")

with tab2:
    st.subheader("Key Projects")
    st.info("**1. 실시간 데이터 대시보드 구축**")
    st.write("- Streamlit과 API를 연동하여 실시간 주식 데이터를 시각화함.")
    st.info("**2. 개인 블로그 자동화 봇**")
    st.write("- Python을 이용해 뉴스 데이터를 수집하고 요약하여 업로드하는 시스템 구축.")

with tab3:
    st.subheader("Experience")
    st.write("- **ABC 테크**: 데이터 분석 인턴 (2023.01 ~ 2023.06)")
    st.write("- **한국대학교**: 컴퓨터공학 전공 (2018.03 ~ 2024.02)")

# 5. 하단 방명록 섹션 (간단한 인터랙션)
st.divider()
st.subheader("💬 응원의 한마디")
name = st.text_input("성함")
message = st.text_area("메시지")
if st.button("보내기"):
    st.success(f"{name}님, 소중한 의견 감사합니다!")
