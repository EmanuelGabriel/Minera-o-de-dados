# Importando as dependências da API - SINESP
"""
 Le um arquivo delimitado e mostra os campos na tela.
"""

from sinesp_client import SinespClient
import requests
import json
import csv

# Mineração de dados dos veículos/Piauí
# Criado na data: Quinta-feira - 01/03/2018
# Autor: Emanuel A. Gabriel
# Usando API Pública do SINESP
# Mineração de dados



# Entrada da dados para acesso


busca = SinespClient(proxy_address='proxy.tjpi.local', proxy_port=3128)
dados_do_veiculo = input("Digite a PLACA do Veículo: EX. ABC1234: ")

# Buscando os dados digitados no campo - 'dados_do_veiculo'
resultado = busca.search(dados_do_veiculo)

# Abrindo arquivos - dados_de_veiculos
f = open("veiculos_pi.csv", "w")

situcao = csv.writer(f)


modelo_da_api = '''return_code return_message status_code status_message chassis
             model brand color year model_year plate date city state'''.split()


situcao.writerow(modelo_da_api)
# Fechando a conexãoreturn_code
f.close()


# Exibir os resultados
print("Exibindo os dados: ", resultado)






