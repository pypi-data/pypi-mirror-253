import requests
from bs4 import BeautifulSoup

def buscarNoMercadoLivre(nomeBusca, valorBusca):
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
