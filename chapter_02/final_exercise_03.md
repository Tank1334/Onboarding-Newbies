# Final Exrceise 03 - Embracing DevOps: GitLab, Docker, and CI/CD Pipeline 🚀

## Overview

**Goals:**

- Introduce the concept of Continuous Integration and Continuous Deployment (CI/CD) using GitLab.
- Learn how to set up SSH authorization for secure interaction with the repository.
- Understand the process of building Docker images and pushing them to a Docker registry.
- Implement a CI/CD pipeline for automating the build, test, and deployment processes.

**⚠️ Note:**

- In this exercise, you will need to work with Offical [GitLab](https://gitlab.com/) and [Docker.io](https://Docker.io/) artifactory in the public web, If you do the exercise in our internal network, you need to do the adjustment (Or Ask your mentor for help).
- Please Create 14 days free trial account on [GitLab](https://gitlab.com/) to push and pull your code and work with the full features of GitLab.
- Familiarize yourself with GitLab's interface and features as it will be an integral part of your development process.
- Ensure Docker is correctly set up on your machine and you have access to Docker.io to push and pull images.

## Chapter 1: GitLab and SSH Authorization

### Tasks

1. **Create a New Repository on GitLab:**
   - Initialize a new GitLab repository named "The Last Airbender" at [GitLab](https://gitlab.com/).
   - Clone the repository to your local machine to start working on the project.

2. **SSH Key Setup and Authorization:**
   - Generate an SSH key pair on your local machine if you haven't already.
   - Add the public SSH key to your GitLab account for secure and password-less communication with the repository.
   - After establishing SSH authorization, connect to your repo via SSH.

3. **Adding 'The Last Airbender' Files to the Project:**
   - Ensure that the project's repository is correctly cloned to your local machine.
   - Add the files related to ["The Last AirBender"](https://github.com/883G/The-Last-AirBender) into the cloned project directory.
   - Commit and push the changes to the GitLab repository.
   - Use GitLab's web interface to verify that the files are successfully pushed to the repository.
4. **Setting Up the Project Structure:**
   - Create a directory structure for the project, including the necessary files and directories for the Python application.
   - Organize the project files and directories to ensure a clean and structured layout.
5. **Do The AIRBENDER Exercise:**
   - Do the ["The Last AirBender"](https://github.com/883G/The-Last-AirBender) exercise and push the code to the GitLab repository.
   - Good Luck!

## Chapter 2: Docker Introduction and Image Creation

### Core Concepts

1. **Docker Overview:**
   - Understand the fundamentals of Docker and how it encapsulates applications and their environments using containers.

2. **Writing a Dockerfile:**
   - Create a Dockerfile for the Python application. Define the base image, set up the environment, copy the application code, and specify the entry command.

3. **Building and Testing the Docker Image:**
   - Build the Docker image from the Dockerfile.
   - Test the Docker image locally to ensure the application runs as expected.

4. **Pushing to Docker.io:**
   - Tag the Docker image with the appropriate version number and repository name.
   - Push the Docker image to your Docker.io registry to make it available for deployment.

## Chapter 3: Implementing CI/CD with GitLab

### Core Concepts and Tasks

1. **CI/CD Pipeline Overview:**
   - Understand the stages of a CI/CD pipeline: Build, Test, and Deploy.

2. **Creating `.gitlab-ci.yml`:**
   - Write the `.gitlab-ci.yml` file defining the CI/CD pipeline configuration.
   - Specify the stages, scripts, and conditions for each stage of the pipeline.

3. **Build Stage:**
   - Configure the pipeline to build the Docker image from the Dockerfile.
   - Ensure the image is built correctly and is ready for testing and deployment.

4. **Test Stage:**
   - Run the predefined tests in the repository to ensure the code meets the quality standards.
   - Use PyTest for executing the test cases in the Python application.

5. **Deploy Stage:**
   - Push the successfully built and tested Docker image to Docker.io.
   - (Optional) Define deployment steps if you have a specific environment to deploy the application.

## Wrapping Up the Day

**Reflection and Planning:**

- Review the CI/CD pipeline's execution and ensure every stage completes successfully.
- Plan any further enhancements or optimizations you might want to introduce to the pipeline. 

## **Action Items:**
- **CI/CD Pipeline Review:** Discuss the CI/CD pipeline with your mentor and seek feedback on the implementation.
- **Pipeline Enhancements:** Identify areas for pipeline optimization and discuss potential enhancements with your mentor.
- **Project Planning:** This is your first project in 883 group, discuss with your mentor about the project planning and how to manage the project in the future, based on your mistakes and the feedback from your mentor.