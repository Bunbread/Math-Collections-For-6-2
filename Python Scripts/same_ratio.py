def how(n1, n2):
    sp = " "*10
    sp2 = " "*5
    steps = []
    steps.append(f"วิธีทำ {n1}:{n2} = {n1} x 2:{n2} x 2")
    r1 = f"{n1*2}:{n2*2}"
    steps.append(f"{sp}= {r1}")
    steps.append(f"{sp2}{n1}:{n2} = {n1} x 3:{n2} x 3")
    r2 = f"{n1*3}:{n2*3}"
    steps.append(f"{sp}= {r2}")
    steps.append(f"{sp2}{n1}:{n2} = {n1} x 4:{n2} x 4")
    r3 = f"{n1*4}:{n2*4}"
    steps.append(f"{sp}= {r3}")

    steps.append(f"ดังนั้น {n1}:{n2} = {r1} = {r2} = {r3}")
    steps.append(f"ตอบ {r1} และ {r2} และ {r3}")
    return steps

questions = [
    [80,105],
    [36,40],
    [270,90],
    [38,30],
    [224,152],
    [240,32],
    [6,12],
    [5,20],
    [20,18],
    [60,132],
    [16,4],
    [24,26],
    [6,18],
    [27,21],
    [18,54],
    [42,60]
]

for i,q in enumerate(questions, start=1):
    print(f"{i}.")
    print(*how(q[0], q[1]), sep="\n")
    print("--------------------")

