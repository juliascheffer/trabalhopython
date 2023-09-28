import pandas as pd

# Carregar o DataFrame a partir do arquivo CSV
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
