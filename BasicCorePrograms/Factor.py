'''Factors
a. Desc -> Computes the prime factorization of N using brute force.
b. I/P -> Number to find the prime factors
c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
d. O/P -> Print the prime factors of number N.'''
#taking user input
num=int(input("Enter a Number : "))
i = 2            
while num>1:            
    if num % i == 0 :  
        print(i)
        num = num / i                
    else:
         i=i+1
                    
                