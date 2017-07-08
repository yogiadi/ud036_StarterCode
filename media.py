# Define class Video with attributes
class Video:
    def __init__(self, title, poster_img_url, trailer_youtube_url, storyline):
        self.title = title
        self.poster_image_url = poster_img_url
        self.trailer_youtube_url = trailer_youtube_url
        self.storyline = storyline
# Define class Movie derived from Video.


class Movie(Video):
    pass
# Define class Tvshow derived from Video.


class Tvshow(Video):
    def setChannel(self, channel):
        self.channel = channel

    def setSeason(self, season):
        self.season = season
