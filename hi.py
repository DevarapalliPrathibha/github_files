#to remove duplicate numbers in the list
list_a=[1,2,3,4,5,6,7,3,2,4]
print(set(list_a))
#to remove a list of numbers if present in the set.read input as comma seperated
list_a=[1,3,4,5,6,7]
set_b={3}
list_a.remove(3)
print(list_a)
#superset,subset,disjoint
set_a={1,2,3,4,5,6}
set_b={1,2,3,4}
set_c={1,2}
set_d={8,9}
is_superset=set_a.issuperset(set_b)
print(is_superset)
is_subset=set_c.issubset(set_b)
print(is_subset)
is_disjoint=set_d.isdisjoint(set_c)
print(is_disjoint)

#common elements in three sets
set_a={1,2,3,4,5,6}
set_b={1,3,4,9,65}
set_c={2,8,4,1}
intersection=set_a & set_b & set_c
print(intersection)
#min and max values in a list of tuples
list_a=[(10,5,2),(15,2,8),(20,3,9),(55,1,2)]
max_tuple=max(list_a)
print(max_tuple)
list_a=[(10,5,2),(15,2,8),(20,3,9)]
min_tuple=min(list_a)
print(min_tuple)
tuple_a="2,3,4"
tuple_b="9,7,6"
tuple_c="7,4,1 "
print(list_a)
#update dictionary
dict_a={'name':'pinky','age':'21','height':'5.6'}
dict_a['country']='india'
print(dict_a)
del dict_a["age"]
print(dict_a)