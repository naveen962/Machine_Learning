'''Leap Year
a. I/P -> Year, ensure it is a 4 digit number.
b. Logic -> Determine if it is a Leap Year.
c. O/P -> Print the year is a Leap Year or not.'''

#taking year as input
year=int(input("Enter the YEAR : "))

#checking condition
if year%4==0 and year%100!=0 or year%400==0 :
    print("Leap Year")
else:
    print(year, "is not a Leap Year") 