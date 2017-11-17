str = raw_input('Enter a string: ')
count = 0
vowelA = False
vowelE = False
vowelI = False
vowelO = False
vowelU = False

for ch in str:
    if (ch == 'a' or ch == 'A'):
        vowelA = True
        count += 1
    elif (ch == 'e' or ch == 'E'):
        vowelE = True
        count += 1
    elif (ch == 'i' or ch == 'I'):
        vowelI = True
        count += 1
    elif (ch == 'o' or ch == 'O'):
        vowelO =  True
        count += 1
    elif (ch == 'u' or ch == 'U'):
        vowelU =  True
        count += 1
    else:
        continue
if (vowelA or vowelE or vowelI or vowelO or vowelU):
    print 'String: %r' %str, ' contains %d' %count
    if (vowelA):
        print "String contain vowel 'a'"
    if (vowelE):
        print "String contain vowel 'e'"
    if (vowelI):
        print "String contain vowel 'I'"
    if (vowelO):
        print "String contain vowel 'o'"
    if (vowelU):
        print "String contain vowel 'u'"
else:
    print 'String does not contain vowels.'
