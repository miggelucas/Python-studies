from funcao import Processador

def test_deve_contar_palavras():
	texto = "eu gosto muito de macaxeira frita com calabresa acebolada"
	processador = Processador(texto)
	numero_de_palavras = processador.conta_palavras()

	assert numero_de_palavras == 9

def test_deve_contar_caracteres():
	texto = "eu gosto muito de macaxeira frita com calabresa acebolada"
	processador = Processador(texto)
	numero_de_caracteres = processador.conta_caracteres()

	assert numero_de_caracteres == 57

	