from fractions import Fraction
import math

def get_target(n, target):
    multiplier = 1
    while True:
        if n * multiplier == target:
            break
        else:
            multiplier += 1
    return multiplier

def add_sub_steps(f1, f2, operator, n):
    steps = []
    if operator == '+':
        lcms = math.lcm(f1.denominator, f2.denominator)
        steps.append(f"{n}. {f1} + {f2}")
        steps.append(f"วิธีทำ ค.ร.น. ของ {f1.denominator}, {f2.denominator} คือ {lcms}")
        f1_target = get_target(f1.denominator, lcms)
        f2_target = get_target(f2.denominator, lcms)
        steps.append(f"     {f1} + {f2} = ({f1} x {f1_target}/{f1_target}) + ({f2} x {f2_target}/{f2_target})")
        steps.append(f"     = {f1.numerator * f1_target}/{f1.denominator * f1_target} + {f2.numerator * f2_target}/{f2.denominator * f2_target}")
        steps.append(f"     = {f1 + f2}")
        steps.append(f"ดังนั้น {f1} + {f2} = {f1 + f2}")
        steps.append(f"ตอบ {f1 + f2}")
    elif operator == '-':
        lcms = math.lcm(f1.denominator, f2.denominator)
        steps.append(f"{n}. {f1} + {f2}")
        steps.append(f"วิธีทำ ค.ร.น. ของ {f1.denominator}, {f2.denominator} คือ {lcms}")
        f1_target = get_target(f1.denominator, lcms)
        f2_target = get_target(f2.denominator, lcms)
        steps.append(f"     {f1} - {f2} = ({f1} x {f1_target}/{f1_target}) - ({f2} x {f2_target}/{f2_target})")
        steps.append(f"     = {f1.numerator * f1_target}/{f1.denominator * f1_target} - {f2.numerator * f2_target}/{f2.denominator * f2_target}")
        steps.append(f"     = {f1 - f2}")
        steps.append(f"ดังนั้น {f1} - {f2} = {f1 - f2}")
        steps.append(f"ตอบ {f1 - f2}")
    return steps

questions_list = [
    [Fraction(1,6), Fraction(2,5), '+'],
    [Fraction(3,8), Fraction(1,3), '+'],
    [Fraction(1,12), Fraction(2,7), '+'],
    [Fraction(30,7), Fraction(1,6), '+'],
    [Fraction(3,4), Fraction(1,8), '+'],
    [Fraction(1,10), Fraction(9,15), '+'],
    [Fraction(11,12), Fraction(1,9), '+'],
    [Fraction(5,7), Fraction(7,18), '-'],
    [Fraction(8,15), Fraction(1,4), '-'],
    [Fraction(7,6), Fraction(3,4), '-'],
    [Fraction(21,5), Fraction(6,12), '-'],
    [Fraction(3,2), Fraction(11,21), '-'],
    [Fraction(5,6), Fraction(8,15), '-'],
    [Fraction(13,8), Fraction(9,14), '-'],
    [Fraction(7,15), Fraction(2,9), '-'],
    [Fraction(6,10), Fraction(1,3), '-'],
]

x = 1
for j in questions_list:
    for i in add_sub_steps(*j, x):
        print(i)
    x += 1
    print("------------------")