from Fraction_class import NF
import re


def pretty_expression(expr: str) -> str:
    # Tokenize everything including NF(...) and math symbols
    tokens = re.findall(r'NF\(\d+,\d+,\d+\)|[()+\-*/]', expr)
    
    # Replace NF(...) with evaluated version using your class
    def nf_eval(token):
        if token.startswith("NF"):
            numbers = list(map(int, re.findall(r'\d+', token)))
            return str(NF(*numbers))
        return token

    replaced_tokens = [nf_eval(tok) for tok in tokens]

    # Replace only top-level math symbols (not inside NF)
    pretty_tokens = []
    for tok in replaced_tokens:
        if tok == '/':
            pretty_tokens.append('÷')
        elif tok == '*':
            pretty_tokens.append('×')
        else:
            pretty_tokens.append(tok)

    # Join all tokens with spaces for clarity
    return ' '.join(pretty_tokens)


questions = [
    "NF(0,150,1) - (NF(50,18,25) + NF(25,6,75))",
    "NF(0,57,1) * NF(5,8,19)",
    "NF(80,5,6) / NF(5,7,18)",
    "NF(145,11,30) / NF(20,23,30)",
    "(NF(0,15,1) - NF(3,3,4)) / NF(7,7,8)",
    "(NF(12,1,9) * NF(0,18,1)) + (NF(7,1,20) * NF(0,40,1))",
    "NF(163,4,5) - NF(155,5,9)",
    "NF(1,11,13) + NF(2,7,8)"
]

for i, question in enumerate(questions, 2):
    answer = eval(question, {"NF": NF}).simplify().to_mixed()
    print(f"ข้อ {i}")
    print(f"ประโยคสัญลักษณ์ {pretty_expression(question)} = []")
    print(f"ตอบ {answer}")
    print("-----------------------")