from spiders.gov_br_scraper import web_scraping
from utils.pdf_extraction import extrair_pdf
from utils.pdf_to_sheet import transformar_pdf

if __name__ == "__main__":
    web_scraping()
    extrair_pdf()
    transformar_pdf()
