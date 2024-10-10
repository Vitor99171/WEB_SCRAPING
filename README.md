# Catho Job Scraper

Este projeto é um web scraper desenvolvido para extrair informações de vagas de emprego no site Catho, utilizando Selenium e BeautifulSoup. O usuário pode realizar buscas personalizadas de vagas por palavra-chave, e os dados extraídos, como título, empresa, salário, localização e data de publicação, são armazenados em um banco de dados SQLite.

## ⚙️ Funcionalidades

- 🔍 **Busca automatizada de vagas** por palavra-chave no site da Catho.
- 📝 **Extração de informações das vagas**, incluindo:
  - **Título da vaga**
  - **Nome da empresa**
  - **Salário**
  - **Localização**
  - **Data de publicação**
- 🗄️ **Armazenamento dinâmico**: As vagas são salvas em uma tabela SQLite, cujo nome é gerado automaticamente com base no termo de pesquisa fornecido pelo usuário.
- 🚫 **Bypass automático de anúncios** e pop-ups que aparecem durante o carregamento do site.
- ⌨️ Uso de teclas (Enter) para simular a pesquisa diretamente no campo de busca.

## 🛠️ Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- [Python 3.x](https://www.python.org/downloads/)
- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [SQLite3](https://www.sqlite.org/index.html) (para o banco de dados)
- [Geckodriver](https://github.com/mozilla/geckodriver/releases) (para rodar com o Firefox)

Instale as dependências necessárias executando:

```bash
pip install selenium beautifulsoup4 sqlite3


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
vagas.db: Arquivo de banco de dados SQLite que será criado automaticamente para armazenar as vagas extraídas.

🔧 Personalização
Você pode ajustar a busca para filtrar vagas por diferentes critérios, como localização, tipo de contrato, entre outros, ajustando o campo de pesquisa e os seletores de CSS no script.

Os dados são armazenados em um banco de dados SQLite com uma tabela cujo nome é gerado dinamicamente no formato:

Exemplo: Se o usuário buscar por "Desenvolvedor Python", a tabela será criada como vagas_de_desenvolvedor_python.

As colunas da tabela incluem:

id: Identificador único da vaga (chave primária).
titulo: Título da vaga.
empresa: Nome da empresa.
salario: Salário oferecido (se disponível).
localizacao: Localização da vaga.
data_publicacao: Data de publicação ou atualização da vaga.

🛠️ Futuras Implementações
Melhor tratamento de exceções.
Exportação dos dados extraídos para um arquivo CSV ou JSON.
Suporte a diferentes navegadores além do Firefox.

🤝 Contribuição
Sinta-se à vontade para contribuir com este projeto. Para isso, faça um fork, crie uma branch, faça suas alterações e envie um pull request.
