class StringUpper():
    
    def retrieveString(self):
        self.userInput = input("Enter a String: ")
        
        return self.userInput
    
    def upperLetter(self):
        return str(self.userInput.upper())
    

userString = StringUpper()
print(userString.retrieveString())
print(f"Uppercase: {userString.upperLetter()}")