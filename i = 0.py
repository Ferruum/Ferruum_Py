i = 0 
deist = ""
float = 0
print("Введите количество операций")
oper = int(input())
print("Введите первое число")
number1 = float()(input())
print("Введите второе число")
number2 = float()(input())
print("Выберете операцию:\n|+|-|*|/|st|os|")
deist = input()
if(deist == "+"):
        summ = number1 + number2
        print(f"{summ}")
elif(deist == "-"):
        summ = number1 - number2
        print(f"{summ}")
elif(deist == "*"):
        summ = number1 * number2
        print(f"{summ}")
elif(deist == "/"):
    if (number1 and number2 == 0):
        print ("Деление на ноль")
    else:
        summ = number1 / number2
        print(f"{summ}")

elif(deist == "st"):
        summ = number1**number2
        print(f"{summ}")
elif(deist == "os"):
        summ = number1 % number2
        print(f"{summ}")
while(i != oper-1):
    print("Введите следующее число")
    number2 = int(input())
    print("Выберете операцию:\n|+|-|*|/|st|os|")
    deist = input()
    if(deist == "+"):
        summ = summ + number2
        print(f"{summ}")
    elif(deist == "-"):
        summ = summ - number2
        print(f"{summ}")
    elif(deist == "*"):
        summ = summ * number2
        print(f"{summ}")
    elif(deist == "/"):
        summ = summ / number2
        print(f"{summ}")
    elif(deist == "st"):
        summ = summ**number2
        print(f"{summ}")
    elif(deist == "os"):
        summ = summ % number2
        print(f"{summ}")
    i = i+1
