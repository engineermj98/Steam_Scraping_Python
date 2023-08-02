# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 13:24:52 2020

@author: pichoncito
"""
#Importamos las librerias necesarias
from bs4 import BeautifulSoup
import requests
import pandas as pd
#Se establece el url tipo string de la pagina que utilizaremos para sacar la informacion. 
url = 'https://store.steampowered.com/specials#tab=TopSellers'
#Se descarga el contenido del html con requests
page = requests.get(url)
#Se transofmra a formato bs para identificar diferentes elementos de html, para seleccionar distintas partes de una pagina
soup= BeautifulSoup(page.content, 'html.parser')

#////////////////////////////////////////////////Nombres de los juegos
ju= soup.find_all('div', class_='tab_item_name') #div es el origen de donde se originan los datos del html, o la parte que estoy buscando...class_ porque solo class lo reconoce como funcion de python

#Sacar solo los nombres
#print('JUEGOS')
juegos= list()
#Para descartar que se adquiera la informacion excesiva de todos los elementos que tengan como class tab item name, se hace una seleccion de la cantidad de datos que queremos obtener
count = 0
for i in ju:
    if count<20:#Muestra el listado de los primeros 20 elementos de la pagina
        juegos.append(i.text)
    else:
        break
    count+=1

#print(juegos, len(juegos))   

#////////////////////////////////////////////////Ofertas en % de los juegos

#print('DESCUENTOS')


of=soup.find_all('div', class_='discount_pct')
ofertas=list()
count=0
for i in of:
    if count <20:
        ofertas.append(i.text)
    else:
        break
    count+=1
    
#print(ofertas, len(ofertas)) 

#////////////////////////////////////////////////Ofertas en precio de los juegos

#print('PRECIOS FINALES')


pr=soup.find_all('div',class_='discount_final_price')
precios=list()
count=0
for i in pr:
    if count <20:
        precios.append(i.text)
    else:
        break
    count+=1
    
#print(precios, len(precios))

#Meteremos todo en un DataFrame de pandas
df = pd.DataFrame({'Nombre': juegos, 'Ofertas': ofertas, 'Precio Final': precios}, index=list(range(1,21))) #Indice que inicia del 1 al 21 por la cantidad de elementos
print(df)

#Lo guardamos como fichero de texto csv
df.to_csv('TheNewSStore.csv', index=False)#Para que no guarde el indice, se deja enfalso.
