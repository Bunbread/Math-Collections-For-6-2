from math import gcd
from fractions import Fraction

class RawFraction:
    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator
        self.value = Fraction(numerator, denominator)

    def __str__(self):
        return f"{self.n}/{self.d}"

    def scale(self, multiplier):
        return RawFraction(self.n * multiplier, self.d * multiplier)

    def to_mixed(self):
        whole = self.n // self.d
        remainder = self.n % self.d
        if remainder == 0:
            return f"{whole}"
        elif whole == 0:
            return f"{remainder}/{self.d}"
        else:
            return f"{whole} {remainder}/{self.d}"

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def to_improper(whole: int, frac: RawFraction):
    return RawFraction(whole * frac.d + frac.n, frac.d)

def add_sub_mixed(
    operands: list[tuple[int, RawFraction]],  # [(whole1, frac1), (whole2, frac2), ...]
    operator: str = '+'
):
    steps = []

    # 👁️ 1. Show the original mixed expression
    expression = f" {operator} ".join(f"{w} {f}" for w, f in operands)
    steps.append(expression)

    # 👁️ 2. Convert each mixed to improper
    impropers = [to_improper(w, f) for w, f in operands]
    improper_str = f" {operator} ".join(str(f) for f in impropers)
    steps.append(f"วิธีทำ {expression} = {improper_str}")

    # 🧠 3. Find LCM of all denominators
    all_denoms = [f.d for f in impropers]
    current_lcm = all_denoms[0]
    for d in all_denoms[1:]:
        current_lcm = lcm(current_lcm, d)
    steps.append(f"    ค.ร.น. ของ {', '.join(map(str, all_denoms))} คือ {current_lcm}")

    # 🧪 4. Scale each fraction
    scaled = []
    scale_steps = []
    for f in impropers:
        factor = current_lcm // f.d
        scaled_f = f.scale(factor)
        scaled.append(scaled_f)
        scale_steps.append(f"({f} x {factor}/{factor})")

    steps.append(f"    {improper_str} = " + f" {operator} ".join(scale_steps))
    steps.append("               = " + f" {operator} ".join(str(f) for f in scaled))

    # 🧾 5. Add or subtract numerators
    if operator == '+':
        result_num = sum(f.n for f in scaled)
    else:
        result_num = scaled[0].n
        for f in scaled[1:]:
            result_num -= f.n

    result = RawFraction(result_num, current_lcm)
    steps.append(f"               = {result}")
    steps.append(f"               = {result.to_mixed()}")
    steps.append(f"ดังนั้น {expression} = {result.to_mixed()}")
    steps.append(f"ตอบ {result.to_mixed()}")

    return steps

operands = [
    (2, RawFraction(5, 4)),  # 2 5/4
    (3, RawFraction(5, 3))   # 3 5/3
]
for line in add_sub_mixed(operands, '+'):
    print(line)