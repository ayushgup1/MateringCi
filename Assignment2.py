#List CURD
myList = list([2,3]);
print(myList);

myList = list();
print(myList);

myList=['JAVA',2,80.0];
print(myList);

myList.append("Python");
print(myList);

myList.insert(0,'C');
print(myList);

myList.extend([20,90.0,'Script']);
print(myList);

list1 = [44,88];
myList.extend(list1);
print(myList);

myList.pop(6);
print(myList);

myList.remove('C');
print(myList);

#String slice

String1 = "Capgemini";
print(String1[2:5]);
print(String1[:5]);
print(String1[2]);
print(String1[-2]);

print(String1.replace(String1,"India"));
print(String1);