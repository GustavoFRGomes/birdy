import json
import pymongo

def save_to_mongo(data, mongo_db, mongo_db_coll, **mongo_conn_kw):

    client = pymongo.MongoClient(**mongo_conn_kw)
    db = client[mongo_db]
    coll = db[mongo_db_coll]

    return coll.insert(data)

def load_from_mongo(mongo_db, mongo_db_coll, return_cursor=False, \
        criteria=None, projection=None, **mongo_conn_kw):

    client = pymongo.MongoClient(**mongo_conn_kw)
    db = client[mongo_db]
    coll = db[mongo_db_coll]

    if criteria is None:
        criteria = {}

    if projection is None:
        cursor = coll.find
    else:
        cursor = coll.find(criteria, projection)

    if return_cursor:
        return cursor
    else:
        return [ item for item in cursor ]

if __name__ == '__main__':
    q = 'Crossfit' # random query to search the for tweets

    twitter_api = oauth_login()

    results = twitter_search(twitter_api, q, max_results=10)

    save_to_mongo(results, 'search_results', q)

    load_from_mongo('search_results', q)
