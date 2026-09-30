print("== 조건문 & 반복문 ==")
students = [{"name": "철수", "score": 85},{"name": "영희", "score": 55} ]

for s in students:
    if s["score"] >= 60:
        result = "합격"
    else:
        result = "재시험"
    print(f"{s['name']}: {result}({s['score']}점)")