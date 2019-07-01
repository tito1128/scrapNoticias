'''import urllib.request
try:
    import json
except ImportError:
    import simplejson as json
with urllib.request.urlopen("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty") as url:
    s = url.read()
    # I'm guessing this would output the html source code ?
    print(s)'''

'''
try:
    import json
except ImportError:
    import simplejson as json
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
'''


import json
import urllib.request
import pymongo
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db=connection.noticias
record1 = db.book_collection1
record1.drop()
page = urllib.request.urlopen("http://l4wisdom.com/pymongo/code/insert/test.json")
parsed = json.loads(page.read())
for item in parsed["Records"]:
    record1.insert(item)
	#print(item)


