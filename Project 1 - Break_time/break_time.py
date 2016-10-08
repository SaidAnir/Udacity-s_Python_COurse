
"""
This program lets the user take a break each and every 
once in a while. What it does is that every time a certain amount
of time passes, It automatically opens a youtube video 

"""

import time         # importing he time library as we're making use of time-realted functions
import webbrowser   # importing the webbromser library which contains functions for manipulating the web.

video_link = "https://www.youtube.com/watch?v=L___6FKM79U" # link to a youtube video to play during the break

wait_time = 3  # time that the user spends doing his/her activity (in seconds)
total_breaks = 3  # number of breaks throughout the day
counter = 0   # initializing a counter that counts the breaks

print("This program started on {}".format(time.ctime())) # displaying the current time

# Looping through as long as we haven't passed the total number of breaks
while break_count < total_breaks: 
	time.sleep(wait_time)        # making use of time's library sleep function 
	webbrowser.open(video_link)        # calling the method open of the webbrowser library to open the link to the video
	break_count += 1             # incrementing the counter