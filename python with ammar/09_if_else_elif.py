name=input("Please enter your name?")
#age=16
age=int(input("What's your age?"))
# print(type(age))
if age >= 5 and age < 10:
     print("Hello", name, "You are eligible for this admission")
     print("eligible for school")
elif age>=10 and age<20:
    print("eligible for high school")

else:
  print("not eligible")


   

# else: 

#     print("Hello", name, "You are too young for school")