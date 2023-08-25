#Jokenpô
from random import randint                       #Importar o modulo random
from time import sleep

itens = ("Pedra" , "Papel" , "Tesoura")
computador = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input("Qual é a sua Jogada ?\n"))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(2)
print("-=" * 11)

print(f"Computador Jogou: {itens[computador]}")
print(f"Jogador Jogou: {itens[jogador]}")
print("-=" * 11)

if computador == 0: #pedra

    if jogador == 0: #pedra + pedra = empate
        print("EMPATE")

    elif jogador == 1: #pedra + papel = papel
        print("JOGADOR VENCE")

    elif jogador ==2: #pedra + tesoura = pedra
        print("COMPUTADOR VENCE")

    else: 
        print("JOGADA INVÁLIDA!")

elif computador == 1: #papel

    if jogador == 0:# papel + pedra = papel
        print("COMPUTADOR VENCE")

    elif jogador == 1:# papel + papel = empate
        print("EMPATE")

    elif jogador == 2:# papel + tesoura = tesoura
        print("JOGADOR VENCE")

    else:
        print("JOGADA INVÁLIDA!")

elif computador == 2: #tesoura

    if jogador == 0: # Tesoura + pedra = pedra
        print("JOGADOR VENCE")

    elif jogador == 1: # Tesoura + papel = tesoura
        print("COMPUTADOR VENCE")

    elif jogador == 2: # Tesoura + tesoura = empate
        print("EMPATE")

    else:
        print("JOGADA INVÁLIDA!")

#by Paulo Vinícius :)