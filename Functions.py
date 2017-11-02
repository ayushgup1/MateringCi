# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

myGlobal = 5

def func1():
    global myGlobal
    myGlobal= 42

def func2():
    print(myGlobal)


func2()
func1()
print(myGlobal)


#Add using function
def add(a,b):
   c=a+b;
   return c

ans = add(3,4)
print("Result :",ans)


#List as parameter
def funlist(list):
    list[1]="Java1";
    return


list=["Oracle","Java"]

print("Before",list)
funlist(list)
print("After",list)


# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme( str = "My string")
printme("test")