from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017',
        username='lentils',
        password='',
        authSource='admin')

db = client.admin

# var for the database itself
twitdb = client['twitdb']

# var for the collection named cringe
cringecol = twitdb['cringe']

# insert into cringe collection
cringecol.insert({'name':'test', 'text':'test text'})

# find from cringe collection
cringecol.find()
