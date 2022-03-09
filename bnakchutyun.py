import random
import os

name = input("enter your file name: ")

t=True
while t:
    name = input("enter your file name: ")
    f=open(name,"x")
    if FileExistsError:
        print("the file already exists")
        name = input("enter your file name: ")
        t=False
    
f=open(name,"w")

population = int(input(f"enter quantity of {name.title()}'s population: "))
age0 = int(input("enter the youngest age: "))
age1 = int(input("enter the oldest age: "))

for i in range(population):
    x = random.randint(age0, age1)
    f.write(f"{str(x)}\n" )
    
f.close()

f=open(name)
print(f.read())
f.close()
"""
if os.path.exists(name):
    os.remove(name)
else:
    print("The file does not exist")
"""
