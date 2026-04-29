import time 
actual = time.time()
print(time.ctime(actual))
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("Happy Birthday")