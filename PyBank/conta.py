class Conta:
    def __init__(self, nome, codigo):
        if self.nome_valido(nome):
            self.__nome = nome
        self.__codigo = codigo
        self.__carteira = 0

    def __str__(self):
        return f">>> {self.__nome} (#{self.__codigo}) tem R${self.__carteira} de saldo na carteira<<<"

    def deposita(self, valor):
        self.__carteira += valor

    def retira(self, valor):  
        if self.tem_saldo_valido(valor):
            self.__carteira -= valor
        else:
            raise ValueError("Não tem saldo o suficiente na carteira para realizar operação...")

    def transfere(self, valor, other):
        if self.tem_saldo_valido(valor):
            self.__carteira -= valor
            other.__carteira += valor
        else:
            raise ValueError("tas achando que é rico, é? \n"
                             "não tem saldo o suficiente")

    def tem_saldo_valido(self, valor):
        if valor <= self.__carteira:
            return True
        else:
            return False

    @property
    def nome(self):
        return self.__nome

    @property
    def codigo(self):
        return self.__codigo

    def extrato(self):
        print(f"Essa conta tem saldo de R${self.__carteira}")

    @property
    def carteira(self):
        return self.__carteira

    def nome_valido(self, nome):
        if type(nome) == str:
            return True
        else:
            return False