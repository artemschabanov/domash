x = input ("ввведите строку") 
f =len(x)
if(f>10):
    print(x[0:-1],"!!!")
elif(f<10):
    print(x[1])