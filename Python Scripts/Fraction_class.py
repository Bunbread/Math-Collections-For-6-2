from math import gcd, lcm
import math

def get_target(n, target):
    return target / n
    
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
    
    def to_mixed_able(self):
        mixed = self.to_mixed()
        if mixed == self:
            return False
        else:
            return True

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

class NF:
    def __init__(self, whole, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Idiot")
        self.whole = whole
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        if self.numerator == 0:
            return str(self.whole)
        elif self.denominator == 1:
            return str(self.whole + self.numerator)
        elif self.whole != 0:
            return f"{self.whole} {self.numerator}/{self.denominator}"
        else:
            return f"{self.numerator}/{self.denominator}"
    def to_improper(self):
        return NF(0, self.whole * self.denominator + self.numerator, self.denominator)
    def __add__(self, other):
        lcms = lcm(self.denominator, other.denominator)

        self_mul = lcms // self.denominator
        other_mul = lcms // other.denominator

        t1 = NF(self.whole, self.numerator * self_mul, self.denominator * self_mul).to_improper()
        t2 = NF(other.whole, other.numerator * other_mul, other.denominator * other_mul).to_improper()

        return NF(0, t1.numerator + t2.numerator, t1.denominator)
    def __sub__(self, other):
        lcms = lcm(self.denominator, other.denominator)

        self_mul = lcms // self.denominator
        other_mul = lcms // other.denominator

        t1 = NF(self.whole, self.numerator * self_mul, self.denominator * self_mul).to_improper()
        t2 = NF(other.whole, other.numerator * other_mul, other.denominator * other_mul).to_improper()

        return NF(0, t1.numerator - t2.numerator, t1.denominator)
    def simplify(self):
        common = gcd(self.numerator, self.denominator)
        n1 = self.numerator // common
        n2 = self.denominator // common
        return NF(self.whole, n1, n2)
    def to_mixed(self):
        if self.numerator < self.denominator:
            return self 

        total = self.numerator
        whole = total // self.denominator
        remainder = total % self.denominator
        return NF(self.whole + whole, remainder, self.denominator) # hi