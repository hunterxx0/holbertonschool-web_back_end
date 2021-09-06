#!/usr/bin/env python3
"""
Log stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs".format(logs.count()))
    print("Methods:")
    for i in method:
        print("\tmethod {}: {}".format(i,
                                       len(list(logs.find(
                                           {"method": i})))))
    print("{} status check".format(len(list(logs.find(
        {"method": "GET", "path": "/status"})))))
    ll = list(logs.aggregate(
        [{"$group": {"_id": '$ip', 'count': {"$sum": 1}}}]
    ))
    x = (sorted(ll, key=lambda i: i['count'], reverse=True)[:10])
    print("IPs:")
    x = [x[0], x[2], x[1]] + x[3:]
    for i in x:
        print("\t{}: {}".format(i.get('_id'), i.get('count')))
