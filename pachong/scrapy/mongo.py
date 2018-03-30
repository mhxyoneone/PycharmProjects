import pymongo

client = pymongo.MongoClient('localhost',27017)

db = client['test']
test1 = db['test1']
insertDate = '2017-10-10'
count = 20
insert_record = {'endDate': insertDate, 'count': count}
insert_res = test1.insert_one(insert_record)