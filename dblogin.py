# Function - getUserName
# Description - asks the user to input their username to authenticate
def getUserName():
    global db_username
    db_username = input('Enter your username: ')
    
# Function - getPassword
# Description - asks the user to input their password to authenticate
def getPassword():
    global db_password
    db_password = getpass.getpass('Enter your password: ')
