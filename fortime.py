import time

n = 11

busy_work = 0

start_time = time.time()
for i in range(10**n):
    busy_work = busy_work + 1

end_time = time.time()
elapsed_time = end_time - start_time

print("Elapsed Time: {:2.2f} sec".format(elapsed_time))
