from extrator_argumentos_url import ExtratorArgumentosUrl

url_byte_bank = ExtratorArgumentosUrl("https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700%E2%80%9D")
moeda_origem, moeda_destino = url_byte_bank.obter_nome_moedas()

print("Moeda Origem: {}".format(moeda_origem.capitalize()))
print("Moeda Destino: {}".format(moeda_destino.capitalize()))