# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 17:20:57 2017

@author: Paulina Moreno
"""
import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        .tv_show_bg { 
            background-color: #1abc9c;
            color: #607D8B;
         }
        .movie_bg { 
          margin-top: 2cm;
          background-color: #474e5d; 
          color: #607D8B;
        }
        .btnDescription { 
          -webkit-border-radius: 28;
          -moz-border-radius: 28;
          border-radius: 28px;
          font-family: Georgia;
          color: #0f0e0e;
          font-size: 15px;
          background: #f0ed57;
          padding: 10px 20px 10px 20px;
          text-decoration: none;
        }
        
        .btn:hover {
          background: #fc8c3c;
          text-decoration: none;
        }

        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
     
        .tv_show-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
            
        // Start playing the video whenever the trailer modal is opened , for movie
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Start playing the video whenever the trailer modal is opened , for tv_show
        $(document).on('click', '.tv_show-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });

        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
          // Animate in the tv_shows when the page loads
          $('.tv_show-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
          $('.btnDescription').bind("click", function () {
                var movie_title =$(this).parent().parent().find('.title').text()
                var movie_storyline = $(this).parent().parent().find('.storyline').text()
                var movie_img=$(this).parent().parent().find('.movieimg').attr('src')
                console.log(movie_img)
                var url = "video_information.html?title=" + encodeURIComponent(movie_title)+ "&storyline=" + encodeURIComponent(movie_storyline)+ "&srcimage=" + encodeURIComponent(movie_img);
            
                window.location.href = url;
            });
 
        });
   
    </script>

</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Smash Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container tv_show_bg">
      <h2> TV Shows <h2>
      {tv_show_tiles}

     </div>
    <div class="container movie_bg">
      <h2> Movies <h2>
      {movie_tiles}
    </div>
   </body>
</html>
'''
# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <div>
        <img class="movieimg" src="{poster_image_url}" width="250" height="360">
        <h4 class="title">{movie_title}</h4>
        <p class="storyline" hidden>{movie_storyline}</p>
    </div>
    <div>
        <input type="button" class="btnDescription" value="see more ..." />
        </br>
   </div>
 </div>
 
'''
# A single tv_show entry html template
tv_show_tile_content = '''
<div class="col-md-6 col-lg-4 tv_show-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="250" height="360">
    <h4>{tv_show_title}</h4>

</div>
'''
def create_tv_show_tiles_content(tv_shows):
    # The HTML content for this section of the page
    content = ''
    for tv_show in tv_shows:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', tv_show.youtube_trailer_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', tv_show.youtube_trailer_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
        print("tv "+trailer_youtube_id)
        # Append the tile for the tv_show with its content filled in
        content += tv_show_tile_content.format(
            tv_show_title=tv_show.title,
            poster_image_url=tv_show.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content
def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.youtube_trailer_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.youtube_trailer_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
        print("movie "+trailer_youtube_id)
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_videos_page(movies ,tv_shows):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie and tv_show tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles = create_movie_tiles_content(movies), tv_show_tiles = create_tv_show_tiles_content(tv_shows))
    
    # Output the file
    output_file.write(main_page_head + rendered_content )
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
