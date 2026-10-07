import streamlit as st

# 페이지 제목 설정

st.title("나의 첫 Streamlit 앱")


# 텍스트 출력

st.write("Streamlit을 이용해 만든 웹 애플리케이션입니다.")


# 사용자 입력 받기

name = st.text_input("이름을 입력하세요:")


# 버튼 클릭 이벤트

if st.button("인사하기"):

    if name:

        st.success(f"안녕하세요, {name}님!")

    else:

        st.warning("이름을 입력해주세요.")

