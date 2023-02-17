CorrectYear = [31,28,31,30,31,30,31,31,30,31,30,31]
VisocosnyYear = [31,29,31,30,31,30,31,31,30,31,30,31]
while(True):
    QuantityDays = 0
    #repeat = 777

    #while (repeat == 777):
    print("Выберете год")
    Year = int(input())

    if ((Year % 4) == 0):
        for i in range(0,12):
            for j in range(1,CorrectYear[i]+1):
                if(j>9):
                    while j > 0:
                        QuantityDays = QuantityDays + (j % 10)
                        j = j // 10
                else: QuantityDays = QuantityDays + j 
        print(f"В {Year} году сумма цифр: {QuantityDays}")

    else:
        for i in range(0,12):
            for j in range(1,VisocosnyYear[i]+1):
                if(j>9):
                    while j > 0:
                        QuantityDays = QuantityDays + (j % 10)
                        j = j // 10
                else: QuantityDays = QuantityDays + j 
        print(f"В {Year} году сумма цифр: {QuantityDays}")
