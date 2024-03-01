# Day 17 - Introduction to Iceberg Concepts, Terminology, and Architecture :iceberg:

## Overview
**Goals:**
- Introduce fundamental concepts, terminology, and architecture of Apache Iceberg.
- Lay the groundwork for understanding and utilizing Iceberg for efficient and scalable table management in data lakes.

:warning: **Note:**
- Understanding Iceberg's core concepts and architecture is crucial for managing large-scale tables in data lakes efficiently.

## Morning Session - Understanding Iceberg Concepts and Terminology

### Read the following chapters from the [Iceberg Documentation](https://iceberg.apache.org/documentation/)
#### Chapter 1: Introduction to Iceberg

- **Topics Covered:**
  - **What is Iceberg?:**
    - Introduction to Apache Iceberg, its features, and its role in managing tables in data lakes.
  - **Key Concepts and Terminology:**
    - Definitions of essential terms such as tables, manifests, snapshots, metadata, and schema evolution.
  - **Partitioning and Sorting:**
    - Explanation of partitioning and sorting strategies for organizing data within Iceberg tables.
  - **Schema Evolution:**
    - Understanding how Iceberg handles schema changes and evolution over time.

#### Core Concepts

##### 1. **What is Iceberg?:**
   - Understand the motivation behind Iceberg's development and its advantages over traditional table formats.
   - Explore Iceberg's features for transactional and incremental processing, schema evolution, and data retention.

##### 2. **Key Concepts and Terminology:**
   - Learn essential terms and concepts used in Iceberg, such as tables, manifests, snapshots, metadata, and schema evolution.
   - Gain familiarity with Iceberg's table structure and how it differs from traditional formats like Parquet and ORC.

##### 3. **Partitioning and Sorting:**
   - Explore different partitioning and sorting strategies supported by Iceberg for efficient data retrieval and processing.
   - Understand the benefits of partition pruning and data skipping in Iceberg tables for query performance.

## Afternoon Session - Exploring Iceberg Architecture and Best Practices

### Read the following chapters from the [Iceberg Documentation](https://iceberg.apache.org/documentation/)
#### Chapter 2: Iceberg Architecture

- **Topics Covered:**
  - **Table Structure and Layout:**
    - Overview of Iceberg's table layout, including metadata storage, data files, and manifest files.
  - **Snapshot Management:**
    - Understanding how Iceberg manages table snapshots and maintains a consistent view of table data.
  - **Metadata Store Integration:**
    - Explanation of integrating Iceberg with external metadata stores for improved scalability and reliability.
  - **Performance and Scalability Considerations:**
    - Best practices for optimizing performance and scalability when working with Iceberg tables.

#### Core Concepts

##### 1. **Table Structure and Layout:**
   - Dive deeper into Iceberg's table structure and layout, including the organization of data files and metadata.
   - Understand the role of manifest files in tracking data file additions, deletions, and modifications.

##### 2. **Snapshot Management:**
   - Explore Iceberg's snapshot isolation mechanism and how it ensures consistent table views across concurrent transactions.
   - Learn about snapshot management operations such as commit, rollback, and snapshot isolation levels.

##### 3. **Metadata Store Integration:**
   - Understand the benefits of integrating Iceberg with external metadata stores such as Apache Hive Metastore or Amazon S3.
   - Explore configuration options and best practices for setting up metadata store integration in Iceberg.

## **Wrapping Up:** :hourglass_flowing_sand:
Reflect on today's learnings with your mentor and peers. Discuss potential projects or use cases where you can leverage Iceberg for efficient table management in data lakes. Consider how Iceberg can improve scalability, reliability, and performance in your data lake architecture.

## Recommended Articles and Videos:
- [Iceberg: Table Format for Large-scale Data Lakes](https://iceberg.apache.org/) - Official website for Apache Iceberg, featuring documentation, tutorials, and best practices.
- [Introduction to Iceberg: A New Table Format for the Data Lake](https://databricks.com/blog/2020/07/22/introducing-iceberg-table-format-apache-iceberg.html) - A comprehensive blog post introducing Iceberg and its benefits for data lake management.
- [Apache Iceberg - A Table Format for Huge Analytic Datasets](https://www.youtube.com/watch?v=mf8Hb0coI6o) - A video presentation on Apache Iceberg's features and architecture for managing large-scale analytic datasets in data lakes.
- [AWS analytics Shortclip: Apache Iceberg on EMR (Hebrew)](https://www.youtube.com/watch?v=af8Okzx5NkM) - A short video clip demonstrating the use of Apache Iceberg on Amazon EMR for efficient table management in data lakes.