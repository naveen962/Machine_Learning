'''2D Array
a. Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.
b. I/P -> M rows, N Cols, and M * N inputs for 2D Array. Use Java Scanner Class
c. Logic -> create 2 dimensional array in memory to read in M rows and N cols
d. O/P -> Print function to print 2 Dimensional Array. In Java use PrintWriter with
OutputStreamWriter to print the output to the screen.'''


def TwoDimensionalArray(Num): #function definition
        for j in range(2):
             print(Num,end=" ")
        print()

n=int(input("Enter a Number : ")) #taking user input
TwoDimensionalArray(n) #calling function
