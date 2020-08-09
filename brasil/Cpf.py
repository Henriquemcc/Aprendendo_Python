class Cpf:
    #Metodo construtor
    def __init__(self, cpf):
        cpf = str(cpf)
        if self.__cpf_eh_valido(cpf):
            self.__cpf = cpf
        else:
            raise ValueError("Cpf Inválido!!")
    #Fim do metodo __init__

    #Verifica se o cpf eh valido
    def __cpf_eh_valido(self, cpf):
        eh_valido = False

        #Verificando o tamanho do cpf
        if len(cpf) == 11:
            #Verificando o primeiro digito verificador

            # Calculando o primeiro digito verificador
            divisao = (int(cpf[0])*10 + int(cpf[1])*9 + int(cpf[2])*8 + int(cpf[3])*7 + int(cpf[4])*6 + int(cpf[5])*5 + int(cpf[6])*4 + int(cpf[7])*3 + int(cpf[8])*2) / 11
            resto = (int(cpf[0])*10 + int(cpf[1])*9 + int(cpf[2])*8 + int(cpf[3])*7 + int(cpf[4])*6 + int(cpf[5])*5 + int(cpf[6])*4 + int(cpf[7])*3 + int(cpf[8])*2) % 11
            if(resto == 0 or resto == 1):
                primeiro_digito_verificador = 0
            else:
                primeiro_digito_verificador = 11 - resto

            # Verificando se o primeiro digito verificador eh igual ao digito verificador calculado
            if str(primeiro_digito_verificador) == cpf[9]:
                #Verificando o segundo digito verificador

                # Calculando o segundo digito verificador
                divisao = (int(cpf[0]) * 11 + int(cpf[1]) * 10 + int(cpf[2]) * 9 + int(cpf[3]) * 8 + int(cpf[4]) * 7 + int(cpf[5]) * 6 + int(cpf[6]) * 5 + int(cpf[7]) * 4 + int(cpf[8]) * 3 + int(cpf[9]) * 2) / 11
                resto = (int(cpf[0]) * 11 + int(cpf[1]) * 10 + int(cpf[2]) * 9 + int(cpf[3]) * 8 + int(cpf[4]) * 7 + int(cpf[5]) * 6 + int(cpf[6]) * 5 + int(cpf[7]) * 4 + int(cpf[8]) * 3 + int(cpf[9]) * 2) % 11
                if(resto == 0 or resto == 1):
                    segundo_digito_verificador = 0
                else:
                    segundo_digito_verificador = 11 - resto

                # Verificando se o segundo digito verificador eh igual ao digito verificador calculado
                if str(segundo_digito_verificador) == cpf[10]:
                    eh_valido=True

        return eh_valido
    #Fim do metodo __cpf_eh_valido

    #Metodo get do cpf
    @property
    def cpf(self):
        return self.__cpf
    #Fim do metodo cpf

    #Formata o cpf para que ele fique com pontos e um traco
    def formatar_cpf(self):
        return "{}.{}.{}-{}".format(self.cpf[:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:])
    #Fim do metodo formatar_cpf

    #Metodo que converte a classe em str
    def __str__(self):
        return self.formatar_cpf()
    #Fim do metodo __str__