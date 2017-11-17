list1 = [1,3,5,7,9,11,13,15]
list2 = [1,2,3,4,5,6,7,8,9]
inThefirst = set(list1)
inThesecond = set(list2)
inThesecondButnotINfirst = inThesecond - inThefirst
Result = list1 + list(inThesecondButnotINfirst)
print Result
