import re
from pymongo import MongoClient

def main():
    getTrendyPres()

def getTrendyPres():
    client = MongoClient('mongodb://127.0.0.1:27017',
            username='bdb',
            password='bigdatabois',
            authSource='admin')

    db = client.admin
    twitdb = client['twitdb']
    prescol = twitdb['president']


    regxPre = re.compile("pres", re.IGNORECASE)
    regxCand = re.compile("cand", re.IGNORECASE)
    presTrend = list(prescol.aggregate([
        {"$match": 
            { "$and": [
                { "$or": [
                    {"text": regxPre },
                    {"text": regxCand }
                ] },
                {"lang": { "$eq": "en" } }
            ] } },
        {"$group": {"_id": "$president", "count": { "$sum": 1 } } },
        {"$sort": { "count": -1} } 
    ]))
    return presTrend[0]['_id']

if __name__ == '__main__':
    main()
