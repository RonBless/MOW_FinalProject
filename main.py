from DAL.Movie.MovieDal import MovieDal


def onStartup():
    print("Welcome to MOW!\n")
    print("We are gonna help you estimate your desired movie opening weekend revenue according to Twitter\n")
    print("Please enter the Movie Name\n")
    movie_name = input()
    print("We are on it!\n Loading...\n")
    dal = MovieDal()
    data = dal.getMovie(name)


if __name__ == '__main__':
    onStartup()

    name = "Spider-man"
    dal = MovieDal()
    data = dal.getMovie(name)
    print(data)

