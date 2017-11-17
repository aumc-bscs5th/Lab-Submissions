def isPalindromString(string):
    strNum = ''
    size = len(string)
    i = -1
    j = 0
    while (j<size):
        strNum += string[i]
        i -= 1
        j += 1
    if(strNum == string):
        return True
    else:
        return False

def isPalindromNum(n):
    num = n
    strNum = ''
    while (n != 0):
        x = n % 10
        n = n - x
        n = n / 10
        strNum += str(x)
    tempNum = int(strNum)
    if(tempNum == num):
        return True
    else:
        return False

while True:
    string = raw_input('Enter a string: ')
    if isPalindromString(string):
        print 'String is Palindrom'
    else:
        print 'String is not Palindrom'
    num = input('Enter a number: ')
    if isPalindromNum(num):
        print 'Number is Palindrom'
    else:
        print 'Number is not Palindrom'
