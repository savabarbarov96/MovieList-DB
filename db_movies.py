import time
import sqlite3


conn = sqlite3.connect("movies.db")

cursor = conn.cursor()
## Create table
# conn.execute("""CREATE TABLE movies (
#                 movie_name  text,
#                 genre text,
#                 director text
#)""")



USER_MENU = "\nType list to list movies, type add to add movies to the list, search database or type q to quit the program\n"


def movie_to_list():
    add_movie = input("What is the name of the movie ")
    movie_genre = input("What is the genre ")
    movie_director = input("Who is the movie director ")

    cursor.execute("INSERT INTO movies VALUES (?, ?, ?)", (add_movie,movie_genre,movie_director))

    conn.commit()
    print(f"{add_movie} was added to the list")
def list_movies():
    cursor.execute("SELECT * FROM movies ")
    print(cursor.fetchall())
    conn.commit()
    conn.close()


def find_movies():
    search = input("What do you want to search with:Name, Genre, Director:\n")
    if search.lower() == "name":
        name_search = input("What is the name of the movie\n")
        cursor.execute("SELECT * FROM movies WHERE lower(movie_name) LIKE lower(?)", ('%'+name_search+'%',))
        print(cursor.fetchall())

    elif search.lower() == "ganre" and "genre":
        genre_search = input("What is the ganre of the movie?\n")
        cursor.execute("SELECT * FROM movies WHERE lower(genre) LIKE lower(?)", ('%' + genre_search + '%',))
        print(cursor.fetchall())

    elif search.lower() == "director":
        director_search = input("Who is the director of the movie?\n")
        cursor.execute("SELECT * FROM movies WHERE lower(director) LIKE lower(?)", ('%' + director_search + '%',))
        print(cursor.fetchall())
    else:
        print("Invalid input")
        find_movies()
# list movies
selection = input(USER_MENU)
while selection != "q":
    # list movies
    if selection.lower() == "list":
        list_movies()

    # add movies
    elif selection.lower() == "add":
        movie_to_list()
    # find movies
    elif selection.lower() == "search":
        find_movies()
    elif selection.lower() == "quit":
        quit()
    else:
        print("Invalid input")



    selection = input(USER_MENU)

## Sava Barbarov
