#!/usr/bin/env python3
"""Print Nginx logs stats from MongoDB"""
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def main():
    """Provides some stats about Nginx logs stored in MongoDB"""
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://127.0.0.1:27017', serverSelectionTimeoutMS=2000)
        
        # Test the connection
        client.admin.command('ping')
        
        # Access the logs collection
        collection = client.logs.nginx

        # Total number of logs
        total_logs = collection.count_documents({})
        print(f"{total_logs} logs")

        # Methods count
        print("Methods:")
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        for method in methods:
            count = collection.count_documents({"method": method})
            print(f"    method {method}: {count}")

        # Status check count
        status_check = collection.count_documents({
            "method": "GET",
            "path": "/status"
        })
        print(f"{status_check} status check")
        
    except ConnectionFailure:
        print("Error: Could not connect to MongoDB. Please ensure MongoDB is running.")
        print("To install and start MongoDB, run the following commands:")
        print("1. sudo apt-get update")
        print("2. sudo apt-get install -y mongodb")
        print("3. sudo service mongodb start")
        return 1
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())