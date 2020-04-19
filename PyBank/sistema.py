from PyBank.conta import Conta

class Sistema():
    def __init__(self):
        self.__clientes = []

    def cria_conta(self, nome, codigo):
        conta_nova = Conta(nome, codigo)
        self.adiciona_no_sistema(conta_nova)

    def adiciona_no_sistema(self, conta_nova):
        if self.codigo_livre(conta_nova):
            self.__clientes.append(conta_nova)
        else:
            raise (ValueError("Já existe no sistema uma conta com esse código"))

    def remove_do_sistema(self, conta):
        self.__clientes.remove(conta)

    def lista_de_clientes(self):
        for conta in self.__clientes:
            print(conta)

    def sistema_transfere(self, origem, valor, destino):
        if self.transferencia_valida(origem, valor):
            origem.transfere(valor, destino)
        else:
            raise ValueError("transferencia invalida")

    def codigo_livre(self, conta_nova):
        # função verifica se ja tem uma conta com o mesmo código
        for conta in self.__clientes:
            if conta_nova.codigo == conta.codigo:
                return False
        return True


    def transferencia_valida(self, origem, valor):
        if origem.tem_saldo_valido(valor):
            return True
        else:

            return False
