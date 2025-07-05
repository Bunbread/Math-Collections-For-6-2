import math
from Fraction_class import *

def get_target(n, target):
    return target / n
        
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
    
    if bn.can_simplify():
        steps.append(f"                 = {bn.simplify()}")
        
    if steps[len(steps) - 1] == steps[len(steps) - 2]:
        del steps[len(steps) - 1]
    
    steps.append(f"ดังนั้น {f1} {operator} {f2} = {bn.simplify()}")
    steps.append(f"ตอบ {bn.simplify()}")


    return steps

questions = [
    [F(9,3,4), F(9,1,40), '+'],
    [F(6,19,40), F(4,7,24), '-'],
    [F(6,7,22), F(0,5,1), '-'],
    [F(5,7,9), F(3,1,5), '+'],
    [F(4,17,30), F(0,3,1), '-'],
    [F(12,9,10), F(9,3,8), '-'],
    [F(9,1,5), F(9,1,11), '+'],
    [F(0,5,4), F(0,11,6), '+'],
    [F(0,17,24), F(0,13,20), '-'],
    [F(0,48,48), F(0,4,1), '+'],
]

x = 1
for j in questions:
    for i in add_sub_steps(j[0], j[1], j[2], x):
        print(i)
    print("---------------")
    x += 1