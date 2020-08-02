class Filme:
    #Metodo construtor
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    #Permite obter o valor de nome fora da classe
    @property
    def nome(self):
        return self.__nome

    #Permite alterar o valor de nome fora da classe
    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    #Permite obter o valor de likes fora da classe
    @property
    def likes(self):
        return self.__likes

    #Incrementa mais um do valor de likes
    def dar_like(self):
        self.__likes += 1

class Serie:
    #Metodo construtor
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    #Permite obter o valor de nome fora da classe
    @property
    def nome(self):
        return self.__nome

    #Permite alterar o valor de nome fora da classe
    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    #Permite obter o valor de likes fora da classe
    @property
    def likes(self):
        return self.__likes

    #Incremente mais um do valor de likes
    def dar_like(self):
        self.__likes += 1