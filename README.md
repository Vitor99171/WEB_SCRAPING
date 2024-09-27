# Catho Job Scraper

Este projeto é um web scraper desenvolvido para extrair informações de vagas de emprego no site Catho, usando Selenium e BeautifulSoup. O objetivo é permitir ao usuário realizar buscas personalizadas de vagas e extrair dados como título, empresa, salário, localização e data de publicação diretamente da página.

## ⚙️ Funcionalidades

- 🔍 Busca automatizada de vagas por palavra-chave no site da Catho.
- 📝 Extração de informações das vagas, como:
  - **Título da vaga**
  - **Nome da empresa**
  - **Salário**
  - **Localização**
  - **Data de publicação**
- 🚫 Bypass automático de anúncios e pop-ups que aparecem ao carregar o site.
- ⌨️ Uso de teclas (Enter) para simular a pesquisa diretamente no campo de busca.

## 🛠️ Pré-requisitos

Certifique-se de que você tenha as seguintes ferramentas instaladas em sua máquina:

- [Python 3.x](https://www.python.org/downloads/)
- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Geckodriver](https://github.com/mozilla/geckodriver/releases) (para usar com o Firefox)

Instale as dependências necessárias executando:

```bash
pip install selenium beautifulsoup4


🚀 Configuração
Clone este repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/catho-job-scraper.git
cd catho-job-scraper
Baixe e configure o Geckodriver e adicione-o ao seu PATH, ou indique o caminho no script.

Execute o script:

bash
Copiar código
python web.py
Após rodar o script, você será solicitado a digitar o cargo ou palavra-chave para buscar as vagas.

📂 Estrutura do Código
web.py: Script principal que executa a automação do navegador, faz a busca da vaga, extrai os dados e exibe no console.
requirements.txt: Lista das dependências para o projeto.
🔧 Personalização
Você pode ajustar a busca para filtrar vagas por diferentes critérios, como localização, tipo de contrato, entre outros, ajustando o campo de pesquisa e os seletores de CSS no script.

🛠️ Futuras Implementações
Melhor tratamento de exceções.
Exportação dos dados extraídos para um arquivo CSV ou JSON.
Suporte a diferentes navegadores além do Firefox.
🤝 Contribuição
Sinta-se à vontade para contribuir com este projeto. Para isso, faça um fork, crie uma branch, faça suas alterações e envie um pull request.
