firstList = [7,24,5,1,6,8,9,2]
secondList = [7,5,9,6,4,24,78,55]
in_first = set(firstList)
in_second = set(secondList)
in_second_but_not_in_first = in_second - in_first
result = firstList + list(in_second_but_not_in_first)
print (result)
