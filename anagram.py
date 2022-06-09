str1=input("Enter the first string:")
str2=input("Enter the second string:")
if (len(str1)==len(str2)):
	r=sorted(str1)
	h=sorted(str2)
	if (r==h):
		print("anagram of given string")
	else:
		print("not an anagram")
else:
	print("The length is not equal")

