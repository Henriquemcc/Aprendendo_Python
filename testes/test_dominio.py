from unittest import TestCase
from dominio import Usuario, Lance, Leilao, Avaliador

#Esta classe serve para relizar os testes nos metodos da classe Avaliador
class TestAvaliador(TestCase):
    #Este metodo serve para testar a classe Avaliador passando a ela dois lances em ordem crescente e verificando o maior e o menor valor dos lances
    def test_quando_passado_dois_lances_em_ordem_crescente_deve_retornar_o_maior_e_menor_valor_de_um_lance(self):
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
    #Fim do metodo test_quando_passado_dois_lances_em_ordem_crescente_deve_retornar_o_maior_e_menor_valor_de_um_lance

    #Este metodo serve para testar a classe Avaliador passando a ela dois lances em ordem decrescente e verificando o maior e o menor valor dos lances
    def test_quando_passado_dois_lances_em_ordem_decrescente_deve_retornar_o_maior_e_menor_valor_de_um_lance(self):
        # Criando os usuarios Fulano e Ciclano
        fulano = Usuario("Fulano")
        ciclano = Usuario("Ciclano")

        # Crindo os lances de Fulano e Ciclano
        lance_do_fulano = Lance(fulano, 500)
        lance_do_ciclano = Lance(ciclano, 1500)

        # Criando um leilao
        leilao = Leilao("Celular")

        # Adicionando os lances de Fulano e Ciclano ao leilao
        leilao.lances.append(lance_do_ciclano)
        leilao.lances.append(lance_do_fulano)

        # Criando um avaliador
        avaliador = Avaliador()
        avaliador.avalia(leilao)

        # Definindo o menor e o maior valor esperado
        menor_valor_esperado = 500
        maior_valor_esperado = 1500

        # Comparando se os valores da instncia da classe Avaliador correspondem ao menor e o maior valor esperado
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
    # Fim do metodo test_quando_passado_dois_lances_em_ordem_decrescente_deve_retornar_o_maior_e_menor_valor_de_um_lance

    #Este metodo serve para testar a classe Avaliador passando a ela apenas um lance e verificando o maior e o menor valor do lance
    def test_quando_passado_apenas_um_lance_no_leilao_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_valor_de_um_lance(self):
        # Criando o usuario Ze
        ze = Usuario("Zé")

        # Crindo o lances do Ze
        lance_do_ze = Lance(ze, 500)

        # Criando um leilao
        leilao = Leilao("Computdor")

        # Adicionando o lances do Ze
        leilao.lances.append(lance_do_ze)

        # Criando um avaliador
        avaliador = Avaliador()
        avaliador.avalia(leilao)

        # Definindo o menor e o maior valor esperado
        valor_esperado = 500

        # Comparando se os valores da instncia da classe Avaliador correspondem ao menor e o maior valor esperado
        self.assertEqual(valor_esperado, avaliador.menor_lance)
        self.assertEqual(valor_esperado, avaliador.maior_lance)
    #Fim do metodo test_quando_passado_apenas_um_lance_no_leilao_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_valor_de_um_lance

    #Este metodo serve para testar a classe Avaliador passando a ela tres lances e verificando o maior e o menor valor dos lances
    def test_quando_passado_tres_lances_deve_retornar_o_maior_e_menor_lance(self):
        # Criando os usuarios Fulano e Ciclano
        fulano = Usuario("Fulano")
        ciclano = Usuario("Ciclano")
        ze = Usuario("Zé")

        # Crindo os lances de Fulano e Ciclano
        lance_do_fulano = Lance(fulano, 500)
        lance_do_ciclano = Lance(ciclano, 1500)
        lance_do_ze = Lance(ze, 1200)

        # Criando um leilao
        leilao = Leilao("Celular")

        # Adicionando os lances de Fulano e Ciclano ao leilao
        leilao.lances.append(lance_do_ciclano)
        leilao.lances.append(lance_do_fulano)
        leilao.lances.append(lance_do_ze)

        # Criando um avaliador
        avaliador = Avaliador()
        avaliador.avalia(leilao)

        # Definindo o menor e o maior valor esperado
        menor_valor_esperado = 500
        maior_valor_esperado = 1500

        # Comparando se os valores da instncia da classe Avaliador correspondem ao menor e o maior valor esperado
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
    #Fim do metodo test_quando_passado_tres_lances_deve_retornar_o_maior_e_menor_lance

#Fim da classe TestAvaliador