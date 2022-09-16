import random
import jogos

def play():
    print("*********************************")
    print("Welcome from game of divination!!")
    print("*********************************")

    secret_number = random.randrange(1,101)
    points = 1000

    print("")
    print("{1} Ease", "{2} Medium" , "{3} Hard" , sep="\n")
    print("")

    nivel = int(input("Define your difficult of prefer: "))

    if(nivel == 1):
        attempts = 15
    elif(nivel == 2):
        attempts = 10
    else:
        attempts = 5


    while attempts > 0:
        print("")

        attempts = attempts-1

        if(attempts == 0):
            print("❤ last")
        else:
            print("❤{}x".format(attempts))

        number = input("Type a number between 1 and 100: ")

        print("Do you type: " , number)

        number = int(number)

        if(number < 1 | number > 100):
            attempts = attempts+1
            print("You must type a number between 1 and 10")
            continue

        right = number == secret_number
        bigger = number > secret_number
        lower = number < secret_number

        if(right):
            print("You're right the number is {} and received {} points 🥳".format(number , points))
            print("")
            again = input("Play again ? {y} yes {n} not: ")

            if (again == "y"):
                play()
            break
        else:
            if(bigger):
                print("**********************************************************************")
                print("You're number not is right , your number is bigger than the secret number 😥")
                print("**********************************************************************")
            elif(lower):
                print("**********************************************************************")
                print("You're number not is right , your number is lower than the secret number 😥")
                print("**********************************************************************")
            lost_points = abs(secret_number - number)
            points = points - lost_points

    if(attempts == 0):
        print("")
        print("")
        print("**********************************************************************")
        print("You dont have more lives :(")
        print("**********************************************************************")
        print("")
        again = input("Play again ? {y} yes {n} not: ")

        if(again == "y"):
            play()

    jogos.choose_game()


if(__name__ == "__main__"):
    play()

