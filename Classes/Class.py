class Student:
    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo

    def displayDetails(self):
        a=90;
        print(a);
        #a cannot get accessed outside this function
        print(self.name,self.rollNo)

stu1 = Student("Ayush",1);
stu2 = Student("Gupta",2);
setattr(stu1,'Subject','JAVA');
print(stu1.Subject);
stu1.displayDetails();
stu2.displayDetails();

