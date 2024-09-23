from random import randint

vitorias = 0
partidas = 0
contador = 0
derrotas = 0

while True:

    print("0 - Pedra")
    print("1 - Papel")
    print("2 - Tesoura")
    print("3 - Sair")

    jogador = int(input("Escolha uma opção: "))

    print("Quantidade de partidas: " + str(partidas + 1))

    if jogador == 3:
        break

    computador = randint(0, 2)

    if jogador == computador:
        print("Empate")
    elif jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
        print("Jogador venceu")
        vitorias += 1
    else:
        print("Computador venceu")
        derrotas += 1
    partidas += 1

print("=="*10)
print("Resultado final")
print("Vitórias: " + str(vitorias))
print("Derrotas: " + str(derrotas))
print("Empates: " + str(partidas - vitorias - derrotas))

