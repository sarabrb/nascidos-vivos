#!/usr/bin/env python
# coding: utf-8

### Bibliotecas
import pandas as pd
from datetime import datetime
import re

### Limpeza e tratamento de dados

# Leitura dos dados

data = pd.read_csv(r'DNOPEN24.csv', sep=";", low_memory=False)

data = data.apply(pd.to_numeric, errors='coerce')

# Conversão para int nas colunas que são float
for col in data.select_dtypes(include=['float']).columns:
    data[col] = data[col].astype('Int64', errors='ignore')

base_dados = pd.DataFrame(data)

print(base_dados.columns)


# Selecionando apenas as colunas de interesse
colunas_desejadas = [
    "LOCNASC", "IDADEMAE", "ESTCIVMAE", "ESCMAE", "PARTO", 
    "CONSULTAS", "DTNASC", "SEXO", "IDANOMAL", 
    "IDADEPAI", "SEMAGESTAC"
]

base_filtrada = pd.DataFrame(base_dados)
base_filtrada = base_dados[colunas_desejadas].copy()

# Eliminando os valores NaN das colunas de datas
base_filtrada = base_filtrada.dropna(subset=['DTNASC'])

display(base_filtrada)


# Função para corrigir as datas com regex
def corrigir_datas(data):
    if pd.isna(data):  # Verifica valores ausentes
        return None
    regex = r"\b(\d{1,2})(\d{1,2})(\d{2}|\d{4})\b"
    match = re.match(regex, str(data))
    if match:
        dia, mes, ano = match.groups()
        if len(ano) == 2:  # Ajusta ano para 4 dígitos, já que a base é para o ano de 2024
            ano = "20" + ano
        return f"{dia}/{mes}/{ano}"  # Retorna no formato DD/MM/YYYY
    return None  # Retorna None para valores inválidos

# Aplicação da função na coluna DTNASC
base_filtrada['DTNASC'] = base_filtrada['DTNASC'].apply(corrigir_datas)

# Convertendo para datetime após a correção
base_filtrada['DTNASC'] = pd.to_datetime(base_filtrada['DTNASC'], format='%d/%m/%Y', errors='coerce')

# Resultado
display(base_filtrada[['DTNASC']].head())


### Mapeamento das categorias e aplicação na base de dados


# Criando o dicionário para substituir variáveis
mapa = {
    'LOCNASC': { 
        1: "Hospital", 2: "Outros estabelecimentos de saúde", 3: "Domicílio", 4: "Outros", 5: "Aldeia Indígena"
    },
    'ESTCIVMAE': {
        1: "Solteira", 2: "Casada", 3: "Viúva", 4: "Separada judicialmente/divorciada", 5: "União estável", 9: "Ignorada"
    },
    'ESCMAE': {
        1: "Nenhuma", 2: "1 a 3 anos", 3: "4 a 7 anos", 4: "8 a 11 anos", 5: "12 e mais", 9: "Ignorado"
    },
    'PARTO': {
        1: "Vaginal", 2: "Cesárea", 9: "Ignorado"
    },
    'CONSULTAS': {
        1: "Nenhuma", 2: "de 1 a 3", 3: "de 4 a 6", 4: "7 e mais", 9: "Ignorado"
    },
    'SEXO': {
        1: "Masculino", 2: "Feminino", 0: "Ignorado"
    },
    'IDANOMAL': {
        1: "Sim", 2: "Não", 9: "Ignorado"
    },
}

# Substituindo os valores nas colunas conforme o dicionário
for col, mapa in mapa.items():
    base_filtrada[col] = base_filtrada[col].map(mapa)

# Resultado
display(base_filtrada)


# Contar NaT na coluna 'DTNASC'
quantidade_nat = base_filtrada['DTNASC'].isna().sum()
print(f"Quantidade de NaT: {quantidade_nat}")

percentual_nat = (base_filtrada['DTNASC'].isna().mean()) * 100
print(f"Percentual de NaT: {percentual_nat:.2f}%")

# Optei por eliminar os NaTs
base_filtrada = base_filtrada.dropna(subset=['DTNASC'])
display(base_filtrada)


# Transformando base_filtrada em dataframe
base_filtrada = pd.DataFrame(base_filtrada)


# Calculando a data mínima e máxima da base de dados
data_minima = base_filtrada['DTNASC'].min()
data_maxima = base_filtrada['DTNASC'].max()

print("Data mínima de nascimento:", data_minima)
print("Data máxima de nascimento:", data_maxima)


