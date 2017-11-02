#file = open('D:\\Users\\ayushgup\\Downloads\\fileHandling.txt', "w+");
file= open("D:/Users/ayushgup/Downloads/createdByPython.txt","w+")
#print(file.read());
file.write("Line 5 \n");
file.write("Line 6 \n");
file.write("Line 7 \n");
file.write("Line 8 \n");
file.seek(0);
print(file.read())
file.close();

#file = open('D:\\Users\\ayushgup\\Downloads\\fileHandling.txt', "r");
#print(file.read());
#