n= int(input())
if n%2!=0:
    print("Raro") 
elif n % 2==0 and n>1 and n<=5:
    print ("No es raro") 
elif n % 2==0 and n>5 and n<20: 
    print ("Raro") 
elif n %2 ==0 and n>20 and n<100:
    print ("No es raro") 
else:pass


   
