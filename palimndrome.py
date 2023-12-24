# Write a python program to check if the given string is a palindrome or not....

s=input("Enter a string :")
temp=(s[::-1])
print("reverse =",temp)
if(s==temp):
    print("palimdrome")
else:
    print("not palindrome")


#-----------------------------------------------------
'''  output
Enter a string :mam
reverse = mam
palimdrome


Enter a string :mili
reverse = ilim
not palindrome
'''