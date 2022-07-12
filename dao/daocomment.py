from .connectMongo import getDatabase
from bson import ObjectId
# data functions


def getCommentsByMovieId(movieId):
    db = getDatabase()
    comments = db.get_collection('comments')
    data = comments.aggregate([
        {
            '$match': {
                'movie_id': ObjectId(movieId)
            }
        }, {
            '$project': {
                '_id': {
                    '$toString': '$_id'
                },
                'name': 1,
                'email': 1,
                'text': 1,
                'date': 1
            }
        }
    ])
    return list(data)
