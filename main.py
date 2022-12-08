import random

name = input("Name: ")
print(name)

username = input("Username: ")
print(username)

password = input("Password: ")
print(password)

classSize = int(input("Class Size: "))
print(classSize)

if classSize <= 40:
  
  numOfInput = 0
  
  assignedNumbers = []
  
  while True:
    
    try:
      
      for _ in range(classSize):
        
        assignedNumbers.append(input("Enter Student Name: "))
        
        numOfInput += 1
    
    except ValueError:
      
      continue
    
    if numOfInput == classSize:
      
      print(assignedNumbers)
      
      break

else: 
  
  print("Class size is too big")

numGenerated = 0

n = 0

while True:
  
  rand = random.randint(1,classSize)
  
  if rand not in assignedNumbers:
    
    assignedNumbers.append(rand)
    
    print(rand, "-", assignedNumbers[n])
    
    n += 1
    numGenerated += 1
  
  if numGenerated == classSize:
   
    break

