#si es multiplo de 3 y 5 o solo 3 o 5
for i in range(1,50):
    if i%3==0 and i%5==0 :
        print("tres y cinco")    
    elif i%3==0:
      print("tres")
    elif i%5==0:
        print("cinco")
    else:
        print(i)
        
        
        