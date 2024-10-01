# Scripting Python Foundations


# List of favorite movies with their release years
movies_list = [
    ("It", 2017),
    ("Spirited Away", 2001),
    ("The Matrix", 1999),
    ("Jaws", 1975),
    ("Your Name", 2016),
    ("Clue", 1985),
    ("My Neighbor Totoro", 1988)
]

# Function to check if a movie was released before or after 2000
def check_movie_release_date(movie, release_year):
    if release_year < 2000:
        print(f"{movie} was released before 2000.")
        return False
    else:
        print(f"{movie} was released after 2000.")
        return True

# List to store recent movies (released after 2000)
recent_movies = []
for movie, year in movies_list:
    if check_movie_release_date(movie, year):
        recent_movies.append(movie)

# Print recent movies
print("Recent movies:", recent_movies)
