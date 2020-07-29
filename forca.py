import random

def jogar():
    #Exibindo a tela de bem vindo
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    #Lendo o arquivo de palavras
    arquivo = open("palavras.txt", "r")
    palavras = []

    #Lendo linha por linha
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    #Fechando o arquivo
    arquivo.close()

    #Escolhendo uma palavra aleatoriamente
    numero = random.randrange(0, len(palavras))
    palavra_secreta=palavras[numero]

    # Inicializando as letras acertadas
    letras_acertadas = ["_" for letra in palavra_secreta]

    letras_erradas = []
    maximo_tentativas = 6

    #Convertendo a palavra_secreta para lower
    palavra_secreta = palavra_secreta.lower()

    #Inicializando as variaveis de controle do laco
    enforcou=False
    acertou=False

    while((not enforcou) and (not acertou)):

        #Exibindo as letras acertadas e erradas
        print("Letras acertadas: {}.".format(letras_acertadas))
        print("Letras erradas: {}.".format(letras_erradas))

        #Obtendo o chute
        chute = input("Qual letra? ")

        #Tratando o chute do usuario, removendo os espacos e convertendo para mnusculo
        chute = chute.strip()
        chute = chute.lower()

        #Verificando se a palavra digitada pelo usuario se encontra na pelavra secreta
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index]=chute
                index+=1
        else:
            letras_erradas.append(chute)
            letras_erradas.sort()
            print("Voce errou. Restam {} tentativas".format(maximo_tentativas-len(letras_erradas)))

        #Verificando se o usuario acertou ou se enforcou
        acertou =(not "_" in letras_acertadas)
        enforcou = (len(letras_erradas) >= maximo_tentativas)

    #Exibindo mensagem caso o usuario se enforque o ganhe o jogo
    if(enforcou):
        print("Voce se enforcou!")
    else:
        print("Voce ganhou!")

    #Exibindo mensagem de fim de jogo
    print("Fim do jogo")
    print("A palavra secreta eh: {}".format(palavra_secreta))

if(__name__ == "__main__"):
    jogar()