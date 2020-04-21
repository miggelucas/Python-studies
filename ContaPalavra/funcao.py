
class Processador:
	def __init__(self, texto):
		if self.texto_eh_valido(texto):
			self.texto = texto


	def conta_caracteres(self, texto):
		numero_de_caracteres = 0
		for caracter in str(texto):
			numero_de_caracteres += 1
		return numero_de_caracteres

	def conta_palavra(self, texto):
		numero_de_palavra = 0
		lista_de_palavras = str(texto).split()
		for palavra in lista_de_palavras:
			numero_de_palavra += 1
		return numero_de_palavra

	@staticmethod
	def texto_eh_valido(texto):
		if texto == str():
			return True
		else:
			raise ValueError("não use números, pfv")