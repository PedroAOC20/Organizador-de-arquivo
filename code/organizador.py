import os
import shutil
import time

# Função para selecionar o diretório a ser organizados
def selecionarDir():
    diretorio = filedialog.askdirectory()
    if diretorio:
        organizar_arquivos(diretorio)

# Função para organizar os arquivos em subdiretório
def organizarDir(diretorio):
    try:
        # Dicionário com as extensões e categorias
        tipos_arquivos = {
            'imagens': ['.jpg', '.jpeg', '.png', '.gif'],
            'documentos': ['.txt', '.pdf', '.doc', '.docx'],
            'musicas': ['.mp3', '.wav', '.flac'],
			'video': ['.mp4', '.WebM']
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