import fresh_tomatoes
import media

"""The format to create a movie instance is "instance name" = media.Movie("Movie
Name", "Movie Storyline", "URL to Poster Image", "URL to YouTube Movie Trailer")
"""

transcendence = media.Movie("Transcendence",
                        "a man uploads his consciousness into AI and transcendes his physical form before he dies.",
                        "http://t3.gstatic.com/images?q=tbn:ANd9GcTImP4LsMOSM0eDX0bPk2OwqGEFJ8b5PGKlpLg4Br6R_J7FELL1",
                        "https://www.youtube.com/watch?v=QheoYw1BKJ4")

live_free_or_die_hard = media.Movie("Live Free or Die Hard",
                     "An action pack movie with Bruce Willis about hackers vs hackers on a national scale.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/4/46/Live_Free_or_Die_Hard.jpg/220px-Live_Free_or_Die_Hard.jpg",
                     "https://www.youtube.com/watch?v=xqjICXgcsZM")

antitrust = media.Movie("Antitrust",
                        "Computer genius discovers corruption within huge software company NURV.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2a/Antitrust_poster.jpg",
                        "https://www.youtube.com/watch?v=I7hhqX1PANU")

pirates_of_silicon_valley = media.Movie("Pirates of Silicon Valley",
                                        "The story of Bill Gates and Steve Jobs",
                                        "http://www.gstatic.com/tv/thumb/dvdboxart/22971/p22971_d_v8_aa.jpg",
                                        "https://www.youtube.com/watch?v=lEyrivrjAuU")
hackers = media.Movie("Hackers",
                      "A story about hackers.",
                      "http://www.gstatic.com/tv/thumb/movieposters/17164/p17164_p_v8_ab.jpg",
                      "https://www.youtube.com/watch?v=Rn2cf_wJ4f4")

the_social_network = media.Movie("The Social Network",
                                 "The story of facebook's creator Mark Zuckerberg.", 
                                 "https://images-na.ssl-images-amazon.com/images/I/41AVOQln14L.jpg",
                                 "https://www.youtube.com/watch?v=lB95KLmpLR4")

#Create an array called movies that contains the names of each instance of the
#Movie class.

movies = [transcendence, live_free_or_die_hard, antitrust,
          pirates_of_silicon_valley, hackers, the_social_network]

#send the above movies array as an argument to the open_movies_page function
#within fresh_tomatoes.py

fresh_tomatoes.open_movies_page(movies)


