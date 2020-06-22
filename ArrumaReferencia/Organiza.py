""" 
Sort a .txt file

"""

with open("Referências.txt", "r", encoding = "utf-8") as arquivo:

	ref = sorted(arquivo)
		
	with open("ref_org.txt", "w", encoding = "utf-8") as ref_org:
		ref_org.writelines(ref)
	
