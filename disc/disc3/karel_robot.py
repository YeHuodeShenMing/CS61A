# write any code you want
from karel.stanfordkarel import *

def main():
   # your code here...
    while left_is_clear():
        move()
        move()
        turn_around()
        move()
        turn_around()
   
def turn_around():
   
   turn_left()
   turn_left()