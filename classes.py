#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Owner
#
# Created:     07/01/2016
# Copyright:   (c) Owner 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import webbrowser

class Movie():
    def __init__(self, title, story, image, trailer):
        self.title = title
        self.storyline = story
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_url)

