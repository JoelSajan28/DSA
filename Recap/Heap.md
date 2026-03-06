# Heaps (Priority Queue Data Structure)

A **heap** is a special **tree-based data structure** that satisfies the **heap property**.

Heaps are usually implemented using **arrays**, not pointers.

They are primarily used for **priority queues**.

---

# 1. Heap Property

There are two main types of heaps.

## Min Heap

Parent node is **smaller than or equal to its children**

```
        1
      /   \
     3     6
    / \
   5   9
```

Smallest element is always at the **root**.

---

## Max Heap

Parent node is **greater than or equal to its children**

```
        9
      /   \
     5     6
    / \
   2   3
```

Largest element is always at the **root**.

---

# 2. Why Heaps Use Arrays

Instead of storing nodes with pointers, heaps store elements in an array.

Example Min Heap:

```
        1
      /   \
     3     6
    / \
   5   9
```

Array representation:

```
[1, 3, 6, 5, 9]
```

---

# 3. Index Relationships

For an element at index **i**

| Relation | Formula |
|--------|--------|
| Left child | `2*i + 1` |
| Right child | `2*i + 2` |
| Parent | `(i - 1) // 2` |

Example:

```
Index:  0 1 2 3 4
Value: [1 3 6 5 9]
```

---

# 4. Heap Operations

| Operation | Time Complexity |
|----------|----------------|
| Insert | O(log n) |
| Extract Min/Max | O(log n) |
| Peek | O(1) |
| Build Heap | O(n) |

---

# 5. Insert Operation

Steps:

1. Insert element at the **end**
2. Perform **heapify-up (bubble up)**

Example:

Insert `2` into:

```
[1,3,6,5,9]
```

After insert:

```
[1,3,6,5,9,2]
```

Bubble up:

```
[1,3,2,5,9,6]
```

---

# 6. Extract Min / Max

Steps:

1. Remove root
2. Move last element to root
3. Heapify down

Example:

```
[1,3,2,5,9,6]
```

Remove `1`

```
[6,3,2,5,9]
```

Heapify down

```
[2,3,6,5,9]
```

---

# 7. Heapify (Down Operation)

Heapify ensures the heap property is maintained.

```
def heapify_down(heap, i, n):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and heap[left] < heap[smallest]:
        smallest = left

    if right < n and heap[right] < heap[smallest]:
        smallest = right

    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        heapify_down(heap, smallest, n)
```

---

# 8. Python Heap (heapq)

Python provides a built-in **min heap**.

```
import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)

print(heapq.heappop(heap))
```

Output:

```
2
```

---

# 9. Convert List to Heap

```
import heapq

nums = [5,3,8,1,2]
heapq.heapify(nums)

print(nums)
```

Time complexity:

```
O(n)
```

---

# 10. Max Heap in Python

Python only supports **min heap**.

To simulate a **max heap**:

```
import heapq

heap = []

heapq.heappush(heap, -10)
heapq.heappush(heap, -5)
heapq.heappush(heap, -20)

print(-heapq.heappop(heap))
```

---

# 11. When to Use Heaps

Use heaps when you need:

| Problem | Reason |
|------|------|
| Priority queues | fastest min/max access |
| Top K elements | efficient selection |
| Scheduling | task priority |
| Dijkstra algorithm | shortest path |
| Merge K sorted lists | efficient merging |

---

# 12. Heap vs Sorted List

| Feature | Heap | Sorted List |
|------|------|------|
| Insert | O(log n) | O(n) |
| Get Min | O(1) | O(1) |
| Remove Min | O(log n) | O(n) |

Heaps are faster when **many inserts + removals** occur.

---

# Mental Model

Think of heap as:

```
a tree that keeps the most important element on top
```

Min heap → smallest priority first  
Max heap → largest priority first