import math
import random

zadanie = random.randint(1, 5)
x = random.randint(1, 5)

wynik = 0
while True:
    if wynik == 10:
        print("Congratulations! Your score is 10")
        break


    if zadanie == 1:
        z = math.factorial(x)
        print("What's a factorial of ", x)
        w = int(input("Enter number >> "))
        if w == z:
            print("Great job!")
            wynik += 1
            zadanie = random.randint(1, 5)
            x = random.randint(1, 5)
        else:
            print("Try again")

    if zadanie == 2:
        y = random.randint(1, 100)
        print(f"How much is {x} * {y}")
        w = int(input("Enter number >> "))
        if w == x*y:
            print("Great job!")
            wynik += 1
            zadanie = random.randint(1, 5)
            x = random.randint(1, 5)
        else:
            print("Try again")

    if zadanie == 3:
        y = random.randint(1, 20)
        print(f"How much is {y} to the power of {x} ?")
        w = int(input("Enter number >> "))
        if w == y**x:
            print("Great job!")
            wynik += 1
            zadanie = random.randint(1, 5)
            x = random.randint(1, 5)
        else:
            print("Try again")

    if zadanie == 4:
        pierwiastki = ["4", "9", "16", "25", "36", "49", "64", "81", "100", "121", "144", "169", "196", "225", "256", "289", "324", "361", "400"]
        random.shuffle(pierwiastki)
        for y in pierwiastki:
            print(f"How much is square root of {y}")
            break
        w = int(input("Enter number >> "))
        if w == math.sqrt(int(y)):
            print("Great job!")
            wynik += 1
            zadanie = random.randint(1, 5)
            x = random.randint(1, 5)
        else:
            print("Try again")
    if zadanie == 5:
        y = random.randint(1, 500)
        
        y % x != 0
        while True:
                if y % x == 0:
                    break
                else:
                    y = random.randint(1, 500)
                    continue
        print(f"How much is {y} divided by {x}")
        w = int(input("Enter number >> "))
        if w == y / x:
            print("Great job!")
            wynik += 1
            zadanie = random.randint(1, 5)
            x = random.randint(1, 5)
        else:
            print("Try again")
