import pymongo

client = pymongo.MongoClient('localhost', 27017)

db = client['test_python']
test_m = db['test_m']