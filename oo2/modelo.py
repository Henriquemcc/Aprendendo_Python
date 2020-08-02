class Programa:
    #Metodo construtor
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    #Permite obter o valor de nome fora da classe
    @property
    def nome(self):
        return self._nome

    #Permite alterar o valor de nome fora da classe
    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    #Permite obter o valor de likes fora da classe
    @property
    def likes(self):
        return self._likes

    #Incrementa mais um do valor de likes
    def dar_like(self):
        self._likes += 1

    def imprime(self):
        print("Nome: {} - Ano: {} - Likes: {} .".format(self._nome, self.ano, self._likes))

class Filme(Programa):
    #Metodo construtor
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    #Metodo construtor
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
