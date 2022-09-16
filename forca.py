import random

import jogos

def play():
    print("*********************************")
    print("Welcome from game of Hangman!!")
    print("*********************************")
    print("")

    archive = open("palavras.txt" , "r")
    word = []

    for line in archive:
        line = line.strip()
        word.append(line)

    archive.close()

    secret_word = word[random.randrange(0,len(word))].upper()
    right_word = ["_" for letter in secret_word]

    error = False
    corret = False

    lives = 7

    while(not error and not corret):
        print("")
        print("❤{}x".format(lives))
        tentative = input("What's is word: ")

        tentative = tentative.strip().upper()

        if(tentative in secret_word):
            index = 0
            for letter in secret_word:
                if(tentative.upper() == letter.upper()):
                    right_word[index] = tentative
                index = index+1
        else:
            lives = lives - 1
            desenha_forca(lives)

        if(lives == 0):
            ## INCORRET
            print("")
            print("*********************************")
            imprime_mensagem_perdedor(secret_word)
            print("*********************************")
            print("")
            error = True
            again = input("Play again ? {y} yes {n} not: ")
            if (again == "y"):
                play()
        else:

            print(right_word)

            ## CORRET
            if('_' not in right_word):
                print("")
                imprime_mensagem_vencedor()
                print("")

                again = input("Play again ? {y} yes {n} not: ")
                corret = True
                if (again == "y"):
                    play()

    jogos.choose_game()




def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")



def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")
    if(erros == 7):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

















if(__name__ == "__main__"):
    play()
