import pandas as pd

# Supondo que você já carregou seus dados em um DataFrame chamado 'df'
# Se você não tiver carregado os dados ainda, carregue-os da maneira apropriada.
df = pd.read_csv("spotify2023.csv")

# Solicite que o usuário insira o nome da música
nome_musica = input("Insira o nome da música: ")

# Filtrar as linhas que correspondem à música específica
musicas_filtradas = df[df["track_name"] == nome_musica]

# Obter o número de playlists em que a música está
num_playlists = musicas_filtradas["in_spotify_playlists"].values[0]

if num_playlists > 0:
    print(f"A música '{nome_musica}' está em {num_playlists} playlists do Spotify.")
else:
    print(f"A música '{nome_musica}' não está em nenhuma playlist do Spotify.")
