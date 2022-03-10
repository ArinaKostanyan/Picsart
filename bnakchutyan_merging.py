import random
#import os
import sys
import pathlib

name = input("enter your file name: ")

file =pathlib.Path(name)
if file.exists():
    print("the file already exists")
    name = input("enter your file name: ")
else:
    f=open(name,"x")

f.close()

f=open(name,"w")


population = int(input(f"enter quantity of {name.title()}'s population: "))
age0 = int(input("enter the youngest age: "))
age1 = int(input("enter the oldest age: "))

for i in range(population):
    x = random.randint(age0, age1)
    f.write(str(x))
    if i != population-1:
        f.write("\n")
    
f.close()


"""
if os.path.exists(name):
    os.remove(name)
else:
    print("The file does not exist")
"""

#2

#merge sort

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1


f=open(name) 

line=f.readline()

aver_size = sys.getsizeof( line )
print(f"One line is {aver_size} expressed in bytes ")

reg_size = 10**4 #hishoxutyunic ogtagortsvum e 2MB taratsq
listi_qanak = reg_size//aver_size

f.close()

f=open(name,"r")


while population >= 0:
    population-=listi_qanak
    lst = []
    tmp=0
    for i in range(listi_qanak):
        try:
            lst.append(int(line))    
        except:
            tmp=-1
        line=f.readline()


    
    mergeSort(lst)
    print(lst)
    for i in lst:
        f.write(str(x) + "\n")

f.close()


    