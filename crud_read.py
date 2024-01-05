# find code goes here
from database import coll, client
cursor = coll.find()

# iterate code goes here
for doc in cursor:
    print(doc)
    
# Close the connection to MongoDB when you're done.
client.close()