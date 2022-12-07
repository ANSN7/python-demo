from time import process_time

st = process_time()
sum_x = 0
for i in range(1000000):
    sum_x += i
print('Sum of first 1 million numbers is:', sum_x)
et = process_time()
res = et - st
print('CPU Execution time:', res, 'seconds')
