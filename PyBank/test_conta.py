from PyBank.conta import Conta
from PyBank.sistema import Sistema

import pytest

def test_deve_ser_capaz_de_adicionar_uma_conta_no_sistema():
    conta1 = Conta("lucas", 1)
    sistema = Sistema()
    sistema.adiciona_no_sistema(conta1)

def test_não_deve_permitir_adicionar_conta_com_codigo_ja_existente_ao_sistema():
    with pytest.raises(ValueError):
        conta1 = Conta("lucas", 1)
        conta2 = Conta("may", 1)

        sistema = Sistema()
        sistema.adiciona_no_sistema(conta1)
        sistema.adiciona_no_sistema(conta2)

def test_sistema_deve_ser_capaz_de_transferir_de_conta_para_outra():
    conta1 = Conta("lucas", 1)
    conta2 = Conta("may", 2)
    conta1.deposita(50)

    sistema = Sistema()
    sistema.adiciona_no_sistema(conta1)
    sistema.adiciona_no_sistema(conta2)
    sistema.sistema_transfere(conta1, 50, conta2)

    assert conta2.carteira == 50


def test_usuario_deve_ser_capaz_de_depositar_na_carteira_e_mostrar():
    conta1 = Conta("lucas", 1)
    conta1.deposita(50)

    assert conta1.carteira == 50


def test_usuario_nao_pode_sacar_mais_do_que_tem_na_carteira():
    with pytest.raises(ValueError):
        conta1 = Conta("lucas", 1)
        conta1.deposita(100)
        conta1.retira(150)

def test_deve_ser_capaz_de_realizar_transferencias():
    conta1 = Conta("lucas", 1)
    conta2 = Conta("may", 2)
    conta1.deposita(50)
    conta1.transfere(50, conta2)

def test_nao_deve_permitir_transferencias_com_valor_maior_que_carteira():
    with pytest.raises(ValueError):
        conta1 = Conta("lucas", 1)
        conta2 = Conta("may", 2)
        conta1.deposita(50)
        conta1.transfere(60, conta2)





