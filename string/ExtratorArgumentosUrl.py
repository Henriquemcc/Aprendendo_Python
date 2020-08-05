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

    def extrair_argumentos(self):

        indice_inicial_moeda_origem = self.url.find("=")+1
        indice_final_moeda_origem = self.url.find("&", indice_inicial_moeda_origem)

        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        indice_inicial_moeda_destino = self.url.find("=", indice_final_moeda_origem) + 1
        indice_final_moeda_destino = self.url.find("&", indice_inicial_moeda_destino)

        moeda_destino = self.url[indice_inicial_moeda_destino:indice_final_moeda_destino]

        return moeda_origem, moeda_destino





