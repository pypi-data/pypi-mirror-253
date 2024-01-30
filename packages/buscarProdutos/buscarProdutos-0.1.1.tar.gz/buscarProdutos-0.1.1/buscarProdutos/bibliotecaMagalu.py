import requests
from bs4 import BeautifulSoup

def buscarNaMagalu(nomeDaBusca, precoBusca):

    """
    Realiza uma busca no site da Magazine Luiza com base no nome do produto e verifica se o preço
    é menor que o valor especificado.

    Parâmetros:
    - nomeDaBusca (str): O nome do produto a ser pesquisado no site da Magazine Luiza.
    - precoBusca (float): O preço máximo que o produto pode ter para ser incluído nos resultados.

    Retorno:
    Uma lista de tuplas contendo o link do produto e seu preço, se o preço for menor que precoBusca.
    Cada tupla tem a seguinte estrutura: (link_do_produto, preco_do_produto).

    Funcionamento:
    1. Constrói o link de busca no site da Magazine Luiza com base no nome fornecido.
    2. Realiza uma requisição HTTP para obter o conteúdo da página.
    3. Utiliza a biblioteca BeautifulSoup para analisar o HTML da página e extrair informações.
    4. Procura por elementos HTML específicos que contêm informações sobre produtos e preços.
    5. Filtra os resultados com base no preço máximo fornecido.
    6. Retorna uma lista de tuplas com links e preços dos produtos que atendem aos critérios.

    Exemplo de Uso:
    -> python3 biblioteca.py
    # Início, só para pegar os valores:
    -> nomeDaBusca = input('Insira o que você busca: ')
    -> precoBusca = float(input('Insira o preço que não pode ser ultrapassado: '))
    -> retorno = buscarNaMagalu(nomeDaBusca, precoBusca)


    Nota:
    Certifique-se de ter as bibliotecas `requests` e `BeautifulSoup` instaladas para utilizar esta função.

    Dica:
    Considere utilizar ambientes virtuais para isolar as dependências deste script de outros projetos Python.
    """

    #Importando o link:
    link = 'https://www.magazineluiza.com.br/busca/' + nomeDaBusca + '/' #Link para a busca simples na magalu
    requisicao = requests.get(link) #Importação do link

    try:
        site = BeautifulSoup(requisicao.text, "html.parser") #Pra ficar na estrutura normal do html

        pesquisa = site.find_all("li", "sc-kTbCBX ciMFyT")
        precos = site.find_all("div", "sc-dhKdcB ryZxx")
        #print(requisicao.text)
        #print(site)
        listaDeValores = []
        listaRetorno = []
        for preco in precos:
            
            valor = str(preco).split("<")
            valor = valor[2].split(">")
            valor = valor[1].split()
            listaAuxiliar = ''
            for a in valor:
                listaAuxiliar = a
            
            listaAuxiliar = listaAuxiliar.replace(',', '.') #Troca as ',' pelos '.'
            listaAuxiliar = listaAuxiliar.split('.') # Tira os pontos do valor, separando os números em índices da lista
            valorFinal = '' #Responsável por pegar o número
            for i in listaAuxiliar:
                    
                valorFinal += i
            listaDeValores.append(float(valorFinal) / 100.0)

        for i, pesq in enumerate(pesquisa):

            if len(listaDeValores) < i:
                break
            linkBusca = 'https://www.magazineluiza.com.br/'
            linkBusca += pesq.a['href']
            if listaDeValores[i] < precoBusca:
                
                listaRetorno.append((linkBusca, listaDeValores[i])) 
            

        return listaRetorno
    except:

        return []

#Início, só para pegar os valores:

nomeDaBusca = input('Insira o que você busca: ')
precoBusca = float(input('Insira o preço que não pode ser ultrapassado: '))
retorno = buscarNaMagalu(nomeDaBusca, precoBusca)

for i in retorno:
    print(i)
