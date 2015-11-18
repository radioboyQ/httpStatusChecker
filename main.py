#Objective: Try and connect to the defined URLs and determine if they are up or not.  If not, email everyone in the list provided.
#Logic for the script:
#Define list of URLs to check
#Open a connection to each one, keep a dictionary of the response code
#if response code != 200:
#---Future---#
##if prior error status != current error status and current error status != 200:
###Log to a file
###Email the addresses in the defined list
###Write to a config file what the last status was
##elif prior error status == current error status and current error status != 200:
###Do nothing but log the event

def main():
	urlCheckList = list()
	emailList = list()

	

if __name__ == '__main__':
	main():