# Write a python program to count all letters digits and special symbol from the given string  string="p@#yn26at^&i5ve"

string="p@#yn26at^&i5ve"
letters=0
digits=0
special_symbol=0
for i in range(len(string)):
    if((string[i]>='a' and string[i]<='z')or (string[i]>='A' and string[i]<='Z')):
        letters=letters+1
    elif(string[i]>='0' and string[i]<='9'):
        digits=digits+1
    else:
        special_symbol=special_symbol+1
print("Total number of letters in the string :",letters)
print("Total number of digits in the string :",digits)
print("Total number of special_symbol in the string :",special_symbol)



#----------------------------------------------------------------------------------------------------------------
'''    output
Total number of letters in the string : 8
Total number of digits in the string : 3
Total number of special_symbol in the string : 4

'''
