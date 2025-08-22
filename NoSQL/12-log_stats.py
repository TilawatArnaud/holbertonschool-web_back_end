#!/usr/bin/env python3
"""
Provides stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

if __name__ == "__main__":

    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx

    x = collection.count_documents({})
    print("{} logs".format(x))
    print("Methods:")

    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for i in method:
        count = collection.count_documents({"method": i})
        print("\tmethod {}: {}".format(i, count))

    check_GET = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(check_GET))
