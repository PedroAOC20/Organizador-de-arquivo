from organizador import *

'''

import shutil
from tkinter import filedialog
import tkinter as tk
import time
import os

# Função para organizar os arquivos em s
def organizar_arquivos(diretorio):
    try:
        # Dicionário com as extensões e seus respectivos diretórios de destino
        tipos_arquivos = {
            'imagens': ['.jpg', '.jpeg', '.png', '.gif'],
            'documentos': ['.txt', '.pdf', '.doc', '.docx'],
            'musicas': ['.mp3', '.wav', '.flac']
            # Adicione mais tipos de arquivo conforme necessário
        }

        # Criar os diretórios de destino se não existirem
        for subdir in tipos_arquivos.keys():
            if not os.path.exists(os.path.join(diretorio, subdir)):
                os.makedirs(os.path.join(diretorio, subdir))

        # Percorrer os arquivos no diretório
        for filename in os.listdir(diretorio):
            # Ignorar subdiretórios
            if os.path.isdir(os.path.join(diretorio, filename)):
                continue
            
            # Obter a extensão do arquivo
            _, extensao = os.path.splitext(filename)

            # Mover o arquivo para o diretório correspondente
            for tipo, extensoes in tipos_arquivos.items():
                if extensao.lower() in extensoes:
                    shutil.move(
                        os.path.join(diretorio, filename),
                        os.path.join(diretorio, tipo, filename)
                    )
                    break
        
        label_status.config(text="Arquivos organizados com sucesso!")
        # Esperar 5 segundos antes de abrir o diretório
        time.sleep(5)
        os.startfile(diretorio)  # Abrir o diretório após 5 segundos
    except Exception as e:
        label_status.config(text=f"Erro ao organizar arquivos: {e}")

# Função para selecionar o diretório a ser organizado
def selecionar_diretorio():
    diretorio = filedialog.askdirectory()
    if diretorio:
        organizar_arquivos(diretorio)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Organizador de Arquivos")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_instrucoes = tk.Label(frame, text="Selecione o diretório a ser organizado:")
label_instrucoes.pack()

button_selecionar = tk.Button(frame, text="Selecionar Diretório", command=selecionar_diretorio)
button_selecionar.pack(pady=10)

label_status = tk.Label(frame, text="")
label_status.pack()

root.mainloop()
'''