
def convert_to_lakh_crore(number):
    crore = number // 10000000 # get the number of crores
    lakh = (number % 10000000) // 100000 # get the number of lakhs
    return crore, lakh # return the values

number = int(input("Enter the number: "))
crore, lakh = convert_to_lakh_crore(number)

print(f"{number} is equivalent to ",end='')

if crore:
    print(f'{crore} crore ',end='') # print the number of crores without moving cursor to new line

if lakh and crore :
    print(f'and {lakh} lakh')
else:
    if lakh and crore == 0:
        print(f'{lakh} lakh') # if there are no crores then no need to put "and"
