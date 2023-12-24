# A transport company charges thr fare according to the following table 
# distance charges
#1-50 8Rs./km  51-100 10rs/km    >100 12rs/km

dis=int(input("enter the distance :"))
if(dis>=1 and dis<=50):
    fare=dis*8
elif(dis>=51 and dis<=100):
    fare=dis*10
elif(dis>100):
    fare=dis*12
else:
    print("invalid fare")
print("total fare is ",fare)

# output 
# enter the distance :200
#total fare is  2400
