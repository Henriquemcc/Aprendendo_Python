class ExtratorArgumentosUrl:
    #Metodo construtor
    def __init__(self, url):
        self.url = url

    #Retorna o valor da variavel url
    @property
    def url(self):
        return self.__url

    #Altera o valor da variavel url
    @url.setter
    def url(self, url):
        if (url is not None) and (type(url) == str) and bool(url):
            self.__url = url
        else:
            raise LookupError("URL inválida!")

    #Retorna os nomes das moedas de origem e de destino respectivamente
    def obter_nome_moedas(self):
        #Declarando os parametros utilizados na URL para definir as moedas de origem e destino
        argumento_moeda_origem = "moedaorigem"
        argumento_moeda_destino = "moedadestino"

        #Obtendo a moeda de origem
        indice_inicial_moeda_origem = self.__obter_indice_inicial_do_argumento(argumento_moeda_origem)
        indice_final_moeda_origem = self.url.find("&", indice_inicial_moeda_origem)
        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        #Obtendo a moeda de destino
        indice_inicial_moeda_destino = self.__obter_indice_inicial_do_argumento(argumento_moeda_destino)
        indice_final_moeda_destino = self.url.find("&", indice_inicial_moeda_destino)
        moeda_destino = self.url[indice_inicial_moeda_destino:indice_final_moeda_destino]

        return moeda_origem, moeda_destino

    #Retorna o indice inicial do argumento da URL
    def __obter_indice_inicial_do_argumento(self, parametro):
        return self.url.find(parametro) + len(parametro) + 1