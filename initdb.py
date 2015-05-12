#!/usr/bin/env python3

import dblogin, getpass, sys

# Constants
CONLANG_NAME = "gvwtokori"
CONLANG_DB = CONLANG_NAME + "DB"

# Global variables
db_username = ''
db_password = ''
db_address = ''
db_port = -1

print(dblogin.__name__)
