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
        self.__maior_lance = sys.float_info.min
        self.__menor_lance = sys.float_info.max
    #Fim do metodo __init__

    #Este metodo serve para obter uma copia dos lances de uma instancia da classe Leilao
    @property
    def lances(self):
        return self.__lances[:]
    #Fim do metodo lances

    #Este metodo serve para adicionar um novo lance a instancia da classe Leilao
    #lance Instancia da classe Lance que sera adicionada ao leilao
    def propoe(self, lance:Lance):

        #Verificando se o usuario que propos o lance eh diferente do usario do lance anterior
        if not self.__lances or self.__lances[-1].usuario != lance.usuario:
            if lance.valor > self.__maior_lance:
                self.__maior_lance = lance.valor
            if lance.valor < self.__menor_lance:
                self.__menor_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError("O mesmo usuario não pode propor dois lances seguidos")

    #Fim do metodo propoe

    #Este metodo serve para obter o maior lance de uma instancia da classe Leilao
    @property
    def maior_lance(self):
        return self.__maior_lance
    #Fim do metodo maior_lance

    #Este metodo serve para obter o menor lance de uma instancia da classe Leilao
    @property
    def menor_lance(self):
        return self.__menor_lance
    #Fim do metodo menor_lance

#Fim da classe Leilao