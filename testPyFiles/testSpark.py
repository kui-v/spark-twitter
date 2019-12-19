import sys
from operator import add

from pyspark.sql import SparkSession
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017',
        username='bdb',
        password='bigdatabois',
        authSource='admin')

db = client.admin
twitdb = client['twitdb']
prescol = twitdb['president']

spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

presCur = prescol.aggregate([{"$group": {'_id':"$president", 'count':{"$sum":1}}}])



'''
tweetsCur = cringecol.find({}, {"president":1, "text":1})
presidentsList = list(cringecol.find({}, {"president"}).distinct("president"))
'''
# for each president, get count of all their tweet records in cringe colle

    '''
    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    counts = lines.flatMap(lambda x: x.split(' '))\
            .map(lambda x: (x, 1))\
            .reduceByKey(add)

    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))
    '''
spark.stop()