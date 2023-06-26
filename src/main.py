from queue import Queue

# Создание экземпляра очереди
queue: Queue[int] = Queue()

# Добавление элементов в очередь
queue.put(10)
queue.put(20)
queue.put(30)

# Удаление элементов из очереди
item1 = queue.get()
item2 = queue.get()

print(item1)  # Вывод: 10
print(item2)  # Вывод: 20
