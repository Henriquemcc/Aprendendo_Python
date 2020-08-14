from src.leilao.dominio import Usuario, Lance, Leilao

#Criando os usuarios Fulano e Ciclano
fulano = Usuario("Fulano")
ciclano = Usuario("Ciclano")

#Crindo os lances de Fulano e Ciclano
lance_do_fulano = Lance(fulano, 500)
lance_do_ciclano = Lance(ciclano, 1500)

#Criando um leilao
leilao = Leilao("Celular")

#Adicionando os lances de Fulano e Ciclano ao leilao
leilao.lances.append(lance_do_fulano)
leilao.lances.append(lance_do_ciclano)

#Imprimindo os lances do leilao
for lance in leilao.lances:
    print("O usuário {} deu um lance de {}.".format(lance.usuario.nome, lance.valor))

#Criando um avaliador
avaliador = Avaliador()

#Avaliando o leilao
avaliador.avalia(leilao)

#Imprimindo os valores do menor e maior lance
print("O menor lance foi: {}. E o maior lance foi: {}.".format(avaliador.menor_lance, avaliador.maior_lance))