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
        multiplied_f = f * NF(0, mul, mul)
        steps.append(f"วิธีทำ {f} = {f} x {mul}/{mul}")
    else:
        # Fraction needs simplifying
        mul = needed_multiplier(simplified_f.denominator)
        multiplied_f = simplified_f * NF(0, mul, mul)
        steps.append(f"วิธีทำ {f} = {f}")
        steps.append(f"{sp}= {simplified_f} x {mul}/{mul}")

    steps.append(f"{sp}= {multiplied_f}")
    steps.append(f"{sp}= {answer}")
    steps.append(f"ดังนั้น {f} = {answer}")
    steps.append(f"ตอบ {answer}")

    return steps

questions = [
    NF(0,6,50),
    NF(0,348,160),
    NF(0,304,16),
    NF(0,91,350),
    NF(0,232,200),
    NF(0,18,900),
    NF(0,77,125),
    NF(0,282,120),
    NF(0,343,140),
    NF(0,304,16)
]

for i, q in enumerate(questions, start=1):
    for l in to_num_steps(q, i):
        print(l)
    print("--------------")