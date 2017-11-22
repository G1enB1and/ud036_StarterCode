import webbrowser


class Movie():
    """This class provides a way to store movie related information.

    Attributes:
        movie_title: a string representing the movie title.
        movie_storyline: a astring representing the movies storyline.
        poster_image: a string representing a url to the movies poster image.
        youtube_trailer: a string representing a url to the movies youtube
        trailer.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Inits Movie class with title, storyline, poster_image_url, and
        trailer_youtube_url."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens a webbrowser to the URL of the youtube movie trailer for the
        movie that called it."""
        webbrowser.open(self.trailer_youtube_url)
