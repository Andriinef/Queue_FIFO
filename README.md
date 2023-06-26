# Queue with Length Limit

This is a Python implementation of a queue data structure with a maximum length limit. The `Queue` class allows you to create a queue object with a specified maximum size and provides methods to add elements to the queue (`_append`) and retrieve elements from the queue (`_get`). If the queue length exceeds the limit, a `LengthLimitException` is raised.

## Usage

```python
obj = Queue(limit)
obj._append(value)
element = obj._get()
```

## Example

```python
obj = Queue(3)
obj._append(1)
obj._append(2)
obj._append(3)

print(obj._get())  # Output: 1
print(obj._get())  # Output: 2
print(obj._get())  # Output: 3

obj._append(4)
obj._append(5)
obj._append(6)

print(obj._get())  # Output: None

obj._append(7)

print(obj.objects)  # Output: [6, 7]
```

## Exception

The `LengthLimitException` is raised when the queue length exceeds the specified limit.

```python
class LengthLimitException(Exception):
    def __init__(self, message: str = "Queue length over limit"):
        self.message = message
```

Note: The `_append` and `_get` methods are intended to be used internally within the `Queue` class. It is recommended to use the public interface provided by the class whenever possible (`obj._append` and `obj._get` are used in the example for demonstration purposes).

Please note that using methods or attributes prefixed with an underscore (`_`) is a convention in Python to indicate that they are intended for internal use and should not be accessed directly from outside the class.
