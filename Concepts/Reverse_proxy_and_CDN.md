# Reverse Proxy Explained

## 1️⃣ Where is a Reverse Proxy Located?

A **reverse proxy sits in front of your backend servers**.

### Request Flow

```
User (Browser / Client)
        ↓
Reverse Proxy
        ↓
Application Server(s)
        ↓
Database
```

So it sits:

> **Between the client and the server**

Important clarification:

- The **browser is the client**
- The reverse proxy is **server-side infrastructure**
- It is **not between the user and the client**

---

# 2️⃣ Can a Reverse Proxy Act as a Cache?

Yes — absolutely.

Many reverse proxies support caching.

### Examples

- **Nginx**
- **Varnish**
- **HAProxy**
- **Cloudflare** (reverse proxy + CDN)
- **AWS CloudFront** (CDN style reverse proxy)

### What Can Be Cached

- Static files
- HTML responses
- API responses
- Images
- JSON
- Anything cacheable via HTTP headers

---

# 3️⃣ Is a Reverse Proxy the Same as a CDN?

Not exactly. They are similar but operate at different scales.

## Reverse Proxy Cache

- Usually located in **one data center**
- Caches responses **near your backend**
- Primarily reduces **backend load**

Example:

```
User → Reverse Proxy (Ireland) → Backend (Ireland)
```

## CDN (Content Delivery Network)

- **Globally distributed**
- Multiple **edge locations**
- Caches content **close to users**

Example:

```
User (US) → CDN Edge (US) → Backend (Ireland)
```

### Key Difference

| Feature | Reverse Proxy | CDN |
|------|------|------|
| Location | Single data center | Global |
| Purpose | Reduce backend load | Reduce latency |
| Distribution | Local | Worldwide |

---

# 4️⃣ How Reverse Proxy Caching Works

When a user requests:

```
GET /homepage
```

The reverse proxy checks its cache.

### Cache Decision

**If cached**

```
Return response immediately
```

**If not cached**

```
Forward request to backend
Store response
Return response to client
```

### Cache Control Headers

Caching is controlled using HTTP headers:

- `Cache-Control`
- `ETag`
- `Expires`
- `TTL` settings

---

# 5️⃣ Typical Real Production Architecture

```
User
   ↓
CDN (Cloudflare / CloudFront)
   ↓
Load Balancer
   ↓
Reverse Proxy (Nginx)
   ↓
Application Servers (Kubernetes / EC2)
   ↓
Database
```

### CDN Responsibilities

- Global distribution
- DDoS protection
- TLS termination
- Edge caching

### Reverse Proxy Responsibilities

- Internal routing
- Response caching
- SSL termination
- Rate limiting
- Compression
- Request rewriting

---

# 6️⃣ Why Use Reverse Proxy Caching?

### Benefits

- Reduces backend CPU load
- Reduces database queries
- Improves response time
- Protects backend from traffic spikes
- Centralizes TLS handling

---

# 7️⃣ Important Distinction

| Proxy Type | Purpose |
|------|------|
| **Forward Proxy** | Protects clients |
| **Reverse Proxy** | Protects servers |

This distinction is where most confusion happens.

---

# 8️⃣ Final Direct Answers

### Can a reverse proxy act like a CDN?

Yes — it can cache content similarly, but it usually operates **locally** rather than globally.

### Where is it located?

> **Between the client and the server, on the server side.**

---

# Possible Next Topics

- Difference between **Load Balancer vs Reverse Proxy**
- How **Kubernetes Ingress Controllers** work
- Reverse proxy usage in **IBM Cloud / OpenShift architectures**