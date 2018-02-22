import json
import sys
import requests


class Crawler:
    def __init__(self, uf):
        self.url = "http://www.cnj.jus.br/bnmp/rest/pesquisar"
        self.uf = uf
        input("Teste uf: " + uf + " pode ir?")
        self.total_paginas = self.baixa_estado(acha_total_pagina=True) // 10 # quantidade de páginas por pesquisas
        self.arquivo_dados = open("dados_mandados.json", "a")
        print("Total de paginas é {} \n\n".format(self.total_paginas))

        for i in range(1, self.total_paginas + 1):
            print("Baixando {}...".format(i))
            self.salva_dados(self.baixa_estado(n_pagina = i))


    def baixa_estado(self, n_pagina = None, acha_total_pagina = False):
        if n_pagina is None:
            n_pagina = 1
        pagina_dict = '{"paginaAtual":' + str(n_pagina) + '}'
        dados = '{"criterio":{"orgaoJulgador":{"uf":"' + self.uf + '","municipio":"","descricao":""},"orgaoJTR":{},"parte":{"documentos":[{"identificacao":null}]}},"paginador":' + pagina_dict + ',"fonetica":"true","ordenacao":{"porNome":false,"porData":false}}'
        headers = {'Accept':'application/json, text/plain, */*',
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language":"pt-BR,pt;q=0.8,en-US;q=0.6,en;q=0.4",
                "Connection":"keep-alive",
                "Content-Length":"213",
                "Content-Type":"application/json;charset=UTF-8",
                "Host":"www.cnj.jus.br",
                "Origin":"http://www.cnj.jus.br",
                "Referer":"http://www.cnj.jus.br/bnmp/",
                "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"}
        for k in range(1000):
            try:
                pagina = requests.post(self.url, data=dados, headers = headers)
                break
            except:
                pass
        dados_volta = json.loads(pagina.text)
        if acha_total_pagina:
            return dados_volta['paginador']['totalRegistros']
        return dados_volta['mandados']

    def salva_dados(self, dados):
        for j in dados:
            self.arquivo_dados.write(json.dumps(j) + '\n')

x = Crawler(sys.argv[1])
