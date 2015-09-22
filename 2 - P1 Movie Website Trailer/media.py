import webbrowser

class Movie():
	"""This class provides a way to store movie related information"""

	# available ratings
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	# this is the constructer, it accepts details of a movie as arguments
	def __init__(self, movie_title, movie_storyline, movie_duration, movie_release_date, movie_director, movie_rating, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.duration = movie_duration
		self.release = movie_release_date
		self.director = movie_director
		self.rating = movie_rating
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	# this method opens the trailer link in a browser
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

	# this method checks the given rating and return an appropriate rating
	def show_rating(self):
		if self.rating in ["G", "PG", "PG-13", "R"]:
			return self.rating
		else:
			return "NA"