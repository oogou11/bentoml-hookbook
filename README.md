# BentoML Practical Guide - Example Code

Welcome to the example code repository for the "BentoML Practical Guide"! This repository contains all the example code and practical use cases from the book, designed to help you better understand and apply BentoML for model service and deployment.

## Table of Contents

- [Project Overview](#project-overview)
- [Environment Requirements](#environment-requirements)
- [Installation Guide](#installation-guide)
- [How to Run Example Code](#how-to-run-example-code)
- [Contribution Guidelines](#contribution-guidelines)

## Project Overview

The "BentoML Practical Guide" is a book aimed at machine learning engineers and data scientists, helping them master the process of packaging, deploying, monitoring, and optimizing machine learning models using BentoML. The repository contains all the example code from the book, allowing you to quickly learn how to deploy models and manage them with BentoML.

The example code in this repository is based on BentoML version 1.3.10, and it is compatible with Ubuntu 20.04.6 LTS and Python 3.11. The examples cover a wide range of machine learning use cases, such as classification, regression, and image processing, to help you understand BentoML's core applications.

## Environment Requirements

To ensure the example code runs smoothly, it is recommended to set up your environment according to the following requirements:

- **Operating System**: Ubuntu 20.04.6 LTS (other operating systems may work but have not been thoroughly tested)
- **Python Version**: Python 3.11
- **Virtual Environment Management Tool**: Conda 24.4.0
- **BentoML Version**: 1.3.10
- **GPU**: NVIDIA GeForce RTX 4090 (if GPU acceleration is required)
- **CUDA Version**: CUDA 12.4 (for GPU support)

### Additional Recommended Configurations

- **NVIDIA Driver**: A version compatible with CUDA 12.4
- **cuDNN**: A version compatible with CUDA 12.4
- **all-MiniLM-L6-v2 Download**:  [If downloading is difficult, you can download via cloud storage.](https://pan.baidu.com/s/1PQW1-5DPo1Geh46Hr10NgA?pwd=5hv5)

## Installation Guide

### 1. Install Miniconda (if not already installed)

First, install Miniconda to create a virtual environment:

- **Miniconda download page**: [Miniconda Official Download Page](https://docs.conda.io/en/latest/miniconda.html)

Choose the appropriate version for your operating system and install it. After installation, confirm it was successful by running:

```bash
conda --version
```
### 2. Create a Virtual Environment and Install Dependencies
Create a new virtual environment and activate it:
```bash
conda create -n bento_env python=3.11
conda activate bento_env
```
Then, install BentoML:
```bash
pip install bentoml==1.3.10
```
### 3. Clone the Repository
Clone this repository to access the example code:
```bash
git clone git@github.com:oogou11/bentoml-hookbook.git
cd bentoml-hookbook
```
## How to Run Example Code
Here are some basic steps to run the code from this repository. Make sure you have installed all dependencies and activated the virtual environment before running any scripts.

### 1. Start BentoML Service Locally
If you need to run a local Bento service, use the following command in your terminal:
```bash
bentoml serve service.py:Service
```
This will start the BentoML API service, and you can interact with it using REST API and BentoML RPC Client, the default port is 3000.
```bash
bentoml grpc-serve grpc_service.py:svc
```
This will start the BentoML gRPC API service, and you can interact with it using REST API and BentoML gRPC Client, the default port is 3000.

## Contribution Guidelines

Thank you for considering contributing to this repository! To maintain the quality and consistency of the project, please follow the guidelines below:

### 1. Code of Conduct

By contributing to this project, you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md).

### 2. Reporting Issues

If you find any bugs or issues with the code, please:

- Check the [existing issues](https://github.com/oogou11/bentoml-hookbook/issues) to see if your issue has already been reported.
- If not, open a new issue with a clear description of the problem, the steps to reproduce it, and any relevant logs or error messages.

### 3. Forking and Cloning the Repository

To contribute, follow these steps:

1. **Fork** the repository to your own GitHub account.
2. **Clone** your forked repository to your local machine:
   
    ```bash
    git clone git@github.com:oogou11/bentoml-hookbook.git
    ```
3. Navigate to the repository directory:
    ```bash
    cd bentoml-hookbook
    ```
### 4. Creating a New Branch
Before making any changes, create a new branch with a descriptive name:  
```bash
git checkout -b your-branch-name # example feature/embedding_model
```
### 5. Making Changes
When making changes to the codebase:

- **Follow the Code Style**: Please adhere to the coding style and conventions outlined in the project. For Python projects, you can refer to the [PEP 8 guidelines](https://www.python.org/dev/peps/pep-0008/).
- **Write Clear Code**: Your code should be clean, readable, and easy to understand. Add comments where necessary to explain the logic.
- **Document Your Changes**: Ensure that you document your changes in the relevant places, such as code comments or documentation files.
- **Create Unit Tests**: If you're fixing a bug or adding a feature, add corresponding unit tests to ensure that everything works as expected. Tests should be placed in the appropriate test directories.
### 6. Running Tests
Before committing your changes, ensure that all tests pass. To run the tests:
```bash
pytest
```
### 7. Committing Changes
Commit your changes with a clear, concise commit message describing what you have done:
```bash
git commit -m "Brief description of changes"
```
### 8. Pushing Changes
Push your changes to your forked repository:
```bash
git push origin your-branch-name # example feature/embedding_model
```
### 9. Submitting a Pull Request

- Navigate to the original repository on GitHub and click on **Pull Requests**.
- Click on **New Pull Request**, select the branch with your changes, and provide a description of the changes.
- Make sure your PR is targeted at the **main** branch (or the branch specified by the project owner).

  Once your pull request is reviewed, it will be merged into the main branch if everything looks good.
### 10. Code Review
- Pull requests will be reviewed by the project maintainers.
- Please be responsive to any comments or feedback and make necessary updates to your pull request.
### 11. Thank You!  
We appreciate your contribution! Your help improves this project and benefits the community. If you have any questions, feel free to ask or open an issue.

---

### Explanation:
- **Code of Conduct**: Mentions the project’s code of conduct (you can link to a separate file if you have one).
- **Reporting Issues**: Instructs how to report bugs or issues effectively.
- **Forking and Cloning the Repository**: Describes the process to fork and clone the repository.
- **Creating a New Branch**: Explains how to create a new branch for changes.
- **Making Changes**: Ensures contributors follow coding standards and document their changes.
- **Running Tests**: Reminds contributors to run tests before committing.
- **Committing Changes**: Guides on making proper commit messages.
- **Pushing Changes**: Describes how to push changes to the fork.
- **Submitting a Pull Request**: Explains how to submit a PR for review.
- **Code Review**: Outlines the process for code review after a PR is submitted.
- **Thank You**: Acknowledges and appreciates the contributions.

This Markdown format should fit neatly into your repository’s `README.md` or any other file dedicated to contributing guidelines!
