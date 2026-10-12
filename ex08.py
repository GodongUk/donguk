import streamlit as st

# 페이지 제목 설정

st.title("KBO 순위 목록")

# 텍스트 출력

st.write("sasasasa")

col1, col2, col3 = st.columns(3)

with col1:
    team = ["KT 위즈", "삼성라이온즈", "LG 트윈스", "KIA 타이거즈", "두산 베어스", "NC 다이노스", "SSG 랜더스", "롯데자이언츠", "한화 이글스", "키움 히어로즈"]
    st.success("팀 명")
with col2:
    ranking = [1,2,3,4,5,6,7,8,9,10]
    st.success("팀 순위")
    for rankings in ranking:
        st.write(rankings)
with col3:
    st.success("팀 승률")

