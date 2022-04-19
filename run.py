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

def get_sales_data():
    """
    Get sales figures input from the user.
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    
    sales_data = data_str.split(",")
    #This will remove the commas from the string.
    validate_data(sales_data)
    #call the function


def validate_data(values):
    """create a new function  to handle our validation, we’ll call it  
    validate_data(). And we will pass it a parameter  of “values” which will be our sales data list. """
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


get_sales_data()


