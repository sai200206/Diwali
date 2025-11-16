
# import math
# name = 'vinayaka'
# print(f'the name is {name}')

# #exercise 1 (AREA)
# length = float(input("Enter lenght :"))
# breadth = float(input("Enter breadth :"))
# area = length*breadth
# if length==breadth:
#     print("it is a SQUARE")
# else:
#     print(f"it is a Rectangle, Area={area}")

# #exercise 2 (BILL)
# item = input("Enter the item name : ")
# quantity = int(input("enter the quantity : "))
# price = float(input("enter the price : "))

# total = quantity*price
# bill = (f"For the {item},\nOf {quantity} no's,\nThe total price is {total}")
# print(bill)

# #arithmetic operators
# a=5
# # a=a+5
# a+=4
# print(a)

# print(math.pi)

# #exercise -3 (Circumference)
# r=float(input("Enter the radius of the circle: "))
# area = (2*math.pi*r)
# print(f"Area of the circle is = {area}")

# #exercise -4 (Hypotenuse of the Triangle)
# a = float(input("enter the a side of the triangle : "))
# b = float(input("enter the b side of the triangle : "))
# c = math.sqrt((a**2)+(b**2))
# print(f"length of third side = {c}")

# #exercise -5 (calculator program)
# a=float(input("Enter a value : "))
# b=input("enter an operation(+,-,*,/) : ")
# c=float(input("enter the value : "))

# if b=="+":
#     print("sum = ", {a+c})
# elif b=="-":
#     print("diff = ", a-c)
# elif b=="*":
#     print("prod = ", a*c)
# elif b=="/":
#     print("div = ", a/c)
# else:
#     print("Type the correct operator")
    
    
# # exerecise - 6 (weight converter)

# weight = float(input("enter the weight : "))
# units= input("Enter the unit : ")
# if units=="kg":
#     grams=(weight*1000)
#     print(f"weight in grms = {grams}")
# elif units=="ton":
#     kg=weight*1000
#     print(f"weight in kg = {kg}")
# else:
#     print(f"you entered an invalid '{units}' unit")

# #exercise -7 (Temperature converter)

# temp = float(input("enter the Temperature : "))
# unit = input("enter the units (centigrede or forhen heat) : ")
# if unit =="centigrede" or unit =="c"  :
#     temperature = (temp*9/5)+32
#     print(f"Todays weather report 'celcisu'{temperature}")
# elif unit== "forhen heat" or unit== "f":
#     temperature = (temp*9/5)-32
#     print(f"Todays weather report 'forhein' {temperature}")
# else:
#     print("invalid unit")


#conditional expressions (Ternary operators) -> x if condition else y

# temperature = 38
# wind=30
# x=("windy" if temperature<wind else "normal")
# print(x)

# #string methods 
# U_NAME=input("write a line : ")
# length=len(U_NAME)
# U_NAME=U_NAME.replace(" ","")

# if length<=12 and U_NAME.isalpha():
#     print(f"valid username : {U_NAME} {length}")
# else:
#     print(f"invalid username : {U_NAME}")


# #string indexing 

# card=input("enter credit card number : ")
# four=card[-5:-1]
# print(f"This is your credit card number : \n XXXX XXXX XXXX {four}")


# #while loop - executes some code while some condition remains true

# username=input("enter username : ")
# while username=="":
#     print("Please Enter user name")   
#     username=input("enter username : ") 
# print(f"This is your user name : {username}")

# #for loop 
# a=int(input("enter value of A : "))
# b=int(input("enter value of B : "))
# c=int(input("enter value of C : "))
# for x in range(a,b,c):
#     print(x)
   

# #exercise - 8 (stop watch program)
# import time
# for x in range(1,11):
#     print(x)
#     time.sleep(1)
# print("Time up")

# # continue and break
# for x in range(1,11):
#     if x==6:
#         continue
#     elif x==9:
#         break
#     else:
#         print(x)
#     time.sleep(1) 
# print("Time up")

# import time
# timer = int(input("Enter the time : "))
# for x in reversed(range(timer)):
#     seconds=(x%60)
#     mins=int(x/60)%60
#     hours=int(x/3600)
#     print(f"{hours}:{mins}:{seconds}sec")
#     time.sleep(1)
# print("Times up")

# #nested loops

# for x in range(3):
#     print(x, end=" ")
#     for y in range(56,61):
#         print(y,end=" ")
#     print()

#collections - single variable used to store multiple values (List, Tuple, set, dictionary)
froots=["apple", "banana", "chickoo", "darwin"]
check=("energy" in froots)
while check==False:
    print("No energy in froots")
    froot=(input("add energy by typing : "))
    froots.append(froot)
    check=("energy" in froots)
    if check==True:
        break
    
print(f"froots = {froots}")

