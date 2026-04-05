# LinkedIn Job Scraper

Script que busca vagas de emprego no LinkedIn e salva os resultados em um arquivo CSV. Você informa o cargo, a cidade e o tipo de trabalho (remoto, híbrido ou presencial), e o programa abre o navegador, coleta as vagas e gera o arquivo automaticamente.

---

## Tecnologias usadas

- Python 3.10+
- FastAPI
- Selenium
- Webdriver Manager
- Uvicorn

---

## O que o projeto faz

O projeto abre o Chrome de forma automática (usando Selenium), acessa o LinkedIn e coleta informações sobre as vagas encontradas: nome da vaga, empresa, localização e link. No final, salva tudo em um arquivo `.csv` que você pode abrir no Excel.

Ele também tem uma pequena API feita com FastAPI, que você acessa pelo navegador em `/docs`. Lá você pode preencher os filtros e clicar em "Execute" sem precisar usar o terminal.

---

## Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/bernardop-d/linkedin-job-scraper.git
cd linkedin-job-scraper
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicie o servidor

```bash
python -m uvicorn main:app --reload
```

### 5. Acesse no navegador

Abra: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

- Clique em **GET /vagas/**
- Clique em **Try it out**
- Preencha os campos (cargo, localização, tipo de trabalho)
- Clique em **Execute**

O arquivo CSV será gerado e baixado automaticamente.

---

## Observações importantes

- O projeto abre o Chrome durante a execução. Isso é normal — o Selenium precisa de um navegador para funcionar.
- Você precisa ter o **Google Chrome instalado** na sua máquina. O Webdriver Manager cuida do restante.
- O LinkedIn pode bloquear a busca se perceber que é automação. Se isso acontecer, tente rodar novamente depois de alguns minutos.

---

## Como rodar os testes

```bash
pip install pytest
pytest tests/ -v
```

---

## Estrutura de arquivos

```
linkedin-job-scraper/
├── main.py            # Código principal com a API e o scraper
├── requirements.txt   # Dependências do projeto
├── tests/
│   └── test_main.py   # Testes unitários
└── README.md
```

---

Feito por [Bernardo P. D.](https://github.com/bernardop-d)
