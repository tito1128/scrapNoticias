import datetime
import urllib.request
import re
import pymongo
from bs4 import BeautifulSoup

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["noticias"]
mycol = mydb["diarios"]
coleccionNotas = mydb["notas"]
mydoc = mycol.find()

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
#url = ["https://www.eldinamo.cl/"]
#url = ["https://www.rockandpop.cl/","https://www.eldinamo.cl/","https://www.biobiochile.cl/"]

for medios in mydoc:
#for medios in url:
    headers={'User-Agent':user_agent,}
    request=urllib.request.Request(medios["url"],None,headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    direcciones = []
    soup = BeautifulSoup(data, 'html.parser')
    
    for a in soup.find_all('a', href=True):
        #z = re.match("(g\w+)\W(g\w+)",a['href'])
        z = re.match("("+medios["url"]+"\w+)",a['href'])
        if z:
            #print(a['href'])
            direcciones.append((a['href']))
            
        
    direccionesDos = set(direcciones) # elimino duplicados
    #print(direccionesDos)
            
    for sitios in direccionesDos:
        try:
            request=urllib.request.Request(sitios,None,headers)
            response = urllib.request.urlopen(request)
            data = response.read()
            soup = BeautifulSoup(data,'html.parser')    
            try:
                urlOgg = soup.find("meta", property="og:url").get('content')
                imgOgg = soup.find("meta",  property="og:image").get('content')
                titleOgg = soup.find("meta",  property="og:title").get('content')
                descriptionOgg = soup.find("meta",  property="og:description").get('content')
                fechaOgg = soup.find("meta",  property="article:published_time").get('content')
                #clave = result = hashlib.md5(titleOgg.encode())
                mydict = {"titulo":titleOgg,"descripcion":descriptionOgg,"url":urlOgg,"fecha":fechaOgg,"imagen":imgOgg,"idmedio":medios["_id"],"fecha_scrap":datetime.datetime.now()}    
    
                print(titleOgg)
                print(medios["url"])
                print("========================================")
                
                try:
                    x = coleccionNotas.insert_one(mydict)
                except:
                    continue
    
            except:
                continue
        except:
            continue





    