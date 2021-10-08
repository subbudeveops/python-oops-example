#mutlipel inheritance
class Mother:
    mothername=""
    def __init__(self):
        print(self.mothername)

class Father:
    fathername=""
    def __init__(self):
        print(self.fathername)

class Child(Mother,Father):
    def parents(self):
        print('Mother:',self.mothername)
        print('Father:',self.fathername)
c=Child()
c.mothername='Rajeswaramma'
c.fathername='Subbareddy'
c.parents()