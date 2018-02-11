import webbrowser

class Movie():
    """Movie class for a popup that is displayed at site top.

    Attributes:
        title: A string indicating a movie title.
        poster_image_url: A string indicating a movie thumbnail image url.
        trailer_youtube_url: A string indicating a movie url.
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Set movie info."""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens youtube movie on a browser."""
        webbrowser.open(self.trailer_youtube_url)
