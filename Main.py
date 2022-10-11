class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None:
    if self.last is None:
            self.head = Node(data)
            self.last = self.head
    else:
        self.last.next = Node(data)
        self.last = self.last.next

  def dequeue(self) -> None:
    if self.head is None:
            return None
    else:
        to_return = self.head.data
        self.head = self.head.next
        return to_return

  def status(self) -> None:
    temp = self.head
    while temp!= None:
      print(temp.data, "=>", sep="", end = "")
      temp = temp.next
    print("None")

# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
