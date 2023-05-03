from collections import Counter, deque


def create_kolo_fortuny(*args) -> deque:
    return deque(Counter(args).elements())


print(create_kolo_fortuny(1,2,3,4,5,6,7,8,9,10,11,23,45,33,1,2,3,4))
