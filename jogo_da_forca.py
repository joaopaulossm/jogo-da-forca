# -*- coding: utf-8 -*-
"""jogo da forca.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MYM6KhjWtq50LYpWizVmJEoE5wBeoMBO
"""

import random

lista_palavras = ["casa", "bola", "massa"]

print('''******************************
 JOGO DA FORCA 
******************************''')
print("\n")

while True:
    inicio = int(input("Digite (1) para Inicar ou (0) para Sair: "))

    if inicio:

        pos = random.choice(0, len[lista_palavras]-1)
        palavra = lista_palavras[pos]
        riscos = [" _ "] * len(palavra)

        print("\n")
        print("Inicio do jogo!!!")

        erros = 0
        while erros <= 2 :
            letra = input("Digite uma letra: ")

            if letra in palavra:
                pos = palavra.find(letra)
            for i in range(pos, len(palavra)):                 
                    if letra == palavra[i]:
                        riscos[i] = letra                    
            else:
                erros += 1
                print ("Ops... tente novamente!")

            print('Palavra:\n', riscos)

        print(palavra)
    else:
        print("Fim de jogo!!!")
        print("\n")
        print("Volte sempre!!!")
        break