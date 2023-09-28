# Trabalho Análise de Dataset - Tópicos Especiais de Software
Alunos: Hellen Gurgacz, Julia Scheffer, Gabriel Tavares, Sara Alves

Dataset: Músicas mais tocadas no Spotify 2023
https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023

Nosso objetivo com este dataset é realizar análises referente aos dados que nos foram fornecidos.

Realizaremos o pré-processamento dos dados, incluindo a limpeza de dados ausentes, a normalização de dados numéricos, a codificação de variáveis categóricas e a transformação de dados, conforme necessário.
Faremos uma análise exploratória da compreensão da estrutura do conjunto de dados, a visualização de distribuições e a detecção de outliers.

#mais tocadas 
import pandas as pd
import matplotlib.pyplot as plt

# Carrega DataFrame
df = pd.read_csv("spotify2023.csv")


ano_desejado = int(input("Digite o ano desejado: "))

# Converter a coluna "streams" para valores numéricos
df["streams"] = pd.to_numeric(df["streams"], errors="coerce")

# Remover linhas com valores NaN (se houver)
df = df.dropna(subset=["streams"])

# Filtrar as músicas do ano desejado
df_ano = df[df["released_year"] == ano_desejado]

# Classificar o DataFrame pelas músicas mais tocadas em ordem decrescente
df_ano = df_ano.sort_values(by="streams", ascending=False)

# Especificar o número de músicas a serem exibidas no ranking
num_musicas_no_ranking = 10

# Selecionar as N músicas mais tocadas do ano desejado
top_musicas_ano = df_ano.head(num_musicas_no_ranking)

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
#criando grafico na horizontal
plt.barh(top_musicas_ano["track_name"], top_musicas_ano["streams"], color="skyblue")
plt.xlabel("Streams")
plt.ylabel("Música")
plt.title(
    f"Top {num_musicas_no_ranking} Músicas lançadas {ano_desejado} mais tocadas em 2023"
)
plt.gca().invert_yaxis()  # Inverter a ordem das músicas para a mais tocada no topo

# Mostrar o gráfico
plt.show()


#Musicas 2023 

import pandas as pd

# Carrega o DataFrame 
df = pd.read_csv("spotify2023.csv")

while True:
    # Insira o nome do artista
    artista_pesquisado = input(
        "Digite o nome do artista (ou 'listar' para ver a lista de artistas, ou 'sair' para encerrar): "
    )

    if artista_pesquisado.lower() == "sair":
        print("Encerrando o programa.")
        break  # Encerrar o loop e o programa

    if artista_pesquisado.lower() == "listar":
        # Mostrar lista de artistas disponíveis
        artistas_disponiveis = df["artist(s)_name"].unique()
        print("\nArtistas disponíveis:")
        for artista in artistas_disponiveis:
            print(artista)
        continue  # Voltar ao início do loop

    # Filtrar as músicas desse artista
    musicas_artista = df[df["artist(s)_name"] == artista_pesquisado]

    # Verificar se o artista foi encontrado no DataFrame
    if not musicas_artista.empty:
        # Encontrar a música mais tocada do artista
        musica_mais_tocada = musicas_artista[
            musicas_artista["streams"] == musicas_artista["streams"].max()
        ]

        # Imprimir o nome do artista e a música mais tocada
        print(f"Artista: {artista_pesquisado}")
        print(f"Música mais tocada: {musica_mais_tocada.iloc[0]['track_name']}")
    else:
        print(f"Artista '{artista_pesquisado}' não encontrado no DataFrame.")


#Playlist que a musica mais tocou
import pandas as pd


df = pd.read_csv("spotify2023.csv")

#  insira o nome da música
nome_musica = input("Insira o nome da música: ")

# Filtrar as linhas que correspondem à música específica
musicas_filtradas = df[df["track_name"] == nome_musica]

# Obter o número de playlists em que a música está 
# values[0]  valor na primeira posição desse array
num_playlists = musicas_filtradas["in_spotify_playlists"].values[0]

if num_playlists > 0:
    print(f"A música '{nome_musica}' está em {num_playlists} playlists do Spotify.")
else:
    print(f"A música '{nome_musica}' não está em nenhuma playlist do Spotify.")

#Posição da musica 
import pandas as pd

# Carregue o arquivo CSV em um DataFrame
df = pd.read_csv("spotify2023.csv")

while True:
    # Insira o nome do artista
    artista_interesse = input(
        "Digite o nome do artista (ou 'listar' para ver a lista de artistas, ou 'sair' para encerrar): "
    )

    if artista_interesse.lower() == "sair":
        print("Encerrando o sistema.")
        break  # Encerrar o loop e o programa

    if artista_interesse.lower() == "listar":
        # Mostrar lista de artistas disponíveis
        artistas_disponiveis = df["artist(s)_name"].unique()
        print("\nArtistas disponíveis:")
        for artista in artistas_disponiveis:
            print(artista)
        continue  # Voltar ao início do loop

    # Filtrar as músicas desse artista
    df_artista = df[df["artist(s)_name"] == artista_interesse]

    # Exibir as posições nas paradas para cada música do artista
    for index, row in df_artista.iterrows():
        print(
            f"A música '{row['track_name']}' ficou na posição {row['in_spotify_charts']} nas paradas do Spotify."
        )

#Ranking das musicas

import pandas as pd
import matplotlib.pyplot as plt

# Carregue o arquivo CSV em um DataFrame
df = pd.read_csv("spotify2023.csv")

# Agrupe os dados por nome do artista e calcule a média das posições nas paradas
# mean usado para calcular as medicas depois do agrupamento
rank_artistas = df.groupby("artist(s)_name")["in_spotify_charts"].mean().reset_index()

# Classifique o DataFrame com base na média das posições nas paradas
rank_artistas = rank_artistas.sort_values(by="in_spotify_charts")

# usuário insira o número de artistas a serem exibidos no gráfico
num_artistas_exibidos = int(
    input("Digite o número de artistas a serem exibidos no gráfico: ")
)
# Filtrar os N artistas com as melhores posições nas paradas
# head para selecionar as primeiras N linhas do DataFrame
top_artistas = rank_artistas.head(num_artistas_exibidos)


# Criar o gráfico de barras
plt.figure(figsize=(10, 5))

#criando grafico horizontal nomes e as medias da posições 
plt.barh(
    top_artistas["artist(s)_name"], top_artistas["in_spotify_charts"], color="skyblue"
)
plt.xlabel("Média das Posições nas Paradas do Spotify")
plt.ylabel("Artista")
plt.title(
    f"Ranking dos {num_artistas_exibidos} Melhores Artistas nas Paradas do Spotify"
)

# Mostrar o gráfico
plt.show()
