import webbrowser

class Movie():
	"""This class provides a way to store movie related information"""

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, movie_title, movie_storyline, movie_duration, movie_release_date, movie_director, movie_rating, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.duration = movie_duration
		self.release = movie_release_date
		self.director = movie_director
		self.rating = movie_rating
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)		