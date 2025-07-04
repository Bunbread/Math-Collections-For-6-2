import math
from Fraction_class import *

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

def add_sub_steps(f1, f2, operator, n):
    steps = []
    steps.append(f"{n}. {f1} {operator} {f2}")

    a1, b1 = f1.to_improper()
    a2, b2 = f2.to_improper()

    ff1 = F(0, a1, b1)
    ff2 = F(0, a2, b2)
    steps.append(f"วิธีทำ {f1} {operator} {f2} = {ff1} {operator} {ff2}")
    lcms = math.lcm(f1.denominator, f2.denominator)
    steps.append(f"     ค.ร.น. ของ {f1.denominator}, {f2.denominator} คือ {lcms}")

    ff1_target = get_target(ff1.denominator, lcms)
    ff2_target = get_target(ff2.denominator, lcms)
    steps.append(f"     {ff1} {operator} {ff2} = ({ff1} x {ff1_target}/{ff1_target}) {operator} ({ff2} x {ff2_target}/{ff2_target})")

    nf1 = F(0, ff1.numerator * ff1_target, ff1.denominator * ff1_target)
    nf2 = F(0, ff2.numerator * ff2_target, ff2.denominator * ff2_target)

    steps.append(f"                 = {nf1} {operator} {nf2}")
    if operator == '+':
        bn = F(0, nf1.numerator + nf2.numerator, nf1.denominator)
        steps.append(f"                 = {bn}")
        steps.append(f"                 = {bn.to_mixed()}")
    else:
        bn = F(0, nf1.numerator - nf2.numerator, nf1.denominator)
        steps.append(f"                 = {bn}")
        steps.append(f"                 = {bn.to_mixed()}")
    if steps[len(steps) - 1] == steps[len(steps) - 2]:
        del steps[len(steps) - 1]
    
    steps.append(f"ดังนั้น {f1} {operator} {f2} = {bn}")
    steps.append(f"ตอบ {bn}")

    return steps

questions_list = [
    [F(0, 1,6), F(0, 2,5), '+'],
    [F(0,3,8), F(0,1,3), '+'],
    [F(0,1,12), F(0,2,7), '+'],
    [F(0,30,7), F(0,1,6), '+'],
    [F(0,3,4), F(0,1,8), '+'],
    [F(0,1,10), F(0,9,15), '+'],
    [F(0,11,12), F(0,1,9), '+'],
    [F(0,5,7), F(0,7,18), '-'],
    [F(0,8,15), F(0,1,4), '-'],
    [F(0,7,6), F(0,3,4), '-'],
    [F(0,21,5), F(0,6,12), '-'],
    [F(0,3,2), F(0,11,21), '-'],
    [F(0,5,6), F(0,8,15), '-'],
    [F(0,13,8), F(0,9,14), '-'],
    [F(0,7,15), F(0,2,9), '-'],
    [F(0,6,10), F(0,1,3), '-'],
]

x = 1
for j in questions_list:
    for i in add_sub_steps(*j, x):
        print(i)
    x += 1
    print("------------------")