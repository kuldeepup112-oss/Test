
print("Project do work of the calculater 🧮🧮🧮")
print('chose the number : \n1. addtion\n2. subtraction\n3. multiplecation \n4. division')

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2


def mul(num1,num2):
    return num1*num2


def div(num1,num2):
    return num1/num2

Select = int(input ('Select the operater  1 - 4 : '))

number1 = int(input("Enter the first number : "))
number2 = int(input("Enter the second number : "))

if Select ==1:
    print(add(number1,number2))

elif Select ==2:
    print(sub(number1,number2))


elif Select ==3:
    print(mul(number1,number2))
    

elif Select ==4:
    print(div(number1,number2))



  
