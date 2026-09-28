import os
import shutil

def organizar_arquivos(diretorio_base):
    if not os.path.exists(diretorio_base):
        print(f"O diretório {diretorio_base} não existe.")
        return

    for arquivo in os.listdir(diretorio_base):
        caminho_arquivo = os.path.join(diretorio_base, arquivo)

        if os.path.isdir(caminho_arquivo):
            continue

        extensao = os.path.splitext(arquivo)[1].lower().strip('.')
        if not extensao:
            extensao = "_sem_extensao"  # ← underscore evita conflito de nome

        pasta_destino = os.path.join(diretorio_base, extensao)

        # Move o arquivo ANTES de criar a pasta, se necessário
        try:
            os.makedirs(pasta_destino, exist_ok=True)
            destino_final = os.path.join(pasta_destino, arquivo)
            shutil.move(caminho_arquivo, destino_final)
            print(f"Movido: {arquivo} → {pasta_destino}")
        except PermissionError:
            print(f"Permissão negada ao mover {arquivo}.")
        except Exception as e:
            print(f"Erro ao mover {arquivo}: {e}")

if __name__ == "__main__":
    diretorio = r"C:\Users\Gabriel\Downloads"
    organizar_arquivos(diretorio)
