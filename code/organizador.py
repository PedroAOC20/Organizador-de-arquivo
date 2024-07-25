import os
import shutil

msmFinal = 'Arquivos organizados com sucesso!'

def organizarDir(diretorio):
    tipos_arquivos = {
        'imagens': ['.jpg', '.jpeg', '.png', '.gif'],
        'documentos': ['.txt', '.pdf', '.doc', '.docx'],
        'musicas': ['.mp3', '.wav', '.flac'],
        'videos': ['.mp4', '.webm']
    }

    try:
        # Verificar se o diretório existe
        if not os.path.exists(diretorio):
            raise FileNotFoundError('Diretório não encontrado!')

        # Percorrer os arquivos no diretório
        for filename in os.listdir(diretorio):
            filepath = os.path.join(diretorio, filename)

            # Ignorar subdiretórios
            if os.path.isdir(filepath):
                continue

            # Obter a extensão do arquivo
            _, extensao = os.path.splitext(filename)

            # Mover o arquivo para o diretório correspondente, criando-o se necessário
            for tipo, extensoes in tipos_arquivos.items():
                if extensao.lower() in extensoes:
                    pasta_destino = os.path.join(diretorio, tipo)
                    os.makedirs(pasta_destino, exist_ok=True)  # Cria a pasta se não existir
                    shutil.move(filepath, os.path.join(pasta_destino, filename))
                    break  # Sai do loop interno após mover o arquivo

        return msmFinal

    except FileNotFoundError as e:
        return f"Erro: {e}"
    except PermissionError as e:
        return f"Erro: {e}"
    except Exception as e:
        return f"Erro ao organizar arquivos: {e}"
