# Day 04 - Hadoop Distributed File System (HDFS) :elephant:

## Overview:
Today's session is all about getting to know the Hadoop Distributed File System (HDFS) and understanding it's place within the Hadoop ecosystem.

**The focus is on gaining a deeper understanding at HDFS - the base of the Hadoop ecosystem.**

## Goals:
- Gain a foundational understanding of HDFS.
- Explore it's role in the Hadoop ecosystem.
- Continue working on your time estimation and planning.

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

## 5. Hadoop Distributed File System (HDFS) :star:
- [Hadoop Distributed File System (HDFS)](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html)

Hadoop Distributed File System (HDFS) is a foundational component of the Hadoop ecosystem, designed to store and manage large volumes of data across a distributed cluster.

### Core Concepts

#### 1. NameNode and DataNode
- **NameNode:**
  - Centralized metadata repository managing file system namespace and hierarchy.
  - Keeps track of file metadata and the location of data blocks.
- **DataNode:**
  - Stores and manages the actual data blocks.
  - Communicates with the NameNode to report block information and perform block-related operations.

#### 2. Block Storage
- HDFS divides files into fixed-size blocks (default 128 MB or 256 MB).
- Each block is stored redundantly across multiple DataNodes for fault tolerance.
- Redundant storage ensures data availability even in the case of node failures.

#### 3. Replication
- HDFS replicates data blocks to multiple DataNodes to ensure data durability and fault tolerance.
- The default replication factor is three, but it can be configured based on specific requirements.

#### 4. Rack Awareness
- HDFS is rack-aware, meaning it considers the physical network topology.
- Replication is done across racks to enhance fault tolerance and reduce network congestion.

#### 5. High Availability (HA)
- HDFS supports High Availability configurations for the NameNode.
- In HA mode, two NameNodes (Active and Standby) work in coordination to ensure continuous operation in the event of a NameNode failure.

#### 6. Data Integrity
- HDFS ensures data integrity through checksums.
- Checksums are calculated for data blocks, and any corruption is detected during read operations.

#### 7. HDFS Federation
- HDFS Federation allows multiple independent HDFS namespaces to share a common cluster.
- Enhances scalability by distributing namespace and storage across multiple NameNodes.

#### 8. Snapshots
- HDFS supports snapshots for creating point-in-time copies of a directory or the entire file system.
- Useful for data recovery, testing, and backup purposes.

#### 9. JournalNode
  - In HDFS High Availability (HA) configurations, JournalNodes are integral for synchronizing the file system metadata between Active and Standby NameNodes. They maintain a shared edit log, ensuring that any changes made by the Active NameNode are quickly replicated to the Standby NameNode.
  - The Active NameNode records each metadata change to multiple JournalNodes (forming a quorum) for fault tolerance. This approach ensures that the Standby NameNode can seamlessly transition to an Active role if needed, providing robustness against failures.
  - The deployment of JournalNodes is crucial and should be strategically planned to ensure network reliability and reduce the risk of simultaneous failures, thus maintaining the high availability and integrity of the HDFS namespace.

  #### 10. NameService
  - The NameService in HDFS is a logical grouping of NameNodes in a federated setup. It facilitates the use of multiple NameNodes in the cluster, each managing a distinct namespace volume.
  - Each NameService is configured with one or more NameNodes for redundancy and high availability, ensuring the file system's resilience and reliability.

#### 11. Block Report
  - Block Reports are periodic messages sent by DataNodes to the NameNode. These reports contain a list of all blocks on a DataNode, allowing the NameNode to keep its block mapping up-to-date.
  - Block Reports are crucial for maintaining the integrity of the file system, enabling the NameNode to identify missing blocks and initiate necessary replication to maintain the desired level of redundancy.

