import random
import funcoes
def jogar():
    numero_secreto = random.randint(1, 100)
    total_de_tentativas = 0
    pontos = 1000

    funcoes.titulo("Bem vindo ao jogo de Adivinhação!")
    print('Escolha o nível de dificuldade !')
    print(' (1) Fácil  (2) Médio (3) Difícil ')
    nível = int(input('Sua escolha: '))

    if nível == 1:
        total_de_tentativas = 20
    elif nível == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if acertou:
            print("Você acertou! e fez {} pontos" .format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if maior:
                print("Você errou! O seu chute foi maior que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))
            elif menor:
                print("Você errou! O seu chute foi menor que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))

    print("Fim do jogo")
if __name__ == "__main__":
    jogar()