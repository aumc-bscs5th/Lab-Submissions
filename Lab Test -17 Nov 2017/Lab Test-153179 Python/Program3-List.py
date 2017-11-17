list1=[1,2,3,6,5]
list2=[1,19,4,3,5,6]
first = set(list1)
second = set(list2)
third = second - first
result = list1 + list(third)
print (result)
