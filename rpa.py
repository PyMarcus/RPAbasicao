from selenium import webdriver
import time
import os
import shutil
import rarfile
from rarfile import RarFile
from getpass import getuser

user = getuser()
localBase = f'C:\\Users\\{user}'
pastaDestino = f"C:\\Users\\{user}\\Documents\\DadosdoCovid\\"


class Covid:
    def __init__(self, site):
        self.site = site

    def download(self):
        # abrir navegador
        navegador = webdriver.Firefox()

        # navegar em uma pagina especifica
        navegador.get(self.site)

        time.sleep(3)

        # localizar um elemento
        # find_element_by_id('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/div[1]/div[2]/ion-button')
        button = navegador.find_element_by_xpath(
            '/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/div[1]/div[2]/ion-button')
        button.click()

    def move_unzip(self):
        arquivoCSV = ""
        pastaDownload = f"C:\\Users\\{user}\\Downloads"
        os.chdir(pastaDownload)  # muda o diretório atual para o destino no programa

        # encontra na pasta de downloads
        for itens in os.listdir(pastaDownload):
            if itens.startswith('HIST_'):
                arquivoCSV = itens
        # move para a pasta desejada:
        if arquivoCSV not in os.listdir(pastaDestino):
            shutil.move(arquivoCSV, pastaDestino)

    def descompacta(self):
        # encontra no destino
        os.chdir(pastaDestino)
        for itens in os.listdir(pastaDestino):
            if itens.startswith('HIST_'):
                if rarfile.is_rarfile(itens):  # verifica
                    rf = RarFile(itens)
                    for arquivos in rf:
                        rf.extract(arquivos)


if __name__ == '__main__':
    site = "https://covid.saude.gov.br/"
    covid = Covid(site)
    covid.download()
    covid.move_unzip()
    covid.descompacta()
