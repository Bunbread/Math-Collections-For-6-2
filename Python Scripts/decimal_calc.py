questions = [
    "(3.85 + (157 / 100)) - 4.95",
    "15 * 125.25",
    "116.784 / 3",
    "55.25 / 5",
    "5000 + (1668.25 * 12)",
    "381 / 12",
    "(256.82 + 341.26) / 3",
    "(856.98 - 660.42) / 4",
    "(2.6 + 3.72) * 180",
    "5368.25 - 459.75"
]

def bq(q):
    result = q.replace("/", "÷").replace("*", "x")
    return f"{result} = []"

for i,q in enumerate(questions, 1):
    print(f"ข้อ {i}")
    qq = bq(q)
    print(f"ประโยคสัญลักษณ์ {qq}")
    print(f"ตอบ {round(eval(q), 3)}")
    print("--------------")
