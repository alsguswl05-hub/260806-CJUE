import streamlit as st

st.title("👋 안녕하세요!")

st.header("간단한 자기소개")

st.write("제가 만든 페이지에 오신 것을 환영합니다.")

st.markdown(
    """
- 이름: 민현지
- 직업: 학생
- 과: 미술교육과
- 목표: 다이어트 하기, 독서 하기
- 취미: 넷플릭스 보기, 음악 듣기

"""
)

st.subheader("추가로 하고 싶은 말")
st.write(
    "집가서 넷플릭스 보고싶어요!"
)
