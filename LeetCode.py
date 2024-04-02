
def convert_to_lakh_crore(number):
    crore = number // 10000000
    lakh = (number % 10000000) // 100000
    return crore, lakh

number = int(input("Enter the number: "))
crore, lakh = convert_to_lakh_crore(number)

print(f"{number} is equivalent to ",end='')

if crore:
    print(f'{crore} crore ',end='')

if lakh and crore :
    print(f'and {lakh} lakh',end='')
else:
    if lakh and crore == 0:
        print(f'{lakh} lakh',end='')
