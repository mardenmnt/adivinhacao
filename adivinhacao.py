import random

def jogar():

    # Apresentação
    print('*' * 50)
    print('        Bem vindo(a) ao jogo de adivinhação!')
    print('*' * 50)

    # Número no qual o jogador deve acertar
    numero_secreto = random.randrange(1, 101)     # gera número aleatório de 1 a 100

    # Configuração de tentativas
    total_tentativas = 0

    # Escolha um nível
    print("Qual o nível de dificuldade?")
    print("(1) Fácil | (2) Médio | (3) Difícil")
    nivel = int(input("Escolha um nível: "))

    while nivel < 1 or nivel > 3:
        print('Nível inválido!\n')
        print("[1] Fácil | [2] Médio | [3] Difícil")
        nivel = int(input("Escolha um nível: "))

    if nivel == 1:
        total_tentativas = 20
        print(f'\nBem vindo(a) ao nível Fácil, você tem {total_tentativas} tentativas!')
    elif nivel == 2:
        total_tentativas = 10
        print(f'\nBem vindo(a) ao nível Médio, você tem {total_tentativas} tentativas!')
    else:
        total_tentativas = 5
        print(f'\nBem vindo(a) ao nível Difícil, você tem {total_tentativas} tentativas!')

    # Sistema de pontuação, definir quantidades de pontos e retirar a cada rodada perdida. O Fator é determinado pelo nível
    pontos = 1000
    retirar = int(1000 / total_tentativas)

    # Laço de tentativas
    for rodada in range(1, total_tentativas + 1):
        print('\nTentativa: {} de {}'.format(rodada, total_tentativas))
        chute = int(input('Digite um número de 1 a 100: '))
        print('Você digitou', chute)

    # Criando um while dentro do for para continuar na rodada atual e não continuar para proxima

        while chute < 1 or chute > 100:
            print('Chute inválido!\n')
            chute = int(input('Digite um número de 1 a 100: '))
            print('Você digitou', chute)
            continue

        # Caso o valor do chute seja o mesmo do número secreto, o jagador ganha
        if chute == numero_secreto:
            print(f'Você acertou e fez {pontos}!')
            break

        # Caso o valor do chute esteja errado, dicas para jogador
        elif chute > numero_secreto:
            print('Você errou!\nO seu chute foi maior que o número secreto')

        else:
            print('Você errou!\nO seu chute foi menor que o número secreto')

        # Outro modo de descontar os pontos
        # pontos_perdidos = pontos - (abs(chute - numero_secreto))
        # pontos_perdidos = abs(numero_secreto - chute) # abs() retira sinal do resultado e pega somente o número absoluto

        pontos = pontos - retirar

    if pontos > 0:
        print(f'\nFim do jogo! Sua pontuação foi {pontos} pontos.')
    else:
        print(f'\nFim do jogo! Sua pontuação foi {pontos} pontos. O número secreto é {numero_secreto}')

if __name__ == '__main__':
    jogar()

# Programa principal vs Programa importado

# Arquivo executado diretamente -> __name__ == '__main__'
# Arquivo importado -> __name__ == 'nome_do_arquivo'

