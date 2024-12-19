def scalon(a,b): 
     for i in range(5):
         print(a+b,a+b,b+b)
         b+=1
        
r=scalon(0, 1)
print(r)


def scalon(a,b):  
    i=a+b
    for i in range(10):
        if  a % 3 == 0 and  b % 3==0:
          print(a+b,a+b,b+b)
        a+=1
        
r=scalon(0, 1)
print(r)