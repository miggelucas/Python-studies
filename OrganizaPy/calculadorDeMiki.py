import argparse


def somar(operador1, operador2):
    return operador1 + operador2


def subtrair(operador1, operador2):
    return operador1 - operador2


def multiplicar(operador1, operador2):
    return operador1 * operador2


def dividir(operador1, operador2):
    return operador1 / operador2


def exponeciar(operador1, operador2):
    return operador1 ** operador2


def resto(operador1, operador2):
    return operador1 % operador2


calculadora = {"+": somar,
              "-": subtrair,
              "*": multiplicar,
              "/": dividir,
              "e": exponeciar,
              "r": resto
              }


parser = argparse.ArgumentParser(description='ler arquivo de pastas..')

parser.add_argument("operation", choices=calculadora.keys(),
                    help="escolha o operador a ser aplicado nos interiros")

parser.add_argument("inteiros", metavar="I", nargs=2, type=int,
                    help="i deve ser pertencente aos numeros interios")


args = parser.parse_args()
operator = args.operation
inteiros = args.inteiros
resultado = calculadora[operator](inteiros[0], inteiros[1])
print(resultado)
