import streamlit as st

st.title("나의 첫 웹앱")
st.info("파이썬으로 제작하는 UI")

col1, col2 = st.columns(2)

with col1:
    st.success("왼쪽 영역")
with col2:
    st.write("오른쪽 영역")

# 새로고침 시 데이터 유지
if "user_list" not in st.session_state:
    st.session_state.user_list = []

with st.form("input_form"):
    name = st.text_input("이름")
    if st.form_submit_button("등록") and name:
        st.session_state.user_list.append(name)

tasks = [
    "1. API 스펙 문서 작성",
    "2. 프론트엔드 컴포넌트 개발",
    "3. 배포 파이프라인(CI/CD) 구축"
]

st.subheader(" 금일 할 일 목록")

for task in tasks:

    # border=True를 주면 각 반복 요소가 단정한 상자로 감싸 집니다.
    with st.container(border=True):

        st.write(task)

