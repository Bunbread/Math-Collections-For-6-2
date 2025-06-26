import math, fractions

test = fractions.Fraction(26,20)

def is_prime(n):
    if n <= 1:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


def lowest_fractions_steps(f1, f2):
    # Make sure inputs are integers
    n = fractions.Fraction(int(f1), int(f2))
    temp_n = fractions.Fraction(n)  # Keep original for final line
    divisor = 2
    steps = [f"วิธีทำ {f1}/{f2} = {f1}/{f2}"]  # Start with original inputs (before simplification)

    while divisor <= min(n.numerator, n.denominator):
        if n.numerator % divisor == 0 and n.denominator % divisor == 0:
            n = fractions.Fraction(n.numerator // divisor, n.denominator // divisor)
            steps.append(f"           = {n}")
        else:
            divisor += 1

    if len(steps) == 1:
        steps.append(f"           = {n}")

    steps.append(f"ดังนั้น {f1}/{f2} = {n}")
    steps.append(f"ตอบ {n}")
    return steps


questions = [["26", "20"],
            ["14", "14"], 
            ["55", "15"], 
            ["9", "18"],
            ["15", "18"],
            ["20", "48"],
            ["12", "33"],
            ["35", "20"],
            ["56", "232"],
            ["186", "216"],
            ["54", "117"],
            ["63", "189"],
            ["81", "108"],
            ["105", "225"],
            ["224", "154"]]

x = 1
for i in questions:
    print("-------------")
    print(f"{x}. {'/'.join(i)}")
    x +=1 
    for line in lowest_fractions_steps(*i):
        print(line)