### Estatísticas básicas da idade das mães
print("Estatísticas da Idade das Mães:")
print(base_filtrada['IDADEMAE'].describe())

### Outliers na idade das mães

# Contando quantos mães têm mais de 48 anos
maes_mais_48 = base_filtrada[base_filtrada['IDADEMAE'] > 48]

# Número total de mães na base
total_maes = base_filtrada['IDADEMAE'].count()

# Contagem e porcentagem
contagem_mais_48 = maes_mais_48['IDADEMAE'].count()
porcentagem_mais_48 = (contagem_mais_48 / total_maes) * 100

# Criando a tabela resumo
tabela_resumo = pd.DataFrame({
    'Contagem': [contagem_mais_48],
    'Porcentagem (%)': [porcentagem_mais_48]
})

print(tabela_resumo)

### Estatísticas básicas da idade dos pais

print(base_filtrada['IDADEPAI'].describe())
print(f"Registros restantes: {len(base_filtrada)}")


### Outliers na idade dos pais

# Contando quantos pais têm mais de 52 anos
pais_mais_52 = base_filtrada[base_filtrada['IDADEPAI'] > 52]

# Número total de pais na base
total_pais = base_filtrada['IDADEPAI'].count()

# Contagem e porcentagem
contagem_mais_52 = pais_mais_52['IDADEPAI'].count()
porcentagem_mais_52 = (contagem_mais_52 / total_pais) * 100

# Criando a tabela resumo
tabela_resumo = pd.DataFrame({
    'Contagem': [contagem_mais_52],
    'Porcentagem (%)': [porcentagem_mais_52]
})

print(tabela_resumo)


### Há mais anomalias registradas em nascidos de pais ou mães de mais idade?

# Definindo as faixas de idade
faixa_idade = ['10-30', '31-40', '41-50', '51-60', '60+']
bins = [10, 30, 40, 50, 60, float('inf')]  # Limites das faixas
labels = faixa_idade  # Etiquetas para as faixas

# Criando uma nova coluna 'faixa_idade' usando pd.cut para agrupar as idades em faixas
base_filtrada['faixa_idade_mae'] = pd.cut(base_filtrada['IDADEMAE'], bins=bins, labels=labels, right=False)
base_filtrada['faixa_idade_pai'] = pd.cut(base_filtrada['IDADEPAI'], bins=bins, labels=labels, right=False)

# Função para mapear os valores de anomalia
def mapear_anomalia(valor):
    if pd.isna(valor) or valor == 'Ignorado':
        return 0  # Ignora ou trata como 0
    return 1 if valor == 'Sim' else 0  # 'Sim' é 1, 'Não' é 0

# Contagem de anomalias por faixa de idade das mães
anomalias_por_idade_mae = base_filtrada.groupby('faixa_idade_mae', observed=False)['IDANOMAL'].agg(
    anomalias=lambda x: x.map(mapear_anomalia).sum(),  # Mapeia e soma as anomalias
    total='count'  # Conta o total de registros
).reset_index()

# Calculando a porcentagem de anomalias por faixa de idade das mães
anomalias_por_idade_mae['porcentagem_anomalias'] = (anomalias_por_idade_mae['anomalias'] / anomalias_por_idade_mae['total']) * 100

# Contagem de anomalias por faixa de idade dos pais
anomalias_por_idade_pai = base_filtrada.groupby('faixa_idade_pai', observed=False)['IDANOMAL'].agg(
    anomalias=lambda x: x.map(mapear_anomalia).sum(),  # Mapeia e soma as anomalias
    total='count'  # Conta o total de registros
).reset_index()

# Calculando a porcentagem de anomalias por faixa de idade dos pais
anomalias_por_idade_pai['porcentagem_anomalias'] = (anomalias_por_idade_pai['anomalias'] / anomalias_por_idade_pai['total']) * 100

# Exibindo as tabelas
print("Anomalias por Faixa de Idade das Mães:")
print(anomalias_por_idade_mae)

print("\nAnomalias por Faixa de Idade dos Pais:")
print(anomalias_por_idade_pai)

### Gestações normais e prematuras por tipo de parto

# Definindo as faixas de gestação
def classificar_gestacao(semanas):
    if pd.isna(semanas):  # Caso tenha NaN
        return 'Desconhecido'
    elif semanas <= 28:
        return 'Prematuro extremo (até 28 semanas)'
    elif 28 < semanas <= 32:
        return 'Prematuro muito precoce (28 a 32 semanas)'
    elif 32 < semanas <= 37:
        return 'Prematuro moderado a tardio (32 a 37 semanas)'
    elif 37 < semanas <= 42:
        return 'Gestação normal (37 a 42 semanas)'
    else:
        return 'Gestação a termo (+42 semanas)'

