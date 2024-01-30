import requests
from bs4 import BeautifulSoup

def buscarNoMercadoLivre(nomeBusca, valorBusca):

    """
    Realiza uma busca por produtos no Mercado Livre, filtrando por nome e valor máximo.

    Parâmetros:
    - nomeBusca (str): O título da busca para os produtos no Mercado Livre.
    - valorBusca (float): O preço máximo que a busca deve considerar.

    Retorna:
    Uma lista de tuplas contendo links e preços dos produtos encontrados.
    Cada tupla tem a seguinte estrutura: (link_do_produto, preco_do_produto).

    Funcionamento:
    1. Constrói o link de busca no site da Magazine Luiza com base no nome fornecido.
    2. Realiza uma requisição HTTP para obter o conteúdo da página.
    3. Utiliza a biblioteca BeautifulSoup para analisar o HTML da página e extrair informações.
    4. Procura por elementos HTML específicos que contêm informações sobre produtos e preços.
    5. Filtra os resultados com base no preço máximo fornecido.
    6. Retorna uma lista de tuplas com links e preços dos produtos que atendem aos critérios.

    Detalhes:
    - Utiliza a biblioteca BeautifulSoup para fazer o parsing da página HTML do Mercado Livre.
    - Os links e preços dos produtos são extraídos das tags HTML correspondentes.
    - Os resultados são filtrados com base no valor máximo especificado.
    - Retorna uma lista de produtos que atendem aos critérios de busca.

    Nota:
    Certifique-se de ter as bibliotecas `requests` e `BeautifulSoup` instaladas para utilizar esta função.

    """

    link = 'https://lista.mercadolivre.com.br/' + nomeBusca

    requisicao = requests.get(link) #Importação do link

    try:
        site = BeautifulSoup(requisicao.text, "html.parser") #Pra ficar na estrutura normal do html
        pesquisa = site.find_all("li", "ui-search-layout__item")
        precos = site.find_all("span", "andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript")

        #Enchendo o vetor com os preços, na ordem das classes especificadas no site:
        listaPrecos = []
        for preco in precos:

            preco = str(preco).split('"') #Separa as strings por aspas duplas, colocando-as em uma lista
            aux = str(preco[1]).split() #Separa as strings por espaços simples

            valor = 0.0
            if len(aux) > 2:
                
                valor = float(aux[0]) + (float(aux[3])/100)
            else:

                valor = float(aux[0])

            listaPrecos.append(valor)


        #Colocando os links com o preço respectivo da busca encontrada:
        listaRetorno = []
        for i, pesq in enumerate(pesquisa):

            if(len(listaPrecos) > i):
                if listaPrecos[i] < valorBusca:
                
                    listaRetorno.append((str(pesq.a['href']), listaPrecos[i]))


        return listaRetorno
    except:

        return []

'''
nomeBusca = input('Insira o titulo de sua busca: ')
valorBusca = float(input('Informe o preço máximo que a busca deve ter: '))

lista = buscarNoMercadoLivre(nomeBusca, valorBusca)
for i in lista:
    print(i)
'''
