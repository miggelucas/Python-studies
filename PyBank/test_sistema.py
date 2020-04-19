from PyBank.sistema import Sistema
from PyBank.conta import Conta

import pytest


def test_não_deve_permitir_criar_conta_com_codigo_ja_existente():
    with pytest.raises(ValueError):
        conta1 = Conta("lucas", 1)
        conta2 = Conta("may", 1)

        sistema = Sistema()
        sistema.adiciona_no_sistema(conta1)
        sistema.adiciona_no_sistema(conta2)
