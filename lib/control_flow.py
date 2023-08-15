#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or  username == "ADMIN") and password =="12345":
        return "Access granted"
    else: 
        return "Access denied"

admin_login("admin", "12345")

def hows_the_weather(temperature):
   temperature <= 40
   if temperature >=40 and temperature <= 60:
       return "It's a little chilly out there!"
   if temperature >60 and temperature<= 85:
       return "It's perfect out there!"
   if temperature> 85:
       return "It's too dang hot out there!"
   else:
       return "It's brisk out there!"
hows_the_weather(33)

def fizzbuzz(num):
   if num%3==0 and num%5 ==0 :
       return "FizzBuzz"
   if num%3 == 0:
       return "Fizz"
   elif num % 5==0 :
       return "Buzz"
   
   else:
       return num
       

def calculator(operation, num1, num2):
    if operation == "+":
        return num1+num2
    elif operation == "-":
        return num1-num2
    elif operation == "*":
        return num1*num2
    elif operation == "/":
        return num1/num2
    else:
        return  "Invalid operation!"
calculator("a", 1, 2)
    