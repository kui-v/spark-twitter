# Output: Dictionary of 
import re
from pymongo import MongoClient
#from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

def main():
    getWordsAssociated()

def getWordsAssociated():
    #conf = SparkConf().setAppName("Get Words Associated").setMaster("local[*]")
    #sc = SparkContext(conf = conf)
    spark = SparkSession \
        .builder \
        .appName("myApp") \
        .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/twitdb.impeach") \
        .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/twitdb.impeach") \
        .getOrCreate()

    client = MongoClient('mongodb://127.0.0.1:27017',
            username='bdb',
            password='bigdatabois',
            authSource='admin')

    df = spark.read.format("mongo").load
    print("~~~~~~~~~~","","","",type(df),"","","~~~~~~~~~~~")
'''
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
'''
if __name__ == '__main__':
    main()
