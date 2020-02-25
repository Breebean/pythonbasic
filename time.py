import time

a = time.time()
print(a)

b = time.asctime()
print(b)

c = time.ctime()
print(c)

d = time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime(time.time()))
print(d)