# Core LangChain Concepts for Agentic + Distributed Systems

## 1️⃣ LLM vs Chat Model

An **LLM / ChatModel** is the **brain** that produces text or tool calls.

In distributed systems, treat it as a **stateless dependency**:

- Can swap providers (OpenAI, Anthropic, IBM Granite, etc.)
- Apply rate limiting
- Retry failed calls
- Scale horizontally

---

# 2️⃣ Prompt + System Instructions

Prompts act as the **agent policy layer**.

They define:

- behavioral rules
- output format constraints
- refusal policies
- tool usage rules

### Production Tip

Use **tight tool policies**, for example:

> “Only call tool `search_docs` when question requires external knowledge.”

This prevents:

- runaway loops
- unnecessary tool calls
- exploding token costs

---

# 3️⃣ Tools (Where Real Work Happens)

Tools are how agents interact with the world.

This is where **distributed architecture begins**.

Tools can include:

- HTTP microservices  
  - Search service  
  - Jira reader  
  - GitHub reader

- Database queries
- Queue producers (publish jobs)
- Internal services  
  - policy validator  
  - permission checker

### Best Practices

Tools should be:

- **Idempotent**
- **Observable**

Always log:

- inputs
- outputs
- trace IDs

---

# 4️⃣ Agent (Reasoning Loop)

An agent follows a loop:

1. Decide what to do
2. Call tools
3. Incorporate results
4. Repeat until finished

LangChain offers helpers, but **LangGraph** is better for production systems because it gives more control over execution.

---

# 5️⃣ State vs Memory

These are often confused.

### State

Information needed **within the current run**:

- messages
- intermediate outputs
- tool results
- temporary variables

### Memory

Information persisted **across runs**:

- user profiles
- stored facts
- vector embeddings

### In distributed systems

- **State** → workflow runtime
- **Memory** → external storage

Examples:

- Redis
- Postgres
- Vector databases

---

# 6️⃣ Runnables / Chains

Runnables create **deterministic pipelines**.

Example flow:

```
Input → Prompt → Model → Parser → Output
```

Use these when:

- summarizing text
- extracting fields
- classification
- formatting structured output

Avoid agents when deterministic pipelines suffice.

---

# 7️⃣ LangGraph (Critical for Distributed Agents)

LangGraph models workflows as **state machines / graphs**.

### Components

**Nodes**

Steps in the workflow:

- LLM calls
- tool calls
- validation steps

**Edges**

Routing logic:

```
if tool_needed → tool node
else → final node
```

### Features

- supports cycles (agent loops)
- retries
- checkpoints
- failure handling

This structure maps naturally to **distributed execution**.

---

# What "Agentic Distributed System" Actually Means

A realistic architecture:

```
Orchestrator (LangGraph)
        ↓
Tool Services (microservices)
        ↓
Job Queue (optional)
        ↓
Storage Layer
        ↓
Observability
```

---

# System Components

## Orchestrator

- LangGraph
- manages workflow
- controls state

---

## Tool Services

Examples:

- search service
- ticket reader
- document parser
- policy validator

---

## Job Queue (optional)

Used for long-running work:

- document parsing
- embedding generation
- indexing

Examples:

- Celery
- Kafka
- RabbitMQ

---

## Storage Layer

Typical stack:

- **Postgres** → metadata
- **Redis** → fast cache / state
- **Vector DB** → retrieval
- **Object storage** → documents

---

## Observability

Essential for debugging:

- tracing
- logs
- metrics

Without this, agents become **impossible to debug**.

---

# Distributed System Problems You Must Handle

- retries + idempotency
- timeouts
- concurrency limits
- rate limiting
- prompt versioning
- tool versioning
- audit trails

You must track:

- what the agent did
- why it did it
- which tool was called

---

# Example: A Simple Agentic System

## Goal

Question → Agent decides whether to use search → Answer with citations.

The agent chooses between:

- answering directly
- calling a tool first

---

# Minimal Design

## State

```
question
messages
tool_result
```

---

## Nodes

### Decide

LLM decides:

```
{
 "action": "search" | "final",
 "query": "..."
}
```

---

### Search Tool

Calls a search microservice.

Returns:

```
top_results
```

---

### Final

LLM generates answer using tool results.

---

# Graph Structure

```
decide → search_tool → final
decide → final
```

---

# Conceptual Pseudocode

```
decide(question):
  if question needs external knowledge:
      return action = search
  else:
      return action = final

search_tool(query):
  return results

final(question, tool_result):
  generate answer
```

This is the **simplest real agent system**.

---

# How This Becomes Distributed

## Step 1: Split Tools into Services

Examples:

- search-service
- document-service
- code-execution-service

Agents call them via HTTP.

---

## Step 2: Add a Queue for Long Jobs

For example:

- document indexing
- embedding generation

Agent workflow:

```
enqueue job → poll status tool
```

---

## Step 3: Add Guardrails

Examples:

- tool allowlist
- max tool calls per run
- token budget limits
- strict JSON parsers

---

## Step 4: Add Validator Agents

A second LLM checks:

- completeness
- hallucinations
- policy violations

---

# Example Distributed Agent Architecture

A practical design might include:

### Router Agent

Classifies requests:

- solution generator
- validator
- RFI processor

---

### Tool Agents

Examples:

- Issue Reader
- Document Parser
- COS Fetcher

---

### Validator Node

Applies:

- rule checks
- LLM critique

---

### Persistence

- Postgres
- Cloud Object Storage

---

### Observability

All tool calls include:

- trace IDs
- request IDs
- logs
```