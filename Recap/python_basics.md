# Python Data Structures Comparison

| Type  | Ordered          | Mutable | Allows Duplicates | Hash-based | Typical Use                |
| ----- | ---------------- | ------- | ----------------- | ---------- | -------------------------- |
| list  | ✅ Yes            | ✅ Yes   | ✅ Yes             | ❌ No       | Sequence of items          |
| tuple | ✅ Yes            | ❌ No    | ✅ Yes             | ❌ No       | Fixed sequence             |
| set   | ❌ No (unordered) | ✅ Yes   | ❌ No              | ✅ Yes      | Unique items + fast lookup |
| dict  | ✅ Yes (Py 3.7+)  | ✅ Yes   | Keys unique       | ✅ Yes      | Key → value mapping        |

---

# Adding / Inserting Elements

## 1️⃣ List

```python
A = [1,2]
A.append(3)      # O(1) amortized
A.extend([4,5])  # O(k)
A + [6,7]        # O(n+k) creates new list
```

⚠️ `+` creates new list  
⚠️ `.extend()` modifies in place

---

## 2️⃣ Tuple (Immutable)

```python
T = (1,2)
T = T + (3,)   # creates new tuple O(n)
```

Cannot append in-place.

---

## 3️⃣ Set

```python
A = {1,2}
A.add(3)          # O(1)
A.update({4,5})   # O(k)
A | {6,7}         # union, returns new set
```

⚠️ No duplicates  
⚠️ No order guarantee

---

## 4️⃣ Dictionary

```python
d = {"a":1}
d["b"] = 2          # O(1)
d.update({"c":3})   # O(k)
d1 | d2             # merge (Python 3.9+)
```

⚠️ Keys must be hashable  
⚠️ Adding existing key overwrites value

---

# Updating / Merging Two Structures

## List

```python
A + B          # new list
A.extend(B)    # in-place
```

Time: `O(len(B))`

---

## Tuple

```python
T1 + T2        # new tuple
```

Always creates new object.

---

## Set

```python
A | B          # union new set
A.update(B)    # in-place union
```

Time: `O(len(A) + len(B))`

---

## Dict

```python
d1 | d2          # new dict (Python 3.9+)
d1.update(d2)    # in-place merge
```

If key overlaps → **right side wins**

---

# Membership Check

| Operation | list | tuple | set | dict |
|----------|------|------|------|------|
| `x in ?` | O(n) | O(n) | O(1) avg | O(1) avg (checks keys) |

This is the **most important performance difference**.

---

# Removal

## List

```python
A.remove(x)  # O(n)
A.pop()      # O(1)
```

---

## Set

```python
A.remove(x)   # O(1)
A.discard(x)  # safe version
```

---

## Dict

```python
del d[key]    # O(1)
d.pop(key)    # O(1)
```

---

# Index Access

| Structure | Supports Index? |
|----------|----------------|
| list | ✅ O(1) |
| tuple | ✅ O(1) |
| set | ❌ No |
| dict | ❌ No (key-based) |

---

# Hashing Behavior

| Structure | Uses Hash Table Internally? |
|----------|-----------------------------|
| list | ❌ |
| tuple | ❌ |
| set | ✅ |
| dict | ✅ |

---

# Memory Behavior

- **list → dynamic array**
- **tuple → fixed array**
- **set → hash table**
- **dict → hash table (key-value)**

---

# When to Use What

| If you need... | Use |
|---------------|-----|
| Ordered collection | list |
| Immutable sequence | tuple |
| Fast lookup + uniqueness | set |
| Key-value mapping | dict |