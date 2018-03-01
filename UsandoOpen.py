import sys

# Arquivo
arquivo = open('arquivo.txt', 'r')

for i in range(0,100):
    print(i)
    print(arquivo.read())

# Método - main
def main():
    try:
        arquivo = sys.argv[1]
    except:
        print("Necessário fornecer um parâmetro: nome do arquivo")
        sys.exit(1)


    try:
        f = open(arquivo)
        for linha in f.readlines():
            limpa = linha.strip("\n")
            print(limpa)
        f.close()
    except IOError:
        print("Não foi possível abrir arquivo", arquivo)
        sys.exit(1)

if __name__ == "__main__":
    main()














