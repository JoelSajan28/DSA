# Rate Limiting Algorithms & Patterns

## 1️⃣ Fixed Window Counter

### Scenario
You run a public REST API.

Rule:

> Max **5 requests per minute per user**

Time window:

```
10:00:00 → 10:00:59
```

User behavior:

```
10:00:50 → 5 requests (allowed)
10:01:00 → counter resets
10:01:01 → 5 more requests (allowed)
```

Result:

User makes **10 requests in 11 seconds**, even though the limit is 5/minute.

### Real-world example

Basic login attempt limiting:

> "Max 5 login attempts per minute"

Cheap and simple, but allows **bursty traffic**.

---

# 2️⃣ Sliding Window Log

### Scenario

Limit: **5 requests per minute**

At **10:00:30**, user already made 5 requests between:

```
10:00:00 – 10:00:30
```

At **10:00:31**, the user sends another request.

System checks:

```
Are there 5 timestamps between 9:59:31 – 10:00:31?
```

Yes → **Reject request**

This prevents burst loopholes.

### Real-world example

Financial APIs (trading platforms)

Where **strict fairness** is required.

---

# 3️⃣ Sliding Window Counter (Hybrid)

Instead of storing every request timestamp, the system stores:

- Current window count
- Previous window count

### Example

Limit:

```
10 requests per minute
```

Current window progress:

```
30 seconds into the minute
```

User activity:

```
Previous minute: 8 requests
Current 30 sec: 6 requests
```

Effective count:

```
6 + (8 × 0.5) = 10
```

Result:

```
Reject request
```

### Why this method?

- More accurate than **Fixed Window**
- Less storage than **Sliding Window Log**

### Real-world example

Stripe-style API rate limiting.

---

# 4️⃣ Token Bucket (Most Important)

### Scenario

Bucket configuration:

```
Bucket size = 10 tokens
Refill rate = 1 token/sec
```

At **10:00**, bucket is full:

```
10 tokens
```

User sends:

```
10 requests instantly → allowed
11th request → rejected
```

After **5 seconds**:

```
5 tokens refilled
```

User can burst again.

### Why it's popular

- Allows bursts
- Enforces long-term average rate

### Real-world examples

- AWS API Gateway
- Kubernetes Ingress Controllers
- Cloudflare

---

# 5️⃣ Leaky Bucket

Think of a **bucket with a hole** leaking water at a constant rate.

Incoming traffic:

```
20 requests instantly
```

Processing rate:

```
2 requests/sec
```

System queues requests and processes them smoothly.

If queue becomes full → **drop requests**.

### Goal

Smooth out traffic spikes.

### Real-world examples

- Network routers
- Traffic shaping
- Video streaming platforms

---

# 6️⃣ Concurrency Limiting

Not time-based.

Example:

```
Max 100 concurrent database connections
```

If request **101 arrives**:

- Wait
- Queue
- Or fail

### Real-world examples

- Thread pools
- Database connection pools
- Async worker pools

Goal:

Prevent **resource exhaustion**.

---

# 7️⃣ Distributed Rate Limiting

Scenario:

You run **5 servers behind a load balancer**.

User sends **10 requests**.

Without coordination:

```
Each server allows 10
Total allowed = 50 ❌
```

### Solution

Use centralized shared state.

Common approach:

```
Redis shared counter
Atomic increment
```

### Real-world examples

- Public SaaS APIs
- Cloud APIs
- Banking systems

---

# 8️⃣ Adaptive Rate Limiting

Rate limit changes dynamically based on system health.

Example triggers:

- CPU usage > 80%
- Error rate rising
- System latency increasing

Rate adjustment:

```
1000 req/sec → 500 req/sec
```

### Real-world examples

- DDoS protection systems
- Cloud auto-scaling infrastructure

---

# 9️⃣ Client-side Rate Limiting

Instead of the server rejecting requests, the **client throttles itself**.

Example:

An SDK ensures:

```
Max 5 requests per second
```

Even if developer code loops aggressively.

### Real-world examples

- Google Maps SDK
- Twitter API SDK

Benefits:

- Reduces unnecessary server load
- Better developer experience

---

# 🔟 Hierarchical Rate Limiting

Multiple limits applied simultaneously.

Example configuration:

```
Per user: 100 requests/min
Per IP: 500 requests/min
Global system cap: 10,000 requests/min
```

### Benefit

Prevents:

- Single user exhaustion
- Single IP abuse
- Entire system overload

### Real-world examples

- Stripe
- OpenAI API
- AWS