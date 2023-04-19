def posortowane(d: dict, keyy: callable) -> dict:
    sortowane = {}
    for k, v in d.items():
        sortowane = sorted(filter(lambda x: isinstance(x, int), v), key=keyy)
        posortowane[k] = sortowane
    return sortowane


d = {'Karolina': [1,2,3,22,345,6], 'Weronika': [2,3,4,5,11]}
print(posortowane(d,keyy=sum))
print(posortowane(d,keyy=max))
print(posortowane(d,keyy=min))