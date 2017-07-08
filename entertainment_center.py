# Import classes Movie , Tvshow and functions such as open_videos_page

from media import Movie, Tvshow
from fresh_tomatoes import open_videos_page
# Create Instances of Movie and Tvshow class
video1 = Movie('Dark Knight',
               'http://paulmmartinblog.files.wordpress.com/2011/07/the_dark_knight_poster.jpg',  # noqa
               'https://www.youtube.com/watch?v=yQ5U8suTUw0',  # noqa
               'When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham,the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.')  # noqa
video2 = Tvshow('The Flash',
                'http://www.impawards.com/tv/posters/flash_xlg.jpg',  # noqa
                'https://www.youtube.com/watch?v=Yj0l7iGKh8g',  # noqa
                'After being struck by lightning, Barry Allen wakes up from his coma to discover he''s been given the power of super speed, becoming the Flash, fighting crime in Central City.')  # noqa
video3 = Tvshow('Elementary',
                'https://s-media-cache-ak0.pinimg.com/736x/ce/6a/3b/ce6a3b18bd9dc4c5ecde9fefe7bddd06--elementary-tv-movie-posters.jpg',  # noqa
                'https://www.youtube.com/watch?v=ff-XiZzJLxw',  # noqa
                'A modern take on the cases of Sherlock Holmes, with the detective now living in New York City. ')  # noqa
video4 = Movie('Wonder woman',
               'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeYgGK80L-LTaMQC404ryBlUdm1thV78oDpUF89MZ1ZLs75eaa0w',  # noqa
               'https://www.youtube.com/watch?v=VSB4wGIdDwo',  # noqa
               'Before she was Wonder Woman, she was Diana, princess of the Amazons, trained warrior. When a pilot crashes and tells of conflict in the outside world, she leaves home to fight a war, discovering her full powers and true destiny. ')  # noqa
video5 = Movie('Doctor Strange',
               'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3fEXk4BUBt2-l4nrxgRG8sE3y3rOEMwPSawb8CZSsdPN78CHylw',  # noqa
               'https://www.youtube.com/watch?v=Lt-U_t2pUHI',  # noqa
               'While on a journey of physical and spiritual healing, a brilliant neurosurgeon is drawn into the world of the mystic arts. ')  # noqa
video6 = Movie('Avengers age of ultron',
              'http://www.designbolts.com/wp-content/uploads/2015/03/Avengers-Age-of-Ultron-Official-Wallpaper-HD2.jpg',  # noqa
              'https://www.youtube.com/watch?v=tmeOjFno6Do',  # noqa
               'When Tony Stark and Bruce Banner try to jump-start a dormant peacekeeping program called Ultron, things go horribly wrong and it''s up to Earth''s mightiest heroes to stop the villainous Ultron from enacting his terrible plan.')  # noqa
video7 = Tvshow('Arrow',
                'https://s-media-cache-ak0.pinimg.com/originals/eb/a4/df/eba4df809a662b2f43a8b065903f5ddc.jpg',  # noqa
                'https://www.youtube.com/watch?v=POfJZGqdjDM',  # noqa
                'Spoiled billionaire playboy Oliver Queen is missing and presumed dead when his yacht is lost at sea. He returns five years later a changed man, determined to clean up the city as a hooded vigilante armed with a bow. ')  # noqa
video8 = Tvshow('Game of thrones',
                'http://images4.fanpop.com/image/photos/20000000/Game-of-Thrones-Poster-game-of-thrones-20026735-338-500.jpg',  # noqa
                'https://www.youtube.com/watch?v=1Mlhnt0jMlg',  # noqa
                'Nine noble families fight for control over the mythical lands of Westeros, while a forgotten race returns after being dormant for thousands of years. ')  # noqa
# Create list of all the videos including both Movie and Tvshow objects
videos = [video1, video2, video3, video4, video5, video6, video7, video8]
# Call function from fresh_tomatoes.py and pass the list
open_videos_page(videos)
