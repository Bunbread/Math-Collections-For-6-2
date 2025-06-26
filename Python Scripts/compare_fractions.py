import math
from fractions import Fraction

def compare_fractions_steps(f1,f2):
    steps = []
    if f1 > f2:
        steps.append(f"{f1} > {f2}")
    elif f1 < f2:
        steps.append(f"{f1} < {f2}")
    else:
        steps.append(f"{f1} = {f2}")
    steps.append(f"วิธีทำ {f1} {f2}")
    steps.append(f"      {f1.numerator * f2.denominator} {f2.numerator * f1.denominator}")
    return steps

def compare_fractions(f1,f2):
    steps = ""
    if f1 > f2:
        steps = f">"
    elif f1 < f2:
        steps = f"<"
    else:
        steps = f"="
    return steps

questions_list = [
    [Fraction(5,8), Fraction(3,4)],
    [Fraction(1) + Fraction(1,2), Fraction(1) + Fraction(2,5)],
    [Fraction(10, 12), Fraction(5,6)],
    [Fraction(8,11), Fraction(9,16)],
    [Fraction(14,15), Fraction(17,12)],
    [Fraction(39,21), Fraction(13,7)],
    [Fraction(28, 19), Fraction(25, 16)],
]

x = 1
for i in questions_list:
    print(f"{x}. {compare_fractions(*i)}")
    x+=1