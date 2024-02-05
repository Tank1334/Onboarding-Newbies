# Day 11 - Basic Spark Topics :sparkles:

## Overview
**Goals:**
- Explore advanced topics in Apache Spark to enhance your understanding and capabilities in big data processing.
- Dive deeper into Spark's core concepts and features.

:warning: **Note:**
- Advanced topics in Spark will help you optimize your Spark applications and gain a deeper insight into its inner workings.
- These topics are essential for building high-performance Spark applications.

## Read the following chapters from the [Spark Book](https://github.com/hemant-rout/BigData/blob/master/Learning%20Spark%20%20Lightning-Fast%20Big%20Data%20Analysis%20.pdf)
### Chapter 3: Programming with RDDs

- **Topics Covered:**
  - RDD Basics page
  - Creating RDDs 
  - RDD Operations 
  - Transformations 
  - Actions 
  - Lazy Evaluation 
  - Passing Functions to Spark
  - Python, Scala, Java 

#### Core Concepts

##### 1. **Advanced RDD Operations:**
   - Dive deeper into RDD operations and explore advanced techniques for manipulating data with RDDs.
   - Pay attention to performance optimizations, including the use of `mapPartitions()` and `aggregate()` for efficiency.

##### 2. **Lazy Evaluation in Depth:**
   - Gain an in-depth understanding of Spark's lazy evaluation mechanism and how it impacts application performance and resource management.
   - Learn to utilize lazy evaluation effectively for improved computation.

##### 3. **Passing Functions to Spark:**
   - Explore advanced techniques for passing functions to Spark, including custom functions and lambdas.
   - Pay attention to function serialization and best practices to avoid serialization issues.

### Chapter 6: Advanced Spark Programming

- **Topics Covered:**
  - Accumulators 
  - Broadcast Variables 
  - Working on a Per-Partition Basis 

#### Core Concepts

##### 1. **Accumulators:**
   - Learn advanced uses of accumulators in Spark for distributed counters and aggregations.
   - Pay attention to thread safety when using accumulators in multi-stage Spark applications.

##### 2. **Broadcast Variables:**
   - Explore advanced optimizations using broadcast variables to efficiently share read-only data across Spark nodes.
   - Understand scenarios where broadcast variables can significantly improve performance, especially in joins and lookups.

### Wrapping Up the Day

- **Discussion and Q&A (1 hour):**
  - Engage in a discussion with mentors and peers to share insights and experiences related to advanced Spark topics.
  - Ask questions and seek clarification on any challenging concepts.

**Congratulations on completing Day 11! You've delved into advanced Spark topics, which are crucial for optimizing and fine-tuning your Spark applications. Keep exploring and applying these concepts to excel in big data processing with Spark.**
