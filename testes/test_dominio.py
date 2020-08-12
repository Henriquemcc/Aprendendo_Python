from unittest import TestCase
from dominio import Usuario, Lance, Leilao, Avaliador

#Esta classe serve para relizar os testes nos metodos da classe Avaliador
class TestAvaliador(TestCase):
    #Este metodo serve para testar o metodo avalia da classe Avaliador
    def test_avalia(self):
        # Criando os usuarios Fulano e Ciclano
        fulano = Usuario("Fulano")
        ciclano = Usuario("Ciclano")

        # Crindo os lances de Fulano e Ciclano
        lance_do_fulano = Lance(fulano, 500)
        lance_do_ciclano = Lance(ciclano, 1500)

        # Criando um leilao
        leilao = Leilao("Celular")

        # Adicionando os lances de Fulano e Ciclano ao leilao
        leilao.lances.append(lance_do_fulano)
        leilao.lances.append(lance_do_ciclano)

        #Criando um avaliador
        avaliador = Avaliador()
        avaliador.avalia(leilao)

        #Definindo o menor e o maior valor esperado
        menor_valor_esperado = 500
        maior_valor_esperado = 1500

        #Comparando se os valores da instncia da classe Avaliador correspondem ao menor e o maior valor esperado
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
    #Fim do metodo test_avalia
#Fim da classe TestAvaliador