# Linked List Fundamentals

## 1. Singly Linked List

### Node Structure

Each node stores:
- value
- pointer to next node

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

## 2. Linked List Class

```python
class LinkedList:

    def __init__(self):
        self.head = None
```

---

## 3. Traverse / Print List

```python
def print_list(self):
    curr = self.head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")
```

---

## 4. Insert at Head

```
new → old_head → rest
```

```python
def insert_head(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

**Time Complexity:** `O(1)`

---

## 5. Insert at Tail

```
head → ... → last → new
```

```python
def insert_tail(self, data):
    new_node = Node(data)

    if not self.head:
        self.head = new_node
        return

    curr = self.head
    while curr.next:
        curr = curr.next

    curr.next = new_node
```

**Time Complexity:** `O(n)`

---

## 6. Insert at Position

Example:

```
1 → 2 → 4
insert 3 at pos 2
```

Result:

```
1 → 2 → 3 → 4
```

```python
def insert_position(self, pos, data):
    new_node = Node(data)

    if pos == 0:
        new_node.next = self.head
        self.head = new_node
        return

    curr = self.head

    for _ in range(pos - 1):
        curr = curr.next

    new_node.next = curr.next
    curr.next = new_node
```

---

## 7. Delete by Value

```python
def delete_value(self, val):

    if not self.head:
        return

    if self.head.data == val:
        self.head = self.head.next
        return

    curr = self.head

    while curr.next:
        if curr.next.data == val:
            curr.next = curr.next.next
            return
        curr = curr.next
```

---

## 8. Delete by Position

```python
def delete_position(self, pos):

    if pos == 0:
        self.head = self.head.next
        return

    curr = self.head

    for _ in range(pos - 1):
        curr = curr.next

    curr.next = curr.next.next
```

---

## 9. Search Element

```python
def search(self, key):

    curr = self.head
    index = 0

    while curr:
        if curr.data == key:
            return index
        curr = curr.next
        index += 1

    return -1
```

---

## Full Singly Linked List Implementation

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_tail(self, data):

        new = Node(data)

        if not self.head:
            self.head = new
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new

    def delete_value(self, val):

        if not self.head:
            return

        if self.head.data == val:
            self.head = self.head.next
            return

        curr = self.head

        while curr.next:
            if curr.next.data == val:
                curr.next = curr.next.next
                return
            curr = curr.next

    def print_list(self):

        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")
```

---

# 10. Doubly Linked List

Nodes store:
- value
- next pointer
- previous pointer

Example:

```
None ← 1 ⇄ 2 ⇄ 3 → None
```

---

## Node Structure

```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

---

## Doubly Linked List Class

```python
class DoublyLinkedList:

    def __init__(self):
        self.head = None
```

---

## Insert at Head

```python
def insert_head(self, data):

    new = DNode(data)

    if self.head:
        self.head.prev = new
        new.next = self.head

    self.head = new
```

---

## Insert at Tail

```python
def insert_tail(self, data):

    new = DNode(data)

    if not self.head:
        self.head = new
        return

    curr = self.head

    while curr.next:
        curr = curr.next

    curr.next = new
    new.prev = curr
```

---

## Delete Node

```python
def delete(self, key):

    curr = self.head

    while curr:

        if curr.data == key:

            if curr.prev:
                curr.prev.next = curr.next
            else:
                self.head = curr.next

            if curr.next:
                curr.next.prev = curr.prev

            return

        curr = curr.next
```

---

## Traverse

```python
def print_list(self):

    curr = self.head

    while curr:
        print(curr.data, end=" <-> ")
        curr = curr.next

    print("None")
```

---

# Key Differences

| Feature | Singly | Doubly |
|------|------|------|
| Pointers | next | next + prev |
| Memory | less | more |
| Traversal | forward only | both directions |
| Delete node | harder | easier |

---

# Time Complexity

| Operation | Time |
|---|---|
| Insert head | O(1) |
| Insert tail | O(n) |
| Delete | O(n) |
| Search | O(n) |