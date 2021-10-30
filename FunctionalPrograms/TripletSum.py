
'''Sum of three Integer adds to ZERO
a. Desc -> A program with cubic running time. Read in N integers and counts the
number of triples that sum to exactly 0.
b. I/P -> N number of integer, and N integer input array
c. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
d. O/P -> One Output is number of distinct triplets as well as the second output is to
print the distinct triplets.'''




def Find_Triplet(list,m):

    flag = False
    #assign i for first value of list
    for i in range(0,m):
        #assign j for second value of list
        for j in range(i+1,m):
            #assign k for third value of list
            for k in range(j+1,m):
                #checking condition
                if (list[i]+list[j]+list[k]==0):
                    print("Triplet Found : ",list[i],list[j],list[k])
                    flag=True
    if (flag==False):
        print("No Triplets found")


#Take input from user
list=[]
size=int(input("Enter the size of an array : "))
print("Enter the Elements")
for i in range(size):
    elements=int(input())
    list.append(elements)

Find_Triplet(list,size)
