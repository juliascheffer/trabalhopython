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
plt.barh(top_musicas_ano["track_name"], top_musicas_ano["streams"], color="skyblue")
plt.xlabel("Streams")
plt.ylabel("Música")
plt.title(
    f"Top {num_musicas_no_ranking} Músicas lançadas {ano_desejado} mais tocadas em 2023"
)
plt.gca().invert_yaxis()  # Inverter a ordem das músicas para a mais tocada no topo

# Mostrar o gráfico
plt.show()
