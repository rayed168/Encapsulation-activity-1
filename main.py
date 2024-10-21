class Private:
    __PrivateVar=10
    def __privateMeth(self):
        print("This is a private function")
    def hello(self):
        print("The value of the private variable is : ",Private.__PrivateVar) 
obj1=Private()
obj1.hello()