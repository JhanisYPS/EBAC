import csv
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Verificar se um argumento foi passado para o nome do arquivo
if len(sys.argv) > 1:
    output_filename = sys.argv[1]
    # Verificar se a extensão do arquivo é válida
    if not os.path.splitext(output_filename)[1] in ['.png', '.jpg', '.jpeg', '.svg', '.pdf']:
        output_filename.replace('.json','.png')
else:
    output_filename = "grafico.png"

# Extraindo as colunas hora e taxa
df = pd.read_csv('./taxa-cdi.csv')

# Criando o gráfico
plt.figure(figsize=(10, 6))  # Definir tamanho da figura, se necessário
grafico = sns.lineplot(x=df['hora'], y=df['taxa'])

# Definindo os ticks no eixo x
grafico.set_xticks(range(len(df['hora'])))

# Definindo as etiquetas dos ticks
grafico.set_xticklabels(labels=df['hora'], rotation=90)

# Salvando o gráfico
grafico.get_figure().savefig(output_filename)