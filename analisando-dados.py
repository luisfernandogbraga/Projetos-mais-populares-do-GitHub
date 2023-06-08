import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('github.csv', delimiter=';')
df.set_index('ranking', inplace=True)
df

df.dtypes

projeto_max_stars = df.loc[df['stars'].idxmax(),'project']
max_stars = df['stars'].max()

print('Projeto com mais estrelas:', projeto_max_stars)
print('Número máximo de estrelas:', max_stars)

df['starts_today'] = pd.to_numeric(df['starts_today'], errors='coerce') # Converter a coluna "starts_today" para o tipo numérico
projeto_max_stars_today = df.loc[df['starts_today'].idxmax(), 'project']
max_stars_today = df['starts_today'].max()

print("Projeto com mais estrelas hoje:", projeto_max_stars_today)
print("Número máximo de estrelas hoje:", max_stars_today)

sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='language', order=df['language'].value_counts().iloc[:10].index)
plt.title('Top 10 Linguagens Mais Usadas')
plt.xlabel('Contagem')
plt.ylabel('Linguagem')
plt.show()

Entre os 10 projetos mais bem avaliados pela comunidade do github há um empate tecnico entre três linguagens mais usadas nos projetos.

sns.set_style("whitegrid")
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='stars', y='language')
plt.title('Relação entre Stars e language')
plt.xlabel('Stars')
plt.ylabel('language')
plt.show()

O gráfico nos mostra que os projetos que usam a linguagem Python são mais bem avaliados que os outros.