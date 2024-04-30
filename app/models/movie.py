from app.db import BaseModel

class Movie(BaseModel):

    SHEET_NAME = "movies"

    COLUMNS = ["title", "director", "year","image"]
#I found the titles and images for these movies at this site https://www.timeout.com/film/best-movies-of-all-time
    SEEDS = [
        {"title": "The Godfather", "director": "Francis Ford Coppola", "year": 1972,"image": "https://media.timeout.com/images/105455970/750/562/image.webp"},
        {"title": "Citizen Kane", "director": "Orson Welles", "year": 1941, "image": "https://media.timeout.com/images/105455971/750/562/image.webp"},
        {"title": "Raiders of the Lost Ark", "director": "Steven Spielberg", "year": 1981, "image": "https://media.timeout.com/images/105455973/750/562/image.webp"},
        {"title": "La Dolce Vita", "director": "Federico Fellini", "year": 1960, "image": "https://media.timeout.com/images/105456105/750/562/image.webp"},
        {"title": "There Will Be Blood", "director": "Paul Thomas Anderson", "year": 2007, "image": "https://media.timeout.com/images/105455978/750/562/image.webp"},
        {"title": "Goodfellas", "director": "Martin Scorsese", "year": 1990, "image": "https://media.timeout.com/images/105536435/750/562/image.webp"},
        {"title": "North by Northwest", "director": "Alfred Hitchcock", "year": 1959, "image": "https://media.timeout.com/images/102240155/750/562/image.webp"},
        {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "image": "https://media.timeout.com/images/105455985/750/562/image.webp"},
        {"title": "Jaws", "director": "Steven Spielberg", "year": 1975, "image": "https://media.timeout.com/images/105455997/750/562/image.webp"},
        {"title": "Star Wars", "director": "George Lucas", "year": 1977, "image": "https://media.timeout.com/images/105456000/750/562/image.webp"},
        {"title": "Alien", "director": "Ridley Scott", "year": 1979, "image": "https://media.timeout.com/images/105456003/750/562/image.webp"},
    ]


if __name__ == "__main__":

    movies = Movie.all()
    print("FOUND", len(movies), "MOVIES")
    if any(movies):
        for movie in movies:
            print(movie.title, movie.director, movie.year)
    else:
        Movie.seed()
