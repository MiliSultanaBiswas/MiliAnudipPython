''' python program to check leap year '''

year=int(input("enter a year :"))
a=year%4
b=year%100
c=year%400
if(a==0 or c==0 and b!=0):
    print("leap year")
else:
    print("not leap year")

''' output
enter a year :2022
not leap year
'''