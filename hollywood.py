hollywood_movies = [
    "Titanic", "The Shawshank Redemption", "Inception", 
    "The Dark Knight", "Pulp Fiction", "The Godfather",
    "Forrest Gump", "Gladiator", "Jurassic Park"
]

def is_hollywood_movie(movie_name):
      movie_name = movie_name.title()
  
    if movie_name in hollywood_movies:
        return True
    else:
        return False

movie_name = input("Enter the movie name: ")
if is_hollywood_movie(movie_name):
    print(f"{movie_name} is a Hollywood movie.")
else:
    print(f"{movie_name} is not a Hollywood movie.")