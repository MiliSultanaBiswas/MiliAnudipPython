# Write a python program to count amd display the vowels of a given text string="welcome to Python Training--"

string="welcome to Python Training "
values=0
a=0
e=0
I=0
o=0
u=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' ):
        values=values+1 

        if(i=='a' or i=='A' ):
            a=a+1
        elif(i=='e' or i=='E' ):
            e=e+1
        elif(i=='i' or i=='I' ):
            I=I+1
        elif(i=='o' or i=='O' ):
            o=o+1
        elif(i=='u' or i=='U' ):
            u=u+1

print("number of vowels are =",values)
print("a=",a)
print("e=",e)
print("I=",I)
print("o=",o)
print("u=",u)

#-------------------------------------------------------------------------------------------------------------
'''   output
number of vowels are = 8
a= 1
e= 2
I= 2
o= 3
u= 0
'''

