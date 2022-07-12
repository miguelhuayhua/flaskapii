# Import database connection
from .connectMongo import getDatabase
from bson import ObjectId

# getting a movie batch information


def getMoviesBySize(skip=0, limit=20):
    movies = getDatabase().get_collection('movies')
    data = movies.aggregate([
        {
            '$skip': skip
        }, {
            '$limit': limit
        }, {
            '$set': {
                '_id': {
                    '$toString': '$_id'
                }
            }
        }
    ])
    return list(data)

# getting movies by movie title


def getMoviesByTitle(title=''):
    movies = getDatabase().get_collection('movies')
    data = movies.aggregate([
        {
            '$match': {
                'title': {
                    '$regex': title,
                    '$options': 'ia'
                }
            }
        }, {
            '$set': {
                '_id': {
                    '$toString': '$_id'
                }
            }
        }
    ])
    return list(data)

# getting movies by attributes


def getMoviesByAttributes(genre="", type=0, size=0):
    genre = str(genre)
    genre = genre.strip()
    type = int(type)
    size = int(size)
    genres = genre.split(' ')
    property = Undefined
    propertyValue = Undefined
    if(type == 0):
        property = 'imdb.rating'
        propertyValue = -1
    elif (type == 1):
        property = 'year'
        propertyValue = -1
    elif (type == 2):
        property = 'year'
        propertyValue = 1
    movies = getDatabase().get_collection('movies')
    data = movies.aggregate([
        {'$match':
            {
                'genres': {'$all': genres},
            }
         },
        {'$sort': {property: propertyValue}
         },
        {
            '$skip': 20*size
        },
        {
            '$limit': 20
        },
        {
            '$set': {'_id': {'$toString': '$_id'}}
        }
    ])
    return list(data)

# getting movies by id


def getMovieById(id=""):
    movies = getDatabase().get_collection('movies')
    return list(movies.aggregate([
        {
            '$match': {
                '_id': ObjectId(id)
            }
        }, {
            '$set': {
                '_id': {
                    '$toString': '$_id'
                }
            }
        }
    ]))

# getting titles using by the app search


def getTitles(title=""):
    if title == "":
        return []
    else:
        movies = getDatabase().get_collection('movies')
        return list(movies.aggregate([
            {
                '$match': {
                    'title': {
                        '$regex': title,
                        '$options': 'ia'
                    }
                }
            },
            {
                '$project': {
                    '_id': {
                        '$toString': '$_id'
                    },
                    'title': 1
                }
            }, {'$limit': 10
                }
        ]))
