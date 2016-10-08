"""
This program checks text documents and alerts the 
user if it contains cursed words.

TO write this program, we wanted to make use of Google's "what do you love" 
website which allows you to check whether or not a query
contains cursed words by rendering a JSON but Google shut it down 
and the service is no longer active.

Alternatively, I utilized another Rest API provided by a website called:
	https://market.mashape.com/neutrinoapi/bad-word-filter
You can a key to start using the API just by startig a new application.

The main function that does the verifying exists in two samples, one where I utlized the
above API and the other was developed using Google's WDYL API.

We also made use of UNIREST, a lightweight HTTP cleint library

$ pip install unirest 

"""



import urllib
import unirest

def read_text():
	quotes = open("text_sample.txt")
	content_of_file = quotes.read()
	quotes.close()
	check_profanity(content_of_file)

# checks availability of cursed words in a document paased as an argument
def check_profanity(textToCheck):
	response = unirest.post("https://neutrinoapi-bad-word-filter.p.mashape.com/bad-word-filter",
    headers={
  	# replace with your key
    "X-Mashape-Key": "VpUT3dWsXOmshOTV8XEaT8ozYWJvp1TOL9Rjsn31Lydmyn9juf", 
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  	},
  	params={
    "censor-character": "*", # This field is optional
    "content": textToCheck
  	}
	)
	# print response.body
	if response.body['is-bad'] == "True":
		print "Text contains cursed words!!"
	elif response.body['is-bad'] == "False":
		print "This document has no curse words!"
	else: print "The document could not be parsed!, Check out your API key availability"

# The function with Google's WDYL which's no longer working
def check_profanity_alternate(textToCheck):
	# Google's "What Do You Love" website
	base_url = "http://www.wdyl.com/profanity"

	# Establishing the query
	query = "?q=" + textToCheck
	
	connection = urllib.urlopen(base_url + query)
	output = connection.read()
	connection.close()
	if "true" in output:
		print("Profanity Alert!!")
	elif "false" in output:
		print("This document has no curse words!")
	else:
		print("Could not scan the document properly.")

read_text()