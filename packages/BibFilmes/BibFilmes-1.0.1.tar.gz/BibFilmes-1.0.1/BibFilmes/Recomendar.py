"""
Script para encontrar e mostrar títulos de filmes no IMDb com base em um gênero específico.

Dependências:
    - BeautifulSoup
    - requests
"""

from bs4 import BeautifulSoup
import requests
def Recomendar(genero):
  while True:
    # Solicita que o usuário insira o nome do gênero em inglês ou 'sair' para encerrar


    # Verifica se o usuário deseja encerrar o programa
    if genero.lower() == 'sair':
        print("Programa encerrado.")
        break

    # Constrói a URL para acessar a página de pesquisa no IMDb com base no gênero fornecido
    url = f'https://www.imdb.com/search/title/?title_type=feature&genres={genero}&user_rating=,10&sort=num_votes,desc'

    # Cabeçalhos para a requisição HTTP
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"}

    # Realiza a requisição HTTP para obter o conteúdo da página
    requisicao = requests.get(url, headers=headers)

    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if requisicao.status_code == 200:
        # Utiliza o BeautifulSoup para analisar o conteúdo HTML da página
        site = BeautifulSoup(requisicao.text, "html.parser")
        # Encontra todos os elementos <h3> com a classe "ipc-title__text"
        pesquisa = site.find_all("h3", class_="ipc-title__text")

        # Filtra apenas os títulos dos filmes, excluindo números (considerados indesejados)
        titulos = [titulo.text.strip() for titulo in pesquisa if not titulo.text.strip().isdigit()]

        # Exibe os títulos dos filmes
        print("Títulos dos filmes:")
        for i, titulo in enumerate(titulos, start=1):
            print(f" {titulo}")
    else:
        # Exibe uma mensagem de erro caso a requisição não seja bem-sucedida
        print(f"Erro na requisição: {requisicao.status_code}")
