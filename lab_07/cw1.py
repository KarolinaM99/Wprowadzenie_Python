from typing import List, Any


def extract_numbers(vals: List[Any]) -> List[int | float]:
    return list(filter(lambda x: isinstance(x, (int, float)), vals))


print(extract_numbers([1,2,3,3.4,5.6,7,"hej"]))