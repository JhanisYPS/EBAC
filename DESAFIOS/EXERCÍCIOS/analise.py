# combinação dos scripts de extração e visualização
import os
import time
import json
from random import random
from datetime import datetime
import csv
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'

# Captando a taxa CDI do site do BCB

try:
  response = requests.get(url=URL)
  response.raise_for_status()
except requests.HTTPError as exc:
  print("Dado não encontrado, continuando.")
  cdi = None
except Exception as exc:
  print("Erro, parando a execução.")
  raise exc
else:
  dado = json.loads(response.text)[-1]['valor']

# Criando a variável data e hora

for _ in range(0, 10):

  data_e_hora = datetime.now()
  data = datetime.strftime(data_e_hora, '%Y/%m/%d')
  hora = datetime.strftime(data_e_hora, '%H:%M:%S')

  cdi = float(dado) + (random() - 0.5)

  # Verificando se o arquivo "taxa-cdi.csv" existe

  if os.path.exists('./taxa-cdi.csv') == False:

    with open(file='./taxa-cdi.csv', mode='w', encoding='utf8') as fp:
      fp.write('data,hora,taxa\n')

  # Salvando dados no arquivo "taxa-cdi.csv"

  with open(file='./taxa-cdi.csv', mode='a', encoding='utf8') as fp:
    fp.write(f'{data},{hora},{cdi}\n')

  time.sleep(1)

print("Sucesso")


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

