from morefunc import *

questions = [
    "(9.25 - 2.395) / 3",
    "(117.852 * 2000) / 4",
    "(4 * 1000) - (3500 - 398.50)",
    "15.68 + (15.68 * 1.2)",
    "((89.44 + 91.57) + 79) / 3",
    "30500 - (1500.75 * 4)",
    "8659.024 / 360.5",
    "800 - (5.75 * 67)",
    "35000.25 * 12",
    "2550 - 458.25"
]

def bq(q):
    result = q.replace("/", "÷").replace("*", "x")
    return f"{result} = []"

for i,q in enumerate(questions, 1):
    print(f"ข้อ {i}")
    qq = bq(q)
    print(f"ประโยคสัญลักษณ์ {qq}")
    print(f"ตอบ {convert_to_thai_number(f'{smart_format(round(eval(q), 3)):,}')}")
    print("--------------")
