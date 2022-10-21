import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Enter a number from 1 to 100 ="))
    vidas=6
    while numero_aleatorio != numero_elegido:
        if numero_elegido > numero_aleatorio:
            print("Your number is too high, choose a lower number.")
            vidas -=1
            print("You still have", vidas, "Lives")
        else:
            print("Your number is on the floor, choose a higher number.")
            vidas -= 1
            print("You still have", vidas, "Lives")

        numero_elegido = int(input("You have a new opportunity, place a new number = "))
        print("You still have", vidas, "Lives")

        if numero_elegido == numero_aleatorio:
            print("YOU WIN")

        if vidas == 0:
            print("GAME OVER")
            break

if __name__ == "__main__" :
    run()