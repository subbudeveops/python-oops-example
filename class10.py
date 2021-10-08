class Outer:
    def __init__(self):
        print('outer class object creating')
    class Inner:
        def __init__(self):
            print('inner class object creating')
        class InnerInner:
            def __init__(self):
                print('InnerInner object creating')
            def m1(self):
                print('InnerInner class method')
Outer().Inner().InnerInner().m1()

