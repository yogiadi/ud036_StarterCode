# Define a class Video with attributes such as title , poster image URL , trailer link and storyline
class Video:
    def __init__(self,title,poster_image_url,trailer_youtube_url,storyline):
        self.title=title
        self.poster_image_url=poster_image_url
        self.trailer_youtube_url=trailer_youtube_url
        self.storyline=storyline
# Define class Movie derived from Video . Further attributes can be added later.
class Movie(Video):
    pass
# Define class Tvshow derived from Video . Further attributes can be added later.
class Tvshow(Video):
    pass
