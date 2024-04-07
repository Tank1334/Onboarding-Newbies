# Day 18 - Introduction to and Advanced Concepts in Apache Airflow :airflow:

## Overview
**Goals:**
- Introduce fundamental concepts, terminology, and architecture of Apache Airflow for junior participants.
- Dive deeper into advanced Apache Airflow concepts and best practices for senior participants.
- Lay the groundwork for understanding, managing, and optimizing data workflows with Airflow.

:warning: **Note:**
- This combined schedule accommodates both junior and senior participants, offering a comprehensive learning experience covering basic and advanced Airflow topics.

### Read the following chapters from the [Apache Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html)
### Chapter 1: Introduction to Apache Airflow

- **Topics Covered:**
  - **What is Apache Airflow?**
    - Introduction to workflow management systems and Airflow's role.
  - **Key Concepts and Terminology**
    - Definitions of terms like DAGs, Operators, Tasks, DAGRun, TaskInstance, Hook.
  - **Core Components**
    - Detailed explanation of components like Scheduler, Web Interface, Metadata Database, Dag Processor, Triggerer and Executors.
  - **Architecture Overview**
    - High-level overview of Airflow's distributed architecture.
  - **DAGs (Directed Acyclic Graphs)**
    - Understanding DAG structure and its importance in defining workflows.
  - **Operators**
    - Explanation of various types of operators and their functionalities.
  - **Executors**
    - Understanding different executor types and their impact on task execution.
  - **Scheduler**
    - Role of the scheduler in triggering task execution based on dependencies and schedule.
  - **Web Interface**
    - Overview of the Airflow web interface for monitoring and managing workflows.

### Chapter 2: Core Concepts

###### 1. **Directed Acyclic Graphs (DAGs):**
   - Understand the concept of DAGs in Airflow and their role in defining workflows.
   - Learn how to structure and organize tasks within a DAG for efficient pipeline execution.

###### 2. **Operators:**
   - Explore different types of operators available in Airflow for performing tasks within DAGs.
   - Gain familiarity with commonly used operators such as BashOperator, PythonOperator, and more.

###### 2. **Core Features:**
   - Read about Variables, exaplain the puprose of using them.
   - Read about Connections, give example of a connection we are using.
   - Read about Pools and explain the puprose of them.
### Read the following chapters from the [Apache Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html)
### Chapter 3: Advanced Airflow Concepts

- **Topics Covered:**
  - **Custom Operators and Hooks**
    - Techniques for creating custom operators and hooks to extend Airflow's functionality.
  - **XComs (Cross-Communication)**
    - Role of XComs in facilitating communication between tasks within a DAG.
  - **DynamicTaskMapping and TaskGroups**
    - Organizing and managing complex workflows using DynamicTaskMapping and TaskGroups.
  - **Trigger Rules**
    - Configuring trigger rules for defining task dependencies and execution triggers.
  - **Airflow Sensors and Deferrable Operator**
    - What are deferrable operators? Why they help us? Explain the flow when running deferred operator.
    - Implementing sensors for waiting on external conditions before task execution.
  - **Macros and Templating**
    - Using macros and Jinja templating for dynamic task generation and parameterization.
  - **Maintainers**
    - Plugins help us to extend airflow abilities. 
    - Cluster Policies gives us the ability to check or mutate DAGs or Tasks on a cluster-wide level.

##### Core Concepts

###### 1. **Custom Operators and Hooks:**
   - Explore techniques for creating custom operators and hooks to extend Airflow's functionality.
   - Learn best practices for writing reusable and maintainable custom components tailored to specific workflow requirements.

###### 2. **XComs (Cross-Communication):**
   - Understand the role of XComs in facilitating communication between tasks within a DAG.
   - Explore advanced use cases for leveraging XComs to share data and coordinate task execution.

### Wrapping Up the Day

- **Joint Discussion and Q&A (1 hour):**
  - Engage in a collective discussion with mentors and peers to share insights and experiences related to both introduction and advanced Apache Airflow concepts.
  - Address questions and clarify doubts for both junior and senior participants.

**Congratulations to all participants on completing Day 14! You've embarked on a journey to explore Apache Airflow from its foundational concepts to advanced techniques. Keep building on this knowledge to excel in managing and optimizing data workflows with Airflow.**

## **Questions:** ❓
* Can you explain what a DAG is in Airflow?
* Explain the flow of a TaskInstance in Airflow.
* What are Operators in Airflow, and can you name a few types?
* What is the role of the Scheduler in Airflow?
* Can you describe what a Task Instance is in Airflow? Give an example in context of dummy usage
* What are Hooks and how are they used in Airflow?
* Can you explain what the Executor is in Airflow and name a few types? What executor is the most common, and what's executor we generally use? What are the differences between each executor and when we will use each one?
* What is the purpose of the Webserver in Airflow?
* How do you define or create a workflow in Airflow?
* What is deferrable and how Airflow runs it?

## **Wrapping Up:** :hourglass_flowing_sand:
Reflect on today's learnings with your mentor and peers, discussing how you can apply both introductory and advanced Airflow concepts in your projects. Consider potential use cases and scenarios where Airflow can streamline your workflow processes and enhance productivity in data pipeline management.
