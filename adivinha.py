from random import randint

def main():
    input('Prime ENTER para começar.')
    jogo()


def jogo():
    numero_de_tentativas = 3
    tentativas_utilizadas = 0
    numeroPC = randint(1, 10)

    user_guess = int(input('Estou a pensar num número entre 1 e 10, qual?\nTens 3 tentativas: '))

    tentativas_utilizadas += 1

    while user_guess != numeroPC:

        if user_guess < numeroPC:
            user_guess = int(input('Hm... mais alto. Tenta outra vez: '))
            tentativas_utilizadas += 1

        elif user_guess > numeroPC:
            user_guess = int(input('Hm... mais baixo. Tenta outra vez: '))
            tentativas_utilizadas += 1
        
        if (tentativas_utilizadas == numero_de_tentativas):
            if user_guess == numeroPC:
                print('Parabéns, acertaste em {} tentativas!'.format(tentativas_utilizadas))
                jogarDeNovo()
            else:
                print('Excedeste as tuas tentativas, perdeste! Era o número {}.'.format(numeroPC))
                jogarDeNovo()
                break
    
    if user_guess == numeroPC:
        print('Parabéns, acertaste em {} tentativa(s)!'.format(tentativas_utilizadas))
        jogarDeNovo()

def jogarDeNovo():
    pergunta = input('Queres jogar de novo? (S/N): ').upper()
    if pergunta == 'S':
        main()
    elif pergunta == 'N':
        exit()
    else:
        print('Resposta inválida, tenta outra vez: ')
        jogarDeNovo()

main()