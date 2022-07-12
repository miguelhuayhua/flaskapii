#import libraries
from flask import Blueprint, request, jsonify
from dao.daocomment import getCommentsByMovieId
# Create a route for the comments

commentRouter = Blueprint('comment', __name__, url_prefix='/comments')


@commentRouter.route('<id>', methods=['GET'])
def getCommentsByMovie(id):
    return jsonify(getCommentsByMovieId(id))
