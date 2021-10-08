#Inner class Example 
class Person:
    def __init__(self,name,dd,mm,yyyy):
        self.name=name
        self.dob=self.Dob(dd,mm,yyyy)
    def display(self):
      print('hello:',self.name)
      self.dob.display()  
    class Dob:
        def __init__(self,dd,mm,yyyy):
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy

        def display(self):
            print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yyyy))

p=Person('subbu',18,8,1992)
p.display()