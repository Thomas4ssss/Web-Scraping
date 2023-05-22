import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get("https://g1.globo.com/ultimas-noticias/")
content = response.content

site = BeautifulSoup(content, 'html.parser') 

noticias = site.findAll("div", attrs = {"class" : "feed-post-body"})
#print(noticia.prettify()) #usado somente para saber onde extrair o titulo e o link

lista_de_noticias = []

for noticia in noticias:

    titulo = noticia.find("a", attrs = {"class" : "feed-post-link"})

    print((titulo.text))  # para não sair a tag inteira

    print(titulo['href'])

    subtitulo = noticia.find("div" , attrs = {"class" : "feed-post-body-resumo"}) 

    if(subtitulo):
        print(subtitulo.text)
        lista_de_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_de_noticias.append([titulo.text, '', titulo['href']])

    print ('\n ===================================\n')

df = pd.DataFrame(lista_de_noticias, columns = ['Título', 'Subtítulo', 'Link'])

df.to_csv('noticias_do_dia.csv', index = False)

print(df)

