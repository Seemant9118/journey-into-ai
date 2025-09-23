# Type definitions in Python
# Type hints are added using the colon (:) syntax for variables and the -> syntax for
# function return types

a: int = 5
b: str = "Hello"
c: float = 3.14

def add(x: int, y: int) -> int:
    return x + y

def greet(name: str) -> str:
    return f"Hello, {name}!"

# advanced type hints
from typing import List, Dict, Tuple, Optional, Union

def process_data(data: List[int]) -> Dict[str, int]:
    return {"sum": sum(data), "max": max(data), "min": min(data)}

def get_user_info(user_id: int) -> Optional[Dict[str, Union[str, int]]]:
    if user_id == 1:
        return {"name": "Alice", "age": 30}
    else:
        return None

def coordinates() -> Tuple[float, float]:
    return (40.7128, -74.0060)

# Example usage
print(add(2, 3))  # Output: 5
print(greet("Bob"))  # Output: Hello, Bob!
print(process_data([1, 2, 3, 4, 5]))  # Output: {'sum': 15, 'max': 5, 'min': 1}
print(get_user_info(1))  # Output: {'name': 'Alice', 'age
print(get_user_info(2))  # Output: None
print(coordinates())  # Output: (40.7128, -74.0060
# Type hints are not enforced at runtime, but they can be checked using tools like mypy.
# They are mainly used for improving code readability and assisting with static analysis.

