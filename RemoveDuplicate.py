# Write a python program to remove duplicate characters of a given string  String="string and string function"

string="string and string function"
l=string.split()
k=[]
for i in l:
    if (string.count(i)>=1 and (i not in k)) :
       k.append(i)
print(' '.join(k))


#---------------------------------------------------------------------------------
'''   output
string and function
 
'''