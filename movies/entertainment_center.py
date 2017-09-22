import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://bit.ly/2xn9trv",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "http://bit.ly/2xkaxij",
                    "https://www.youtube.com/watch?v=d1_JBMrrYw8")

#print toy_story.storyline
#print avatar.storyline

#avatar.show_trailer()
#toy_story.show_trailer()

movies = [toy_story, avatar]

fresh_tomatoes.open_movies_page(movies)