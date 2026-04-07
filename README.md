# LinkedIn Job Scraper

API REST em **FastAPI** sobre automação com **Selenium** para busca e filtragem de vagas de emprego no LinkedIn, com validação de schema via Pydantic e exportação estruturada em CSV.

---

## O Problema

Buscar vagas manualmente no LinkedIn consome tempo e exige repetição: filtrar por regime de trabalho, rolar a página, copiar dados. Este projeto automatiza esse processo inteiro e expõe o resultado via API, eliminando a necessidade de interação manual.

## A Solução Técnica

O desafio central foi **simular comportamento humano** para contornar a detecção de bots do LinkedIn. As decisões de Back-End foram:

- **Scroll progressivo com delays variáveis** para imitar padrão de leitura humana
- - **Separação de responsabilidades**: a camada de scraping (Selenium) é desacoplada da camada de API (FastAPI), permitindo evoluir cada parte de forma independente
  - - **Validação de schema com Pydantic** antes da serialização — campos ausentes ou malformados são descartados antes de chegar no endpoint
    - - **FastAPI como camada de entrega**: expõe um endpoint `GET /vagas/` com parâmetros de filtro, documentação automática via `/docs` e resposta em JSON ou CSV
     
      - ## Stack
     
      - | Tecnologia | Papel |
      - |---|---|
      - | Python 3.10+ | Linguagem principal |
      - | FastAPI | Camada de API REST e documentação automática |
      - | Selenium | Automação do navegador e extração de dados |
      - | Webdriver Manager | Gerenciamento automático do ChromeDriver |
      - | Pydantic | Validação e serialização dos dados coletados |
      - | Uvicorn | Servidor ASGI para servir a API |
     
      - ## Como Rodar
     
      - ### 1. Clone o repositório
      - ```bash
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

        ### 5. Acesse a API
        Abra: `http://127.0.0.1:8000/docs`

        - Clique em `GET /vagas/` → `Try it out`
        - - Preencha os filtros: `cargo`, `localização`, `tipo de trabalho`
          - - Clique em `Execute`
           
            - O arquivo CSV será gerado e retornado automaticamente.
           
            - ## Estrutura do Projeto
           
            - ```
              linkedin-job-scraper/
              ├── main.py          # Endpoints FastAPI + lógica de scraping
              ├── requirements.txt # Dependências
              ├── tests/
              │   └── test_main.py # Testes unitários
              └── README.md
              ```

              ## Rodando os Testes

              ```bash
              pip install pytest
              pytest tests/ -v
              ```

              ## Observações Técnicas

              - O Chrome é aberto de forma visível durante a execução. É necessário ter o Google Chrome instalado.
              - - O Webdriver Manager detecta e baixa automaticamente a versão correta do ChromeDriver.
                - - O LinkedIn pode bloquear requisições identificadas como automação. Nesse caso, aguarde alguns minutos antes de rodar novamente.
                 
                  - ---

                  Feito por [Bernardo P. D.](https://www.linkedin.com/in/bernardop-d/)
