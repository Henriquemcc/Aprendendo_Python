from unittest import TestCase
from dominio import Usuario, Lance, Leilao
import random
import string

#Esta classe serve para relizar os testes nos metodos da classe Avaliador
class TestAvaliador(TestCase):

    #Metodos que realizam testes aleatorios:

    #Este metodo serve para criar varios instancias da classe Usuario, cada um com um nome aleatorio
    #quantidade Numero de usuarios que serao gerados
    def cria_usuario(self, quantidade:int):
        self.usuarios = []
        for _ in range(quantidade):
            self.usuarios.append(Usuario(''.join(random.choice(string.ascii_letters) for _ in range(2*quantidade))))
    #Fim do metodo cria_usuario

    #Este metodo serve para criar aleatoriamente valores para os lances
    #quantidade Quantidade de valores de lances que serao gerados
    def cria_valores_lances(self, quantidade:int):
        self.valor_lances = []
        for _ in range(quantidade):
            self.valor_lances.append(random.randrange(0, 2*quantidade))
    #Fim do metodo cria_valores_lances

    #Este metodo serve para testar a classe Avaliador passando a ela x lances aleatorios em ordem aleatoria e verificando o maior e o menor valor dos lances.
    #quantidade_de_lances Quantidade de lances aleatorios que serao inseridos no leilao.
    def test_quando_passado_x_lances_aleatorios_em_ordem_aleatoria_deve_retornar_o_maior_e_o_menor_valor_de_um_lance(self, quantidade_de_lances=999):
        #Criando os usuarios
        self.cria_usuario(quantidade_de_lances)

        #Criando os lances
        self.cria_valores_lances(quantidade_de_lances)

        #Criando os lances e adicionando ao leilao
        indice = 0
        while indice < quantidade_de_lances:
            valor_lance = self.valor_lances[indice]
            usuario = self.usuarios[indice]
            lance = Lance(usuario, valor_lance)
            self.leilao.propoe(lance)
            indice += 1

        #Calculando o menor e o maior valor esperado
        menor_valor_esperado = min(self.valor_lances)
        maior_valor_esperado = max(self.valor_lances)

        #Comparando o menor e maior valor esperado com os valores obtidos
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    #Fim do metodo test_quando_passado_x_lances_aleatorios_em_ordem_aleatoria_deve_retornar_o_maior_e_o_menor_valor_de_um_lance

    # Este metodo serve para testar a classe Avaliador passando a ela x lances aleatorios em ordem crescente e verificando o maior e o menor valor dos lances.
    # quantidade_de_lances Quantidade de lances aleatorios que serao inseridos no leilao.
    def test_quando_passado_x_lances_aleatorios_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance(self, quantidade_de_lances=999):
        # Criando os usuarios
        self.cria_usuario(quantidade_de_lances)

        # Criando os lances
        self.cria_valores_lances(quantidade_de_lances)

        # Ordenando os valores dos lances
        self.valor_lances.sort()

        # Criando os lances e adicionando ao leilao
        indice = 0
        while indice < quantidade_de_lances:
            valor_lance = self.valor_lances[indice]
            usuario = self.usuarios[indice]
            lance = Lance(usuario, valor_lance)
            self.leilao.propoe(lance)
            indice += 1

        # Calculando o menor e o maior valor esperado
        menor_valor_esperado = min(self.valor_lances)
        maior_valor_esperado = max(self.valor_lances)

        # Comparando o menor e maior valor esperado com os valores obtidos
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    #Fim do metodo test_quando_passado_x_lances_aleatorios_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance

    # Este metodo serve para testar a classe Avaliador passando a ela x lances aleatorios em ordem decrescente e verificando o maior e o menor valor dos lances.
    # quantidade_de_lances Quantidade de lances aleatorios que serao inseridos no leilao.
    def test_quando_passado_x_lances_aleatorios_em_ordem_decrescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance(self, quantidade_de_lances=999):
        # Criando os usuarios
        self.cria_usuario(quantidade_de_lances)

        # Criando os lances
        self.cria_valores_lances(quantidade_de_lances)

        # Ordenando os valores dos lances
        self.valor_lances.sort(reverse=True)

        # Criando o leilao
        leilao = Leilao("Microondas")

        # Criando os lances e adicionando ao leilao
        indice = 0
        while indice < quantidade_de_lances:
            valor_lance = self.valor_lances[indice]
            usuario = self.usuarios[indice]
            lance = Lance(usuario, valor_lance)
            self.leilao.propoe(lance)
            indice += 1

        # Calculando o menor e o maior valor esperado
        menor_valor_esperado = min(self.valor_lances)
        maior_valor_esperado = max(self.valor_lances)

        # Comparando o menor e maior valor esperado com os valores obtidos
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    #Fim do metodo test_quando_passado_x_lances_aleatorios_em_ordem_decrescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance

    #Metodos que realizam testes nao aleatorios:

    #Este metodo serve para configurar o ambiente de teste
    def setUp(self):
        # Criando os usuarios Fulano, Ciclano e Ze
        self.fulano = Usuario("Fulano")

        # Crindo os lances de Fulano, Ciclano e Ze
        self.lance_do_fulano = Lance(self.fulano, 500)

        # Criando um leilao
        self.leilao = Leilao("Celular")
    #Fim do metodo setUp

    #Este metodo serve para testar a classe Avaliador passando a ela dois lances em ordem crescente e verificando o maior e o menor valor dos lances
    def test_quando_passado_dois_lances_em_ordem_crescente_deve_retornar_o_maior_e_menor_valor_de_um_lance(self):

        #Criando os usuarios ciclano
        ciclano = Usuario("Ciclano")

        #Criando os lances do ciclano
        lance_do_ciclano = Lance(ciclano, 1500)

        # Adicionando os lances de Fulano e Ciclano ao leilao
        self.leilao.propoe(self.lance_do_fulano)
        self.leilao.propoe(lance_do_ciclano)

        #Definindo o menor e o maior valor esperado
        menor_valor_esperado = 500
        maior_valor_esperado = 1500

        #Comparando se os valores da instncia da classe Avaliador correspondem ao menor e o maior valor esperado
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    #Fim do metodo test_quando_passado_dois_lances_em_ordem_crescente_deve_retornar_o_maior_e_menor_valor_de_um_lance

    #Este metodo serve para testar a classe Avaliador passando a ela dois lances em ordem decrescente e verificando o maior e o menor valor dos lances
    def test_quando_passado_dois_lances_em_ordem_decrescente_deve_retornar_o_maior_e_menor_valor_de_um_lance(self):

        # Criando os usuarios ciclano
        ciclano = Usuario("Ciclano")

        # Criando os lances do ciclano
        lance_do_ciclano = Lance(ciclano, 1500)

        # Adicionando os lances de Fulano e Ciclano ao leilao
        self.leilao.propoe(lance_do_ciclano)
        self.leilao.propoe(self.lance_do_fulano)

        # Definindo o menor e o maior valor esperado
        menor_valor_esperado = 500
        maior_valor_esperado = 1500

        # Comparando se os valores da instncia da classe Avaliador correspondem ao menor e o maior valor esperado
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    # Fim do metodo test_quando_passado_dois_lances_em_ordem_decrescente_deve_retornar_o_maior_e_menor_valor_de_um_lance

    #Este metodo serve para testar a classe Avaliador passando a ela apenas um lance e verificando o maior e o menor valor do lance
    def test_quando_passado_apenas_um_lance_no_leilao_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_valor_de_um_lance(self):

        # Adicionando o lances do Ze
        self.leilao.propoe(self.lance_do_fulano)

        # Definindo o menor e o maior valor esperado
        valor_esperado = 500

        # Comparando se os valores da instncia da classe Avaliador correspondem ao menor e o maior valor esperado
        self.assertEqual(valor_esperado, self.leilao.menor_lance)
        self.assertEqual(valor_esperado, self.leilao.maior_lance)
    #Fim do metodo test_quando_passado_apenas_um_lance_no_leilao_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_valor_de_um_lance

    #Este metodo serve para testar a classe Avaliador passando a ela tres lances e verificando o maior e o menor valor dos lances
    def test_quando_passado_tres_lances_deve_retornar_o_maior_e_menor_lance(self):
        # Criando os usuarios ciclano e ze
        ciclano = Usuario("Ciclano")
        ze = Usuario("Zé")

        # Criando os lances do ciclano e do ze
        lance_do_ciclano = Lance(ciclano, 1500)
        lance_do_ze = Lance(ze, 1200)

        # Adicionando os lances de Fulano e Ciclano ao leilao
        self.leilao.propoe(lance_do_ciclano)
        self.leilao.propoe(self.lance_do_fulano)
        self.leilao.propoe(lance_do_ze)

        # Definindo o menor e o maior valor esperado
        menor_valor_esperado = 500
        maior_valor_esperado = 1500

        # Comparando se os valores da instncia da classe Avaliador correspondem ao menor e o maior valor esperado
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    #Fim do metodo test_quando_passado_tres_lances_deve_retornar_o_maior_e_menor_lance
#Fim da classe TestAvaliador