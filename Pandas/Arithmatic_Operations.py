''' program to add, subtract, multiple and divide two Pandas Series '''

import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2                      #Add two series
print("Add two Series:")
print(ds)
print("Subtract two Series:")       #subtract Two series
ds = ds1 - ds2
print(ds)
print("Multiply two Series:")       #Multiply Two series
ds = ds1 * ds2
print(ds)
print("Divide Series1 by Series2:")
ds = ds1 / ds2                     #divide
print(ds)