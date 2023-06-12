length = int(input('Length: '))
unit = input('(C)m or (M): ')
if unit.upper() == "C":
    converted = length / 100
    print(f"Length is {converted} metre")
else:
    converted = length * 100
    print(f"Length is {converted} centimetre ")