from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from concurrent.futures import ThreadPoolExecutor, as_completed
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.file_manager import remover_zip_existente, esperar_download, compactar_anexos
from config import pasta_downloads
import time
import os

def seleniumform():
    """ Inicializa o Chrome configurado para baixar PDFs automaticamente. """
    appdata = os.path.expanduser("~")
    prefs = {
        "download.default_directory": pasta_downloads,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,
        "safebrowsing.enabled": True
    }

    opcoes = webdriver.ChromeOptions()
    opcoes.add_experimental_option("prefs", prefs)
    opcoes.add_argument("start-maximized")
    opcoes.add_argument("window-size=1920x1080")
    opcoes.add_argument("--no-sandbox")
    opcoes.add_argument("--disable-dev-shm-usage")
    opcoes.add_argument("--disable-gpu")
    opcoes.add_argument(f"user-data-dir={appdata}\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

    servico = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=servico, options=opcoes)

def baixar_anexo(driver, nome, xpath, arquivos_esperados):
    """ Baixa um anexo, verificando se o clique foi realizado corretamente. """
    try:
        print(f"Baixando {nome}...")

        link = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, xpath)))

        url_anexo = link.get_attribute("href")
        print(f"URL detectada para {nome}: {url_anexo}")

        if any(url_anexo in arquivo for arquivo in os.listdir(pasta_downloads)):
            print(f"{nome} já foi baixado anteriormente. Pulando...")
            return

        link.click()
        time.sleep(2)

        arquivos = esperar_download(pasta_downloads, arquivos_esperados)
        if arquivos:
            print(f"{nome} baixado com sucesso!")
        else:
            print(f"Erro: {nome} não foi baixado.")

    except Exception as e:
        print(f"Erro ao baixar {nome}: {e}")

def web_scraping():
    remover_zip_existente()

    driver = seleniumform()
    driver.get("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")

    anexos = {
        "Anexo I": '/html/body/div[2]/div[1]/main/div[2]/div/div/div/div/div[2]/div/ol/li[1]/a[1]',
        "Anexo II": '/html/body/div[2]/div[1]/main/div[2]/div/div/div/div/div[2]/div/ol/li[2]/a'
    }

    arquivos_iniciais = len([f for f in os.listdir(pasta_downloads) if f.endswith('.pdf')])

    for index, (nome, xpath) in enumerate(anexos.items(), start=1):
        baixar_anexo(driver, nome, xpath, arquivos_iniciais + index)

    arquivos = esperar_download(pasta_downloads, arquivos_iniciais + len(anexos))
    if arquivos:
        print(f"Todos os anexos baixados corretamente: {arquivos}")
        compactar_anexos()
    else:
        print("Erro: Nem todos os anexos foram baixados.")

    driver.quit()

