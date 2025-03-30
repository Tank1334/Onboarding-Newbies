# Day 03 - Introduction to Data concept & Hadoop Ecosystem :elephant:

## Overview:
Today's session is all about getting to know the Hadoop ecosystem and understanding a few concepts before we dive further in. You'll explore the foundational concepts of Hadoop, and a few base components needed for it's understanding such as Zookeeper, Kafka and Kerberos.

**The focus is on gaining a high-level understanding of the Hadoop ecosystem and its role in big data processing & storing.**

## Goals:
- Gain a foundational understanding of the Hadoop ecosystem.
- Explore it's role in big data processing.
- Make connections between the Hadoop ecosystem and real-world use cases.
- Understand core concepts and components to allow further dive in the ecosystem.
- Start to work with time estimation and planning.

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

## 1 .Introduction to Big Data and Hadoop
- [Apache Hadoop](https://hadoop.apache.org/) 

Apache Hadoop is a robust framework designed for the distributed storage and processing of vast datasets, often linked with tasks related to big data analytics and processing.

### **What are the different vendor-specific distributions of Hadoop?**
   - Hadoop has gained popularity in various industries, leading to the development of different vendor-specific distributions. Some notable distributions include:
     - **Cloudera**: Cloudera offers Cloudera Data Platform (CDP), a comprehensive distribution that includes various Hadoop ecosystem components along with management and monitoring tools.
     - **Amazon EMR**: Amazon Elastic MapReduce (EMR) is a cloud-native Hadoop distribution provided by Amazon Web Services (AWS), offering easy scalability and integration with other AWS services.
     - **Microsoft Azure**: Microsoft provides Azure HDInsight, a Hadoop distribution on the Azure cloud platform, with support for various big data and machine learning frameworks.

## 2. Apache ZooKeeper
- [Apache ZooKeeper](https://zookeeper.apache.org/)

Apache ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. It's an essential component in distributed systems, often used in Hadoop ecosystems to coordinate and manage servers effectively.

### Core Concepts

#### 1. Coordination and Configuration Management
- **ZooKeeper:**
  - Provides a reliable, fast, and simple coordination service for distributed applications.
  - Manages common data in a centralized manner, which allows distributed nodes to coordinate with each other.

#### 2. Znodes - Data Nodes
- ZooKeeper's data model consists of znodes, which are similar to files and directories. Each znode can store data and have children.
- Znodes maintain a stat structure that includes version numbers for data changes, ACL changes, and timestamps to facilitate cache validations.

#### 3. Watches
- Clients can set watches on znodes. A watch will be triggered and a notification sent to the client if the znode changes.
- Watches are a simple mechanism that allows clients to get notified of changes without polling.

#### 4. Consistency
- Ensures a highly reliable data registry for distributed systems.
- Data is replicated over a set of hosts and all interactions happen in the primary server to maintain a consistent data model.

#### 5. Sessions
- Clients connect to ZooKeeper servers using sessions. Sessions are maintained by heartbeats (pings); if a heartbeat is not received within the specified time, the session is considered dead.

#### 6. Atomicity
- Operations in ZooKeeper are atomic. Either an operation is successfully executed, or no change is made to the state of the system.

#### 7. Ephemeral Nodes
- ZooKeeper supports the creation of ephemeral nodes which exist as long as the session that created them is active.
- Useful for locks and leader election in distributed systems.

#### 8. Sequence Nodes
- ZooKeeper can create sequence znodes which are automatically assigned a unique monotonic increasing number.
- Useful for implementing primitives like distributed counters.

### Real-World Examples:

#### 1. **Service Discovery in Microservices Architectures:**
   - *Use Case:* In a microservices architecture, ZooKeeper can be used for service discovery. Each service registers its address in ZooKeeper, and clients use ZooKeeper to look up the addresses dynamically, allowing for loose coupling and easy scaling.

#### 2. **Configuration Management:**
   - *Use Case:* Centralized configuration management allows distributed systems to change their behavior dynamically. Systems read configuration data from ZooKeeper and get notified instantly about the changes, ensuring consistency across the cluster.

#### 3. **Leader Election:**
   - *Use Case:* In distributed systems, leader election is essential for deciding the primary server. ZooKeeper's ephemeral and sequence nodes can be used to implement a robust leader election algorithm.

#### 4. **Distributed Locks:**
   - *Use Case:* ZooKeeper can be used to implement distributed locks that are essential for ensuring that only one node is executing a critical section of code at any point in time.

#### 5. **Cluster Management:**
   - *Use Case:* ZooKeeper is often used in distributed systems for cluster management. It can monitor the nodes joining and leaving the cluster dynamically and trigger necessary actions based on the cluster state changes.

ZooKeeper's ability to coordinate between nodes in a distributed system makes it an indispensable tool in complex, large-scale applications. It provides a simple interface to a powerful coordination mechanism, simplifying the development of distributed applications.

### **What are the different Hadoop configuration files** ❗
   - Hadoop configuration files play a crucial role in defining the behavior and settings of various Hadoop components. Here's an overview of some essential Hadoop configuration files:

     - `core-site.xml`: This file contains core configuration settings, such as the file system, I/O settings, and network addresses. It is used to specify properties like the Hadoop cluster's default file system and various I/O-related configurations.

     - `hdfs-site.xml`: For the Hadoop Distributed File System (HDFS), this file defines configuration parameters like replication factors, block sizes, and data node settings. It is vital for tuning HDFS to suit specific requirements.

     - `mapred-site.xml`: When working with the MapReduce framework, this file is used to configure settings related to job tracking, task scheduling, and resource management. It defines properties like the job tracker address and task tracker settings.

     - `yarn-site.xml`: In the context of Yet Another Resource Negotiator (YARN), this file specifies configurations for resource management, node manager settings, and resource allocation policies. It plays a significant role in optimizing resource utilization in Hadoop clusters.

     - `hadoop-env.sh`: This script allows you to set environment variables and customize options for Hadoop processes. It is particularly useful for configuring memory settings and Java-related parameters for Hadoop components.

Hadoop configuration files provide the flexibility to tailor the behavior of Hadoop components to meet specific performance, scalability, and resource management requirements. Proper configuration is essential for optimizing Hadoop clusters and achieving desired outcomes in big data processing tasks.

Remember that Hadoop's flexibility extends beyond these core configuration files, as it allows you to create custom configurations and adapt the framework to the unique needs of your big data projects.

## 3. Apache Kafka
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)

### Core Concepts:

#### 1. **Topics:**
   - Kafka organizes data into topics, which represent feeds of messages. Producers publish messages to topics, and consumers subscribe to topics to process those messages.

#### 2. **Partitions:**
   - Topics can be divided into partitions, allowing for parallel processing of messages. Each partition is an ordered and immutable sequence of records.

#### 3. **Brokers:**
   - Kafka brokers are servers that store data and serve client requests. They manage the storage and retrieval of messages, as well as the communication between producers and consumers.

#### 4. **Producers:**
   - Producers are responsible for publishing messages to Kafka topics. They send messages to specific topics, and Kafka ensures that these messages are distributed across partitions.

#### 5. **Consumers:**
   - Consumers subscribe to topics and process messages. They can maintain their own offset, indicating the position in the partition from which they have consumed messages.

#### 6. **Consumer Groups:**
   - Consumers can be organized into consumer groups, allowing multiple instances to work together to consume messages from a topic. Each consumer in a group processes a different subset of the partitions.

#### Real-World Use Cases:

1. **Log Aggregation:**
   - *Core Concept Applied:* Topics and Partitions
   - *Use Case:* Imagine a bustling library of online experiences. **LinkedIn** employs Kafka to aggregate logs, creating a comprehensive anthology of user interactions. Each log type is a distinct section, and Kafka partitions ensure parallel processing, turning logs into valuable stories for platform enhancement.

2. **Event Sourcing:**
   - *Core Concept Applied:* Producers and Topics
   - *Use Case:* Picture an eventful journey with **Uber**, where every ride is a story. Kafka captures and replays these events, creating a historical record. The events (chapters) are written by various producers, and Kafka's topics maintain the narrative's integrity for accurate retrospection.

3. **Real-Time Data Processing:**
   - *Core Concept Applied:* Producers, Consumers, and Topics
   - *Use Case:* Enter the fast-paced world of social media at **Twitter**. Kafka processes and analyzes tweets in real-time, crafting a dynamic narrative of trending topics, user sentiments, and global conversations—a real-time storybook that captivates millions.

4. **Microservices Communication:**
   - *Core Concept Applied:* Producers, Consumers, and Topics
   - *Use Case:* Journey into the realm of digital streaming with **Netflix**. Kafka acts as the communication backbone between microservices, allowing seamless interaction. Each microservice contributes to the collective storyline, enabling scalable and fault-tolerant storytelling in the digital entertainment saga.

## 4. Kerberos Authentication

### Core Concepts
#### 1. **Kerberos Protocol:**
   - Kerberos is a network authentication protocol designed to secure communication over an insecure network, providing strong authentication and encryption.

#### 2. **Principal:**
   - A principal is a unique identity, often associated with a user or service, in the Kerberos authentication system. It's represented by a unique name, such as "user@REALM."

#### 3. **KDC (Key Distribution Center):**
   - The Key Distribution Center is the central authentication server in a Kerberos system. It consists of two main components: 
     - Authentication Server (AS): Responsible for initial authentication and issuing tickets.
     - Ticket Granting Server (TGS): Grants service tickets to users for accessing specific services.

#### 4. **Tickets:**
   - Kerberos relies on the use of tickets for authentication. There are two primary types of tickets:
     - Ticket Granting Ticket (TGT): Obtained after initial authentication with the AS and used to request service tickets.
     - Service Ticket: Grants access to a specific service, proving the user's identity to that service.

#### 5. **Authentication Process:**
   - Kerberos authentication involves a series of steps, including authentication, ticket issuance, and ticket validation. The process ensures that users or services can securely access resources.

#### 6. **Single Sign-On (SSO):**
   - Kerberos enables Single Sign-On, allowing users to access multiple services without re-entering their credentials after the initial authentication.

#### 7. **Realm:**
   - A realm is a Kerberos administrative domain where users, services, and the KDC reside. It's represented as a realm name, such as "EXAMPLE.COM."

#### 8. **Key Encryption Key (KEK):**
   - KEK is used for securing the communication between the client and the KDC. It helps protect the TGT from eavesdropping during transmission.

#### 9. **Time Sensitivity:**
   - Kerberos tickets have a limited validity period to enhance security. The short-lived nature of tickets reduces the risk of compromise if they are intercepted.

### Kerberos Commands

#### `kinit` - Kerberos Ticket Initialization
The `kinit` command is used to obtain a Ticket Granting Ticket (TGT) from the Key Distribution Center (KDC) after a user successfully authenticates using their credentials (typically a username and password). It stores the TGT in a cache, allowing the user to request service tickets without entering their credentials again during their session.

**Usage:**
~~~
kinit username@REALM
~~~


#### `klist` - List Kerberos Tickets
The `klist` command is used to display the contents of the Kerberos ticket cache, showing the currently obtained tickets, including the TGT and any service tickets. This command is helpful for users to check their active tickets and their expiration times.

**Usage:**
~~~
klist
~~~

### Real-World Use Cases
1. **Network Security:**
   - Kerberos is widely used in securing network communications, such as authentication in Active Directory for Windows environments.

2. **Cross-Realm Authentication:**
   - Organizations with multiple realms can use Kerberos to establish trust relationships and allow users to access resources across different administrative domains.

3. **Secure Service Access:**
   - Many network services, including databases and web applications, support Kerberos authentication to ensure secure access and data protection.

4. **Single Sign-On (SSO):**
   - Kerberos-based SSO simplifies user authentication, reduces password fatigue, and enhances user experience by requiring users to log in only once.

5. **Data Protection:**
   - The encryption and time-sensitive nature of Kerberos tickets provide robust security for protecting sensitive data during transmission and access.

In summary, Kerberos authentication is a robust and widely-used protocol for securing network communication, ensuring strong authentication, encryption, and Single Sign-On capabilities in various real-world applications. The `kinit` and `klist` commands are essential tools for managing Kerberos tickets and authenticating users.

## Excercise

### Chapter 1: Introduction to Big Data and Hadoop

1.  What is Apache Hadoop?
2.  Can you name a few vendor-specific distributions of Hadoop?
3.  What are the three modes in which Hadoop can run?
4.  What is the primary role of the `hadoop-env.sh` configuration file?
5.  What purpose does the `core-site.xml` file serve?

### Chapter 2: Apache ZooKeeper

6.  What is Apache ZooKeeper and what role does it play in a distributed environment?
7.  Can you explain the concept of znodes in ZooKeeper?
8.  How does ZooKeeper handle coordination and configuration management across distributed systems?
9.  What are ephemeral nodes and sequence nodes in ZooKeeper, and how are they used?
10.  How does ZooKeeper ensure data consistency and reliability across distributed nodes?

### Chapter 3: Apache Kafka

11.  What is Apache Kafka? 
12.  What are Topics in Kafka?
13.  What are Partitions in Kafka?
14.  What is the role of a Broker in Kafka?
15.  What is the difference between a Kafka Producer and a Consumer?

### Chapter 4: Kerberos Authentication

16.  What is the primary purpose of the Key Distribution Center (KDC) in the Kerberos authentication system, and what are its two main components?
17.  How does the "kinit" command contribute to the Kerberos authentication process, and what does it allow users to obtain?
18.  Explain the concept of "Single Sign-On (SSO)" in the context of Kerberos authentication and its benefits for users.
19.  Why is the concept of "time sensitivity" important in Kerberos authentication, and how does it enhance security?
20.  In what real-world scenarios or use cases is Kerberos authentication commonly employed, and how does it contribute to security and ease of use in those contexts?

## Wrapping Up :trophy:
Talk with your mentor about the concepts you have learned today and how they are applied in real-world scenarios. Discuss any questions or challenges you encountered during your self-study. Tomorrow, you will have a Q&A session with your mentor to further solidify your understanding of the Hadoop ecosystem and its components.

## Action Items
- Review the core concepts of Hadoop, ZooKeeper, Kafka and Kerberos.
- Explore real-world use cases for these technologies and understand their practical applications.
- Prepare questions and topics for discussion in the upcoming Q&A session with your mentor.
- Reflect the new conecpet with the Challenge from [Day 01](./day_01#ready-for-a-challenge-trophy) 
:trophy:

## Recommended Articles and Videos:
- [Hadoop Ecosystem Explained](https://www.youtube.com/watch?v=AZovvBgRLIY) - This video provides an overview of the Hadoop ecosystem, explaining the core components and their roles in big data processing.
- [Hadoop Core Components](https://www.youtube.com/watch?v=d2xeNpfzsYI) - This video offers a detailed explanation of the core components of Hadoop, including HDFS, MapReduce, and YARN, and their significance in distributed data processing.
- [ZooKeeper Explained](https://www.youtube.com/watch?v=gZj16chk0Ss) - This video provides an in-depth explanation of Apache ZooKeeper, its features, and its applications in distributed systems coordination.
- [Hadoop Tutorial YouTube Playlist](https://youtube.com/playlist?list=PLkz1SCf5iB4dw3jbRo0SYCk2urRESUA3v) - A playlist featuring tutorials on Hadoop, covering a variety of topics.
- [Introduction to the Hadoop Ecosystem](https://www.analyticsvidhya.com/blog/2020/10/introduction-hadoop-ecosystem/) - An introductory article on the components and functionalities of the Hadoop ecosystem.
- [Understanding the Hadoop Ecosystem](https://www.databricks.com/glossary/hadoop-ecosystem) - A glossary entry by Databricks offering insights into the Hadoop ecosystem.
- [What is Hadoop? Simplilearn Tutorial](https://www.simplilearn.com/tutorials/hadoop-tutorial/what-is-hadoop) - A tutorial providing a foundational understanding of Hadoop.
- [Hadoop Ecosystem Components Explained](https://data-flair.training/blogs/hadoop-ecosystem-components/) - An article detailing the components that make up the Hadoop ecosystem.
- [Comprehensive Guide to the Hadoop Ecosystem](https://www.edureka.co/blog/hadoop-ecosystem/amp/#amp_tf=From%20%251%24s&aoh=16655728574406&referrer=https%3A%2F%2Fwww.google.com) - Edureka's in-depth guide on the Hadoop ecosystem, its components, and functionalities.
- [What is Kerberos?](https://steveloughran.gitbooks.io/kerberos_and_hadoop/content/sections/what_is_kerberos.html) - An article detailing the Kerberos protocol and it's integration with the Hadoop ecosystem.
- [Taming Kerberos - Computerphile](https://www.youtube.com/watch?v=qW361k3-BtU) - Kerberos is an authentication method - Dr Mike Pound explains how it works so neatly.
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
  
