#  Write a python program to check if the given number is a armstring or not....

num=int(input("enter a number :"))
temp=num
sum=0
while(num!=0):
    rim=num%10
    sum=sum+rim*rim*rim
    num=num//10
if(temp==sum):
    print("armstrong")
else:
      print("not armstrong")


#-----------------------------------------------------------
'''   output
enter a number :153
armstrong

enter a number :154
not armstrong

      
      
'''