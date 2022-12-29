
#return the argument
def Name(a,b):
    add=a+b
    print(add)
    return add
bat=Name(2,3)
print("\n")
#concat welcome hcl
def name(word):
    msg="welcome" ' ' + word
    print(msg)
cat=name("hcl")
print("\n")
#return area and perimeter of a square.
import math
def areasq(d):
    area=pow(d,2)
    print(area)
    return area
def perimetersq(c):
    perimeter=4*c
    print(perimeter)
    return perimeter
pinky=areasq(3)
pavi=perimetersq(4)
print("\n")
#print no.of upper and lowercase
def pinky(str):
    upper=0
    lower=0
    for i in str:
        if i.isupper():
            upper+=1
        else:
            lower+=1
    print(upper)
    print(lower)
pinky("helLO")
print("\n")
#sum,min,max
def deva(box):
    sum=0
    for i in box:
        if i.isdigit()==True:
            s=int(i)
            sum=sum+s
    h=max(box)
    g=min(box)
    print("max",h)
    print("min",g)
    print("sum of numbers is",sum)
hello=deva("134567")
print("\n")

#bill amount as argument
def bill_amount(amount):
    print(amount)
amount=2000
if amount<500:
    print(0.05*amount)
elif amount>=500 and amount<2500:
    print(0.1*amount)
else:
    print(0.2*amount)
bill_amount(2000)








