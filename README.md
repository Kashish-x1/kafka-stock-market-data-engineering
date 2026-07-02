# 📈 Kafka Stock Market Data Engineering Project

An end-to-end stock market data engineering pipeline built using **Apache Kafka**, **Python**, **AWS EC2**, **Amazon S3**, **AWS Glue**, and **Amazon Athena**.

---

## 🚀 Project Overview

This project demonstrates how stock market data can be streamed through Apache Kafka, stored in Amazon S3, cataloged using AWS Glue, and queried using Amazon Athena.

The pipeline simulates real-time stock market streaming by continuously sending stock records from a dataset to Kafka.

---

## 🏗️ Architecture Diagram

<p align="center">
  <img src="./architecture.jpg" width="100%">
</p>
---

## 🔄 Project Workflow

1. Stock market dataset is loaded using Python.
2. Kafka Producer continuously publishes stock records.
3. Apache Kafka running on AWS EC2 receives streaming data.
4. Kafka Consumer reads the messages.
5. Consumer stores JSON files into Amazon S3.
6. AWS Glue Crawler scans the S3 bucket.
7. Glue Data Catalog creates the table schema.
8. Amazon Athena runs SQL queries directly on the data stored in S3.

---

## ⚙️ Tech Stack

- Python
- Apache Kafka
- AWS EC2
- Amazon S3
- AWS Glue
- Amazon Athena
- SQL
- Pandas
- kafka-python
- s3fs

---

## 📁 Project Structure

```text
kafka_stock_market/
│
├── data/
│   └── indexProcessed.csv
│
├── producer.py
├── consumer.py
├── requirements.txt
├── README.md
└── images/
    └── architecture.png
```

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/Kashish-x1/kafka-stock-market-data-engineering.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Kafka

Configure Kafka Broker on AWS EC2.

### Run Producer

```bash
python producer.py
```

### Run Consumer

```bash
python consumer.py
```

---

## 📊 Services Used

| Service | Purpose |
|----------|----------|
| Apache Kafka | Data Streaming |
| AWS EC2 | Kafka Broker |
| Amazon S3 | Data Storage |
| AWS Glue | Metadata Catalog |
| Amazon Athena | SQL Analytics |

---

## 📌 Future Improvements

- Replace CSV with live Yahoo Finance API.
- Store data in Parquet format.
- Build a Streamlit Dashboard.
- Integrate Power BI.
- Deploy using Docker.

---

## 👩‍💻 Author

**Kashish**

Aspiring Data Engineer | Python | Apache Kafka | AWS | SQL

---
