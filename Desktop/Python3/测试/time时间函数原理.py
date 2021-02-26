import time
start_time = time.time()
for i in range(10000):
    i+=1
over_time = time.time()
time=over_time-start_time
print(time)