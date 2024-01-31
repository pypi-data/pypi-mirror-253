from bs4 import BeautifulSoup
import requests
import pandas as pd
# Precisa instalar o puyarrow

def Tabelar(genero, opcao):




    if opcao == 1:
        url = f'https://www.imdb.com/search/title/?title_type=feature&genres={genero}&user_rating=,10&sort=user_rating,desc'
    elif opcao == 2:
        url = f'https://www.imdb.com/search/title/?title_type=feature&genres={genero}&user_rating=,10&sort=num_votes,desc'
    else:
        print("Opção inválida.")


    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"}

    requisicao = requests.get(url, headers=headers)

    if requisicao.status_code == 200:
        site = BeautifulSoup(requisicao.text, "html.parser")
        pesquisa = site.find_all("h3", class_="ipc-title__text")
        avaliacaoimdb = site.find_all("span", class_="ipc-rating-star")

        # Filtrando apenas os títulos
        titulos = [titulo.text.strip() for titulo in pesquisa if not titulo.text.strip().isdigit()]

        # Criando listas para os dados
        dados = {'Título do Filme': [], 'Avaliação IMDb': [], 'Número de Votos': []}

        for i, titulo in enumerate(titulos, start=1):
            # Encontrando a avaliação IMDb correspondente ao título
            indice = i - 1

            rating_element = avaliacaoimdb[indice]
            rating = rating_element["aria-label"].split(":")[
                -1].strip() if "aria-label" in rating_element.attrs else "Sem avaliação"

            # Encontrando o número de votos correspondente ao título
            vote_count_element = rating_element.find_next("span", class_="ipc-rating-star--voteCount")
            vote_count = vote_count_element.text.strip() if vote_count_element else "Sem dados de votos"

            # Adicionando os dados às listas
            dados['Título do Filme'].append(titulo)
            dados['Avaliação IMDb'].append(rating)
            dados['Número de Votos'].append(vote_count)

            # Imprime o título, a avaliação IMDb e o número de votos
            print(f"{titulo} - IMDb: {rating}, Votos: {vote_count}")

        # Criando um DataFrame com os dados
        df = pd.DataFrame(dados)

        # Salvando o DataFrame em um arquivo CSV
        df.to_csv(f'{genero}_filmes.csv', index=False)
        print(f'Tabela salva em {genero}_filmes.csv')
    else:
        print(f"Erro na requisição: {requisicao.status_code}")
