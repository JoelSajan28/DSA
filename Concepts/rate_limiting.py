"""
1️⃣ Fixed Window Counter
Scenario

You run a public REST API.

Rule:

Max 5 requests per minute per user

Time window:
10:00:00 → 10:00:59

User makes:

10:00:50 → 5 requests (allowed)
10:01:00 → counter resets
10:01:01 → 5 more requests (allowed)

They just made 10 requests in 11 seconds, even though limit is 5/minute.

Real-world example

Basic login attempt limiting:

“Max 5 login attempts per minute”

Cheap, simple, but bursty.

2️⃣ Sliding Window Log
Scenario

Limit: 5 requests per minute.

At 10:00:30, user has made 5 requests between 10:00:00–10:00:30.

At 10:00:31 → user sends another request.

System checks:

Are there 5 timestamps between 9:59:31–10:00:31?
Yes → reject.

Now no burst loophole.

Real-world example

Financial APIs (trading platforms)
Where strict fairness matters.

3️⃣ Sliding Window Counter (Hybrid)

Instead of storing every timestamp, system keeps:

Current window count

Previous window count

Example:

Limit: 10 per minute
Current window progress: 30 seconds in.

User made:

8 requests in previous minute

6 in current 30 seconds

Effective count =

6 + (8 × 0.5) = 10

Reject.

More accurate than fixed window, less heavy than full log.

Real-world example

Stripe-style API rate limiting.

4️⃣ Token Bucket (Most Important One)
Scenario

Bucket size = 10 tokens
Refill rate = 1 token/sec

At 10:00 → bucket full (10)

User sends:

10 requests instantly → allowed
11th request → rejected

After 5 seconds:

5 tokens refilled

User can burst again.

Real-world example

AWS API Gateway
Kubernetes ingress controllers
Cloudflare

Why? Because:

Allows bursts

Enforces long-term average rate

5️⃣ Leaky Bucket

Think of water dripping from a hole.

Incoming:

20 requests instantly

Processing rate:

2 requests/sec

System queues them and processes smoothly.

If queue fills → drop.

Real-world example

Network routers
Traffic shaping
Video streaming platforms

Goal: smooth traffic.

6️⃣ Concurrency Limiting

Not time-based.

Example:

Max 100 concurrent database connections.

If 101st request comes → wait or fail.

Real-world example

Thread pools
Database connection pools
Async worker pools

Prevents resource exhaustion.

7️⃣ Distributed Rate Limiting

Now imagine:
You run 5 servers behind a load balancer.

User sends 10 requests.

Without coordination:
Each server might allow 10 → total 50 allowed.

Wrong.

So you use:

Redis shared counter

Atomic increment

Real-world example

Public SaaS APIs
Cloud APIs
Banking systems

8️⃣ Adaptive Rate Limiting

Limit changes dynamically.

If:

CPU > 80%

Error rate rising

Then reduce rate from:

1000 req/sec → 500 req/sec
Real-world example

DDoS protection
Cloud auto-scaling systems

9️⃣ Client-side Rate Limiting

Instead of server rejecting, client self-throttles.

Example:
You write an SDK that ensures:

Max 5 requests per second

Even if developer writes bad loop.

Real-world example

Google Maps SDK
Twitter API SDK

10️⃣ Hierarchical Rate Limiting

Multiple layers:

Per user: 100/min

Per IP: 500/min

Global system cap: 10,000/min

Example:
One user can’t exhaust entire system.

Real-world example

Stripe
OpenAI API
AWS
"""