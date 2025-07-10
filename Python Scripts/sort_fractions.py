from fractions import Fraction
import math

def get_target(n, target):
    multiplier = 1
    while True:
        if n * multiplier == target:
            break
        else:
            multiplier += 1
    return n, multiplier

def get_denominators(*args):
    fracs = [Fraction(str(a)) for a in args]
    denoms = [f.denominator for f in fracs]
    return denoms

def convert_fractostr(f):
    return f"{f.numerator}/{f.denominator}"


def sort_fractions_steps_lth(*f):
    steps = []
    fractions = [Fraction(str(x)) for x in f]
    steps.append(f"{', '.join(f)} จงเรียงเศษส่วนจากน้อยไปมาก")
    
    denoms = [frac.denominator for frac in fractions]
    lcm = math.lcm(*denoms)
    steps.append(f"วิธีทำ ค.ร.น. ของ {', '.join(str(d) for d in denoms)} คือ {lcm}")
    
    converted = []
    for frac in fractions:
        multiplier = lcm // frac.denominator
        new_num = frac.numerator * multiplier
        steps.append(f"     {convert_fractostr(frac)} = {frac.numerator} x {multiplier}/{frac.denominator} x {multiplier} = {new_num}/{lcm}")
        converted.append((frac, Fraction(new_num, lcm)))  # (original, converted)

    # Sort by converted value
    converted.sort(key=lambda x: x[1])

    # Show sorted list in same-denominator form
    sorted_converted_strs = [convert_fractostr(c[1]) for c in converted]
    steps.append(f"จะได้ {', '.join(sorted_converted_strs)}")

    # Then show sorted original fractions
    sorted_original_strs = [convert_fractostr(c[0]) for c in converted]
    steps.append(f"ตอบ {', '.join(sorted_original_strs)}")

    return steps

def sort_fractions_steps_htl(*f):
    steps = []
    fractions = [Fraction(str(x)) for x in f]
    steps.append(f"{', '.join(f)} จงเรียงเศษส่วนจากน้อยไปมาก")

    # Get denominators and LCM
    denoms = [frac.denominator for frac in fractions]
    lcm = math.lcm(*denoms)
    steps.append(f"วิธีทำ ค.ร.น. ของ {', '.join(str(d) for d in denoms)} คือ {lcm}")
    
    converted = []
    # Show conversion step for each fraction
    for frac in fractions:
        multiplier = lcm // frac.denominator
        new_num = frac.numerator * multiplier
        steps.append(f"     {frac} = {frac.numerator} x {multiplier}/{frac.denominator} x {multiplier} = {new_num}/{lcm}")
        converted.append((frac, Fraction(new_num, lcm)))
    
    # Sort by converted value
    converted.sort(key=lambda x: x[1], reverse=True)
    
    # Show sorted fractions by original form
    sorted_str = ", ".join(str(orig) for orig, _ in converted)
    steps.append(f"จะได้ (ไปหาเอาเอง)")
    steps.append(f"ตอบ {sorted_str}")

    return steps

lth = [
    ["4/9", "1/3", "5/6"],
    ["5/7", "5/6", "1/2", "2/3"],
    ["7/10", "3/5", "1/4", "2/2"],
    ["11/16", "1/3", "5/6"],
]

htl = [
    ["8/9", "2/3", "11/18"],
    ["5/6", "2/3", "3/8", "1/2"],
    ["1/3", "5/12", "11/18", "4/9"],
    ["3/25", "2/5", "7/10", "1/15"],
]

print("จากน้อยไปมาก\n")

x = 1
for j in lth:
    print(f"{x}. ")
    for i in sort_fractions_steps_lth(*j):
        print(i)
    print("-------------------------")
    x += 1
x = 1
print("-------------------------")
print("จากมากไปน้อย\n")

for j in htl:
    print(f"{x}.")
    for i in sort_fractions_steps_htl(*j):
        print(i)
    print("-------------------------")
    x += 1
