#!/usr/bin/env python3
""" 8. List all documents in Python
"""

import pymongo


def list_all(mongo_collection):
    """ list_all.
    """
    docs = mongo_collection.find()
    return [x for x in docs]
