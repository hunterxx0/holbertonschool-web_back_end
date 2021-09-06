#!/usr/bin/env python3
"""
list_all Method
"""
import pymongo


def list_all(mongo_collection):
    """
    List all documents in Python.
    """
    return list(mongo_collection.find())
