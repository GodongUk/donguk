import streamlit as st

st.title("메인 제목")
st.info("파란색 알림 박스")
st.success("초록색 성공 메시지")

col1, col2 = st.columns(2)

# 데이터 입력
name = st.text_input("이름:")
btn = st.button("클릭")

# 폼 입력 & 상태 관리
with st.form("my_from"):
    submit = st.form_submit_button("전송")

st.session_state.login = True

