weight = float(input("enter your weight(in kg)"))
height = float(input("enter your height(in meter)"))

BMI = weight/(height*height)
print(BMI)

if(BMI>0):
    if(BMI<=16):
        print("You are saverly underweight")
    elif(BMI<=18.5):
        print("You are underweight")
    elif(BMI<=25):
        print("You are healthy")
    elif(BMI<=30):
        print("You are overweight")
    else:
        print("You are saverely overweight")
else:
    print("Enter valid details")

