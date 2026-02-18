from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from enum import Enum
from pydantic import BaseModel
from typing import List
import time
import random
import csv
import os

# --- 1. MODELOS ---
class TipoTrabalho(str, Enum):
    todos = "todos"
    remoto = "remoto"
    hibrido = "hibrido"
    presencial = "presencial"

class Vaga(BaseModel):
    titulo: str
    empresa: str
    local: str
    link: str

# --- 2. CLASSE DO ROBÔ ---
class LinkedInBot:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument("--log-level=3")
        self.options.add_argument("--lang=pt-BR")
        
        self.service = Service(ChromeDriverManager().install())

    def iniciar_driver(self):
        return webdriver.Chrome(service=self.service, options=self.options)

    def pegar_texto(self, card, seletor_classe):
        try:
            return card.find_element(By.CLASS_NAME, seletor_classe).text.strip()
        except:
            return ""

    def rolar_pagina(self, driver):
        print("   [Bot] Rolando página para carregar mais itens...")
        for _ in range(4): # Aumentei para 4 rolagens
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2.5)
            try:
                driver.find_element(By.CLASS_NAME, "infinite-scroller__show-more-button").click()
                time.sleep(2)
            except:
                pass

    def buscar(self, termo: str, local: str, tipo: TipoTrabalho) -> List[Vaga]:
        driver = self.iniciar_driver()
        lista_vagas = []
        links_vistos = set()

        try:
            # Montagem da URL com filtros
            url = f"https://www.linkedin.com/jobs/search?keywords={termo}"
            
            if local.lower() in ["brasil", "brazil", "br"]:
                url += "&geoId=106057199"
            else:
                url += f"&location={local}"

            filtros = {TipoTrabalho.remoto: "&f_WT=2", TipoTrabalho.hibrido: "&f_WT=3", TipoTrabalho.presencial: "&f_WT=1"}
            url += filtros.get(tipo, "")

            print(f"[*] Acessando: {url}")
            driver.get(url)
            time.sleep(4)

            try: driver.find_element(By.CLASS_NAME, "modal__dismiss").click()
            except: pass

            self.rolar_pagina(driver)

            cards = driver.find_elements(By.CLASS_NAME, "base-search-card") or \
                    driver.find_elements(By.CLASS_NAME, "job-search-card")
            
            print(f"[*] Encontrei {len(cards)} cards potenciais.")

            for card in cards:
                try:
                    link_el = card.find_element(By.TAG_NAME, "a")
                    link = link_el.get_attribute("href").split('?')[0]

                    if link in links_vistos:
                        continue

                    titulo = self.pegar_texto(card, "base-search-card__title") or link_el.text.strip()
                    empresa = self.pegar_texto(card, "base-search-card__subtitle")
                    local_vaga = self.pegar_texto(card, "job-search-card__location")

                    if titulo and link:
                        lista_vagas.append(Vaga(titulo=titulo, empresa=empresa, local=local_vaga, link=link))
                        links_vistos.add(link)

                except:
                    continue
        finally:
            driver.quit()
        
        return lista_vagas

# --- 3. CONFIG API ---
app = FastAPI(title="LinkedIn Job Scraper API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite que o Swagger (ou qualquer site local) acesse a API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bot = LinkedInBot()
ARQUIVO_CSV = "vagas_encontradas.csv"
robo_ocupado = False

@app.get("/")
def home():
    return {"mensagem": "API Online! Acesse /docs para buscar vagas."}

@app.get("/vagas/")
def buscar_vagas(termo: str, local: str = "Brasil", tipo: TipoTrabalho = TipoTrabalho.todos):
    global robo_ocupado
    if robo_ocupado:
        raise HTTPException(status_code=429, detail="O robô já está em uso.")
    
    try:
        robo_ocupado = True
        resultado = bot.buscar(termo, local, tipo)
        
        if not resultado:
            return {"aviso": "Nenhuma vaga encontrada."}
        
        # Salvamento em CSV (UTF-8-SIG para Excel ler acentos)
        with open(ARQUIVO_CSV, mode="w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(["Titulo", "Empresa", "Local", "Link"])
            for v in resultado:
                writer.writerow([v.titulo, v.empresa, v.local, v.link])
        
        return FileResponse(ARQUIVO_CSV, filename=f"vagas_{termo}.csv", media_type='text/csv')

    finally:
        robo_ocupado = False