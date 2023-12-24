# Write a python program to reverse a words in a string -- string="Deeptech Python Training--"

string="Deeptech Python Training"
s=string.split()[::-1]
l=[]
for i in s:
    l.append(i)
print(" ".join(l))


#----------------------------------------------------------------------
'''   output
Training Python Deeptech
'''