# Runnables in LangChain

## Why Runnables?

When the LangChain team started helping developers build LLM-based applications, they introduced core components such as:

- LLMs
- Prompts
- Output parsers

These components were powerful, but they were not designed to seamlessly communicate with each other.

---

## The Era of Chains

As AI became popular, the LangChain team reviewed many AI repositories and identified common patterns.
To simplify development, they introduced **Chains** to combine multiple steps in LLM-based applications.

Over time:

- Many different chains were created for different use cases
- The codebase became large and heavy
- It became hard for AI engineers to identify the right chain for their use case
- Customization and composability became difficult

---

## The Problem

- Too many predefined chains
- Complex and bulky abstractions
- Difficult to reuse small pieces of logic
- Hard to reason about what each chain actually does

---

## The Solution: Runnables

To solve these problems, LangChain introduced **Runnables**.

---

## What is a Runnable?

A **Runnable** is a **unit of work**.

Each runnable has:

- Input
- Processing logic
- Output

Think of it as a small, focused building block that does one dedicated job.

---

## Common Interface

All runnables share a common interface:

```
invoke(input) → output
```

Because every runnable follows the same interface, they can be easily connected together.

---

## Composing Runnables

You can connect multiple runnables like this:

```
[R1] → [R2] → [R3]
```

Each runnable:

- Takes input
- Processes it
- Passes output to the next runnable

---

## Runnable Workflows are Also Runnables

A powerful concept in LangChain:

When you connect multiple runnables to form a workflow, the entire workflow itself becomes a runnable.

This means:

- You can reuse workflows
- You can nest workflows
- You can connect workflows to other workflows

```
[Workflow A] → [Workflow B] → [Workflow C]
```

---

## Key Benefits of Runnables

- Lightweight and modular
- Easy to compose
- Easy to reason about
- Highly reusable
- Avoids large, monolithic chains

---

## In Simple Terms

```
Chains     = Heavy, predefined solutions
Runnables  = Flexible, Lego-like building blocks
```

---

## Summary

Runnables provide a clean, composable, and scalable abstraction for building LLM-powered applications.
They replace rigid, monolithic chains with flexible building blocks, giving developers full control over their workflows.
