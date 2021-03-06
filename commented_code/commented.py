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
    """ we'd like our program to continue to request the data over and over again until we get a valid response.
    We can achieve this with a while loop, which will only  end the loop when the correct data has been given. """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")
        
        sales_data = data_str.split(",")
        #This will remove the commas from the string.
        if validate_data(sales_data):
        #call the function
            print(Data is valid)
            break

    return sales_data

        

def validate_data(values):
    """    
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    print(values)
    try:
        [int(value) for value in values]
        #for each individual value in the values  list, convert that value into an integer.
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    """     Now we need to access our sales  worksheet from our Google Sheet  
    so that we can add our data to it. So  we’ll declare a variable sales_worksheet,  
    and then we use the sheet variable we defined at  the top of our page using the gspread library.
    And we’ll use the gspread worksheet()  method to access our sales worksheet.  
    """
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")


def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.
    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
"""     The simplest way is to use a slice.
In this case stock with square brackets giving it the list index of -1. This will slice the final item from the list and
return it to the new stock variable.  """



def main():
    """
    Run all program functions
    """
data = get_sales_data()
sales_data = [int(num) for num in data]
#assign the result from the list  comprehension to a new variable named sales_data.
update_sales_worksheet(sales_data)
#call the function and pss it out sales_data list 


print("Welcome to Love Sandwiches Data Automation")
main()