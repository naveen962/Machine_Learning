import random

def Generate_Coupon(num):
    list=[]
   
    ran=random.randint(0,100)
    for i in range(num):
        while ran in list:
             ran=random.randint(0,100)
             
        list.append(ran)
    return list

n=int(input("enter the number : "))

print(Generate_Coupon(n))


        

    

    
