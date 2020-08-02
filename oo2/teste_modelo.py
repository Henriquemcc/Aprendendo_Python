from modelo import Filme, Serie

#Filme Duro de Matar
duro_de_matar = Filme("Duro de Matar", 1988, 132)
duro_de_matar.dar_like()
duro_de_matar.dar_like()
duro_de_matar.dar_like()
duro_de_matar.dar_like()
duro_de_matar.dar_like()
duro_de_matar.dar_like()
duro_de_matar.dar_like()
duro_de_matar.dar_like()

#Serie Sherlock
sherlock = Serie("Sherlock", 2010, 4)
sherlock.dar_like()
sherlock.dar_like()
sherlock.dar_like()
sherlock.dar_like()
sherlock.dar_like()
sherlock.dar_like()

filmes_e_series = [duro_de_matar, sherlock]

for programa in filmes_e_series:
    if(hasattr(programa, 'duracao')):
        detalhes = programa.duracao
    else:
        detalhes = programa.temporadas

    print("Nome: {} - Ano: {} - D: {} - Likes: {}".format(programa.nome, programa.ano, detalhes, programa.likes))
