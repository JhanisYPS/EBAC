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


class CDIExtractorVisualizer:
    def __init__(self, url, output_csv='./taxa-cdi.csv'):
        self.url = url
        self.output_csv = output_csv
        self.cdi = None
        self.output_filename = "grafico.png"

    def fetch_data(self):
        # Captando a taxa CDI do site do BCB
        try:
            response = requests.get(url=self.url)
            response.raise_for_status()
        except requests.HTTPError as exc:
            print("Dado não encontrado, continuando.")
            self.cdi = None
        except Exception as exc:
            print("Erro, parando a execução.")
            raise exc
        else:
            self.cdi = json.loads(response.text)[-1]['valor']

    def create_data_points(self):
        # Criando a variável data e hora
        for _ in range(0, 10):
            data_e_hora = datetime.now()
            data = datetime.strftime(data_e_hora, '%Y/%m/%d')
            hora = datetime.strftime(data_e_hora, '%H:%M:%S')

            cdi_value = float(self.cdi) + (random() - 0.5)

            # Verificando se o arquivo "taxa-cdi.csv" existe
            if not os.path.exists(self.output_csv):
                with open(file=self.output_csv, mode='w', encoding='utf8') as fp:
                    fp.write('data,hora,taxa\n')

            # Salvando dados no arquivo "taxa-cdi.csv"
            with open(file=self.output_csv, mode='a', encoding='utf8') as fp:
                fp.write(f'{data},{hora},{cdi_value}\n')

            time.sleep(1)

        print("Sucesso")

    def set_output_filename(self):
        # Verificar se um argumento foi passado para o nome do arquivo
        if len(sys.argv) > 1:
            self.output_filename = sys.argv[1]
            # Verificar se a extensão do arquivo é válida
            if not os.path.splitext(self.output_filename)[1] in ['.png', '.jpg', '.jpeg', '.svg', '.pdf']:
                self.output_filename = self.output_filename.replace('.json','.png')
        else:
            self.output_filename = "grafico.png"

    def visualize_data(self):
        # Extraindo as colunas hora e taxa
        df = pd.read_csv(self.output_csv)

        # Criando o gráfico
        plt.figure(figsize=(10, 6))  # Definir tamanho da figura, se necessário
        grafico = sns.lineplot(x=df['hora'], y=df['taxa'])

        # Definindo os ticks no eixo x
        grafico.set_xticks(range(len(df['hora'])))

        # Definindo as etiquetas dos ticks
        grafico.set_xticklabels(labels=df['hora'], rotation=90)

        # Salvando o gráfico
        grafico.get_figure().savefig(self.output_filename)

    def run(self):
        self.fetch_data()
        self.create_data_points()
        self.set_output_filename()
        self.visualize_data()


if __name__ == "__main__":
    URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'
    cdi_extractor_visualizer = CDIExtractorVisualizer(URL)
    cdi_extractor_visualizer.run()
