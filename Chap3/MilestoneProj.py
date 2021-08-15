# Add new movie to my collections
# list all the movies in my collections
# Find a movie

# Show a menu to user
# Implement each requirement as separate function
# Stop running when q is pressed

# use list
# for each movie store: (use dict) movie
# title, director and release year

print("Welcome to Movie Manager!")

movies = []

def add():
    title = input("Please enter movie's title: ")
    director = input(f"Please enter {title}'s director: ")
    release_year = int(input(f"Please enter {title}'s release year: "))

    _mov = {
        "title": title,
        "director": director,
        "release_year": release_year
    }

    movies.append(_mov)

def list_mov():
    for movie in movies:
        _title = movie["title"]
        _director = movie["director"]
        _r_year = movie["release_year"]
        print(f"Movie: {_title}, Director: {_director}, Release Year: {_r_year}")


def find_movie():
    search_title = input("Enter movie title you're looking for: ")

    for movie in movies:
        if movie["title"] == search_title:
            print("Title: " + str(movie["title"]))
            print("Director: " + str(movie["director"]))
            print("Release Year: " + str(movie["release_year"]))

options = {
    "a": add,
    "l": list_mov,
    "f": find_movie
}

def menu():
    operation = input("press 'a' to add movie, 'l' to list all movies, 'f' to find a movie and 'q' to quit: ")
    while operation != "q":
        if operation in options:
            function_opted = options[operation]
            function_opted()
        else:
            print("unknown command. Please try again")

        operation = input("press 'a' to add movie, 'l' to list all movies, 'f' to find a movie and 'q' to quit: ")

menu()