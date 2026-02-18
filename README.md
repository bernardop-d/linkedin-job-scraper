# LinkedIn Job Scraper 🕵️‍♂️

Ferramenta de automação desenvolvida em Python para monitoramento e coleta de vagas no LinkedIn. Utiliza **Selenium** para navegação e simulação de comportamento humano.

## 🚀 Funcionalidades
- Login automático seguro (senha não salva no código).
- Busca personalizada por cargo e localização.
- Exportação dos resultados para CSV (Excel).
- Anti-bot básico: Delays aleatórios para simular navegação humana.

## 🛠️ Instalação

1. Clone o repositório:
   ```bash
   git clone <seu-repositorio>
   cd linkedin-job-scraper
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Execução

```bash
python main.py
```

## 📁 Output

O script gera um arquivo `jobs_data.csv` contendo:

- Title
- Company
- Link

## ⚠️ Observação

O LinkedIn pode alterar seletores HTML a qualquer momento. Caso o script pare de funcionar, revise as classes utilizadas no código.

---

Desenvolvido para fins educacionais e de portfólio.
