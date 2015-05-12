import getpass

class DBLogin:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.hostaddr = ''
        self.portnum = -1
        
    # Function - promptForUserName
    # Description - asks the user to input their username to authenticate
    def promptForUserName(self):
        self.username = input('Enter your username: ')
    
    # Function - promptForPassword
    # Description - asks the user to input their password to authenticate
    def promptForPassword(self):
        self.password = getpass.getpass('Enter your password: ')
        
    # Function - promptForAddr
    # Description - asks the user to input the db's address
    def promptForAddr(self):
        self.hostaddr = input('Enter the address of the database: ')

    # Function - promptForPort
    # Description - asks the user to input the db's port number
    def promptForPort(self):
        while True:
            p = int(input('Enter the port number to connect to: '))
            if (p >= 0 and p <= 65535):
                self.portnum = p
                return
            else:
                print('Invalid entry. Port number must be between 0 and 65,535.')
                
    # Function - loginPrompt
    # Description - prompts the user enter information to login
    def loginPrompt(self):
        self.promptForAddr()
        self.promptForPort()
        self.promptForUserName()
        self.promptForPassword()
                
    def debugPrint(self):
        print("Username: " + self.username)
        print("Password: " + self.password)
        print("DB address: " + self.hostaddr)
        print("DB port: " + str(self.portnum))
                
