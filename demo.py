import timeit

start = timeit.default_timer()
sum_x = 0
for i in range(1000000):
    sum_x += i
print('Sum of first 1 million numbers is:', sum_x)
stop = timeit.default_timer()
execution_time = stop - start

print("CPU Execution time: "+str(execution_time)+'seconds')
