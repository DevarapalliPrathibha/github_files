for x in range(65,90):
    alpha = chr(x)
    with open(str(alpha),'w') as file:
        file.write(alpha)

list_a =["a","b","c"]
list_a += ["d"]
print(list_a)
list_b =["apple","banana","cherry"]
list_b[1:3] =["watermelon","grapes"]
print(list_b[0])
print(list_b[1])
print(list_b[2])
#print(list_b[3])
