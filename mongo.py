'''This file is me connecting to a mongo db database similar
 to how i connected to my elephantSQL data base in module 2.
 It took me forever to just get pymongo to be able to import.
 I am '''


import pymongo

#this is what we get back when we print sqlite query
test_characters = [
(1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1),
(2, 'Optio dolorem ex a', 0, 0, 10, 1, 1, 1, 1)
]

#this is the same info but as an array of documents
#how our info will be stored inside of mongodb
character_documents = [
    {
    'character_id': 1,
    'name': 'Aliquid iste optio reiciendi',
    'level': 0,
    'exp': 0,
    'hp': 10,
    'strength': 1,
    'intelligence': 1,
    'dexterity': 1,
    'wisdom': 1
    },
    {
    'character_id': 2,
    'name': 'Optio dolorem ex a',
    'level': 0,
    'exp': 0,
    'hp': 10,
    'strength': 1,
    'intelligence': 1,
    'dexterity': 1,
    'wisdom': 1
    }
    ]

# we will grab all values from the tuple
# test_characters by looping over it and
# place in each value from their specific
# position in the tuple? watch again

#credentials
DBNAME = 'test'
PASSWORD = 'PGZRhxOoXQqn5MGI'



def mongo_connect(password=PASSWORD, dbname=DBNAME, collection_name='characters'):
    '''This function allows me to connect to to the client. and grab
    a specific collection from a specific database.'''
    client = pymongo.MongoClient(f'mongodb+srv://Charlieblk9400:{password}@cluster0.3xrf2rj.mongodb.net/{dbname}?retryWrites=true&w=majority')   
    db = client[dbname]
    collection = db[collection_name]

    return collection

 
if __name__ == '__main__':
    collection = mongo_connect(collection_name='people')
    result = collection.find_one({'name': 'Bryan'})
    print(result)
