def calculate_bmi():
    height=float(input('Enter height:'))
    weight=float(input('Enter weight:'))
    BMI= weight/height*height
    print("BMI is "+str(BMI))
    if(BMI<18.5):
        print("Under Weight")
    elif (18.5<=BMI<=25.0):
        print("BMI is normal weight")
    elif(BMI>25.0):
        print("Over weight")
    else:
        print('Invalid')

#calculate_bmi(weight=57,height=1.73)



if __name__=='__main__':#put space between if and __ and must be '__main__'
    calculate_bmi()
