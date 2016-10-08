
"""
This program is meant to allow the user to reveal a secret message to 
a friend. By running it, the user gets to understand the message.

The secret message is contained in a list of photos that exist inside 
a folder with each photo containing a single letter. First, these photos 
are named in a way that their names start with numbers, what the program
does is It delets the numbers in the photos' names resulting in tghem revealing 
a certain message. 

the folder data/prank contains the original photos, after running the program
take a look back at it to read the secretive message.

"""

import os # importing the Operating System module


# The code is structured withins a function
def rename_files():

	file_path = "./data/prank"    # path to the original photoes

	# Get the original photos given the above given path
	# by calling listdir method (list directory)
	file_list = os.listdir(file_path)
	
	# Get the current working directory
	saved_path = os.getcwd()

	# for each file, renamae filenames
	os.chdir(file_path)

	for file_name in file_list:
		new_file_name = file_name.translate(None, "0123456789")  # removes numbers from file's name		
		print("Old name - {}".format(file_name))
		print("New name - {}".format(new_file_name))		
		print("")
		os.rename(file_name, new_file_name) # the file gets renamed without numbers

	os.chdir(saved_path)
	
# Call to the function	
rename_files()