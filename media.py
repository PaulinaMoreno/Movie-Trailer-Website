# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 17:10:27 2017

@author: Paulina Moreno
"""
import webbrowser


class Video():

    """ This Class provides a way to store
     movies and tv shows related information"""
    def __init__(self, title, duration, poster_image, trailer_url):
        print("Video constructor called")
        self.title = title
        self.duration = duration
        self.poster_image_url = poster_image
        self.youtube_trailer_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)


class Movie(Video):

    '''
    This Class provides a way to store
    movie related information
    '''
    VALID_RAITING = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_duration, movie_storyline,
                 movie_poster_image, movie_trailer_url):
        print("Movie constructor called")
        Video.__init__(self, movie_title, movie_duration,
                       movie_poster_image, movie_trailer_url)
        self.storyline = movie_storyline


class Tv_show(Video):

    '''
    This Class provides a way to store tv show
    related information
    '''
    def __init__(self, tv_title, tv_duration, tv_season, tv_episode,
                 tv_station, tv_poster_image, tv_trailer_url):
        print("Tv Show constructor called")
        Video.__init__(self, tv_title, tv_duration,
                       tv_poster_image, tv_trailer_url)
        self.tv_season = tv_season
        self.tv_episode = tv_episode
        self.tv_station = tv_station
