# Python Data Structures – Time & Space Complexity

## 1️⃣ Core Built-in Data Structures (Python)

| Data Structure | Access by Index | Search (`x in ?`) | Insert | Delete | Iteration | Extra Notes |
|---|---|---|---|---|---|---|
| **List** | O(1) | O(n) | Append: O(1)\*<br>Insert at i: O(n) | Pop end: O(1)<br>Delete at i: O(n) | O(n) | Dynamic array. *Append is amortized O(1). Shifts required for middle ops.* |
| **Tuple** | O(1) | O(n) | ❌ (immutable) | ❌ | O(n) | Slightly smaller than list. Hashable if elements hashable. |
| **String** | O(1) | O(n) | ❌ (immutable)<br>Concat: O(n) | ❌ | O(n) | `"".join()` is O(total_chars). Repeated `+=` → **O(n²)** total. |
| **Set** | ❌ | O(1)\* | O(1)\* | O(1)\* | O(n) | Hash table. *Worst case O(n).* No order guarantee. |
| **Dict** | ❌ | O(1)\* (key lookup) | O(1)\* | O(1)\* | O(n) | Hash table. Ordered (Python 3.7+ preserves insertion order). |

---

# 2️⃣ Queue / Stack / Deque

| Structure | Push | Pop | Access Front | Access End | Notes |
|---|---|---|---|---|---|
| **Stack (list)** | O(1)\* | O(1)\* | ❌ | O(1) | Use `append()` / `pop()` |
| **Queue (list)** | O(1)\* | O(n) ❌ (`pop(0)`) | O(1) | O(1) | Don’t use list as queue |
| **Deque** | O(1) | O(1) | O(1) | O(1) | Best for BFS, sliding window |

---

# 3️⃣ Linked List

| Operation | Time |
|---|---|
| Access i-th | O(n) |
| Search | O(n) |
| Insert at head | O(1) |
| Delete at head | O(1) |
| Insert after known node | O(1) |
| Delete after known node | O(1) |

---

# 4️⃣ Heap (Priority Queue – `heapq`)

| Operation | Time |
|---|---|
| Push | O(log n) |
| Pop (min) | O(log n) |
| Peek min | O(1) |
| Heapify | O(n) |

---

# 5️⃣ Binary Search Tree (Conceptual)

| Operation | Balanced BST | Worst Case |
|---|---|---|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Inorder traversal | O(n) | O(n) |

---

# 6️⃣ Graph Representations

| Operation | Time |
|---|---|
| Space | O(V + E) |
| BFS / DFS | O(V + E) |
| Edge check | O(1)\* if set<br>O(deg(v)) if list |

---

# 7️⃣ Sorting & Binary Search (Lists)

| Operation | Time |
|---|---|
| Sort | O(n log n) |
| Binary search | O(log n) |
| Insert in sorted list | O(n) (shift cost) |

---

# 8️⃣ Space Complexity Summary

| Data Structure | Space |
|---|---|
| List | O(n) |
| Tuple | O(n) |
| String | O(n) |
| Set | O(n) + hash overhead |
| Dict | O(n) + hash overhead |
| Linked List | O(n) + pointer overhead |
| Heap | O(n) |
| BST | O(n) |
| Graph (Adj List) | O(V + E) |
| Graph (Adj Matrix) | O(V²) |

---

# 9️⃣ When to Use What (Decision Table)

| Need | Use |
|---|---|
| Fast random access | List |
| Frequent membership checks | Set |
| Key-value lookup | Dict |
| Maintain insertion order + lookup | Dict (Python 3.7+) |
| Repeated min/max | Heap |
| FIFO queue | Deque |
| Sorted order + range queries | Balanced BST (conceptually) |