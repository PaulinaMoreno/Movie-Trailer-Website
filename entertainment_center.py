# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 17:29:17 2017

@author: Paulina Moreno
"""
import fresh_tomatoes
import media

# MOVIES information
toy_story_movie = media.Movie("Toy Story", 90,
                              '''
                              Andy loves to be in his room playing with
                              his toys, especially his doll named 'Woody'.
                              But, what do the toys do when Andy is not with
                              them, they come to life.
                              ''',
                              "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",  # NOQA
                              "https://www.youtube.com/watch?v=KYz2wyBy3kc")
lord_ofthe_rings_movie = media.Movie(
                             '''
                             The Lord of the Rings,The Fellowship of the Ring
                             ''',
                             120,
                             '''
                             The story begins in the Shire, where the hobbit
                             Frodo Baggins inherits the Ring from Bilbo
                             Baggins, his cousin and guardian. Neither hobbit
                             is aware of the Ring's nature, but Gandalf
                             , a wizard and an old friend of Bilbo, suspects it
                             to be Sauron's Ring.
                             ''',
                             "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=V75dMMIW2B4")
avengers_movie = media.Movie(
                            "The Avengers", 90,
                            '''
                            Earth's mightiest heroes must come together and
                            learn to fight as a team if they are going to
                            stop the mischievous Loki and his alien army
                            from enslaving humanity.
                            ''',
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=cFv2xPvQfJ4")
harry_potter_movie = media.Movie(
                            "Harry Potter and the Sorcerer's Stone", 90,
                            '''
                            Rescued from the outrageous neglect of his aunt
                            and uncle, a young boy with a great destiny proves
                            his worth while attending Hogwarts School
                            of Witchcraft and Wizardry.
                            ''',
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=VyHV0BRtdxo")
pacific_rim_movie = media.Movie(
                            "Pacific Rim", 90,
                            '''
                            In 2013, huge alien sea monsters called Kaiju
                            emerge from an interdimensional portal called
                            the Breach at the bottom of the Pacific Ocean.
                            Over the course of three years, the Kaiju wreak
                            havoc upon coastal cities along the Ring of Fire,
                            such as San Francisco, Cabo San Lucas,
                            Sydney, Manila, and Hong Kong.
                            ''',
                            "https://upload.wikimedia.org/wikipedia/en/f/f3/Pacific_Rim_FilmPoster.jpeg",  # NOQA
                            "https://www.youtube.com/watch?v=5guMumPFBag")
blade_runner_movie = media.Movie(
                            "Blade Runner", 110,
                            '''
                            This a 1982 American neo-noir science fiction film
                            directed by Ridley Scott, written by Hampton
                            Fancher and David Peoples, and starring Harrison
                            Ford, Rutger Hauer, Sean Young, and Edward
                             James Olmos.
                            ''',
                            "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=eogpIG53Cis")
# TV SHOWS information
breaking_bad_1_5 = media.Tv_show(
    "Breaking bad", 60, 1, 5, "AMC",
    "http://cdn.collider.com/wp-content/uploads/breaking_bad_season_3_promo_art_01.jpg",  # NOQA
    "https://www.youtube.com/watch?v=HhesaQXLuRY")
breaking_bad_2_5 = media.Tv_show(
    "Breaking bad", 60, 2, 5, "AMC",
    "http://the-back-row.com/wp-content/uploads/2013/08/79438-breaking-bad-breaking-bad-poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=I-8914DuyhY")
walking_dead_1_1 = media.Tv_show(
    "Walking dead-'Days Gone Bye'", 60, 1, 1, "AMC",
    "https://upload.wikimedia.org/wikipedia/en/0/0e/TheWalkingDeadPoster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=35FKJpexDho")
walking_dead_2_1 = media.Tv_show(
    "Walking dead-'What Lies Ahead'", 60, 2, 1, " AMC",
    "https://s-media-cache-ak0.pinimg.com/originals/b0/61/d2/b061d28364202bc96dfb8f267876f534.jpg",  # NOQA
    "https://www.youtube.com/watch?v=1OZ0mu8Ey6A")

# List of movies
list_movies = [lord_ofthe_rings_movie, toy_story_movie,
               avengers_movie, harry_potter_movie, pacific_rim_movie,
               blade_runner_movie]
# List of Tv shows
list_tv_show = [breaking_bad_1_5, breaking_bad_2_5,
                walking_dead_1_1, walking_dead_2_1]

fresh_tomatoes.open_videos_page(list_movies, list_tv_show)
