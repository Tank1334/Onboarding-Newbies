# Day 08 - Introduction to HBase :elephant:

## Overview:
Today's session dives dipper into the world of columnar DB's. You'll explore Hadoop's implemntation - HBase.

**The focus is on gaining a deeper understanding of columnur DB's as a concept, it's implementation in Hadoop - HBase and it's purposes in the ecosystem.**

## Goals:
- Gain a foundational understanding of the columnar DB concept.
- Explore it's role in big data processing.
- Gain an understanding of HBase - How and Why?.

:warning: **Note:**
- This is a self-study day, it is important to be able to work independently and manage your time.
- A lot of newbies have a problem with self-study and time management, so breath and take your time to plan your day carefully.
- Be aware of the importance of time management. 
- Plan your time and tasks, and try to stick to your plan. If you are not able to finish the tasks in the time you have planned, you should discuss it with your mentor, maybe you learn more then you should.
- You need to understand the **full picture** of every concept, so take your time to understand it, *if you can't explain it, you don't understand it*.
- You need to be able to explain each concept and how it relates to the others and how it can be used in real-world scenarios.
- This chapter will cover the essential concepts of the Hadoop ecosystem, and you will have a Q&A session with your mentor to discuss what you have learned.
- To gain a deeper understanding of the concepts and how they are applied in real-world scenarios we'll provide you with key concepts and a brief explanation for each core concept. Your task is to delve deeper into each concept by researching them. 
- Utilize Google, YouTube, or any other reliable source to gather comprehensive information that helps you grasp each concept thoroughly. This preparation will equip you for a productive question-and-answer session with your mentor, where you'll be expected to discuss what you've learned.
- **Before you start**  take a look to the [Exercise](#excercise) and try to understand what you need to do, so you can focus on the main concepts that you need to learn. don't waste your time on the concepts and details that you don't need to know.
- If you have any questions and have conflicts if you need to learn some concept or not, you should discuss it with your mentor.

## 12. Apache HBase
- [Apache HBase](https://hbase.apache.org/)
### Core Concepts

#### 1. **Table:**
- Fundamental data storage unit in HBase, similar to a table in a relational database.

#### 2. **Row Key:**
- Unique identifier for each row in an HBase table.

#### 3. **Column Family:**
- Groups of related columns stored together for efficient retrieval.
- Defined at the table level and must be declared upfront.

#### 4. **Column Qualifier:**
- Part of a column family that further qualifies the data within it.
- Combined with the column family and row key, it forms a unique cell in the table.

#### 5. **Cell:**
- Intersection of a row, column family, and column qualifier.
- Stores the actual data along with a timestamp.

#### 6. **HFile:**
- The underlying storage format for HBase tables.
- Represents the sorted and indexed form of the data on disk.
- Stored in HDFS.

#### 7. **Region:**
- A contiguous range of rows stored together in an HBase table.
- Tables are horizontally partitioned into regions to enable parallel processing.
- The tables are partitioned by lexicography sorting and spliting the table's row keys.

#### 8. **Region Server:**
- Hosts one or more regions and manages read and write requests for those regions.
- Distributes data across regions based on the row key.

#### 9. **ZooKeeper:**
- Coordinates and manages distributed components in HBase.
- Helps in leader election, synchronization, and distributed configuration.

#### 10. **Block Cache:**
- A caching mechanism through which HBase is able to serve random reads with millisecond latency.
- When an HBase data block is read from HDFS, it is cached in the BlockCache.
- A single insatnce is maintained per region server.

#### 10. **Memstore:**
- A buffer that stores data written, in the form of key,value, in memory.
- A single instance is maintained per column family.
- When the MemStore fills up, its contents flush to disk to form an HFile. It forms a new HFile on every flush, rather than writing to an existing HFile.

#### 11. **Mob (Medium Object):**
- A storage feature in HBase for optimizing the storage of large cells (typically larger than 100KB).
- MOBs are stored separately from the normal cell data in a special MOB storage area to prevent large cells from impacting the performance of small cells.

#### 12. **WAL (Write-Ahead Log):**
- A log file where HBase records all changes to data before they are written to the actual storage.
- The WAL ensures data integrity and allows the system to recover from failures by replaying the log entries.

#### 13. **Compaction (Major and Minor):**
- A background process in HBase that reorganizes data to improve read performance and reclaim space.
   - **Minor Compaction:** Merges smaller HFiles into larger ones, reducing the number of files and improving read performance.
   - **Major Compaction:** Merges all HFiles in a region, removing deleted and expired cells. This process also rewrites data according to the latest schema, ensuring data consistency and optimal storage usage.

### **Real-World Use Cases:**

- **Real-time Big Data Access:** HBase excels in providing low-latency access to large datasets, making it suitable for real-time applications.
- **Time-Series Data:** Well-suited for scenarios involving time-series data due to its efficient storage and retrieval mechanisms.
- **Scalable and Distributed Storage:** HBase scales horizontally, making it suitable for handling massive amounts of data across a distributed environment.
Certainly! Here are the three key reasons in Markdown format:

- **Linear Scalability:** HBase is designed for horizontal scalability, allowing organizations to easily scale their clusters by adding more nodes. This ensures consistent performance as data volumes grow, making it suitable for large-scale applications.

- **Low Latency:** HBase is optimized for low-latency data access, making it a strong choice for real-time applications where quick retrieval and updates are crucial. Its architecture enables fast responses to queries, making it ideal for use cases with stringent latency requirements.

- **Integration with Hadoop Ecosystem:** HBase seamlessly integrates with other components of the Hadoop ecosystem, providing a unified platform for storing, processing, and analyzing data. This integration simplifies the development and maintenance of big data pipelines and analytics workflows.


- **Use Case:**
  - Predicting customer churn by analyzing user behavior and subscription patterns to proactively address potential cancellations.

- **Real Example:**
   - Facebook has used HBase to store real-time messages.


## Excercise

### Chapter 12: Apache HBase

31.  What is Apache HBase? Explain its architecture.
32.  What is a Column Family in HBase?
33.  How does HBase achieve its unique efficiency on big datasets?
34.  How does HBase ensure data availability and fault tolerance?
35.  What is the role of Zookeeper in an HBase environment?

## Wrapping Up :trophy:
Talk with your mentor about the concepts you have learned today and how they are applied in real-world scenarios. Discuss any questions or challenges you encountered during your self-study. Tomorrow, you will have a Q&A session with your mentor to further solidify your understanding of the Hadoop ecosystem and its components.

## Action Items
- Review the core concepts of HBase & columnar DB's as a whole.
- Explore real-world use cases for these technologies and understand their practical applications.
- Prepare questions and topics for discussion in the upcoming Q&A session with your mentor.
- Reflect the new conecpet with the Challenge from [Day 01](./day_01#ready-for-a-challenge-trophy) 
:trophy:

## Recommended Articles and Videos:
- [HBase Architecture](https://www.edureka.co/blog/hbase-architecture/) - Edureka's look into apache HBase's architecture. 
- [Apache HBase:How HBase Works](https://www.youtube.com/watch?v=lSrNUyMR_Ek)
