import math
from Fraction_class import *

def get_target(n, target):
    return target // n
        
def add_sub_steps(f1: NF, f2: NF, operator: str):
    steps = []

    # Convert to improper fractions
    t1 = f1.to_improper()
    t2 = f2.to_improper()

    # Find LCM of denominators
    lcms = lcm(t1.denominator, t2.denominator)

    # Find what to multiply numerator and denominator by to reach LCM
    t1_mul = lcms // t1.denominator
    t2_mul = lcms // t2.denominator

    # Step 1: Show multiplication to make common denominator
    steps.append(
        f"วิธีทำ {t1} {operator} {t2} = ({t1} x {t1_mul}/{t1_mul}) {operator} ({t2} x {t2_mul}/{t2_mul})"
    )

    # Step 2: Multiply to match denominators
    nf1 = NF(0, t1.numerator * t1_mul, t1.denominator * t1_mul)
    nf2 = NF(0, t2.numerator * t2_mul, t2.denominator * t2_mul)
    steps.append(f"= {nf1} {operator} {nf2}")

    # Step 3: Perform the operation
    if operator == '+':
        result = NF(0, nf1.numerator + nf2.numerator, nf1.denominator)
    else:
        result = NF(0, nf1.numerator - nf2.numerator, nf1.denominator)

    steps.append(f"= {result}")

    mixed = result.to_mixed()
    if str(result) != str(mixed):
        steps.append(f"= {mixed}")

    if result.simplify().to_mixed() != mixed:
        simplified = result.simplify()
        steps.append(f"          = {simplified.to_mixed()}")

    return steps


questions = [
    [NF(0,4,5), NF(0,3,15), '+'],
    [NF(0,5,8), NF(0,3,10), '-'],
    [NF(0,9,10), NF(0,2,3), '-'],
    [NF(0,1,8), NF(0,3,4), '+'],
    [NF(0,3,10), NF(0,1,4), '+'],
    [NF(0,3,4), NF(0,2,5), '-'],
]

x = 1
for j in questions:
    for i in add_sub_steps(j[0], j[1], j[2]):
        print(i)
    print("---------------")
    x += 1