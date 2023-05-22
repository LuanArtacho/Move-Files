
## Um script simples para mover arquivos.

### Mas apenas move os arquivos que foi passado na busca.

#### E renomealos de acordo com sua vontade, no meu caso eu passei ate uma data

import os
import shutil
from datetime import datetime

# Obter a data atual
data_atual = datetime.now().strftime('%d-%m')

# Caminho dos diretórios
pasta_downloads = r'C:\Users\luanzera\Downloads'
pasta_calculadora = r'C:\Users\luanzera\Desktop\Estudos\Mover arquivos pasta\mover aqui'

# Lista de arquivos a serem movidos
arquivos_para_mover = ['relatorio_de_lastros.xlsx', 'calc_lastros.xlsx']

# Percorrer os arquivos da pasta "Downloads"
for arquivo in os.listdir(pasta_downloads):
    if arquivo in arquivos_para_mover:
        # Caminho completo dos arquivos de origem e destino
        origem = os.path.join(pasta_downloads, arquivo)
        if arquivo == 'relatorio_de_lastros.xlsx':
            destino = os.path.join(pasta_calculadora, f'lastros_vinculados_{data_atual}.xlsx')
        elif arquivo == 'calc_lastros.xlsx':
            destino = os.path.join(pasta_calculadora, f'ConsultaParcelas_{data_atual}.xlsx')

        # Mover e renomear o arquivo
        shutil.move(origem, destino)
        print(f"Arquivo {arquivo} movido com sucesso para {destino}.")
