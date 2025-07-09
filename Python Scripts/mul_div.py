from Fraction_class import *

def mdsteps(f1, f2, o, x):
    steps = []
    steps.append(f"{x}. {f1} {o} {f2}")

    if1 = f1.to_improper()
    if2 = f2.to_improper()
    
    steps.append(f"วิธีทำ {f1} {o} {f2} = {if1} {o} {if2}")

    sif1 = if1.simplify()
    sif2 = if2.simplify()

    if o == 'x':
        steps.append(f"                    = {sif1} x {sif2}")

        mresult = sif1 * sif2
        mrs = mresult.simplify()

        steps.append(f"                    = {mresult}")
        steps.append(f"                    = {mrs}")
        mmrs = mrs.to_mixed()

        steps.append(f"                    = {mmrs}")
        if steps[len(steps) - 1] == steps[len(steps) - 2]:
            steps.pop()
    else:
        sifs2s = NF(0, sif2.denominator, sif2.numerator)
        steps.append(f"                    = {if1} x {sifs2s}")
        steps.append(f"                    = {sif1} x {sifs2s}")
        if steps[len(steps) - 1] == steps[len(steps) - 2]:
            steps.pop()

        mresult = sif1 * sifs2s
        mrs = mresult.simplify()

        steps.append(f"                    = {mresult}")
        steps.append(f"                    = {mrs}")
        

        mmrs = mrs.to_mixed()
        mmrss = mmrs.simplify()

        steps.append(f"                    = {mmrs}")
        if steps[len(steps) - 1] == steps[len(steps) - 2]:
            steps.pop()
    
    steps.append(f"ดังนั้น {f1} {o} {f2} = {mmrs}")
    steps.append(f"ตอบ {mmrs}")
    return steps

questions = [
    [NF(3,3,14), NF(0, 64,49), '/'],
    [NF(0,18,22), NF(0,33,27), 'x'],
    [NF(0,6,35), NF(0,36,50), '/'],
    [NF(0,90,120), NF(0, 81,1), '/'],
    [NF(2,3,4), NF(0, 16,30), 'x'],
    [NF(5,1,7), NF(0, 9,1), '/'],
    [NF(0,25,1), NF(0, 46,150), 'x'],
    [NF(1,7,13), NF(0, 50,39), '/'],
    [NF(0,30,32), NF(10, 4,6), 'x'],
    [NF(10,1,3), NF(0, 18,62), 'x'],
]
x = 1
for i in questions:
    print(*mdsteps(*i, x), sep='\n')
    x += 1
    print("---------------")