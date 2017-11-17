listOne = [2,4,6,8,10,12,14,16]
listTwo = [2,3,4,5,6,7,8,9,10]
one = set(listOne)
two = set(listTwo)
three = one - two
result = listOne + list(three)
print result
