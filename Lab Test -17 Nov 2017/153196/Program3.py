list1 = []
list2 = []
list3 = []
for i in range(0, 3):
    num = input('Enter a number for List#1: ')
    list1.append(num)
for i in range(0, 3):
    num = input('Enter a number for List#2: ')
    list2.append(num)
for element in list1:
    flag = True
    for nextedElement in list2:
        if(element == nextedElement):
            flag = False
    if (flag):
        list3.append(element)
for element in list2:
    flag = True
    for nextedElement in list1:
        if(element == nextedElement):
            flag = False
    if (flag):
        list3.append(element)

print 'List#3: ', list3
