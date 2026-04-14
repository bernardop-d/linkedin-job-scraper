🚀 LinkedIn Job Scraper API
API REST desenvolvida com FastAPI e Selenium para automação de busca, filtragem e extração de vagas de emprego no LinkedIn. O sistema conta com validação rigorosa de dados via Pydantic e exportação estruturada.

📌 O Problema
A busca manual por vagas no LinkedIn é um processo repetitivo e moroso. Filtrar por regime de trabalho, rolar infinitas páginas e organizar dados manualmente consome um tempo que poderia ser dedicado à preparação para entrevistas.

💡 A Solução
Este projeto automatiza o ciclo completo de coleta:

Automação de Navegação: Simula o comportamento humano para navegar entre as vagas.

Extração Inteligente: Captura títulos, empresas, localizações e links.

Entrega via API: Expõe os dados prontos para consumo ou análise em formato JSON/CSV.

🛠️ Stack Técnica
Python 3.10+: Linguagem base.

FastAPI: Framework de alta performance para a camada de API.

Selenium & Webdriver Manager: Automação do navegador com gerenciamento dinâmico de drivers.

Pydantic: Data validation e garantia de integridade dos schemas.

Uvicorn: Servidor ASGI de produção.

⚙️ Funcionalidades e Decisões Técnicas
Mimetismo Humano: Implementação de scroll progressivo e intervalos de tempo (delays) variáveis para mitigar a detecção de bots.

Desacoplamento: Lógica de scraping separada da interface da API, facilitando a manutenção e futuras trocas de biblioteca (ex: para Playwright).

Fail-Fast com Pydantic: Se o LinkedIn alterar a estrutura da página, a validação descarta dados malformados antes de retornar ao usuário, garantindo um CSV limpo.

Documentação Automática: Swagger UI disponível nativamente para teste dos endpoints.

🚀 Como Executar
1. Clonar e Instalar
Bash
git clone https://github.com/bernardop-d/linkedin-job-scraper.git
cd linkedin-job-scraper
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
2. Rodar a Aplicação
Bash
python -m uvicorn main:app --reload
3. Utilizar
Acesse http://127.0.0.1:8000/docs para interagir com a interface:

Endpoint GET /vagas/: Informe o cargo, localização e filtros desejados.

O sistema abrirá o navegador, processará as vagas e retornará o arquivo estruturado.

📂 Estrutura de Arquivos
Plaintext
linkedin-job-scraper/
├── app/
│   ├── scraper.py     # Lógica de automação Selenium
│   ├── schemas.py     # Modelos de dados Pydantic
│   └── main.py        # Endpoints FastAPI
├── tests/             # Testes unitários com Pytest
├── requirements.txt
└── README.md
⚠️ Observações Técnicas
Requisito: É necessário ter o Google Chrome instalado no ambiente.

Rate Limit: O LinkedIn possui mecanismos de defesa robustos. Caso ocorra bloqueio, o scraper foi desenhado para registrar o erro e sugerir um intervalo de espera.

Modo Headless: Atualmente o Chrome abre de forma visível para facilitar o monitoramento da execução.

Desenvolvido por Bernardo Pereira Dutra
