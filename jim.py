import os

import pymongo

from jim_process import process


def main():
    conn = pymongo.Connection()
    db = conn.jim
    coll = db.scores
    for filename in os.listdir('.'):
        if filename.startswith("results-"):
            for (rank, score, lohi, data) in process(filename):
                item = {
                    'rank': rank,
                    'score': score,
                    'lohi': lohi,
                    'data': data
                }
                coll.insert(item)


def reformat():
    conn = pymongo.Connection()
    db = conn.jim
    coll = db.scores
    which_columns = {
        'data': 0,
        '_id': 0,
    }
    for item in coll.find({}, which_columns):
        print(item)


if __name__ == '__main__':
    # main()
    reformat()
