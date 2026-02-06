#Student Score
name = input("Enter Name :")
height = int(input("Enter height in inches :"))
weight = int(input("Enter weight in pounds :"))
marks = int(input("enter your marks percentage : "))
if(marks >= 90):
    print(name," you got A Grade")
elif(marks >= 80):
    print(name," you got B Grade")
elif(marks >= 70):
    print(name," you got C Grade")
elif(marks >= 60):
    print(name," you got D Grade")
else:
    print(name," you are failed")
