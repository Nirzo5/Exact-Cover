class User:
    def __init__(self, Username, Email):           #our user class with the username and email as the attributes
        self.Username = Username
        self.Email = Email
        self.Token = 3

    def decresse_tokens(self): #decreases the tokens of the user by 1
        self.token -= 1

    def get_tokens(self):    #returns the tokens of the user
        return self.Token



