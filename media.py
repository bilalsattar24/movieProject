"""
Author - Bilal Sattar 10/24/16
Udacity Full Stack

This class represents a movie object.

Instance variables:

title - title of movie
storyline - a short description of the movie
poster_image_url - location of image used for boxart of the movie
trailer_youtube_url - URL of youtube movie trailer

Methods:
__init__ - Constructs the movie object with arguments provided

"""

#construct
class Movie():
    def __init__(self, movieTitle, movieStory, movieImage, movieTrailer):
        self.title = movieTitle #set title
        self.storyline = movieStory # set storyline
        self.poster_image_url = movieImage #set image url for box art
        self.trailer_youtube_url = movieTrailer #set youtube trailer url