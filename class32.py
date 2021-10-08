#method overriding
class P:
    def property(self):
        print('cash+gold+land')
    def marry(self):
        print('subbalakshmi')
class c(P):
    def marry(self):
        print('katrina')#overriding same method but child method cnsider
c=c()
c.property()
c.marry()


#in this eample how to call parent class marry method
class P:
    def property(self):
        print('cash+gold+land')
    def marry(self):
        print('subbalakshmi')
class c(P):
    def marry(self):
        super().marry()
        print('katrina')#overriding same method but child method cnsider
c=c()
c.property()
c.marry()