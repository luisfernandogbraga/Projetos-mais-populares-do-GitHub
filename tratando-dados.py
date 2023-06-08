import csv
import requests
from bs4 import BeautifulSoup

response = requests.get ('https://github.com/trending')

content = response.content

site = BeautifulSoup(content, 'html.parser')

dados = [['ranking', 'project', 'language', 'stars', 'starts_today', 'forks']]

# <article class="Box-row">
tabela = site.find_all('article', class_= 'Box-row')

for ranking, projeto in enumerate(tabela[:10], start=1): # criando um hank
    #coletando os dados um por um 
    project_element = projeto.find('span', class_='text-normal')
    project = project_element.text.strip().split('/')[0].strip() if project_element else ''
    
    language_element = projeto.find('span', itemprop='programmingLanguage')
    language = language_element.text.strip() if language_element else ''
    
    starts_element = projeto.find('a', class_='Link--muted d-inline-block mr-3')
    starts = starts_element.text.strip().replace(',', '') if starts_element else ''
    
    #aqui tive q tratar o dado por estar com int junto com string
    starts_today_element = projeto.find('span', class_='d-inline-block float-sm-right')
    starts_today = starts_today_element.text.strip().split()[0] if starts_today_element else ''

    #forks_element = projeto.find('a', class_='Link--muted d-inline-block mr-3') # está dando erro
    forks_element = projeto.find('a', href=lambda href: href and href.endswith('/forks'))
    forks = forks_element.text.strip().split()[0] if forks_element else'burro'
    
    dados.append([ranking,project, language, starts, starts_today, forks])


with open('github.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';')
    escritor_csv.writerows(dados)

print("Dados salvos com sucesso no arquivo github.csv!")