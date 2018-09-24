from collections import namedtuple

Movie = namedtuple("Movie", "id name genre")
User = namedtuple("User", "id gender age ocupation")
Rating = namedtuple("Rating", "user movie stars")

def load_db(file):
	lines = open(file).readlines()
	return [line.rstrip().split("::") for line in lines]

def get_data():
	movies = {int(movie[0]): Movie(int(movie[0]), movie[1], movie[2].split('|')) for movie in load_db("ml-1m/movies.dat")}
	users = {int (user[0]): User(int(user[0]), user[1], int(user[2]), int(user[3])) for user in load_db("ml-1m/users.dat")}
	ratings = [Rating(users[int(rate[0])], movies[int(rate[1])], int(rate[2])) for rate in load_db("ml-1m/ratings.dat")]

	return movies, ratings

if __name__ == "__main__":
	# ratings = load_db("ml-1m/ratings.dat")

	movies = {int(movie[0]): Movie(int(movie[0]), movie[1], movie[2].split('|')) for movie in load_db("ml-1m/movies.dat")}
	users = {int (user[0]): User(int(user[0]), user[1], int(user[2]), int(user[3])) for user in load_db("ml-1m/users.dat")}
	ratings = [Rating(users[int(rate[0])], movies[int(rate[1])], int(rate[2])) for rate in load_db("ml-1m/ratings.dat")]
	
	print(ratings)