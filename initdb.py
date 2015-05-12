#!/usr/bin/env python3

import getpass, sys

# Constants
CONLANG_NAME = "gvwtokori"
CONLANG_DB = CONLANG_NAME + "DB"

# Global variables
db_username = ''
db_password = ''
db_address = ''
db_port = -1

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

print("Welp")
