# Day 05 - MapReduce Programming Model, YARN & Oozie :elephant:

## Overview:
Today's session is all about getting to know the Hadoop ecosystem's processing side of things. You'll explore the foundational concepts of Hadoop resource management, processing and scheduling, while gaining a depper understanding about MapReduce, YARN * OOzie's roles in the hadoop ecosystem.

**The focus is on gaining a deeper understanding of big data processing in the Hadoop ecosystem.**

## Goals:
- Gain a foundational understanding of the resource management, processing and scheduling in Hadoop ecosystem.
- Explore YARN, MapReduce and Oozie's role big data processing.
- Understand real-world use cases and disadvantages of YARN, MapReduce.
- Reflect on the last two days and work on improving with your time management for the next day.

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

## 6. MapReduce Programming Model
- [MapReduce Tutorial](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)

MapReduce is a Java-based, distributed execution framework within the Apache Hadoop Ecosystem.  It takes away the complexity of distributed programming by exposing two processing steps that developers implement: **1) Map** and **2) Reduce**. In the Mapping step, data is split between parallel processing tasks. Transformation logic can be applied to each chunk of data. Once completed, the Reduce phase takes over to handle aggregating data from the Map set. In general, MapReduce uses Hadoop Distributed File System (HDFS) for both input and output. However, some technologies built on top of it, such as Sqoop, allow access to relational systems.

### Core Concepts

