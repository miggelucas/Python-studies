#interface do app
from funcao import *


print("\n*****************************")
print(">>>Bem-vindo ao conta palavra<<<")
print("*****************************\n")
print("Eu posso contar palavras e caracteres de textos pra você...")
print("digite x para desligar")

play = True

while play == True:
    entrada = input("insira aqui o que você quer contar: ")
    if entrada == "x":
        play = False
    else:
        processador = Processador(entrada)
        print(processador, "\n")



