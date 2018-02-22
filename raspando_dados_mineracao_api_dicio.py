# Importando dependência do -> Dicio
from dicio import Dicio

# Criar uma instância do objeto Dicio
dicio = Dicio() # Criado a instância do objeto

# Fazer pesquisa pelo o objeto passado
# palavra = dicio.search("palavra de pesquisa aqui")

entrada_input = str(input("Digite a palavra para pesquisa: "))
palavra = dicio.search(entrada_input)

# Exibir os resultados
# -> palavras.url,
print(palavra, palavra.url, "\n", palavra.meaning)

# Exibir sinônimos da palavra passada na pesquisa
print(palavra.synonyms)

# Exibir informações extras acerca da palavra passada na pesquisa
for chave, p in palavra.extra.items():
    print(chave, "Detalhes: => ", p)


# Carregar informações sobre o primeiro sinônimo da palavra pesquisada
# Imprima a palavra, o URL e o significado do primeiro sinônimo

palavra.synonyms[0].load()
print(palavra.synonyms[0], palavra.synonyms[0].url, "\n", palavra.synonyms[0].meaning)
