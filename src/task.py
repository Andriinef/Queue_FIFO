"""Create a queue object with a given maximum size"""


class LengthLimitException(Exception):
    def __init__(self, message: str = "Queue length over limit"):
        self.message = message


class Queue:
    def __init__(self, limit) -> None:
        self.objects: list = []
        self.limit: int = limit

    def is_empty(self):
        return self.objects == []

    def length(self):
        return len(self.objects)

    def _append(self, value: int | str):
        # import ipdb; ipdb.set_trace()
        if value is None:
            return

        try:
            if self.length() >= self.limit:
                raise LengthLimitException("Queue length exceeded the limit")
        except LengthLimitException as e:
            print(e.message)

        self.objects.append(value)

    def _get(self):
        try:
            return self.objects.pop(0)
        except IndexError:
            return None


obj = Queue(3)
obj._append(1)
obj._append(2)
obj._append(3)

print(obj._get())
print(obj._get())
print(obj._get())
obj._append(4)
obj._append(5)
obj._append(6)

print(obj._get())

obj._append(7)

print(obj.objects)
