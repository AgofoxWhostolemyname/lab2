import re

with open('currency.xml', 'r', encoding='windows-1251') as file:
    content = file.read()

valute_blocks = re.findall(r'<Valute[^>]*>.*?</Valute>', content, re.DOTALL)

num_codes = []
char_codes = []

for block in valute_blocks:
    num_code = re.search(r'<NumCode>([^<]*)</NumCode>', block)
    char_code = re.search(r'<CharCode>([^<]*)</CharCode>', block)
    if num_code and char_code:
        num_codes.append(num_code.group(1))
        char_codes.append(char_code.group(1))

print("NumCodes:", num_codes)
print("CharCodes:", char_codes)