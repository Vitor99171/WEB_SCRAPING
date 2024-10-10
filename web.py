import sqlite3
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time

# Solicitar ao usuário o termo de pesquisa para filtrar as vagas
termo_pesquisa = input("Digite o título ou termo da vaga que você está procurando: ")

# Remover caracteres especiais e espaços do termo de pesquisa para usar como nome da tabela
nome_tabela = "vagas_de_" + re.sub(r'\W+', '_', termo_pesquisa.lower())

# Inicializar o driver do Firefox com opções (como rodar em segundo plano se necessário)
options = Options()
# options.add_argument("--headless")  # Caso queira rodar o navegador em modo invisível
driver = webdriver.Firefox(options=options)

# Abrir o site da Catho
url = 'https://www.catho.com.br/vagas/'
driver.get(url)

# Tempo para a página carregar totalmente
time.sleep(2)

# Localizar o campo de pesquisa e inserir o termo fornecido
campo_pesquisa = driver.find_element(By.ID, 'keyword')  # Usar o ID do campo de pesquisa
campo_pesquisa.send_keys(termo_pesquisa)  # Inserir o termo no campo
botao_buscar = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
botao_buscar.click()  # Clicar no botão "Buscar"

# Tempo para visualizar a digitação
time.sleep(2)

# Extrair o HTML da página de resultados
html = driver.page_source

# Parsear o HTML com BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Fechar o navegador
driver.quit()

# Encontrar as vagas (ajustar de acordo com a estrutura da página de resultados)
vagas = soup.find_all('li', class_='search-result-custom_jobItem__OGz3a')

# Conectar ao banco de dados SQLite (ou criar o arquivo caso não exista)
conn = sqlite3.connect('vagas.db')
cursor = conn.cursor()

# Criar a tabela dinamicamente com base no termo de pesquisa (se ela não existir)
cursor.execute(f'''
CREATE TABLE IF NOT EXISTS {nome_tabela} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    empresa TEXT,
    salario TEXT,
    localizacao TEXT,
    data_publicacao TEXT
)
''')

# Percorrer cada vaga e extrair as informações
for vaga in vagas:
    # Título da vaga usando CSS Selector
    titulo_element = vaga.select_one('h2')  # Localiza o primeiro <h2> dentro da vaga
    titulo = titulo_element.text.strip() if titulo_element else 'Título não disponível'

    # Nome da empresa (adicionando verificação)
    empresa_element = vaga.find('p', class_='sc-bDumWk jqoYXw')
    empresa = empresa_element.text.strip() if empresa_element else 'Confidencial'

    # Salário (adicionando verificação)
    salario_element = vaga.find('div', class_='custom-styled_salaryText__oSvPo')
    salario = salario_element.text.strip() if salario_element else 'Salário não informado'

    # Localização (adicionando verificação)
    localizacao_element = vaga.find('button', class_='sc-kgOKUu eemqfS')
    localizacao = localizacao_element.text.strip() if localizacao_element else 'Localização não disponível'

    # Data de publicação ou atualização (adicionando verificação)
    data_publicacao_element = vaga.find('time')
    data_publicacao = data_publicacao_element.text.strip() if data_publicacao_element else 'Data não disponível'

    # Inserir os dados da vaga no banco de dados
    cursor.execute(f'''
    INSERT INTO {nome_tabela} (titulo, empresa, salario, localizacao, data_publicacao)
    VALUES (?, ?, ?, ?, ?)
    ''', (titulo, empresa, salario, localizacao, data_publicacao))

    # Commitar a inserção ao banco
    conn.commit()

# Fechar a conexão com o banco de dados
conn.close()

# Exibir uma mensagem de confirmação
print(f"As vagas relacionadas ao termo '{termo_pesquisa}' foram salvas na tabela '{nome_tabela}' do banco de dados SQLite.")
