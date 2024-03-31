# Day 20 - Introduction to Trino Concepts, Terminology, and Architecture :bar_chart:

## Overview
**Goals:**
- Introduce fundamental concepts, terminology, and architecture of Trino (formerly known as PrestoSQL).
- Lay the groundwork for understanding and utilizing Trino for distributed query processing and analytics.

:warning: **Note:**
- Understanding Trino's core concepts and architecture is essential for effectively querying and analyzing distributed data sources.

## Morning Session - Understanding Trino Concepts and Terminology

### Read the following chapters from the [Trino Documentation](https://trino.io/docs/current/index.html)
#### Chapter 1: Introduction to Trino

- **Topics Covered:**
  - **What is Trino?:**
    - Introduction to the Trino (formerly PrestoSQL) project, its history, and its role in the data ecosystem.
  - **Key Concepts and Terminology:**
    - Definitions of essential terms such as catalogs, connectors, sessions, transactions, and query stages.
  - **Core Components:**
    - Explanation of the key components in Trino's architecture, including the Coordinator, Worker, and Connector plugins.
  - **Architecture Overview:**
    - High-level overview of Trino's distributed architecture and its components' responsibilities.
  - **Query Execution:**
    - Understanding the lifecycle of a query in Trino, from parsing and planning to execution and result retrieval.

#### Core Concepts

##### 1. **What is Trino?:**
   - Understand the history and evolution of Trino (formerly PrestoSQL) and its role in distributed query processing.
   - Explore Trino's features and capabilities for interactive querying and analytics.

##### 2. **Key Concepts and Terminology:**
   - Learn essential terms and concepts used in Trino, including catalogs, connectors, sessions, and transactions.
   - Gain familiarity with Trino's query lifecycle and execution model.

##### 3. **Core Components:**
   - Explore the components that make up Trino's architecture, including the Coordinator, Worker, and Connector plugins.
   - Understand the responsibilities of each component in query planning, execution, and data retrieval.

## Afternoon Session - Exploring Trino Architecture and Optimization

### Read the following chapters from the [Trino Documentation](https://trino.io/docs/current/index.html)
#### Chapter 2: Trino Architecture

- **Topics Covered:**
  - **High-Level Architecture:**
    - Detailed overview of Trino's distributed architecture, including the roles of Coordinator and Worker nodes.
  - **Communication Protocols:**
    - Understanding communication protocols such as HTTP and Thrift used for inter-node communication and data transfer.
  - **Query Planning and Optimization:**
    - Explanation of Trino's query planning and optimization process, including predicate pushdown and cost-based optimization.
  - **Fault Tolerance:**
    - Overview of fault tolerance mechanisms in Trino to handle node failures and ensure query reliability.

#### Core Concepts

##### 1. **High-Level Architecture:**
   - Gain insights into the overall architecture of Trino, including its distributed nature and component interactions.
   - Understand how Trino's architecture enables scalable and efficient query processing across distributed data sources.

##### 2. **Communication Protocols:**
   - Learn about communication protocols used in Trino for inter-node communication and data transfer.
   - Explore techniques for optimizing network communication to enhance query performance.

##### 3. **Query Planning and Optimization:**
   - Understand how Trino plans and optimizes queries for efficient execution across distributed data sources.
   - Explore query optimization techniques such as predicate pushdown, join reordering, and cost-based optimization.

### Questions: ❓
* What is Apache Trino and what problem does it solve?
* Can you explain how Trino executes queries across different data sources without moving data? (Hint: read about the concept of "Query pushdown")
* What are the key features of Trino? what it does better than Spark, Hive and Impala?
* How does Trino achieve high performance and efficiency in query processing?
* Can you describe a use case where Trino would be particularly beneficial?
* What is the role of a catalog in Trino?
* How does Trino handle data types from different data sources?
* What is the difference between Trino and DB?

## **Wrapping Up:** :hourglass_flowing_sand:
Reflect on today's learnings with your mentor and peers. Discuss potential projects or use cases where you can apply Trino for distributed query processing and analytics. Consider how Trino can enhance your data analysis capabilities and streamline your data workflows.

## Recommended Articles and Videos:
- [Trino (PrestoSQL) Documentation](https://trino.io/docs/current/index.html) - Official documentation to explore Trino's features, architecture, and best practices.
- [Trino: The Definitive Guide](https://www.oreilly.com/library/view/trino-the-definitive/9781098103893/) - A comprehensive guide to mastering Trino for distributed query processing and analytics.
- [Trino: An Origin Story](https://www.youtube.com/watch?v=_VUQ-Jh-M68) - A video tutorial on Trino's capabilities and use cases for interactive querying at scale.
