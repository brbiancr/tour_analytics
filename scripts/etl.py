import pandas as pd

dados = pd.read_csv('../data/concert_tours_by_women.csv')

#Removendo as colunas que não serão usadas
dados = dados.drop(columns=['Peak', 'All Time Peak', 'Ref.'])

#Remover caracteres especias da coluna 'Tour title'
dados['Tour title'] = dados['Tour title'].str.replace(r'[†&‡\[\]*:.]', '', regex=True)
dados['Tour title'] = dados['Tour title'].str.replace(r'\d+a$', '', regex=True).str.strip()

#Criando coluna 'Start year' e 'End year'
dados['Start year'] = dados['Year(s)'].str[:4]
dados['End year'] = dados['Year(s)'].str[-4:]

#Removendo coluna 'Year(s)'
dados = dados.drop(columns=['Year(s)'])

#Convertendo valores para float
dados['Average gross'] = dados['Average gross'].str.replace(r'[\$,]', '', regex=True).astype(float)
dados['Adjustedgross (in 2022 dollars)'] = dados['Adjustedgross (in 2022 dollars)'].str.replace(r'[\$,]', '', regex=True).astype(float)
dados['Actual gross'] = dados['Actual gross'].str.replace(r'[\[\]\$,be]', '', regex=True).astype(float)
dados['End year'] = dados['End year'].str.replace(r'[\[\]\$,be]', '', regex=True).astype(float)
dados['Start year'] = dados['Start year'].str.replace(r'[\[\]\$,be]', '', regex=True).astype(float)

# Renomeando a coluna 'Adjustedgross (in 2022 dollars)' para 'Adjusted gross (in 2022 dollars)'
dados.rename(columns={'Adjustedgross (in 2022 dollars)': 'Adjusted gross (in 2022 dollars)' }, inplace=True)

# Criando a coluna 'Years' que representa a duração da turnê em anos
dados["Years"] = dados["End year"] - dados["Start year"] + 1

# Criando a coluna 'Gross per year' que representa o faturamento anual ajustado pela inflação
dados["Gross per year"] = dados["Adjusted gross (in 2022 dollars)"] / dados["Years"]

dados.to_csv('../data/processed/csv_limpo.csv', index=False)