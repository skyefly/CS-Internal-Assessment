def save_user_info(name, email, password):
    
    with open("user_info.txt", "w") as file:
        
        file.write(name + '\n')
        file.write(email + '\n')
        file.write(password)

def get_saved_user_info():
    
    try:
        
        with open("user_info.txt", "r") as file:
            
            name = file.readline().strip()
            email = file.readline().strip()
            password = file.readline().strip()
            
            return name, email, password
    
    except:
        
        return None, None, None

def login():
    
    name, email, password = get_saved_user_info()
    
    if name:
        
        print("Welcome back,", name)
        
        return name, email, password
    
    else:
        
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        
        save_user_info(name, email, password)
        
        return name, email, password

name, email, password = login()

print("Name:", name)
print("Email:", email)
print("Password:", password)

import turtle
import random

# Set up the turtle graphics window
turtle.setup(width=700, height=500)
turtle.screensize(700, 500)
turtle.title("Seating Chart")

# Ask for number of students
num_students = int(input("Enter the number of students: "))

# Check if number of students is less than or equal to 40
if num_students > 40:
    
    print("The number of students should not exceed 40.")
    
    turtle.done()
    quit()

# Ask for names of students
names = []

for i in range(num_students):
    
    name = input("Enter name of student {}: ".format(i + 1))
    names.append(name)

# Randomly shuffle the names
random.shuffle(names)

# Split the names into groups of 4
groups = [names[n:n + 4] for n in range(0, len(names), 4)]

# Define the draw_square function
def draw_square(x, y, name):
    
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    for i in range(4):
        
        turtle.forward(50)
        turtle.left(90)
    
    turtle.penup()
    turtle.goto(x + 25, y - 25)
    turtle.pendown()
    turtle.write(name, align="center", font=("Arial", 14, "normal"))

# Draw squares for each group of students
x = -250
y = 200

for group in groups:
    
    for name in group:
        
        draw_square(x, y, name)
        x += 100
    
    x = -250
    y -= 100

import os

# Allow the user to make changes to the seating chart
while True:
    
    change = input("Do you want to make any changes to the seating chart (y/n)? ")
    
    if change.lower() == 'n':
      
      final = input("Are you satisfied with your new seating chart (y/n) ") 
      
      if final.lower() == 'y':
        
        print("You're all set!")
        
        logout = input("Do you wish to log out? (y/n) ")
        
        if logout.lower() == 'n':
          
          print("Ok, we'll keep you logged in")
          
          break
        
        if logout.lower() == 'y':
          
          os.remove("user_info.txt")
          
          break
    
    index = int(input("Enter the index of the student you want to change: "))
    
    new_name = input("Enter the the new name of the student: ")
    
    names[index] = new_name
    
    groups = [names[n:n + 4] for n in range(0, len(names), 4)]
    
    turtle.clear()
    
    x = -250
    y = 200
    
    for group in groups:
        
        for name in group:
            
            draw_square(x, y, name)
            
            x += 100
        
        x = -250
        y -= 100

# Keep the turtle graphics window open
turtle.done()  

import pickle

# Function to save the turtle display
def save_display(filename):
    
    with open(filename, 'wb') as file:
        
        pickle.dump(turtle.Screen()._canvas, file)

# Function to load and display the turtle display
def load_display(filename):
    
    with open(filename, 'rb') as file:
        
        turtle.Screen()._canvas = pickle.load(file)

# Example usage
save_display('turtle_display.pkl')

# For when the user logs back in
load_display('turtle_display.pkl')

turtle.done()