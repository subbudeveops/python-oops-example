#classmethod by using how many object creating
class Test:
    count=0
    def __init__(Self):
        Test.count=Test.count+1
    @classmethod
    def noofobject(cls):
        print('no of objected created:',Test.count)

t1=Test()
t2=Test()
t3=Test()
Test.noofobject()
