from Fraction_class import NF
from math import gcd


def decimal_to_NF(value: float) -> NF:
    s = str(value)
    if '.' in s:
        integer_part, decimal_part = s.split('.')
        numerator = int(integer_part + decimal_part)
        denominator = 10 ** len(decimal_part)
    else:
        numerator = int(s)
        denominator = 1

    sign = 0
    if numerator < 0:
        sign = 1
        numerator = -numerator

    return NF(sign, numerator, denominator)

# cross-simplify เศษส่วนสองตัว
def double_simplify(f1: NF, f2: NF):
    g1 = gcd(f1.numerator, f2.denominator)
    g2 = gcd(f1.denominator, f2.numerator)

    sf1 = NF(0, f1.numerator // g1, f1.denominator // g2)
    sf2 = NF(0, f2.numerator // g2, f2.denominator // g1)
    return sf1, sf2

def betterDenom(f):
    denom = f.denominator
    nume = f.numerator
    valid = [10,100,1000]
    multiplier = 1
    while True:
        if denom * multiplier in valid:
            return NF(0, nume*multiplier, denom*multiplier)
        else:
            multiplier+=1
# สร้างขั้นตอนหาร พร้อมแสดงผลลัพธ์เป็น decimal (ทศนิยม)
sp = " " * 16
def divideSteps(n,d,x: int):
    steps = []
    answer = round(n / d, 3)  # decimal answer here

    nD = decimal_to_NF(n)
    dD = decimal_to_NF(d)
    RdD = NF(0, dD.denominator, dD.numerator)  # สลับเศษส่วนตัวหาร (reciprocal)

    SnD, SRdD = double_simplify(nD, RdD)
    Mfraction = SnD * SRdD

    steps.append(f"{x}. {n} ÷ {d}")
    steps.append(f"วิธีทำ {n} ÷ {d} = {nD} ÷ {dD}")
    steps.append(f"{sp}= {nD} x {RdD}")

    # แสดงเฉพาะถ้ามีการย่อเศษส่วนจริง ๆ
    if (SnD != nD) or (SRdD != RdD):
        steps.append(f"{sp}= {SnD} x {SRdD}")

    steps.append(f"{sp}= {Mfraction}")
    steps.append(f"{sp}= {betterDenom(Mfraction)}")
    if steps[-1] == steps[-2]:
        steps.pop()
    steps.append(f"{sp}= {answer}")  # final decimal answer
    steps.append(f"ดังนั้น {n} ÷ {d} = {answer}")
    steps.append(f"ตอบ {answer}")
    return steps

questions = [
    [9.95, 3.98],
    [22.842, 1.296],
    [56.94, 60],
    [38, 30.4],
    [97.23,1.5],
    [62.203, 8.5],
    [54.91,2.5],
    [91,5.2],
    [36,22.5],
    [56.2,4],
    [59.21,2.5],
    [40,12.5]
]
for i, q in enumerate(questions, 1):
    for line in divideSteps(q[0], q[1], i):
        print(line)
    print("---------")
