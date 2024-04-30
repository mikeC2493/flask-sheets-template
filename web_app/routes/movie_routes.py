from flask import Blueprint, render_template, current_app #, session

from app.models.movie import Movie

movie_routes = Blueprint("movie_routes", __name__)

@movie_routes.route("/movies")
def movies():
    movies = Movie.all()
    return render_template("movies.html", movies=movies)