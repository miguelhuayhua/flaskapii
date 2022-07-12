# importing flask and flask CORS
from flask import Flask
from flask_cors import CORS

# importing created routes
from routes.movies import movieRouter
from routes.comments import commentRouter
app = Flask(__name__)
CORS(app)
app.register_blueprint(movieRouter)
app.register_blueprint(commentRouter)
