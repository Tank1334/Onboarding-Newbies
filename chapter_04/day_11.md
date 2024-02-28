# Day 11 - Basic Spark Topics :sparkles:

## Overview:
Today, you'll dive into advanced topics in Apache Spark to enhance your understanding and capabilities in big data processing. You'll explore advanced RDD operations, lazy evaluation, passing functions to Spark, accumulators, broadcast variables, and working on a per-partition basis. These topics are essential for building high-performance Spark applications and optimizing your data processing workflows.

## Goals:
- Explore advanced topics in Apache Spark to enhance your understanding and capabilities in big data processing.
- Dive deeper into Spark's core concepts and features.

:warning: **Note:**
- Advanced topics in Spark will help you optimize your Spark applications and gain a deeper insight into its inner workings.
- These topics are essential for building high-performance Spark applications.

## 3. Programming with RDDs
Read the following chapters from the [Spark Book](https://github.com/hemant-rout/BigData/blob/master/Learning%20Spark%20%20Lightning-Fast%20Big%20Data%20Analysis%20.pdf)

- **Topics Covered:**
  - RDD Basics page
  - Creating RDDs 
  - RDD Operations 
  - Transformations 
  - Actions 
  - Lazy Evaluation 
  - Passing Functions to Spark
  - Python, Scala, Java 

### 1. Spark Core Concepts

#### 1. **Advanced RDD Operations:**
   - Dive deeper into RDD operations and explore advanced techniques for manipulating data with RDDs.
   - Pay attention to performance optimizations, including the use of `mapPartitions()` and `aggregate()` for efficiency.

#### 2. **Lazy Evaluation in Depth:**
   - Gain an in-depth understanding of Spark's lazy evaluation mechanism and how it impacts application performance and resource management.
   - Learn to utilize lazy evaluation effectively for improved computation.

#### 3. **Passing Functions to Spark:**
   - Explore advanced techniques for passing functions to Spark, including custom functions and lambdas.
   - Pay attention to function serialization and best practices to avoid serialization issues.

### 2. Advanced Spark Programming

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

## **Discussion and Q&A:**
  - Engage in a discussion with mentors and peers to share insights and experiences related to advanced Spark topics.
  - Ask questions and seek clarification on any challenging concepts.
   - Discuss real-world applications and implications of advanced Spark programming in big data processing workflows.

## **Wrapping Up:** :hourglass_flowing_sand:
Discuss with your mentor about the day's learnings and explore potential project applications. Reflect on the significance of advanced Spark topics and how you can apply these concepts in your big data processing endeavors.

## **Action Items:**
- Identify areas for deeper exploration.
- Get recommendations on resources for further learning.
- Reflect on how you can integrate advanced Spark concepts into your current or future projects.

## **Recommended Articles and Videos:** :bulb:
- [Spark Memory Management](https://community.cloudera.com/t5/Community-Articles/Spark-Memory-Management/ta-p/317794#:~:text=Spark%20Memory%20is%20the%20memory,storage%20memory%20of%20this%20segment.) - A comprehensive guide to Spark memory management and optimization strategies.
- [Spark Perforence Boosting](https://towardsdatascience.com/apache-spark-performance-boosting-e072a3ec1179) - A guide to boosting performance in Apache Spark applications.
- [Best practices for caching in Spark SQL](https://towardsdatascience.com/best-practices-for-caching-in-spark-sql-b22fb0f02d34?_branch_match_id=1291428628002391767&_branch_referrer=H4sIAAAAAAAAA8soKSkottLXz8nMy9bLTU3JLM3VS87P1Q9LK7cILisqMypNAgBOSaAeIwAAAA%3D%3D) - A comprehensive guide to caching best practices in Spark SQL.
- [Spark Joins Tuning Part-1(Sort-Merge vs Broadcast)](https://medium.com/swlh/spark-joins-tuning-part-1-sort-merge-vs-broadcast-a98d82610cf0) - A detailed explanation of Spark join tuning techniques, including sort-merge and broadcast joins.
- [4 Tips To Write Scalable Apache Spark Code](https://pub.towardsai.net/4-tips-to-write-scalable-apache-spark-code-1c736e4d698e) - A guide to writing scalable Apache Spark code for efficient data processing.
- [Apache Spark Optimization Techniques and Tuning - Almog Gelber (Hebrew)](https://www.youtube.com/watch?v=BzVrPCIeXuY) - A video tutorial on Spark optimization techniques and tuning.
- [Apache Spark Optimization Techniques and Tuning](https://link.medium.com/ssMBzZ2u2ub) - A comprehensive guide to optimizing Spark applications for performance and efficiency.
- [Spark partitioning: the fine print](https://link.medium.com/N5FLo0Xu2ub) - A detailed explanation of Spark partitioning and its impact on application performance.
- [OPTIMIZATION IN SPARK : Data frame focused](https://link.medium.com/qU8KaZPu2ub) - A guide to optimizing Spark DataFrames for improved performance.
- [Spark partitioning: full control](https://link.medium.com/c6HaLDKu2ub) - A comprehensive tutorial on achieving full control over Spark partitioning for optimized data processing.
- [Apache Spark Memory Management](https://link.medium.com/Kp7ANdJu2ub) - An in-depth exploration of Spark's memory management and optimization strategies.
- [Understanding Apache Spark Shuffle](https://link.medium.com/bt6yuLHu2ub) - A detailed explanation of Spark's shuffle mechanism and its impact on application performance.
- [Spark Performance Tuning: Skewness Part 1](https://link.medium.com/75bcHwFu2ub) - A comprehensive guide to handling skewness in Spark applications for improved performance.
- [Understanding Apache Spark Hash-Shuffle](https://link.medium.com/Cbmrk0Du2ub) - A detailed explanation of Spark's hash shuffle mechanism and its impact on application performance.
- [Spark Performance Tuning: Skewness Part 2](https://link.medium.com/MJdZjhzu2ub) - A continuation of the guide to handling skewness in Spark applications for improved performance.
- [Apache Spark Core—Deep Dive—Proper Optimization Daniel Tomes Databricks](https://youtu.be/daXEp4HmS-E) - A deep dive into optimizing Apache Spark Core for performance and efficiency.
- [Deep Dive: Apache Spark Memory Management](https://youtu.be/dPHrykZL8Cg) - A comprehensive video tutorial on Apache Spark memory management and optimization.
- [Understanding Query Plans and Spark UIs - Xiao Li Databricks](https://youtu.be/YgQgJceojJY) - A detailed explanation of query plans and Spark UIs for performance optimization.
- [Optimizing Apache Spark SQL Joins: Spark Summit East talk by Vida Ha](https://youtu.be/fp53QhSfQcI) - A talk on optimizing Apache Spark SQL joins for improved performance.
- [Should I repartition? About Data Distribution in Spark SQL.](https://link.medium.com/eUomzhK0Pub) - A comprehensive guide to understanding data distribution in Spark SQL and its impact on performance.
- [Spark study notes: core concepts visualized](https://link.medium.com/B1S6b3I0Pub) - Visualized study notes on core concepts of Apache Spark.
- [Part 3: Cost Efficient Executor Configuration for Apache Spark](https://link.medium.com/KFlwhEH0Pub) - A guide to cost-efficient executor configuration for Apache Spark applications.
- [Spark OOM Error — Closeup](https://link.medium.com/LLX1pap0Pub) - A detailed explanation of Spark's Out of Memory (OOM) error and strategies to address it.
- [3 Reasons Why Spark’s Lazy Evaluation is Useful](https://link.medium.com/faI3jfc0Pub) - An exploration of the benefits of Spark's lazy evaluation mechanism.
- [Apache Hadoop YARN Concepts and Applications](https://blog.cloudera.com/apache-hadoop-yarn-concepts-and-applications/) - Cloudera's comprehensive guide on the concepts and applications of Apache Hadoop YARN.
- [Oozie Share Lib Installation Guide](https://oozie.apache.org/docs/5.0.0-beta1/AG_Install.html#Oozie_Share_Lib) - Detailed documentation on installing and understanding Oozie's Share Lib.
- [YARN Capacity Scheduler and Node Labels Part 1](https://www.davidmcginnis.net/post/yarn-capacity-scheduler-and-node-labels-part-1) - First part of a detailed discussion on the options available in YARN's capacity scheduler.
- [YARN Capacity Scheduler Overview](https://blog.cloudera.com/yarn-capacity-scheduler/) - An overview of YARN's capacity scheduler provided by Cloudera.
- [Untangling Apache Hadoop YARN Part 1: Cluster and YARN Basics](https://blog.cloudera.com/untangling-apache-hadoop-yarn-part-1-cluster-and-yarn-basics/) - The first part in a series aimed at explaining the basics of clusters and YARN.
- [Hadoop Tutorial YouTube Playlist](https://youtube.com/playlist?list=PLkz1SCf5iB4dw3jbRo0SYCk2urRESUA3v) - A playlist featuring tutorials on Hadoop, covering a variety of topics.
- [Introduction to the Hadoop Ecosystem](https://www.analyticsvidhya.com/blog/2020/10/introduction-hadoop-ecosystem/) - An introductory article on the components and functionalities of the Hadoop ecosystem.
- [Understanding the Hadoop Ecosystem](https://www.databricks.com/glossary/hadoop-ecosystem) - A glossary entry by Databricks offering insights into the Hadoop ecosystem.
- [What is Hadoop? Simplilearn Tutorial](https://www.simplilearn.com/tutorials/hadoop-tutorial/what-is-hadoop) - A tutorial providing a foundational understanding of Hadoop.
- [Hadoop Ecosystem Components Explained](https://data-flair.training/blogs/hadoop-ecosystem-components/) - An article detailing the components that make up the Hadoop ecosystem.
- [Comprehensive Guide to the Hadoop Ecosystem](https://www.edureka.co/blog/hadoop-ecosystem/amp/#amp_tf=From%20%251%24s&aoh=16655728574406&referrer=https%3A%2F%2Fwww.google.com) - Edureka's in-depth guide on the Hadoop ecosystem, its components, and functionalities.

**Congratulations on completing Day 11! You've delved into advanced Spark topics, which are crucial for optimizing and fine-tuning your Spark applications. Keep exploring and applying these concepts to excel in big data processing with Spark.**
