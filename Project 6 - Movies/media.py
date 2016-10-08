"""
THis programs defines the Movie class and defines the 
show_trailer method of the Movie class.

"""


import webbrowser

class Movie(object):
	""" A class that stores movie related information 
	along with ability to show a movie trailer. """

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)