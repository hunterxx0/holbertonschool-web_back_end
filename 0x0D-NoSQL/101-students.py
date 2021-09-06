#!/usr/bin/env python3
"""
Top students
"""
import pymongo


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """
    ll = list(mongo_collection.find({}))

    fres = [{"name": x.get("name"),
             "_id": x.get("_id"),

             "averageScore": (
                 (x.get("topics")[0].get("score") +
                     x.get("topics")[1].get("score") +
                     x.get("topics")[2].get("score")) / 3
    )} for x in ll]
    return sorted(fres, key=lambda i: i['averageScore'], reverse=True)
