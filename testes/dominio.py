import sys

#Esta classe representa o usuario que vai fazer lances no leilao
class Usuario:
    #Este metodo serve para construir uma instancia da classe Usuario
    #nome Nome do usuario
    def __init__(self, nome: str):
        self.__nome = nome
    #Fim do metodo __init__

    #Este metodo serve para obter o nome de uma instancia da classe Usuario
    @property
    def nome(self):
        return self.__nome
    #Fim do metodo nome
#Fim da classe Usuario

#Esta classe representa o lance que o usuario vai fazer no leilao
class Lance:
    #Este metodo serve para construir uma instancia da classe Lance
    #usuario Instancia da classe Usuario
    #valor Valor do lance
    def __init__(self, usuario:Usuario, valor:float):
        self.usuario = usuario
        self.valor = float(valor)
    #Fim do metodo __init__
#Fim da classe Lance

#Esta classe serve para armazenar os lances do leilao
class Leilao:
    #Este metodo serve para construir uma instancia da classe Leilao
    #descricao Descricao do leilao
    def __init__(self, descricao:str):
        self.descricao = descricao
        self.__lances = []
    #Fim do metodo __init__

    #Este metodo serve para obter os lances de uma instancia da classe Leilao
    @property
    def lances(self):
        return self.__lances
    #Fim do metodo lances
#Fim da classe Leilao

#Esta classe representa o avaliador do leilao
class Avaliador:
    #Este metodo serve para construir uma instancia da classe Avaliador
    def __init__(self):
        self.__maior_lance = sys.float_info.min
        self.__menor_lance = sys.float_info.max
    #Fim do metodo __init__

    #Este metodo serve para avaliar o leilao e calcular os lances minimo e o maximo.
    #leilao Leilao que sera avaliado
    def avalia(self, leilao: Leilao):
        for lance in leilao.lances:
            if lance.valor > self.__maior_lance:
                self.__maior_lance = lance.valor
            elif lance.valor < self.__menor_lance:
                self.__menor_lance = lance.valor
    #Fim do metodo avalia

    #Este metodo serve para obter o valor do maior lance de uma instancia da classe Avaliador
    @property
    def maior_lance(self):
        return self.__maior_lance
    #Fim do metodo maior_lance

    #Este metodo serve para obter o valor do menor lance de uma instancia da classe Avaliador
    @property
    def menor_lance(self):
        return self.__menor_lance
    #Fim do metodo menor_lance
#Fim da classe Avaliador