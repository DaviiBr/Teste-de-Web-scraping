# Teste-Web-Scraping

## Descrição
Este projeto tem como objetivo automatizar o processo de obtenção e processamento de arquivos PDF. A aplicação acessa um link especificado, faz o download de dois PDFs, compacta os arquivos na pasta `raw` e converte o PDF do Anexo 1 para arquivos CSV.

## Funcionalidades
- **Download Automático:** A aplicação acessa um link definido e faz o download dos PDFs.
- **Compactação Automática:** Os arquivos são armazenados na pasta `raw` já compactados.
- **Conversão de PDF para CSV:** O PDF do Anexo 1 é convertido para arquivos `.csv` conforme o formato solicitado.

## Estrutura do Projeto
```
Teste-Web-Scraping/
├── data/               # Dados processados e brutos
│   ├── Planilha/       # Contém os PDFs baixados e arquivos CSV gerados
│   │   ├── Anexo_I_Rol_2021RN_465.2021_R... (PDF original)
│   │   ├── Teste_anexo_I_csv.zip (CSV gerado compactado)
│   ├── raw/            # PDFs compactados
│   │   ├── Anexos_Completos.zip
├── logs/               # Logs de execução do sistema
├── src/                # Código-fonte principal
│   ├── spiders/        # Scrapers para download de PDFs
│   ├── utils/          # Módulos utilitários
│   │   ├── file_manager.py  # Gerenciamento de arquivos
│   │   ├── pdf_extraction.py # Extração de dados do PDF
│   │   ├── pdf_to_sheet.py  # Conversão de PDF para CSV
│   ├── config.py       # Configurações do projeto
│   ├── main.py         # Script principal para executar a automação
├── .gitignore          # Arquivos ignorados pelo Git
├── .gitattributes      # Configuração de atributos do Git
├── README.md           # Documentação do projeto
```

## Como Usar
### 1. Instalar Dependências
Certifique-se de ter o Python instalado. Depois, instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

### 2. Executar o Script Principal
Para iniciar o processo de scraping e conversão:
```bash
python src/main.py
```

## Tecnologias Utilizadas
- **Python** (Automatização)
- **Requests** (Download de arquivos)
- **PyPDF2** (Manipulação de PDFs)
- **Pandas** (Conversão para CSV)
- **Zipfile** (Compactação dos PDFs)
