#!/usr/bin/env python3
"""
Log stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs".format(logs.count_documents({})))
    print("Methods:")
    for i in method:
        print("\tmethod {}: {}".format(i,
                                       len(list(logs.find(
                                           {"method": i})))))
    print("{} status check".format(len(list(logs.find(
        {"method": "GET", "path": "/status"})))))
    ll = list(logs.aggregate(
        [{"$group": {"_id": '$ip', 'count': {"$sum": 1}}},
         {"$sort": {"count": -1}},
         {"$limit": 10}
         ]
    ))
    print("IPs:")
    for i in ll:
        print("\t{}: {}".format(i.get('_id'), i.get('count')))
