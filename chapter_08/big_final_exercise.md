# Senior Data Infra Engineer Onboarding Final Exercise :rocket:

## Introduction

Welcome to the Senior Data Infra Engineer Onboarding Exercise! This exercise is designed to assess your understanding of when and how to use various technologies commonly used in data operations, including Kafka, Spark, Airflow, Trino, Iceberg, SQL, and S3/HDFS. Your task is to demonstrate your expertise by designing a data pipeline within the context of a fictional scenario.

## Scenario Creation Prompt

As part of this exercise, you have the opportunity to create a scenario that showcases the integration of the specified technologies to address a specific problem or challenge related to data processing, analysis, or management. Your scenario should:

- Identify a fictional organization or business domain where data plays a crucial role.
- Define a problem or challenge that needs to be addressed.
- Specify how the integration of Kafka, Spark, Airflow, S3/HDFS, SQL, and either Trino or Iceberg can solve the problem effectively.
- Provide a narrative that outlines the roles, responsibilities, and objectives of the DataOps team within the given scenario.

## Your Task

Your task is to create a scenario based on the prompt provided above. Once you've crafted your scenario, document it clearly and concisely, providing sufficient details to convey the context, problem, and solution effectively. You will present your scenario by PowerPoint presentation to the group, followed by a Q&A session to discuss your design decisions and the relevance of the chosen technologies within the context of your scenario.

## Guidelines

- Be creative and imaginative in crafting your scenario. You have the freedom to invent any setting, industry, or business context that you find interesting.
- Ensure that the scenario highlights the relevance and importance of each technology within the context of solving the problem or achieving the objectives.
- Focus on practicality and realism. Avoid including technologies or elements that don't contribute meaningfully to the scenario.
- Prepare a PowerPoint presentation that clearly outlines the scenario, the problem, the solution, and the role of the DataOps team.
- Think about consepts you have learned in [Day 01](./day_01#ready-for-a-challenge-trophy) like fault tolerance, scalability, and performance.

## Requirements

### Technology Integration:
Your scenario must include the following technologies:

- **Airflow:** For orchestrating the data pipeline and workflow management.
- **Spark:** For data processing, transformation, and analysis.
- **Kafka:** For real-time data ingestion and streaming.
- **SQL:** For database querying and management.
- **Either S3/HDFS:** For storing raw data files.
- **Trino or Iceberg:** For advanced data querying and management.

### Monitoring and Troubleshooting:
 - Write prometheus exporter in python for health check of your data pipeline.
 - Deploy your exporter OpenShift with helm and all the best practises you have learned.
 - Create Grafana dashboard for your metrics.
 - Use Pandora and Pulse platform to integrate your exporter to the centric prometheus environment.
 - Create alerts for your metrics.

### Presentation:
Your scenario should be documented in a PowerPoint presentation that includes the following sections:
    - Introduction
    - Storyline Scenario Overview
    - Problem Statement
    - Solutions Overview - what was your options and why you choose this one?
    - Choosen Data Pipeline Architecture
    - Pros and Cons of the choosen architecture
    - Improvement and Future Work

### Calture and Agile:
- Your scenario should include a section that outlines the roles, responsibilities, and objectives of the DataOps team within the given scenario.
- Create Relsase Mail for your project - **DO THIS BEFORE YOU START THE PROJECT**.
- Create a Jira Epic and a Confluence page for the project.
- Create stories for the tasks that you will do in the project.
- Create tasks under the stories.
- Keep our culture with indicative stories, tasks and agile methodologies.
- Create Press Release (PR) and Frequently Asked Questions (FAQ) pages in the confluence page.
- Keep updated the status of the tasks in the confluence page every day.

## Evaluation

- Your scenario and architecture will be evaluated based on its creativity, relevance, coherence, and alignment with the objectives of the exercise. Make sure to demonstrate a deep understanding of the technologies and their practical applications within the context of your scenario.
- Your presentation will be evaluated based on its clarity, organization, and ability to effectively communicate the scenario, problem, solution, and the role of the DataOps team.
- Your monitoring and troubleshooting will be evaluated based on its effectiveness, completeness, and relevance to the scenario.
- Your culture and agile will be evaluated based on keeping updates and the status of the tasks in the confluence page every day, and create indicative stories, tasks and agile methodologies.

---

**Note to Participants:** Be prepared to answer questions like:
- Why use Spark for this task instead of Python vanilla?
- How does the choice of SQL impact the scalability and performance of your data pipeline?
- How does the choice of using either S3 or HDFS for storing raw data files impact the scalability and accessibility of your data infrastructure?

These questions will be part of the evaluation process.
## Recommended Resources:
- [What is REST](https://www.youtube.com/watch?v=Q-BpqyOT3a8)