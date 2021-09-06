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
