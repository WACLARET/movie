movies = []
    
def menu():
   
    user_input = input("Please enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie and 'q' to quit: ").lower()
    while user_input != "q":
        if user_input == "a":
            add_movie()
        elif user_input == "l":
            show_movies(movies)
        elif user_input == "f":
            find_movie()
        else:
            print("Unknown command please Try again")

        user_input = input("\nPlease enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie and 'q' to quit: ").lower()


def add_movie():
    name = input("\nPlease ente the name of the movie: ")
    year = int(input("Please enter the year of the movie: "))
    content = input("Please enter the conten of the movie: ")
    director = input("Please enter the movie director: ")

    movies.append({
        "name": name,
        'year': year,
        "content": content,
        "director": director
    })

def show_movies(movies_list1):
    for movie in movies_list1:
        print(f"\nName is: {movie['name'].capitalize()}")
        print(f"Year is: {movie['year']}")
        print(f"Content is: {movie['content'].capitalize()}")
        print(f"Director is: {movie['director'].capitalize()}\n")

def find_movie():
    find = input("What property of the movie are you looking for? ")
    search = input("What are you searchin for? ")
    found_movies = find_by_inputs(search, lambda x: x[find])
    show_movies(found_movies)
    
def find_by_inputs(expected, finder):
    movies_list = []
    for movie in movies:
        if finder(movie) == expected:
            movies_list.append(movie)
    return movies_list

    
menu()