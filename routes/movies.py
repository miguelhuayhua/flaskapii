# flask routing
from flask import Blueprint, jsonify, request
# movie dao
from dao.daomovie import getMoviesBySize, getMoviesByTitle, getMoviesByAttributes, getMovieById, getTitles


movieRouter = Blueprint('movie', __name__, url_prefix='/movies')


@movieRouter.route('/', methods=['GET', 'POST'])
def mainMovie():
    if(request.method == 'POST'):
        return jsonify(getMoviesByAttributes(request.form.get('genres'), request.form.get('type'), request.form.get('size')))
    else:
        return jsonify(getMoviesBySize())


@movieRouter.route('<title>', methods=['GET'])
def getByTitle(title):
    return jsonify(getMoviesByTitle(title))


@movieRouter.route('/movie/<id>', methods=['GET'])
def getById(id):
    return jsonify(getMovieById(id))


@movieRouter.route('/search', methods=['POST'])
def searchTitle():
    data = getTitles(request.json['title'])
    return jsonify(data)
