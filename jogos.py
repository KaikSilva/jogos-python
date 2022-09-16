import adivinhacao
import forca

def choose_game():
    print("*********************************")
    print("*******Choose your game!*********")
    print("*********************************")

    print("")
    print("{1} Hangman", "{2} Divination" , sep="\n")
    print("")

    jogo = int(input("What's game? "))
    print("")


    if(jogo == 1):
        print("---------------")
        print("Playing hangman")
        print("---------------")
        print("")
        forca.play()
    elif(jogo == 2):
        print("------------------")
        print("Playing divination")
        print("------------------")
        print("")
        adivinhacao.play()


if(__name__ == "__main__"):
    choose_game()
