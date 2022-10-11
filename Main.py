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
