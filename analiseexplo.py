import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\jlsch\\Documents\\trab-spotify\\spotify2023-tratados.csv", encoding="latin-1")

#print(df.head())

# ANALISE EXPLORATORIA:

# resumo estatístico:
colunas_de_interesse = ['track_name', 'artist(s)_name', 'streams', 'artist_count', 'released_year', 'released_month', 'in_spotify_charts', 'in_spotify_playlists']
df_resumo = df[colunas_de_interesse]

estatisticas_descritivas = df_resumo.describe()

# printar resumo estatístico formatado
print("Resumo Estatístico:")
print(estatisticas_descritivas.to_string())

# histograma das streams
plt.figure(figsize=(10, 6))
sns.histplot(df['streams'], bins=20, kde=True, color='white')
plt.title("Distribuição das Streams em 2023")
plt.xlabel("Streams")
plt.ylabel("Contagem")
plt.grid(True)
plt.show()

df['streams'] = pd.to_numeric(df['streams'], errors='coerce')

# outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x='streams', data=df, color='skyblue')
plt.title("Identificação de Outliers em Streams")
plt.xlabel("Streams")
plt.grid(True)
plt.show()

# top 10 músicas mais tocadas lançadas em 2023
musicas_2023 = df[df['released_year'] == 2023]
top_10_musicas_2023 = musicas_2023.nlargest(10, 'streams')

plt.figure(figsize=(12, 8))
sns.barplot(x='streams', y='track_name', data=top_10_musicas_2023, palette="viridis", hue='artist(s)_name')
plt.title("Top 10 Músicas Mais Tocadas Lançadas em 2023")
plt.xlabel("Número de Streams")
plt.ylabel("Nome da Música")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.legend(title="Artista")
plt.show()

# gráfico de variação de streams ao longo dos meses
plt.figure(figsize=(12, 6))
musicas_2023 = df[df['released_year'] == 2023]
streams_por_mes = musicas_2023.groupby('released_month')['streams'].sum().reset_index()
sns.lineplot(x='released_month', y='streams', data=streams_por_mes, marker='o', color='blue')
plt.title("Variação das Streams ao Longo dos Meses em 2023")
plt.xlabel("Mês")
plt.ylabel("Total de Streams")
plt.grid(True)
plt.xticks(range(1, 13), labels=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.show()

# correlações - entre streams, musicas presentes em playlists e o ano de lançamento
correlacoes = df[['streams', 'in_spotify_playlists', 'released_year']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlacoes, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlações entre Streams, Playlists do Spotify e Ano de Lançamento")
plt.show()