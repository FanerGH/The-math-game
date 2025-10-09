import math
import random

zadanie = random.randint(1, 5)
x = random.randint(1, 5)

wynik = 0
while True:
    if wynik == 10:
        print("Gratulacje! Osiągnąłeś wynik 10")
        break


    if zadanie == 1:
        z = math.factorial(x)
        print("Ile wynosi silnia z ", x)
        w = int(input("Wprowadź liczbę >> "))
        if w == z:
            print("Świetna robota!")
            wynik += 1
            zadanie = random.randint(1, 5)
            x = random.randint(1, 5)
        else:
            print("Spróbuj jeszcze raz")

    if zadanie == 2:
        y = random.randint(1, 100)
        print(f"Ile wynosi wynik {x} * {y}")
        w = int(input("Wprowadź liczbę >> "))
        if w == x*y:
            print("Świetna robota!")
            wynik += 1
            zadanie = random.randint(1, 5)
            x = random.randint(1, 5)
        else:
            print("Spróbuj jeszcze raz")

    if zadanie == 3:
        y = random.randint(1, 20)
        print(f"Ile wynosi {x} potęga liczby {y} ?")
        w = int(input("Wprowadź liczbę >> "))
        if w == y**x:
            print("Świetna robota!")
            wynik += 1
            zadanie = random.randint(1, 5)
            x = random.randint(1, 5)
        else:
            print("Spróbuj jeszcze raz")

    if zadanie == 4:
        pierwiastki = ["4", "9", "16", "25", "36", "49", "64", "81", "100", "121", "144", "169", "196", "225", "256", "289", "324", "361", "400"]
        random.shuffle(pierwiastki)
        for y in pierwiastki:
            print(f"Ile wynosi pierwiastek z {y}")
            break
        w = int(input("Wprowadź liczbę >> "))
        if w == math.sqrt(int(y)):
            print("Świetna robota!")
            wynik += 1
            zadanie = random.randint(1, 5)
            x = random.randint(1, 5)
        else:
            print("Spróbuj jeszcze raz")
    if zadanie == 5:
        y = random.randint(1, 500)
        
        y % x != 0
        while True:
                if y % x == 0:
                    break
                else:
                    y = random.randint(1, 500)
                    continue
        print(f"Ile wynosi iloraz liczb {y} i {x}")
        w = int(input("Wprowadź liczbę >> "))
        if w == y / x:
            print("Świetna robota!")
            wynik += 1
            zadanie = random.randint(1, 5)
            x = random.randint(1, 5)
        else:
            print("Spróbuj jeszcze raz")
