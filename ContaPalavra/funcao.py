
class Processador:
	def __init__(self, texto):
		if self.texto_eh_valido(texto):
			self.texto = texto

	def __str__(self):
		return f"O texto possui um total de {self.conta_caracteres()} caracteres e {self.conta_palavras()} palavras"

	def conta_caracteres(self):
		numero_de_caracteres = 0
		for caracter in str(self.texto):
			numero_de_caracteres += 1
		return numero_de_caracteres

	def conta_palavras(self):
		numero_de_palavra = 0
		lista_de_palavras = str(self.texto).split()
		for palavra in lista_de_palavras:
			numero_de_palavra += 1
		return numero_de_palavra

	@staticmethod
	def texto_eh_valido(texto):
		if type(texto) == type("string"):
			return True
		else:
			raise ValueError("não use números, pfv")