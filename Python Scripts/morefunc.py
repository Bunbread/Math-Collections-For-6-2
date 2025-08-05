def convert_to_thai_number(number):
    """
    Convert any number (int, float, or comma-separated) to Thai digits.
    """
    arabic_to_thai = {
        '0': '๐', '1': '๑', '2': '๒', '3': '๓', '4': '๔',
        '5': '๕', '6': '๖', '7': '๗', '8': '๘', '9': '๙',
        '.': '.', ',': ',', '-': '-'
    }
    return ''.join(arabic_to_thai.get(ch, ch) for ch in str(number))

def smart_format(n):
    return int(n) if isinstance(n, float) and n.is_integer() else n

def answer(n):
    return convert_to_thai_number(smart_format(n))