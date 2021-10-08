class Human:
    def __init__(self):
        self.name='sunny'
        self.head=self.Head()
        self.brain=self.head.Brain()
    def display(self):
        print('hello:',self.name)
        self.head.talk()
        self.brain.think()
    class Head:
        def talk(self):
            print('talking')

        class Brain:
            def think(self):
                print('thinking')
h=Human()
h.display()
            