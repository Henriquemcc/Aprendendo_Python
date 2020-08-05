# url = "pagina?argumentos"
# indice = url.find("?")
# print(url[indice+1:])

from ExtratorArgumentosUrl import ExtratorArgumentosUrl

teste = ExtratorArgumentosUrl("https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700%E2%80%9D")
moeda_origem, moeda_destino = teste.extrair_argumentos()

print("Moeda Origem: {}".format(moeda_origem))
print("Moeda Destino: {}".format(moeda_destino))