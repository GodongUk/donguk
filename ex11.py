import json
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Firebase 중복 초기화 방지
if not firebase_admin._apps:
    key_string = st.secrets["firebase_key"]
    cred_dict = json.loads(key_string)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)
db = firestore.client()

# 1.입력 폼 만들기

with st.form("diary_input"):
    content = st.text_input("오늘의 일기")
    submit = st.form_submit_button("기록하기")

    if submit and content:
        db.collection("diary").add({"text": content, "date": "2026-10-14"})
        st.success("저장 완료!"); st.rerun()

# 2.목록 출력 및 삭제

docs = db.collection("diary").stream()
for doc in docs:
    col1, col2 = st.columns([8, 2])
    col1.info(doc.to_dict()["text"])
    if col2.button("삭제", key=doc.id):
        db.collection("diary").document(doc.id).delete()
        st.rerun()
    if "login" not in st.session_state: st.session_state["login"] = False

    if st.session_state["login"]:
        st.title("나만의 다이어리")
        if st.button("로그아웃"): st.session_state["login"] = False; st.rerun()
    else:
        tab1, tab2, tab3 = st.tabs(["로그인", "회원가입", "비밀번호 수정"])
        with tab1:
            l_id = st.text_input("아이디", key="l_id")
            l_pw = st.text_input("비번", type="password", key="l_pw")
            if st.button("로그인"):
                u = db.collection("users").document(l_id).get()
                if u.exists and u.to_dict()["password"] == l_pw:
                    st.session_state["login"] = True; st.rerun()
                else:
                    st.write("입력하신 비밀번호가 다릅니다.")
        with tab2:
            n_id = st.text_input("새 아이디", key="n_id")
            n_pw = st.text_input("새 비번", type="password", key="n_pw")
            if st.button("가입하기"):
                u = db.collection("users").document(n_id).get()
                if u.exists:
                    st.write("이미 있는 아이디입니다.")
                else:
                    db.collection("users").document(n_id).set({"password": n_pw})
                    st.success("회원가입 완료!")
        with tab3:
            l_id = st.text_input("아이디", key="l_id")
            l_pw = st.text_input("비번", type="password", key="l_pw")
            u_pw = st.text_input("새로운 비번", type="password", key="u_pw")
            if st.button("수정하기"):
                u = db.collection("users").document(l_id).get()

                if u.exists and u.to_dict()["password"] == l_pw:
                    db.collection("users").document(l_id).update({
                        "password" : u_pw
                    })
                    st.success("비번 변경 완료")
                else:
                    st.write("비번틀림")
                
