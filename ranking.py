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
