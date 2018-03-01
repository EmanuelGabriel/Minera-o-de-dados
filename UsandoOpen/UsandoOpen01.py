import sys

# Abrir arquivos em Python


""" 
'W' -> WRITE -> ESCREVER 
'R' -> READ -> LER
'A' -> APPEND -> EXTENDER

"""

"""
arquivo = open("OlaArquivo.txt", "w")

# O READ vai escrever qualquer coisa
arquivo.write("Situação com pyton, usando Open em Pyton")
arquivo.write("\n")
arquivo.write("Manga com leite")
#arquivo.writelines(["Ola", "arquivo", "essa", "situação"])


# Fechar o arquivo
arquivo.close()

"""


"""

# Ler o arquivo
arquivo = open("OlaArquivo.txt", "r")

print(arquivo.readlines())

for i in range(2):
    x = arquivo.readline()
    print(x)

arquivo.close()


"""


# Usando o APPEND - VAI PROCURAR, ABRIR O ARQUIVO E O MOSTRAR O ÚLTIMO CARACTERE
arquivo = open("OlaArquivo.txt", "a")
arquivo.write("\nNesta situação os dados estão sendo adicionados com o APPEND")


arquivo.close()










