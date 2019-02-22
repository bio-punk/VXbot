import pymongo

print ("Connecting the DataBase") 
myClient = pymongo.MongoClient("mongodb://localhost:27017/")

print ("Getting the list of DataBase")
dblist = myClient.list_database_names()

print ("Creating DataBase")
if "vxbotdb" in dblist:
  print(u"数据库已存在！")
else:
	myDb = myClient["vxbotdb"]
	myCol = myDb["testCol"]
	myDict = {"recordName":"testINFO" }
	x = myCol.insert_one(myDict)
	print (x)