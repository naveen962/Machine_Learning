import time

start=input("Press s to start time : ")
start_time = time.time()
print(start_time)
stop=input("Press q to end time : ")
end_time = time.time()
print(end_time)
elapsed_time = end_time - start_time
print("Time Elapsed is : ",elapsed_time)