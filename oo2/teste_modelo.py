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
print("Nome: {} - Ano: {} - Duração: {} - Likes: {}".format(duro_de_matar.nome, duro_de_matar.ano, duro_de_matar.duracao, duro_de_matar.likes))

#Serie Sherlock
sherlock = Serie("Sherlock", 2010, 4)
sherlock.dar_like()
sherlock.dar_like()
sherlock.dar_like()
sherlock.dar_like()
sherlock.dar_like()
sherlock.dar_like()
print("Nome: {} - Ano: {} - Temporadas: {} - Likes: {}".format(sherlock.nome, sherlock.ano, sherlock.temporadas, sherlock.likes))
