import os
import shutil

msmFinal = 'Arquivos organizados com sucesso!'

# Função para organizar os arquivos em subdiretório
def organizarDir(diretorio):
    # Tupla com as extensões e categorias
    tipos_arquivos = {
        'imagens': ['.jpg', '.jpeg', '.png', '.gif'],
        'documentos': ['.txt', '.pdf', '.doc', '.docx'],
        'musicas': ['.mp3', '.wav', '.flac'],
        'videos': ['.mp4', '.webm']
    }

    try:
        # Criar os diretórios de destino se não existirem
        for subdir in tipos_arquivos.keys():
           os.makedirs(os.path.join(diretorio, subdir), exist_ok=True)

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
        return msmFinal
    
    except FileNotFoundError:
        return print('Diretorio não encontrado!')
    except PermissionError:
        return print('Seu usuario não possui permissão para mover esse arquivo!')
    except Exception as e:
        return print(f'erro ao organizar arquivos: {e}')
        