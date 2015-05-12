#!/usr/bin/env python3

import dblogin, sys

# Constants
CONLANG_NAME = "gvwtokori"
CONLANG_DB = CONLANG_NAME + "DB"

x = dblogin.DBLogin()
x.loginPrompt()
print("------ DEBUG ------")
x.debugPrint()
