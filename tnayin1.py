#1
"""
h=int(input ("enter hours "))
r=int(input ("enter rate "))
pay=h*r
print(f"your pay will be {pay}.")
"""

#2

continu=True 
lst=[]
while continu :
    st=input("enter a number")
    if st.isdigit():
        lst.append(int(st))
    elif st  == "done":
        continu=False
        break
    else:
        print("invalid")
    
if lst:    
    print(sum(lst))
    print(len(lst))
    print(sum(lst)/len(lst))
#3 
"""
l=input("enter a letter")

dzayn=[ 'a','e','i','o','u']

if l in dzayn : 
    print("dzaynavor e") 
elif l=='y' :
    print ("ev dzaynavor e ev baxadzayn")
else :
    print("baxadzayn")
"""

#4
"""
h=input("enter horizontal coordinates")
v=int(input("enter your vertical voordimates"))
lst=['a','b','c','d','e','f','g','h']

for j in range (8):
    if h == lst[j]:
        index =int(j)
    break 

if (v+index+1)%2==0:
    print ("sev vandak")
else:
    print("spitak vandak")
"""
#5
"""
f=float(input("enter a temperature"))
c=(f-32)/1.8
print(f"temperature by celsius is{c}.")
"""