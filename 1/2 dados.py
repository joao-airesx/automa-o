#1 importar a base dados
import pandas as pd
import openpyxl
import numpy
import plotly.express as px

tabela = pd.read_csv("clientes.csv", encoding="latin", sep=";")

# deletar a coluna inutil
#axis 0 = linha e 1 = coluna
tabela = tabela.drop("Unnamed: 8", axis=1)

#2 visualizar a base dados
#3 tratamento de dados
    # acertar informações que estão sendo reconhecidas de forma errada
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")
    # corrigir informações vazias
tabela = tabela.dropna()
#4 análise inicial -> entender as notas dos clientes
print(tabela.info())
print(tabela)
print(tabela.describe())

#5 análise completa -> entender como cada característica impacta na nota
for coluna in tabela.columns:
    Grafico = px.histogram(tabela, x= coluna, y="Nota (1-100)", histfunc = "avg", text_auto= True )
    Grafico.show()

#média da tebela: print(tabela.describe())