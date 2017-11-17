Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> sentence= input ("Enter a sentence: ")
Enter a sentence: My name is Umamah
>>> VowelsinSentence = 0
>>> for Element in sentence:
	if Element == 'a' or Element == 'e' or Element == 'i' or Element == 'o' or Element == 'u' or Element == 'A' or Element == 'E' or Element == 'I' or Element == 'O' or Element == 'U':
		VowelsinSentence += 1

		
>>> print ("The number of vowels in the sentence are " +str(VowelsinSentence))
The number of vowels in the sentence are 6
>>> 
