from pymongo import MongoClient
# Replace the uri string with your MongoDB deployment's connection string.
uri = "mongodb+srv://admin:james@cluster0.ujzjm.mongodb.net/todoapp?retryWrites=true&w=majority"
client = MongoClient(uri)
# database and collection code goes here
db = client.todoapp
coll = db.trains
# find code goes here
# iterate code goes here
# Close the connection to MongoDB when you're done.
#client.close()