import os
import zipfile
import time
from config import pasta_downloads

def remover_zip_existente():
    """ Remove o arquivo ZIP se ele já existir antes de iniciar o processo. """
    zip_file = os.path.join(pasta_downloads, "Anexos_Completos.zip")
    if os.path.exists(zip_file):
        os.remove(zip_file)
        print(f"Arquivo antigo {zip_file} removido.")

def esperar_download(pasta, arquivos_esperados, tempo_max=60):
    """ Aguarda até que o número esperado de arquivos seja baixado. """
    tempo_inicial = time.time()
    while time.time() - tempo_inicial < tempo_max:
        arquivos = [f for f in os.listdir(pasta) if f.endswith('.pdf')]
        if len(arquivos) >= arquivos_esperados:
            return arquivos
        time.sleep(2)
    return None

def compactar_anexos():
    """ Compacta todos os PDFs baixados em um único arquivo ZIP. """
    zip_file = os.path.join(pasta_downloads, "Anexos_Completos.zip")

    arquivos = [f for f in os.listdir(pasta_downloads) if f.endswith('.pdf')]

    if not arquivos:
        print("Nenhum anexo encontrado para compactação.")
        return

    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta_downloads, arquivo)
            zipf.write(caminho_arquivo, arquivo)
            os.remove(caminho_arquivo)

    print(f"Anexos compactados em: {zip_file}")