#### 12. RPC Requests
  - Remote Procedure Call (RPC) requests in HDFS are used for communication between the NameNode, DataNodes, and clients. They facilitate operations like opening files, creating directories, renaming files, and replicating or deleting blocks.
  - RPC ensures a standardized method of communication across the distributed components of HDFS, providing a seamless operational experience and ensuring the efficiency and reliability of the file system's operations.
  

### Real-World Examples:

#### 1. **Big Data Analytics in Financial Services:**
   - *Use Case:* A financial institution leverages HDFS for storing and managing vast datasets used in big data analytics. The distributed nature of HDFS allows the institution to scale its data storage and processing capabilities to gain insights into market trends, customer behavior, and risk assessment.

#### 2. **Log Storage and Analysis in Cybersecurity:**
   - *Use Case:* A cybersecurity firm utilizes HDFS to store and analyze large volumes of log data generated by various security tools. HDFS's fault-tolerant design ensures that log data is resilient to node failures, and the distributed nature facilitates parallel processing for real-time threat detection and response.

#### 3. **Genomic Data Storage in Healthcare Research:**
   - *Use Case:* In healthcare research, HDFS serves as the storage foundation for large-scale genomic datasets. The ability of HDFS to manage and replicate data across nodes ensures the integrity and availability of genomic data for analysis and research in fields like precision medicine.

#### 4. **Media and Entertainment Content Distribution:**
   - *Use Case:* A media company employs HDFS for the storage and distribution of multimedia content. The distributed nature of HDFS allows efficient storage and retrieval of large video and audio files, supporting content delivery networks and optimizing the streaming experience for end-users.

#### 5. **IoT Data Management for Smart Cities:**
   - *Use Case:* In smart city initiatives, HDFS is used for storing and processing data generated by IoT devices, sensors, and connected infrastructure. The scalability and fault tolerance of HDFS accommodate the diverse and massive data streams, enabling data-driven decision-making for urban planning and management.

These real-world examples illustrate the versatility and applicability of Hadoop Distributed File System (HDFS) across diverse industries and use cases.

## Excercise

### Chapter 5: Hadoop Distributed File System (HDFS)

21.  What is HDFS? Explain its architecture.
22.  What is the role of the NameNode in HDFS?
23.  What is the optimal HDFS files size? how does having multiple small files hurt the HDFS?
24.  How does HDFS achieve fault tolerance?
25.  Explain rack awareness in HDFS, and name it's advantages.

## Wrapping Up :trophy:
Talk with your mentor about the concepts you have learned today and how they are applied in real-world scenarios. Discuss any questions or challenges you encountered during your self-study. Tomorrow, you will have a Q&A session with your mentor to further solidify your understanding of the Hadoop ecosystem and its components.

## Action Items
- Review your understanding of HDFS.
- Explore real-world use cases for these technologies and understand their practical applications.
- Prepare questions and topics for discussion in the upcoming Q&A session with your mentor.
- Reflect the new conecpet with the Challenge from [Day 01](./day_01#ready-for-a-challenge-trophy) 
:trophy:

## Recommended Articles and Videos:
- [Hadoop Core Components](https://www.youtube.com/watch?v=d2xeNpfzsYI) - This video offers a detailed explanation of the core components of Hadoop, including HDFS, MapReduce, and YARN, and their significance in distributed data processing.
- [Hadoop Tutorial YouTube Playlist](https://youtube.com/playlist?list=PLkz1SCf5iB4dw3jbRo0SYCk2urRESUA3v) - A playlist featuring tutorials on Hadoop, covering a variety of topics.
- [Hadoop Ecosystem Components Explained](https://data-flair.training/blogs/hadoop-ecosystem-components/) - An article detailing the components that make up the Hadoop ecosystem.
- [Comprehensive Guide to the Hadoop Ecosystem](https://www.edureka.co/blog/hadoop-ecosystem/amp/#amp_tf=From%20%251%24s&aoh=16655728574406&referrer=https%3A%2F%2Fwww.google.com) - Edureka's in-depth guide on the Hadoop ecosystem, its components, and functionalities.