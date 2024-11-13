Enter your name :yemi
Enter your weight in pounds:180
Enter your height in inches:74
23.10810810810811
name = input ("Enter your name :")
weight = int(input ('Enter your weight in pounds:'))
height = int(input ('Enter your height in inches:'))
bmi= (weight * 703)/ (height * height)
print (bmi)

name = input ("Enter your name :")
weight = int(input ('Enter your weight in pounds:'))
height = int(input ('Enter your height in inches:'))
bmi= (weight * 703)/ (height * height)
print (bmi)
​
#We are building a BMI calculator of scratch 

Now we had our #We are building a BMI calculator of scratch 
benchmark
under 18.5 --> Under zeight 
18,5-24.9-->Normal weight-->Minimal risk
25-29.9-->Overweight-->Increased risk
30-34.9-->Obese-->high risk
35-39.9-->Severly obese-->very risk
40 and over -->Morbidly obese-->Extremly high risk
if bmi>0:
    if(bmi<18.5):
        print('you are underweight.')
    elif(bmi<=24.9):
        print('you are Normal weight.')
    elif(bmi<=29.9):
        print('you are Overweight.')
    elif(bmi<=34.9):
        print('you are Obese.')
    elif(bmi<=39.9):
        print('you are Severly obese.')    
    else:
        print('You are morbidly obese')
else :
    print('enter valid inputs')
#We use a if statement to incorporate our benchmark in our calculator
if bmi>0:
    if(bmi<18.5):
        print('you are underweight.')
    elif(bmi<=24.9):
        print('you are Normal weight.')
    elif(bmi<=29.9):
        print('you are Overweight.')
    elif(bmi<=34.9):
        print('you are Obese.')
    elif(bmi<=39.9):
        print('you are Severly obese.')    
    else:
        print('You are morbidly obese')
else :
    print('enter valid inputs')
you are Normal weight.
#Lets bring both together 
name = input ("Enter your name :")
weight = int(input ('Enter your weight in pounds:'))
height = int(input ('Enter your height in inches:'))
bmi= (weight * 703)/ (height * height)
print (bmi)
if bmi>0:
    if(bmi<18.5):
        print(name+',you are underweight.')
    elif(bmi<=24.9):
        print(name+',you are Normal weight.')
    elif(bmi<=29.9):
        print(name+',you are Overweight.')
    elif(bmi<=34.9):
        print(name+',you are Obese.')
    elif(bmi<=39.9):
        print(name+',you are Severly obese.')    
    else:
        print(name+',You are morbidly obese')
else :
    print(name+',enter valid inputs')
​
Enter your name :yemi
Enter your weight in pounds:184
Enter your height in inches:74
23.62162162162162
yemi,you are Normal weight.
