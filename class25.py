#Hudrid Inheritance
class School:
    def f1(self):
        print('This function is in School')
class Student1(School):
    def f2(self):
        print('This function is in Student1')
class Student2(School):
    def f3(self):
        print('this is function is in student2')
class Student3(Student1,School):
    def f4(self):
        print('this function is in Student3')
object=Student3()
object.f1()
object.f2()
