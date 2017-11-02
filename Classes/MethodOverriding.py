class First:
    def __init__(self):
        super(First, self).__init__()
        print("first")
    def functionBase1(self):
        print("Base1 function")





class Third(First):
    def __init__(self):
        super(Third, self).__init__()
        print("third")

    def functionBase1(self):
        First.functionBase1(self);
        print("Base2 function")


t=Third();
t.functionBase1();