# Aplicando a função para criar a nova coluna de classificação
base_filtrada['faixa_gestacao'] = base_filtrada['SEMAGESTAC'].apply(classificar_gestacao)

# Filtrando os dados por tipo de parto (Vaginal e Cesária)
vaginal = base_filtrada[base_filtrada['PARTO'] == 'Vaginal']
cesarea = base_filtrada[base_filtrada['PARTO'] == 'Cesárea']

# Contagem e porcentagem de nascidos por faixa de gestação para parto vaginal
contagem_vaginal = vaginal.groupby('faixa_gestacao').agg(
    contagem=('SEMAGESTAC', 'count'),
    porcentagem=('SEMAGESTAC', lambda x: (x.count() / len(vaginal)) * 100)
).reset_index()

# Contagem e porcentagem de nascidos por faixa de gestação para parto cesária
contagem_cesarea = cesarea.groupby('faixa_gestacao').agg(
    contagem=('SEMAGESTAC', 'count'),
    porcentagem=('SEMAGESTAC', lambda x: (x.count() / len(cesarea)) * 100)
).reset_index()

# Tabelas
print("Contagem e Porcentagem para Parto Vaginal:")
print(contagem_vaginal)

print("\nContagem e Porcentagem para Parto Cesárea:")
print(contagem_cesarea)

### Escolaridade e estado civil das mães

# Definindo as faixas etárias
faixa_idade = ['10-30', '31-40', '41-50', '51-60', '60+']

# Função para categorizar a idade em faixas
def categorizar_idade(idade):
    if idade >= 10 and idade <= 30:
        return '10-30'
    elif idade >= 31 and idade <= 40:
        return '31-40'
    elif idade >= 41 and idade <= 50:
        return '41-50'
    elif idade >= 51 and idade <= 60:
        return '51-60'
    else:
        return '60+'

# Retirando valores ausentes
base_filtrada = base_filtrada.dropna(subset=['IDADEMAE'])

# Aplicando a função para categorizar a faixa de idade
base_filtrada['faixa_idade'] = base_filtrada['IDADEMAE'].apply(categorizar_idade)

# Filtrando para excluir os valores 'Ignorado'
base_filtrada_filtrada = base_filtrada[(base_filtrada['ESCMAE'] != 'Ignorado') & (base_filtrada['ESTCIVMAE'] != 'Ignorado')]

# Tabela 1: Escolaridade da mãe e faixa de idade
tabela_escolaridade_idade = base_filtrada_filtrada.groupby(['faixa_idade', 'ESCMAE']).size().reset_index(name='contagem')

# Calculando a porcentagem
tabela_escolaridade_idade['porcentagem'] = tabela_escolaridade_idade.groupby('faixa_idade')['contagem'].transform(lambda x: (x / x.sum()) * 100)

# Tabela 2: Estado civil da mãe e faixa de idade
tabela_estado_civil_idade = base_filtrada_filtrada.groupby(['faixa_idade', 'ESTCIVMAE']).size().reset_index(name='contagem')

# Calculando a porcentagem
tabela_estado_civil_idade['porcentagem'] = tabela_estado_civil_idade.groupby('faixa_idade')['contagem'].transform(lambda x: (x / x.sum()) * 100)

# Tabelas
print("Tabela de Escolaridade das Mães por Faixa de Idade:")
print(tabela_escolaridade_idade)

print("\nTabela de Estado Civil das Mães por Faixa de Idade:")
print(tabela_estado_civil_idade)

### O nível de escolaridade influencia na quantidade de consultas pré-natal?

# Agrupando por Escolaridade e Consultas
tabela_consultas = base_filtrada.groupby(['ESCMAE', 'CONSULTAS']).size().unstack(fill_value=0)

# Calculando as porcentagens para cada grupo de escolaridade
tabela_consultas_percentual = tabela_consultas.divide(tabela_consultas.sum(axis=1), axis=0) * 100

# Resetando o índice para transformar 'ESCMAE' em coluna
tabela_consultas_percentual = tabela_consultas_percentual.reset_index()

# Reordenando as colunas
tabela_consultas_percentual = tabela_consultas_percentual[[
    'ESCMAE', 
    'de 1 a 3', 
    'de 4 a 6', 
    '7 e mais', 
    'Ignorado'
]]

# Tabela final
tabela_consultas_percentual
