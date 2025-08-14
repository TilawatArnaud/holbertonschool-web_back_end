#!/usr/bin/env python3

"""
This module provides stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def log_stats():
    """
    Provides stats about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx
    total = collection.count_documents({})
    print(f"{total} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")
    status = collection.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print(f"{status} status check")


if __name__ == "__main__":
    log_stats()