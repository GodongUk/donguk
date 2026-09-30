print("== 함수 재사용 ==")

def calculate_stats(score_list):
    total = sum(score_list)
    avg = total / len(score_list)
    return total, avg

sc = [90, 80, 87]
total, avg = calculate_stats(sc)
print(f"총점: {total}, 평균: {avg:.2f}")