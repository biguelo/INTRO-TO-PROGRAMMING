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

import webbrowser
import fresh_tomatoes

def main():
    pass

if __name__ == '__main__':
    main()

import classes

toy_story = classes.Movie("Toy Story","Story of a boy and his toys that come to live",
                "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = classes.Movie('Avatar', 'A marine in an allien planet',
            'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
            'https://www.youtube.com/watch?v=5PSNL1qE6VY')

school_of_rock = classes.Movie('School of Rock', 'Using rock music to learn',
            'https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
            'https://www.youtube.com/watch?v=XCwy6lW5Ixc')

ratatouille = classes.Movie('Ratatouille','A rat that becomes a chef',
            'https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg',
            'https://www.youtube.com/watch?v=c3sBBRxDAqk')

movies = [toy_story,avatar,school_of_rock,ratatouille]

##fresh_tomatoes.open_movies_page(movies)


class Parent():
    def __init__(self,last_name,eye_color):
        print('Class constructor was called')
        self.last_name = last_name
        self.eye_color = eye_color


billy_cyrus = Parent('Cyrus','blue')
##print(billy_cyrus.last_name)

class Child(Parent):
    def __init__(self,last_name,eye_color,number_toys):
        Parent.__init__(self,last_name,eye_color)
        self.num_toys = number_toys

miley_cyrus = Child('Cyrus','brown',3)
print(miley_cyrus.last_name)
print(miley_cyrus.num_toys)