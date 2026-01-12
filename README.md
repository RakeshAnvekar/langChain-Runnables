
# Runnables in LangChain

## Why Runnables?

When the LangChain team started helping developers build LLM-based applications, they introduced core components such as:
- LLMs
- Prompts
- Output parsers

These components were powerful, but they were not designed to seamlessly communicate with each other.

---

## The Era of Chains

As AI adoption increased, LangChain introduced Chains to combine multiple steps.
Over time, chains became heavy, hard to customize, and difficult to reason about.

---

## The Solution: Runnables

Runnables are lightweight, composable building blocks.

A Runnable is a unit of work with:
- Input
- Processing logic
- Output

All runnables follow a common interface:
invoke(input) → output

---

## Types of Runnables in LangChain

### 1. Task-Specific Runnables

These are core LangChain components converted into runnables.

Examples:
- ChatOpenAI
- PromptTemplate
- Retriever
- Output Parsers

They focus on WHAT task is performed.

---

### 2. Runnable Primitives

These are used to connect and control task-specific runnables.
They focus on HOW tasks are executed.

#### RunnableSequence
Executes runnables sequentially.
[R1] → [R2]

#### RunnableParallel
Executes multiple runnables in parallel and returns a dictionary of outputs.

#### RunnablePassthrough
Returns input as output without modification.

#### RunnableLambda
Allows custom Python logic inside the pipeline.

#### RunnableBranch
Routes input conditionally to different chains.

---

## Summary

Chains are heavy and predefined.
Runnables are flexible, modular, and composable.
