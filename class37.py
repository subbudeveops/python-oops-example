#difference beetween str()  and repr()
#difference beetween __str__ anf __repr__
class Sinteger:
    def __init__(self,integer):
        self.integer=integer
    #def __str__(self):
        #return f"Customized Integer {self.integer}"#f meand format type or both same format
        #return 'customized Integer {}'.format(self.integer)
    def __repr__(self):
         return 'customized Integer {}'.format(self.integer)
            
s=Sinteger(10)
print(str(s))#str()
print(repr(s))#repr()

