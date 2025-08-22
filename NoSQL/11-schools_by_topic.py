#!/usr/bin/env python3
"""  changes all schools by topic """

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ changes all schools by topic """
    collection = mongo_collection
    return collection.find({"topics": topic})
