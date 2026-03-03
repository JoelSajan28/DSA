"""
Python: Mutable vs Immutable — Summary Notes
1️⃣ Core Rule

Everything in Python is an object

Variables store references to objects

Assignment does NOT copy objects

Mutation changes the object

Reassignment changes the reference

2️⃣ Immutable Types

Immutable = cannot change after creation

When modified, Python creates a new object.

Common Immutable Types

int

float

bool

str

tuple

frozenset

Example
a = 5
b = a
a = 10

5 object unchanged

a now points to new object 10

b still points to 5

Key Property

Safe to share between variables

No side effects

Hashable (usually) → can be dictionary keys

3️⃣ Mutable Types

Mutable = can change in place

Common Mutable Types

list

dict

set

most class instances

Example
A = [1, 2, 3]
B = A
A.append(4)

Both A and B now reference [1,2,3,4].

Key Property

Changes affect all references

Not hashable (cannot be dictionary keys)

4️⃣ Assignment Behavior
x = something

This:

Does NOT copy

Just binds name to object

5️⃣ Copying
Shallow Copy
new_list = old_list.copy()

Copies outer container only.

Deep Copy
import copy
new_list = copy.deepcopy(old_list)

Copies everything recursively.

6️⃣ Quick Comparison Table
Feature	Immutable	Mutable
Can change in place?	❌ No	✅ Yes
New object on change?	✅ Yes	❌ No
Safe to share?	✅ Yes	⚠️ Careful
Hashable?	Usually yes	No
Examples	int, str, tuple	list, dict, set
7️⃣ Mental Model

Immutable → Frozen object

Mutable → Editable object

Variable → Label pointing to object

8️⃣ Interview Insight

Most bugs in Python happen because:

People assume assignment copies mutable objects

People forget lists/dicts are shared references
"""