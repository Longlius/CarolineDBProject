import getpass, mysql.connector

class DBLogin:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.hostaddr = ''
        self.portnum = -1
        
    # Getter methods
    def getusername(self):
        return self.username        
    def getpassword(self):
        return self.password
    def gethostaddr(self):
        return self.hostaddr
    def getportnum(self):
        return self.portnum
        
    # Method - promptForUserName
    # Description - asks the user to input their username to authenticate
    def promptForUserName(self):
        self.username = input('Enter your username: ')
    
    # Method - promptForPassword
    # Description - asks the user to input their password to authenticate
    def promptForPassword(self):
        self.password = getpass.getpass('Enter your password: ')
        
    # Method - promptForAddr
    # Description - asks the user to input the db's address
    def promptForAddr(self):
        self.hostaddr = input('Enter the address of the database: ')

    # Method - promptForPort
    # Description - asks the user to input the db's port number
    def promptForPort(self):
        while True:
            p = int(input('Enter the port number to connect to: '))
            if (p >= 0 and p <= 65535):
                self.portnum = p
                return
            else:
                print('Invalid entry. Port number must be between 0 and 65,535.')
                
    # Method - loginPrompt
    # Description - prompts the user enter information to login
    def loginPrompt(self):
        self.promptForAddr()
        self.promptForPort()
        self.promptForUserName()
        self.promptForPassword()
    
    # Method - connectToDBMS
    # Description - connects to the DBMS and returns an object representing the connection 
    def connectToDBMS(self):
        try:
            connection = mysql.connector.connect(user=self.username, password=self.password, host=self.hostaddr, port=self.portnum)
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Incorrect username or password")
            else:
                print(err)
        else:
            return connection
