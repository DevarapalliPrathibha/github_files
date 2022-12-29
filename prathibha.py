print(6+7+8)
print(len("pinky"))
print("python is amazing")
p="pinky"
q="hello"
print(len(p+q))
print(19%2,19//2,)
p=[2,3,4,5]
print(type(p))
t=(2,3,4,5)
print(type(t))
q={5,3,8}
print(type(q))
i="2,3,4"
print(type(i))
c=3+4j
print(type(c))
r={"h":"10"}
print(type(r))
print(id("pinky"))
print(id("hi"))
list_a=[1,2,3]
list_b=list_a
print(id(list_a))
print(id(list_b))
list_b[2]=4
print(list_a)
print(list_b)
list_a=[3,4,5]
list_b=list_a
list_a=list_a+[1,2,9]
print(list_a)
list_r=[8,7]
list_d=list_r
list_r+=[3,2]
print(list_r)
print(list_d)
list_p=[1,2,3]
list_q=[5,list_p]
list_p[2]=9
print((list_p))
print((list_q))
numbers="1 2 3  4"
num_list=numbers.split()
print(num_list)
numbers="1,2,34"
num_list=numbers.split(',')
print(num_list);
numbers="1 2 3  4"
num_list=numbers.split(" ")
print(num_list);

list_w=[1,2,3,4,5]
list_y=list_w[-4:-1:1]
print(list_y)
N=[1,2,3,4,5,6]
a=N[0:1]
b=N[-3:]
print(a+b)
a="Apple"
b="ApPle"
if(a[0:3]==b[0:3]):
    print(True)
else:
    print(False)
a="432"
b="126"
if(a[:1]<b[:-2]):
    print(True)
else:
    print(False)
N=[1,2,3,4,5]
list_a=N[::-1]
print(list_a)
list_a=[4,5,6,7,8]
list_b=list_a[1:4:3]
print(list_b)
# and operator
M=65
P=80
C=50
if(M>=70 and P>=60 and C>=60):
    print("yes")
else:
    print("no")
if(M+P+C>=180):
    print("yes")
else:
    print(no)
    #swap
a="PyThON"
b=a.swapcase()
print(b)
str="PiNkY"
print(str.swapcase())
# replace
a="04-07-2001"
b=a.replace("-","/")
print(b)
#palindrome
str="madam"
if(str[::-1]==str):
    print("palindrome")
else:
    print("not a palindrome")
s="madam"
s[::-1]==s
#valid password
import re
p="Pinky1234"
ant=True
while ant:
    if(len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[@]",p):
        break
    else:
        print("it is a valid")
        ant=False
        break
if ant:
    print("it is not a vallid")

a=24
if a !=0:
    if(a%2==0):
        print("not a prime number")
    else:
        print("prime number")
s="madam"
print(s[::-1]==s)

#print digit in ones place
n=5678
digit_at_ones_place = n % 10
print(digit_at_ones_place)
#coverting numbers into y,w,D
days=1329
no_of_years= days // 365
no_of_days=days- no_of_years*365
print("{} years and {} days".format(no_of_years,no_of_days))
weeks=days/7
print(int(weeks))
#sum of given numbers
list=[1,2,3]
print(sum(list))
#sum of n natural numbers
n=7
sum=0
for i in range(1,8):
    sum+=i
print(sum)
#product of number
a=8
product=1
for i in range(1,9):
    product=product*i
print(product)
print("\n")
#square
i=3
j=3
for i in range(0,4):
    for j in range(0,4):
        print(" * ",end=' ')
    print()
print("\n")

#rectangle
i=5
j=7
for i in range(0,6):
    for j in range(0,8):
        print(" * ",end=' ')
    print()
print("\n")
#triangle(increasing)
n=5
for i in range(n):
    for j in range(0,i+1):
        print(" * ",end=' ')
    print()
print("\n")
#decreasing
n=5
for i in range(n):
    for j in range(i,n):
        print(" * ",end=' ')
    print()
print("\n")
#imaginary right traingle
for i in range(n):
    for j in range(n-i+1):
        print(" ",end=' ')
    for j in range(i):
        print("*",end=' ')
    print()
print("\n")
#

for i in range(n):
    for j in range(n-i+1):
        print(" * ",end=' ')
    print()

    print("\U0001F632")

for i in range(n):
    for j in range(n-i-1):
        print(" ",end=' ')
    for j in range(i):
        print("*",end=' ')
    print()
print("\n")

tuple_a=1,
print(tuple_a)
print(type(tuple_a))
tuple_p=('p','t','y')
(s1,s2,s3)=tuple_p
print(tuple_p)
#sets
set_a={1,[2,3]}
print(set_a)
set_c=set([1,2,4])
print(set_c)
#set
string_a="pinky!"
set_b=set(string_a)
print(set_b)
set_a={1,2,5,45}
set_a(7)

set_1={1,2,3,4,6,7}
set_2={2,3,4}
is_subset=set_2.issubset(set_1)
print(is_subset)









