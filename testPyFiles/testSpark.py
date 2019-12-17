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

tweetsCur = prescol.find({}, {"president":1, "text":1})
presidentsList = list(prescol.find({}, {"president"}).distinct("president"))

# for each president in presidentsList
# get wordcount for all text tweets

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
