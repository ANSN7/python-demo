import timeit
import math
import time
from datetime import datetime, timedelta

start = timeit.default_timer()
print(start)
print(datetime.utcnow())
# sum_x = 1
# for i in range():
#     sum_x += i
sum_x = math.factorial(100000)
# print('Factorial is:', sum_x)
stop = timeit.default_timer()
print(stop)
print(datetime.utcnow())
execution_time = stop - start

print("CPU Execution time: "+str(execution_time)+'seconds')
