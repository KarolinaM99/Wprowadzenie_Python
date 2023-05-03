import datetime
from collections import deque

print("Liczba operacji - 100")

deq = deque()

start = datetime.datetime.now()
for i in range(100):
    deq.append(i)
stop = datetime.datetime.now()
print("Czas Wykonania operacji append dla obiektu typu deque - ",stop - start)

start2 = datetime.datetime.now()
for i in range(100):
    deq.appendleft(i)
stop2 = datetime.datetime.now()
print("Czas Wykonania operacji appendleft dla obiektu typu deque - ",stop2 - start2)

lis = []

start3 = datetime.datetime.now()
for i in range(100):
    lis.append(i)
stop3 = datetime.datetime.now()
print("Czas Wykonania operacji append dla obiektu typu list - ",stop3 - start3)

start4 = datetime.datetime.now()
for i in range(100):
    lis.insert(0, i)
stop4 = datetime.datetime.now()
print("Czas Wykonania operacji insert(0) dla obiektu typu list - ",stop4 - start4)
