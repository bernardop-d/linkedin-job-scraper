# 🕵️‍♂️ LinkedIn Job Scraper API

API robusta desenvolvida em **Python** para automatizar a busca e extração de vagas de emprego no LinkedIn. O projeto utiliza **FastAPI** para fornecer uma interface de usuário interativa e **Selenium** para a automação do navegador com comportamento simulado.

## 🚀 Funcionalidades

- **Interface Visual (Swagger UI)**: Documentação interativa que permite realizar buscas sem escrever uma linha de código.
- **Filtros Dinâmicos**: Suporte para filtrar vagas por cargo, localização e regime de trabalho (Remoto, Híbrido ou Presencial).
- **Scroll Infinito**: Algoritmo de rolagem automática e detecção do botão "Ver mais" para carregar um grande volume de resultados.
- **Exportação Automática**: Gera e baixa um arquivo CSV (Excel) formatado com `utf-8-sig` para garantir a leitura correta de acentos no Windows.
- **Anti-Duplicidade**: Lógica de filtragem por URL para garantir que cada vaga seja listada apenas uma vez no relatório final.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI**: Framework moderno para construção de APIs.
- **Selenium**: Automação de navegador para extração de dados dinâmicos.
- **Webdriver Manager**: Gerenciamento automático de drivers do navegador.
- **Uvicorn**: Servidor ASGI de alta performance.

## 📋 Como rodar o projeto

1. **Clone o repositório**:
   ```bash
   git clone [https://github.com/SEU_USUARIO/linkedin-job-scraper.git](https://github.com/SEU_USUARIO/linkedin-job-scraper.git)
   cd linkedin-job-scraper
Crie e ative seu ambiente virtual:

Bash

python -m venv .venv
# No Windows:
.\.venv\Scripts\activate
Instale as dependências:

Bash

pip install -r requirements.txt
Inicie o servidor:

Bash

python -m uvicorn main:app --reload
Acesse a interface de busca:
Abra http://127.0.0.1:8000/docs no seu navegador, clique em GET /vagas/, depois em Try it out e preencha os campos.

📁 Output (Dados Coletados)
O sistema gera um arquivo CSV contendo:

Título: Nome da posição anunciada.

Empresa: Nome da organização contratante.

Local: Cidade e Estado da vaga.

Link: URL direta para a candidatura no LinkedIn.
