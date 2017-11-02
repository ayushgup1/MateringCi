class First:
    def __init__(self):
        super(First, self).__init__()
        print("first")
    def functionBase1(self):
        print("Base1 function")


class Second:
    def __init__(self):
        super(Second, self).__init__()
        print("second")
    def functionBase1(self):
        print("Base2 function")


class Third(Second, First):
    def __init__(self):
        super(Third, self).__init__()
        print("third")


t=Third();
t.functionBase1();