from math import gcd

import math

def get_target(n, target):
    multiplier = 1
    while True:
        if n * multiplier == target:
            break
        else:
            multiplier += 1
    return multiplier

class F:
    def __init__(self, whole, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Idiot")
        self.whole = whole
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        if self.numerator == 0:
            return str(self.whole)  # Just whole number, no fraction
        elif self.denominator == 1:
            # If whole is zero, just print numerator (whole number)
            if self.whole == 0:
                return str(self.numerator)
            else:
                return str(self.whole + self.numerator)  # whole + numerator because denominator is 1
        elif self.whole != 0:
            return f"{self.whole} {self.numerator}/{self.denominator}"
        else:
            return f"{self.numerator}/{self.denominator}"
        
    def to_improper(self):
        return self.whole * self.denominator + self.numerator, self.denominator
    
    def to_improper_fraction(self):
        num = self.whole * self.denominator + self.numerator
        return F(0, num, self.denominator).simplify()

    def to_mixed(self):
        num = self.whole * self.denominator + self.numerator
        whole = num // self.denominator
        remainder = num % self.denominator
        return F(whole, remainder, self.denominator)

    def add(self, other):
        n1, d1 = self.to_improper()
        n2, d2 = other.to_improper()

        lcm = math.lcm(d1, d2)
        n1 *= lcm // d1
        n2 *= lcm // d2

        total_num = n1 + n2

        new_whole = total_num // lcm
        new_num = total_num % lcm

        if new_num != 0:
            common = gcd(new_num, lcm)
            new_num //= common
            lcm //= common
        else:
            lcm = 1

        return F(new_whole, new_num, lcm)

    def sub(self, other):
        # Convert to improper fractions
        n1, d1 = self.to_improper()
        n2, d2 = other.to_improper()

        # Get common denominator
        lcm = math.lcm(d1, d2)
        n1 *= lcm // d1
        n2 *= lcm // d2

        # Subtract numerators
        total_num = n1 - n2

        # Determine sign and convert back to mixed number
        sign = -1 if total_num < 0 else 1
        total_num = abs(total_num)

        new_whole = (total_num // lcm) * sign
        new_num = total_num % lcm

        # Simplify
        if new_num != 0:
            common = gcd(new_num, lcm)
            new_num //= common
            lcm //= common
        else:
            lcm = 1  # Clean display

        return F(new_whole, new_num, lcm)
    def simplify(self):
        num = self.whole * self.denominator + self.numerator
        den = self.denominator
        common = gcd(num, den)
        num //= common
        den //= common
        whole = num // den
        remainder = num % den
        return F(whole, remainder, den)
    def can_simplify(self):
        return gcd(self.numerator, self.denominator) > 1
        
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
    
    if bn.can_simplify():
        steps.append(f"                 = {bn.simplify()}")
    
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