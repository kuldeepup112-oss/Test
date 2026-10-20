

print('#'*5,'Hello mam pleace give me a icecream','#'*5)
print('#'*5,'COME','#'*5)


Icecream = {
    'Vanilla': 50,
    'Chocolate': 80,
    'Strawberry': 60,
    'Mango': 70,
    'Butterscotch': 90,
    'Black Currant': 100,
    'Pista': 80,
    'Kulfi': 40,
    'Oreo': 120,
    'Choco Chip': 110
}

total = 0
for i in range(5):
    name = input('Enter the Icecream _name----')

    if name in Icecream:
        print('Icecream',name)
        print('Icecream_name_price',Icecream[name])

        total +=Icecream[name]
print('Total BILL ',total)








































