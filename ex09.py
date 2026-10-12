import streamlit as st

# 페이지 제목 설정
st.title("일단 제목")

# 사용자 확인

with st.form("input_form"):
    name = st.text_input("이름을 입력하세요:")
    asd = st.form_submit_button("확인하기")

    if asd:
        if name:
            st.success(f"{name}님 확인 되었습니다.")
        else:
            st.warning("이름")

col1, col2 = st.columns(2)
with col1:

    st.subheader("오늘 할 일 목록")

    day1 = [
        "1. 파이썬 선 수업",
        "2. 헬스장",
        "3. 야구 경기",
        "4. 휴식"
    ]

    for day in day1:
        with st.container(border=True):
            st.write(day)
with col2:

    st.subheader("내일 할 일 목록")
    day2 = [
        "1. 헬스장",
        "2. 휴식"
    ]
    for day in day2:
        with st.container(border=True):
            st.write(day)
col3, col4 = st.columns(2)
with col3:
    st.subheader("오늘 야구 일정")
with col4:
    st.subheader("시작시간 18시 30분")
kbo = [
    "LG vs KIA",
    "롯데 vs 두산 ",
    "KT vs 삼성"
]
for kbos in kbo:
    with st.container(border=True):
        st.write(kbos)