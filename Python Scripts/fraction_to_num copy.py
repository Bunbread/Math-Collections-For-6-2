from Fraction_class import NF

sp = " " * 13

def needed_multiplier(num):
    if num == 0:
        return -1

    for target in [10, 100, 1000]:
        multiplier = target / num
        if multiplier.is_integer(): 
            return int(multiplier)

    return round(1000 / num)

def to_num_steps(f, x):
    steps = []
    steps.append(f"{x}. {f}")
    answer = f.to_num()
    simplified_f = f.simplify()

    if simplified_f.numerator == f.numerator and simplified_f.denominator == f.denominator:
        # Fraction is already simplified
        mul = needed_multiplier(f.denominator)
        multiplied_f = NF(0, f.numerator, f.denominator) * NF(0, mul, mul)
        steps.append(f"วิธีทำ {f} = {f.whole} + ({f.numerator}/{f.denominator} x {mul}/{mul})")
    else:
        # Fraction needs simplifying
        mul = needed_multiplier(simplified_f.denominator)
        multiplied_f = NF(0, simplified_f.numerator, simplified_f.denominator) * NF(0, mul, mul)
        steps.append(f"วิธีทำ {f} = {f.whole} + {f.numerator}/{f.denominator}")
        steps.append(f"{sp}= {f.whole} + ({simplified_f.numerator}/{simplified_f.denominator} x {mul}/{mul})")

    steps.append(f"{sp}= {f.whole} + {multiplied_f}")
    steps.append(F"{sp}= {f.whole} + {multiplied_f.to_num()}")
    steps.append(f"{sp}= {answer}")
    steps.append(f"ดังนั้น {f} = {answer}")
    steps.append(f"ตอบ {answer}")

    return steps

questions = [
    NF(5,3,4),
    NF(9,11,20),
    NF(26,37,40),
    NF(67,48,75),
    NF(12,27,45),
    NF(36,13,65),
    NF(85,29,40),
    NF(99,68,85),
    NF(129,21,105),
    NF(91,57,152),
    NF(132,28,175),
    NF(171,184,460)
]

for i, q in enumerate(questions, start=1):
    for l in to_num_steps(q, i):
        print(l)
    print("--------------")