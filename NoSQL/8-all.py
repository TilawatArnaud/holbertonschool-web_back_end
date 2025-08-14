#!/usr/bin/env python3
"""This module lists all documents in a collection."""

from pymongo import MongoClient


def list_all(mongo_collection):
    """Lists all documents in a collection."""
    documents = mongo_collection.find()
    if not documents:
        return ([])
    else:
        return (documents)
