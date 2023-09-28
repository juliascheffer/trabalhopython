import pandas as pd
from datetime import datetime

df = pd.read_csv("C:\\Users\\jlsch\\Documents\\trab-spotify\\spotify2023-tratados.csv", encoding="latin-1")

#print(df.head())

#Músicas mais tocadas do mês
mes_atual = datetime.now().month
musicas_do_mes = df[df['released_month'] == mes_atual]

print("As 10 músicas mais tocadas do mês são:")
print(musicas_do_mes.head(10)[['track_name', 'artist(s)_name', 'streams', 'in_spotify_charts']])

#Ano de lançamento das músicas mais tocadas
ano_de_lancamento = musicas_do_mes[['track_name', 'artist(s)_name', 'streams', 'released_year']]

print("Ano de lançamento das 10 músicas mais tocadas do mês:")
print(ano_de_lancamento.head(10))

#Música mais tocada de 2023 até o momento
musicas_2023 = df[df['released_year'] == 2023]

musica_mais_tocada_2023 = musicas_2023[musicas_2023['streams'] == musicas_2023['streams'].max()]

print("A música mais tocada do ano de 2023 até o momento é:")
print(musica_mais_tocada_2023[['track_name', 'artist(s)_name', 'streams', 'released_month', 'released_year']])