from datetime import datetime


def receiveBudget():
    print("Lastly please enter the movie's budget")
    while True:
        budget = input()
        if budget.isdigit():
            return budget
        else:
            print("Incorrect budget format, should contains only digits (0-9)")


def receiveReleaseDate():
    while True:
        print("Enter the desired movie release date \n")
        date_string = input()
        try:
            date_obj = datetime.strptime(date_string, '%d/%m/%Y').date()
            if date_obj.year >= 2010:
                return date_obj
            else:
                print("Invalid date, Our system supports only movies released in the year 2010 and beyond.")
        except ValueError:
            print("Incorrect date format, should be dd/mm/yyyy")


def receiveGenre():
    genres = ["Action", "Adventure", "Animation", 'Biography', 'Comedy', 'Crime', 'Drama', 'Family', 'Horror']
    print("Enter the movie genre from the list below that suits your movie the best: \n", ", ".join(genres))
    while True:
        genre = input().capitalize()
        if genre in genres:
            return genre
        else:
            print("Invalid genre, should be on of the following:\n", ", ".join(genres))


def receiveAgeRating():
    ratings = ["G", "PG", "PG-13", 'R']
    print("Enter the movie age rating from the list below that suits your movie the best: \n", ", ".join(ratings))
    while True:
        rating = input().upper()
        if rating in ratings:
            return rating
        else:
            print("Invalid age rating, should be on of the following:\n", ", ".join(ratings))


def receiveName():
    print("Please enter the desired movie name\n")
    return input()
