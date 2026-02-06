#BMI Caluculator
name = input("Enter Name : ")
height = int(input("Enter height in inches : "))
weight = int(input("Enter weight in pounds : "))
bmi= (weight / (height*height)) * 703
if(bmi<18.5):
    print("Hi",name," your BMI Is :", bmi, "you are under weight")
elif(bmi>18.5 and bmi<24.9):
    print("Hi",name," your BMI Is :", bmi, "you are normal weight")
elif(bmi>25 and bmi<29.9):
    print("Hi",name," your BMI Is :", bmi, "you are over weight")
else:
    print("Hi",name," your BMI Is :", bmi, "you need to visit doctor")
