from Fraction_class import NF
questions = [
    "NF(0,8,15)*NF(0,5,2)+(NF(1,5,6) + NF(0,17,9))",
    "NF(0,7,15)/NF(0,7,10)-NF(0,8,12)*NF(0,5,16)",
    "NF(0,8,1)-(NF(1,3,15)-NF(1,1,16)*NF(0,4,5))",
    "NF(7,5,12)-NF(3,5,8)*NF(2,4,5)/NF(6,3,10)",
    "((NF(2,3,8)+NF(0,14,63)/NF(0,16,21)))*NF(0,21,32)"
]

for i, question in enumerate(questions, 1):
    answer = eval(question, {"NF": NF}).simplify().to_mixed()
    print(f"{i}. {answer}")