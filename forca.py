import random

#Exibindo a tela de bem vindo
def imprimir_bem_vindo():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

#Obtem a palavra secreta de forma aleatoria do arquivo
def obter_palavra_secreta():
    # Lendo o arquivo de palavras
    with open("palavras.txt", "r") as arquivo:
        palavras = []

        #Lendo linha por linha
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    #Escolhendo uma palavra aleatoriamente
    numero = random.randrange(0, len(palavras))
    palavra_secreta=palavras[numero]

    return palavra_secreta

#Obtem da entrada padrao o chute do jogador, tratando a entrada
def obter_chute():
    # Obtendo o chute
    chute = input("Qual letra? ")

    # Tratando o chute do usuario, removendo os espacos e convertendo para mnusculo
    chute = chute.strip()
    chute = chute.lower()

    return chute

#Verifica se o chute contem na palavra secreta, e caso verdadeiro modifica as letras acertadas
def testa_e_adiciona_chute(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = chute
        index += 1

    return letras_acertadas

#Imprime mensagem de resultado
def imprime_resultado(acertou):
    if (acertou):
        print("Voce ganhou!")
    else:
        print("Voce se enforcou!")



#Roda o jogo
def jogar():

    imprimir_bem_vindo()

    palavra_secreta = obter_palavra_secreta()

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

        #Obtendo o chute do jogador
        chute = obter_chute()

        #Verificando se a palavra digitada pelo usuario se encontra na pelavra secreta
        if(chute in palavra_secreta):
            letras_acertadas=testa_e_adiciona_chute(palavra_secreta, chute, letras_acertadas)

        else:
            letras_erradas.append(chute)
            letras_erradas.sort()
            print("Voce errou. Restam {} tentativas".format(maximo_tentativas-len(letras_erradas)))

        #Verificando se o usuario acertou ou se enforcou
        acertou =(not "_" in letras_acertadas)
        enforcou = (len(letras_erradas) >= maximo_tentativas)

    #Exibindo mensagem caso o usuario se enforque o ganhe o jogo
    imprime_resultado(acertou)

    #Exibindo mensagem de fim de jogo
    print("Fim do jogo")
    print("A palavra secreta eh: {}".format(palavra_secreta))

#Inicia a funcao jogar caso execute diretamente deste arquivo
if(__name__ == "__main__"):
    jogar()