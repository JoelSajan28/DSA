# SOLID Principles (Software Design)

SOLID is a set of five principles that help design maintainable, scalable, and testable software.

---

# S — Single Responsibility Principle (SRP)

**Definition**

A class should have **one reason to change**.

Meaning: a class should focus on **one responsibility only**.

### Bad Example

One class doing everything:

- parsing
- validation
- database storage
- sending emails

### Good Design

Split responsibilities:

- `InvoiceCalculator` → computes totals
- `InvoiceRepository` → saves/loads invoices
- `InvoiceMailer` → sends invoice emails

### Why it matters

- Easier testing
- Fewer side effects
- Smaller blast radius when code changes

---

# O — Open/Closed Principle (OCP)

**Definition**

Software entities should be:

- **Open for extension**
- **Closed for modification**

Meaning: you should add new behavior **without editing existing stable code**.

### Bad Example

```python
def checkout(provider_name, amount):
    if provider_name == "stripe":
        ...
    elif provider_name == "adyen":
        ...
```

Every new provider requires modifying this function.

### Good Example (Strategy Pattern)

```python
def checkout(provider: PaymentProvider, amount: int):
    return provider.charge(amount)
```

Each payment provider implements its own `charge()` method.

You can add new providers without modifying checkout logic.

---

# L — Liskov Substitution Principle (LSP)

**Definition**

If `S` is a subtype of `T`, then objects of type `T` should be replaceable with objects of type `S` without breaking correctness.

### In simpler terms

Subclasses must follow the **contract of the base class**.

Rules:

- Do not strengthen input requirements
- Do not weaken output guarantees
- Do not introduce unexpected exceptions

### Classic Example

`Square` inheriting from `Rectangle`.

Setting width may change height, which violates expectations.

### Practical Violation

Base class:

```
withdraw(x) works for any x <= balance
```

Subclass:

```
withdraw only works for multiples of 10
```

Now substitution breaks.

---

# I — Interface Segregation Principle (ISP)

**Definition**

Clients should not be forced to depend on methods they do not use.

Meaning: avoid **large "fat" interfaces**.

### Bad Example

```python
class Worker(ABC):
    @abstractmethod
    def work(self): ...
    
    @abstractmethod
    def eat(self): ...
```

Robots don't eat but must implement the method.

### Good Example

Split interfaces:

```python
class Workable(ABC):
    @abstractmethod
    def work(self): ...


class Eatable(ABC):
    @abstractmethod
    def eat(self): ...
```

Now classes only implement what they need.

---

# D — Dependency Inversion Principle (DIP)

**Definition**

High-level modules should not depend on low-level modules.

Both should depend on **abstractions**.

Meaning: depend on **interfaces**, not concrete implementations.

### Bad Example

```python
class UserService:
    def __init__(self):
        self.repo = PostgresUserRepo()
```

Dependency is hard-coded.

### Good Example

```python
class UserRepo(ABC):
    @abstractmethod
    def get_user(self, user_id: int): ...


class UserService:
    def __init__(self, repo: UserRepo):
        self.repo = repo
```

Now we can inject:

- `PostgresUserRepo`
- `InMemoryUserRepo`
- `MockRepo` (for tests)

---

# Summary

| Principle | Meaning |
|---------|--------|
| **S** | Single responsibility per class |
| **O** | Extend behavior without modifying existing code |
| **L** | Subclasses must honor base class behavior |
| **I** | Prefer small, focused interfaces |
| **D** | Depend on abstractions instead of implementations |

---

# Quick Memory Trick

**S O L I D**

- **S** → Single job
- **O** → Extend, don’t edit
- **L** → Subtypes behave like base types
- **I** → Small interfaces
- **D** → Depend on abstractions