from typing import List, Union


def posortowana(lst: List[Union[int, str]], reversed: bool = False) -> List[Union[int, str]]:
    if reversed:
        return sorted(lst, key=lambda x: (isinstance(x, str), x), reverse=True)
    else:
        return sorted(lst, key=lambda x: (isinstance(x, int), x))

print(posortowana([1,2,3,"Karolina","sddd"]))