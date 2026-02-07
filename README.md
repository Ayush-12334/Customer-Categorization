# 🚀 End-to-End Machine Learning Project — Customer Personality Segmentation

---

## 📌 Project Overview

Customer Personality Segmentation is an end-to-end Machine Learning project designed to analyze customer data and predict customer personality segments using ML algorithms.

The system helps malls, retail stores, and product-based companies understand customer behavior by grouping customers into clusters based on personal details and purchasing history.

This project implements a complete production-level ML pipeline including data ingestion, validation, transformation, clustering, model training, and deployment using Flask and Render.

---

## 🎯 Problem Statement

Businesses collect large amounts of customer data, but extracting actionable insights from it can be difficult.

The goal of this project is to:

* Cluster customers based on behavioral and demographic data.
* Identify customer personality segments.
* Predict the cluster number of new customers dynamically using machine learning classification techniques.

This enables:

* Targeted marketing strategies
* Personalized recommendations
* Improved business decision-making

---

## 💡 Proposed Solution

The solution uses a Machine Learning approach where:

1. Historical customer data is processed and validated.
2. Customers are grouped into clusters using unsupervised learning.
3. A classification model learns from clustered data.
4. The system predicts the cluster type for new customers based on input features.

---

## 🧰 Tech Stack

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Backend

* Flask

### Deployment

* Render

### Tools

* Git & GitHub

---

## 📂 Project Structure

```
project_root/
│
├── app.py                       # Flask application
│
├── src/
│   │
│   ├── data_ingestion.py        # Load and ingest raw data
│   ├── data_transformation.py   # Feature engineering & preprocessing
│   ├── data_clustering.py       # Customer clustering logic
│   ├── model_trainer.py         # Model training and evaluation
│   │
│   ├── exception.py             # Custom exception handling
│   ├── logger.py                # Logging system
│
├── pipelines/
│   ├── model_prediction.py      # Prediction pipeline
│
├── artifacts/                   # Saved models and preprocessing files
│
├── templates/                   # HTML templates
├── static/                      # CSS / static files
│
├── requirements.txt
├── README.md
```

---

## ⚙️ Machine Learning Workflow

### 1️⃣ Data Ingestion

* Reads raw customer dataset
* Loads data into pipeline

### 2️⃣ Data Transformation

* Feature engineering
* Data preprocessing
* Scaling and encoding

### 3️⃣ Data Clustering

* Uses clustering algorithms to group customers
* Generates cluster labels

### 4️⃣ Model Training

* Trains classification model using cluster labels
* Evaluates performance
* Saves trained model

### 5️⃣ Prediction Pipeline

* Accepts new customer data
* Applies preprocessing
* Predicts customer cluster dynamically

---

## 🌐 Web Application

A Flask-based web interface allows users to:

* Enter customer details
* Submit purchase information
* Predict customer personality segment instantly

---

## 🚀 Deployment

The application is deployed using Render:

1. Push project to GitHub
2. Connect repository with Render
3. Configure build and start commands
4. Deploy Flask application

---

## ▶️ Run Locally

### Clone Repository

```bash
git clone <your-repo-url>
cd project_name
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## 📊 Use Cases

* Customer segmentation
* Retail analytics
* Marketing personalization
* Customer behavior analysis

---

## 🔮 Future Improvements

* Real-time predictions
* Dashboard visualization
* Advanced clustering techniques
* Model monitoring

---

## 👨‍💻 Author

Ayush Ghadai
Bachelor's in Electronics and Computer Science
Machine Learning & Backend Development Enthusiast

---

⭐ If you found this project useful, give it a star on GitHub!
