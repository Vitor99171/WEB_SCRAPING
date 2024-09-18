from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
# Solicitar ao usuário o termo de pesquisa para filtrar as vagas
termo_pesquisa = input("Digite o título ou termo da vaga que você está procurando: ")

# Inicializar o driver do Firefox com opções (como rodar em segundo plano se necessário)
options = Options()
# options.add_argument("--headless")  # Caso queira rodar o navegador em modo invisível
driver = webdriver.Firefox(options=options)

# Abrir o site da Catho
url = 'https://www.catho.com.br/vagas/'
driver.get(url)

# Tempo para a página carregar totalmente
time.sleep(0)
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

# Lista para armazenar os dados das vagas
dados_vagas = []

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

    # Armazenar as informações extraídas
    dados_vagas.append({
        'Título': titulo,
        'Empresa': empresa,
        'Salário': salario,
        'Localização': localizacao,
        'Data de Publicação': data_publicacao
    })

# Exibir as vagas filtradas
if dados_vagas:
    for vaga in dados_vagas:
        print(f"Título: {vaga['Título']}")
        print(f"Empresa: {vaga['Empresa']}")
        print(f"Salário: {vaga['Salário']}")
        print(f"Localização: {vaga['Localização']}")
        print(f"Data de Publicação: {vaga['Data de Publicação']}")
        print('-' * 40)
else:
    print(f"Nenhuma vaga encontrada para o termo: {termo_pesquisa}")
