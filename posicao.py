import pandas as pd

# Carregue o arquivo CSV em um DataFrame
df = pd.read_csv("spotify2023.csv")

while True:
    # Insira o nome do artista
    artista_interesse = input(
        "Digite o nome do artista (ou 'listar' para ver a lista de artistas, ou 'sair' para encerrar): "
    )

    if artista_interesse.lower() == "sair":
        print("Encerrando o programa.")
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