A MapReduce system is usually composed of three steps (even though it's generalized as the combination of Map and Reduce operations/functions). The MapReduce operations are:

#### 1. **Map:** 
- The input data is first split into smaller blocks. The Hadoop framework then decides how many mappers to use, based on the size of the data to be processed and the memory block available on each mapper server. Each block is then assigned to a mapper for processing. Each ‘worker’ node applies the map function to the local data, and writes the output to temporary storage. The primary (master) node ensures that only a single copy of the redundant input data is processed.

#### 2. **Shuffle:**
- combine and partition: worker nodes redistribute data based on the output keys (produced by the map function), such that all data belonging to one key is located on the same worker node. As an optional process the combiner (a reducer) can run individually on each mapper server to reduce the data on each mapper even further making reducing the data footprint and shuffling and sorting easier. Partition (not optional) is the process that decides how the data has to be presented to the reducer and also assigns it to a particular reducer.

#### 3. **Reduce:**
- A reducer cannot start while a mapper is still in progress. Worker nodes process each group of <key,value> pairs output data, in parallel to produce <key,value> pairs as output. All the map output values that have the same key are assigned to a single reducer, which then aggregates the values for that key. Unlike the map function which is mandatory to filter and sort the initial data, the reduce function is optional.

## 7. Hadoop YARN
- [Apache Hadoop YARN](https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/YARN.html)

YARN (Yet Another Resource Negotiator) is a fundamental component in the Hadoop ecosystem, serving as a resource management layer to efficiently share resources among multiple applications in a Hadoop cluster.

### Core Concepts

#### 1. Resource Manager (RM)
- Central component managing and allocating resources across the Hadoop cluster.
- Keeps track of available resources and schedules applications based on their resource requirements.

#### 2. Node Manager (NM)
- Runs on each machine in the cluster, managing resources (CPU, memory, etc.) on that specific node.
- Communicates with the Resource Manager to provide information about available resources and request resources for running applications.

#### 3. Application Master (AM)
- Created for each application submitted to YARN.
- Negotiates with the Resource Manager to obtain resources and coordinates the execution of tasks on Node Managers.
- Acts as a liaison between the application and the resource manager.

#### 4. Container
- Fundamental unit of resource allocation in YARN.
- Represents the allocated resources (CPU, memory) on a specific node for a particular application.
- Applications may consist of one or more containers.

#### 5. Application Lifecycle
- When a client submits a job to YARN, an Application Master is created for that job.
- The Application Master negotiates with the Resource Manager to obtain resources and launches containers on the Node Managers.
- Containers execute the tasks of the application.

#### 6. Schedulers
- YARN supports different schedulers, such as CapacityScheduler and FairScheduler.
- CapacityScheduler allows sharing resources among multiple queues with allocated capacities.
- FairScheduler assigns resources in a balanced manner, ensuring that all applications get a fair share.

#### 7. Resource Allocation
- YARN supports dynamic resource allocation, allowing applications to request additional resources or release unused resources during runtime.
- This flexibility enables optimal resource utilization based on the varying needs of applications.

#### 8. Fault Tolerance
- YARN provides fault tolerance by monitoring the health of Node Managers and restarting failed containers on healthy nodes.
- Ensures the reliability of applications by handling node failures and container restarts.

#### 9. Security
- YARN includes security features such as authentication and authorization to control access to cluster resources.
- Helps maintain the integrity and security of the Hadoop cluster.

#### 10. Preemption
- Preemption is a feature in YARN that allows the Resource Manager to interrupt and reclaim resources from running applications.
- Useful in multi-tenant environments where higher-priority applications may need resources currently allocated to lower-priority applications.

#### 11. Queue
- In the context of Apache Hadoop YARN, a "queue" refers to a logical subdivision or container for managing and allocating resources within a cluster.
- YARN queues play a crucial role in the resource management layer, allowing organizations to control how resources are shared among different applications or user groups.
- Queues facilitate multi-tenancy by providing distinct containers for different teams or applications, preventing resource contention and ensuring efficient workload isolation.

### Real-World Examples:
In real-world scenarios, Apache Hadoop YARN serves as a crucial resource management layer, enabling dynamic resource allocation and workload diversity. Here are detailed examples showcasing the practical applications of Apache Hadoop YARN:

#### 1. **Large-Scale Data Processing in E-commerce:**
   - *Use Case:* A multinational e-commerce company relies on YARN to process and analyze vast amounts of customer and transaction data in a cloud environment. YARN dynamically allocates resources for diverse workloads, from routine batch processing to complex analytics, ensuring optimal resource utilization. This enables the company to handle the global scale of its operations efficiently.

#### 2. **Enterprise Data Lakes for Financial Analysis:**
   - *Use Case:* A financial institution employs YARN to manage its enterprise data lake for in-depth financial analysis. YARN's resource allocation capabilities support concurrent execution of data processing tasks, allowing financial analysts to run complex algorithms and queries without contention. This ensures timely insights into market trends, risk assessment, and investment strategies.

#### 3. **Genomic Data Processing in Healthcare:**
   - *Use Case:* A healthcare research institution utilizes YARN for processing large-scale genomic data. YARN's ability to dynamically allocate resources based on the computational needs of genomic analysis tasks ensures efficient utilization of cluster resources. This accelerates genomic research, enabling scientists to analyze and interpret vast datasets for precision medicine initiatives.

#### 4. **Log Analysis for Cybersecurity:**
   - *Use Case:* A cybersecurity firm employs YARN for log analysis to detect and respond to security threats. YARN's resource management ensures that log processing tasks receive the necessary resources for real-time analysis. This allows the firm to identify and mitigate security incidents promptly, enhancing the overall cybersecurity posture.

#### 5. **Media and Entertainment Content Processing:**
   - *Use Case:* A media and entertainment company uses YARN to process and analyze content data, including video transcoding and metadata extraction. YARN's flexibility in handling diverse workloads allows the company to efficiently allocate resources for tasks like video processing, image recognition, and content recommendation, optimizing the content delivery pipeline.

These examples demonstrate how Apache Hadoop YARN plays a pivotal role in diverse industries, providing scalable and efficient resource management for a wide range of data processing tasks.

## 8. Oozie Workflow Scheduler

### Core Concepts
#### 1. **Oozie Overview:**
   - Apache Oozie is a workflow scheduler for Hadoop systems. It is used to manage and coordinate complex workflows of jobs, such as Hadoop MapReduce, Pig, Hive jobs, and more.

#### 2. **Workflow:**
   - An Oozie Workflow is a collection of actions (jobs) arranged in a directed acyclic graph (DAG). Workflows define the sequence of jobs to be executed.

#### 3. **Coordinator:**
   - An Oozie Coordinator job is a higher-level abstraction that allows the management of recurrent Workflow jobs triggered by time (frequency) and data availability.

#### 4. **Bundle:**
   - An Oozie Bundle provides a way to package multiple Coordinator and Workflow jobs and manage their lifecycle together.

#### 5. **Action Node:**
   - In an Oozie workflow, an action node represents a workflow task, like running a MapReduce job, executing a Hive script, or running a Pig script.

#### 6. **Control Node:**
   - Control nodes in Oozie workflows manage the workflow execution path with nodes for defining the start and end of a workflow and decision, fork, and join nodes for controlling the workflow execution flow.

#### 7. **Job Properties:**
   - Oozie jobs are configured with properties files, which are XML files containing job-specific parameters and settings.

#### 8. **Application Master:**
   - Oozie uses YARN’s Application Master to manage the lifecycle of a workflow. Each Oozie workflow job is a YARN application.

#### 9. **SLA Monitoring:**
   - Oozie supports Service Level Agreement (SLA) monitoring for jobs, allowing users to track the progress and performance of their workflows against predefined SLAs.

### Oozie Commands

#### `oozie job` - Oozie Job Operations
The `oozie job` command is used to perform job operations such as running, starting, suspending, resuming, and killing Oozie Workflow, Coordinator, or Bundle jobs.

**Usage:**
~~~
oozie job -oozie <oozie_URL> -config <job.properties> -run
~~~

### Real-World Use Cases
1. **Complex Data Pipelines:**
   - Oozie is used to schedule and manage complex data processing pipelines involving multiple stages and dependencies, ensuring that jobs are executed in the correct order.

2. **Recurring Jobs:**
   - With Oozie's Coordinator jobs, organizations can manage recurring jobs, ensuring that data processing tasks are performed at regular intervals or triggered by data availability.

3. **Resource Management:**
   - Oozie integrates with YARN to ensure efficient resource allocation and management for Hadoop jobs, optimizing cluster resource usage.

4. **SLA Compliance:**
   - Oozie’s SLA feature allows organizations to monitor and enforce service level agreements, ensuring that data processing jobs meet performance expectations.

5. **Scalability and Reliability:**
   - Oozie's robust architecture allows it to manage a large number of jobs reliably, making it suitable for enterprise-scale data processing.

Oozie's integration with the Hadoop stack, its ability to manage complex workflows, and its support for SLA monitoring make it an essential tool for efficient and reliable data processing and job scheduling in Hadoop ecosystems.

## Excercise

### Chapter 6: MapReduce Programming Model

26.  What is MapReduce? Explain its key concepts.
27.  What is the role of a Mapper in MapReduce?
28.  What is the role of a Reducer in MapReduce?
29.  What is meant by "Shuffling" in MapReduce?
30.  Can a MapReduce job have zero Reducers?

### Chapter 7: Hadoop YARN

31.  What is YARN? Explain its architecture.
32.  Explain the difference between YARN's schedulers.
33.  What is the role of the Node Manager in YARN?
34.  Explain a YARN application lifecycle. 
35.  How does YARN provide fault tolerance?

### Chapter 8: Oozie Workflow Scheduler

36.  What is Apache Oozie, and how does it facilitate job scheduling and workflow management in a Hadoop environment?
37.  Can you differentiate between an Oozie Workflow job and a Coordinator job? Provide an example of when you would use each.
38.  Describe the lifecycle of an Oozie job. What are the typical states an Oozie job can be in, and what are the implications of each state?
39.  How does Oozie support SLA (Service Level Agreement) monitoring, and why is it important in managing data processing jobs?
40.  What are the main components of an Oozie Workflow job, and what is the role of each component?

## Wrapping Up :trophy:
Talk with your mentor about the concepts you have learned today and how they are applied in real-world scenarios. Discuss any questions or challenges you encountered during your self-study. Tomorrow, you will have a Q&A session with your mentor to further solidify your understanding of the Hadoop ecosystem and its components.

## Action Items
- Review the core concepts of YARN, MapReduce & Oozie.
- Explore real-world use cases for these technologies and understand their practical applications.
- Prepare questions and topics for discussion in the upcoming Q&A session with your mentor.
- Reflect the new conecpet with the Challenge from [Day 01](./day_01#ready-for-a-challenge-trophy) 
:trophy:

## Recommended Articles and Videos:
- [Apache Yarn in AWS](https://aws.amazon.com/blogs/big-data/configure-hadoop-yarn-capacityscheduler-on-amazon-emr-on-amazon-ec2-for-multi-tenant-heterogeneous-workloads/) - This article explains how to configure Hadoop YARN CapacityScheduler on Amazon EMR for multi-tenant heterogeneous workloads, providing insights into resource management and scheduling.
- [MapReduce - Computerphile](https://www.youtube.com/watch?v=cvhKoniK5Uo) - This video offers a comprehensive overview of the MapReduce programming model, its core concepts, and its role in distributed data processing.
- [Apache Hadoop YARN Concepts and Applications](https://blog.cloudera.com/apache-hadoop-yarn-concepts-and-applications/) - Cloudera's comprehensive guide on the concepts and applications of Apache Hadoop YARN.
- [YARN Capacity Scheduler and Node Labels Part 1](https://www.davidmcginnis.net/post/yarn-capacity-scheduler-and-node-labels-part-1) - First part of a detailed discussion on the options available in YARN's capacity scheduler.
- [YARN Capacity Scheduler Overview](https://blog.cloudera.com/yarn-capacity-scheduler/) - An overview of YARN's capacity scheduler provided by Cloudera.
- [Untangling Apache Hadoop YARN Part 1: Cluster and YARN Basics](https://blog.cloudera.com/untangling-apache-hadoop-yarn-part-1-cluster-and-yarn-basics/) - The first part in a series aimed at explaining the basics of clusters and YARN.
  
