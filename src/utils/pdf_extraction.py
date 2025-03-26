import os
import shutil
import zipfile

def extrair_pdf():
    # Caminhos
    raw_folder = os.path.join("data", "raw")
    zip_file = os.path.join(raw_folder, "Anexos_Completos.zip")
    planilha_folder = os.path.join("data", "Planilha")

    # Criar a pasta Planilha se não existir, e limpar caso já exista
    if os.path.exists(planilha_folder):
        shutil.rmtree(planilha_folder)  # Remove todos os arquivos e a pasta
    os.makedirs(planilha_folder, exist_ok=True)  # Recria a pasta vazia

    # Copiar o arquivo ZIP para a pasta Planilha
    zip_copy = os.path.join(planilha_folder, "Anexos_Completos.zip")
    shutil.copy(zip_file, zip_copy)

    # Extrair o ZIP na pasta Planilha
    with zipfile.ZipFile(zip_copy, "r") as zip_ref:
        zip_ref.extractall(planilha_folder)

    # Remover o ZIP após extração
    os.remove(zip_copy)

    # Remover arquivos que não começam com "Anexo_I_"
    for file in os.listdir(planilha_folder):
        file_path = os.path.join(planilha_folder, file)
        if not file.startswith("Anexo_I_"):
            os.remove(file_path)

    print("Processo concluído: apenas arquivos 'Anexo_I_' foram mantidos.")
