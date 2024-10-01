# Realtime Data Streaming | End-to-End Data Engineering Project

## Table of Contents
- [Introduction](#introduction)
- [System Architecture](#system-architecture)
- [What You'll Learn](#what-youll-learn)
- [Technologies](#technologies)
- [Getting Started](#getting-started)

## Introduction

This project serves as a comprehensive guide for constructing an end-to-end data engineering pipeline. It encompasses all stages, from data ingestion and processing to storage, leveraging a powerful technology stack that includes Apache Airflow, Python, Apache Kafka, Apache Zookeeper, and Apache Spark.

The data is ingested from the Twitter API, allowing for real-time analysis of tweets and trends. Processed data is then stored in PostgreSQL, a robust relational database that ensures efficient querying and management of data. The entire setup is containerized with Docker, ensuring easy deployment and scalability..

## System Architecture

![System Architecture](https://github.com/airscholar/e2e-data-engineering/blob/main/Data%20engineering%20architecture.png)

The project is designed with the following components:

- **Data Source**: We utilize the Twitter API to ingest real-time tweet data for our pipeline.
- **Apache Airflow**: Acts as the orchestrator for the pipeline, overseeing task management and storing retrieved data in a PostgreSQL database.
- **Apache Kafka and Zookeeper**: Used for facilitating the streaming of data from PostgreSQL to the processing engine, enabling continuous data flow.
- **Control Center and Schema Registry**: Provides monitoring capabilities for Kafka streams and manages data schemas.
- **PostgreSQL**: Serves as the storage solution for processed data, ensuring effective data management and retrieval.

## What You'll Learn

- Establishing a data pipeline using Apache Airflow
- Streaming real-time data through the Twitter API with Apache Kafka
- Ensuring distributed synchronization via Apache Zookeeper
- Implementing data processing methods utilizing Apache Spark
- Storing processed data using PostgreSQL as the primary database
- Containerizing the entire data engineering infrastructure with Docker

## Technologies

- Apache Airflow
- Python
- Apache Kafka
- Apache Zookeeper
- PostgreSQL
- Docker

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/syafriedf/twitter-etl-streaming.git
    ```

2. Navigate to the project directory:
    ```bash
    cd twitter-etl-streaming
    ```

3. Run Docker Compose to spin up the services:
    ```bash
    docker-compose up --build
    ```
    
