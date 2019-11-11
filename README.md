# Aida_Revived
This Aida Project been Revived. An open source AI project developed by SWAQ Community Members.

CURRENT STATE: Aida is currently a Facebook Messenger ECHO BOT

WORKING PROGRESS: Aida is currenlty undergoing a development of intergrating a Business AI in her.

GOAL: We want Aida to have a business intelligence that can enable her carry out market research.

TODO: On app.py enable mutltiple user connections, On google.py collect top 5 companies data from a single random url picked from the query search result links

google.py should return top 5 company list based on the keyword input.


HOW google.py works: google.py collects an input called keyword, a query of 'top 5 keword companies' is searched for in goolge
Which returns a list of 10 reuslt links for each website. We take the second on the list (this should be a random selection) and
send a get request to pull of the website data, we parse the data using html5lib to create a html tree structure and use bs4 to navigate
for the data we seek.

HOW app.py works: app.py connects with facbook webhook for getting trigger notification of messages that comes in from facebook messenger and send an echo response back to the user. To use this feature you will need knowledge on how to create a facebook developer account and messenger webhook on facebook.

HOW TO RUN Aida:
(Optional but recommended) 
1. pip install virtualenv 
2. virtualenv env
3. Pull from repo
4. pip install -r requirments.txt

To run app.py
5. Download NGROK for server
6. Create a config.py file and place the following code inside
VERIFY_TOKEN = 'your_verified_token'
PAGE_ACCESS_TOKEN = 'your_page_access_token' this enable you to connect your facebook webhook to it
7. run python app.py

To run google.py
5. python run google.py
You can get the details from your facebook developer account



