import gspread
#gspread, which is a library of code  that we will use to access and update data in our spreadsheet. Essentially this import, imports the entire gspread library,  
from google.oauth2.service_account import Credentials
""" google-auth, which will use our creds.json file  
to set up the authentication needed  to access our Google Cloud project. 
 imports the Credentials class,  
which is part of the service_account  function from the Google auth library.   """

#Now we have our imports, the next thing we need  to do is set our scope. The scope lists the APIs that the  program should access in order to run.

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

""" Now our scope and creds variables  are ready, we’ll create a new variable, 
called SCOPED_CREDS. Using the  with_scopes method of the creds object,  
and pass it our scope variable. """

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

""" Next, we create our GSPREAD_CLIENT.  
Using the gspread authorize method,  and pass it our SCOPED_CREDS. """

GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

""" And finally, we can access our  love_sandwiches sheet, 
using the open() method on our client object  and passing it the name we gave our spreadsheet. """

SHEET = GSPREAD_CLIENT.open('love_sandwiches')

sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)