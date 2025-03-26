import os
import pandas as pd
import pdfplumber
import zipfile

def transformar_pdf():
    # Caminho da pasta onde o PDF foi extraído
    planilha_folder = os.path.join("data", "Planilha")

    # Caminho do arquivo CSV de saída
    csv_path = os.path.join(planilha_folder, "Anexo_I_Convertido.csv")

    # Caminho do arquivo ZIP
    zip_path = os.path.join(planilha_folder, "Teste_anexo_I_csv.zip")

    # Verificar se o arquivo ZIP já existe e apagar, caso necessário
    if os.path.exists(zip_path):
        os.remove(zip_path)
        print(f"Arquivo ZIP existente {zip_path} apagado.")

    # Identificar o arquivo PDF que começa com "Anexo_I_"
    pdf_file = None
    for file in os.listdir(planilha_folder):
        if file.startswith("Anexo_I_") and file.endswith(".pdf"):
            pdf_file = os.path.join(planilha_folder, file)
            break

    if pdf_file is None:
        print("Nenhum arquivo PDF 'Anexo_I_' encontrado.")
        exit()

    # Extrair dados do PDF e converter para planilha
    data = []
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                data.extend(table)  # Adiciona todas as linhas da tabela

    # Criar DataFrame
    df = pd.DataFrame(data)

    # Substituir abreviações pelas descrições completas nas colunas
    df.replace({"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"}, inplace=True)

    # Salvar como CSV
    df.to_csv(csv_path, index=False, header=False, encoding="utf-8")

    # Compactar o CSV em um arquivo ZIP
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, os.path.basename(csv_path))

    # Excluir o arquivo CSV após a compactação
    os.remove(csv_path)
    print(f"Arquivo CSV excluído. Apenas o arquivo ZIP {zip_path} permanece.")
