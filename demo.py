import timeit
import math

start = timeit.default_timer()
# sum_x = 1
# for i in range():
#     sum_x += i
sum_x = math.factorial(1000000)
print('Factorial is:', sum_x)
stop = timeit.default_timer()
execution_time = stop - start

print("CPU Execution time: "+str(execution_time)+'seconds')
