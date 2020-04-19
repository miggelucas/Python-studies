print ("eu posso calcular se voce vai ter que pagar alguma multa")
peso = int(input("qual o peso do peixe?: "))

if peso < 50:
	print ("tudo certo! n vai precisar pagar multa")
else:
	excesso = peso - 50
	valor = 4
	multa = excesso * valor
	print ("voce vai ter que pagar " + multa + " de multa")	
