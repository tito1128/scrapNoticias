'''import pymongo
medios = ["https://www.eldinamo.cl/","https://www.biobiochile.cl/","https://www.fayerwayer.com/"]
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["noticias"]
mycol = mydb["demo"]
for diarios in medios:
    mydict = {"url": diarios}
    x = mycol.insert_one(mydict)'''


import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["noticias"]
mycol = mydb["diarios"]
mydoc = mycol.find()
for x in mydoc:
  print(x['url'])




'''import pymongo
medios = ["https://www.eldinamo.cl/","https://www.biobiochile.cl/","https://www.fayerwayer.com/"]
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["noticias"]
mycol = mydb["diarios"]
mydb.diarios.drop();
for diarios in medios:
    mydict = {"url": diarios}
    x = mycol.insert_one(mydict) '''



'''import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["noticias"]
mycol = mydb["demo"]
mydoc = mycol.find()
#mydb.test.drop();
for x in mydoc:
	print(x)
  #print(x{"url":""})
























