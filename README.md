# 🚀 End-to-End Machine Learning Project — Customer Personality Segmentation

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Machine Learning](https://img.shields.io/badge/ML-ScikitLearn-orange)
![Flask](https://img.shields.io/badge/Framework-Flask-black)
![Deployment](https://img.shields.io/badge/Deploy-Render-green)

---

## 📌 Project Overview

Customer Personality Segmentation is an end-to-end Machine Learning project designed to analyze customer data and predict customer personality segments using machine learning algorithms.

The system helps malls, retail stores, and product-based companies understand customer behavior by grouping customers into meaningful clusters based on personal details and purchasing history.

This project demonstrates a complete production-level ML pipeline including:

* Data ingestion
* Data transformation
* Customer clustering
* Model training
* Prediction pipeline
* Flask web application
* Deployment using Render

---

## 🌐 Live Demo

You can access the deployed application here:

👉 [https://customer-categorization-94gw.onrender.com/prediction](https://customer-categorization-94gw.onrender.com/prediction)

Enter customer details and get real-time personality cluster prediction.

---

## 🎯 Problem Statement

Businesses collect large amounts of customer data, but extracting actionable insights from it can be challenging.

The objectives of this project are:

* Cluster customers based on behavioral and demographic data.
* Identify customer personality segments.
* Predict cluster numbers dynamically for new customers using classification techniques.

This enables:

* Targeted marketing strategies
* Personalized product recommendations
* Improved business decision-making

---


## 💡 Proposed Solution

The solution follows a machine learning pipeline:

1. Historical customer data is ingested and validated.
2. Customers are grouped using clustering algorithms.
3. Cluster labels are used to train a classification model.
4. New customer inputs are processed through the prediction pipeline to determine cluster type.

---

## 🧰 Tech Stack

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Backend Framework

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
│   ├── data_ingestion.py        # Data loading
│   ├── data_transformation.py   # Feature engineering & preprocessing
│   ├── data_clustering.py       # Customer clustering logic
│   ├── model_trainer.py         # Model training
│   ├── exception.py             # Custom exception handling
│   ├── logger.py                # Logging configuration
│
├── pipelines/
│   ├── model_prediction.py      # Prediction pipeline
│
├── artifacts/                   # Saved models and preprocessors
├── templates/                   # HTML files
├── static/                      # CSS and static assets
│
├── requirements.txt
├── README.md
```

---

## ⚙️ Machine Learning Workflow

### 1️⃣ Data Ingestion

* Reads raw dataset
* Loads data into pipeline

### 2️⃣ Data Transformation

* Feature engineering
* Encoding and scaling
* Data preprocessing pipeline

### 3️⃣ Data Clustering

* Groups customers into clusters
* Generates cluster labels

### 4️⃣ Model Training

* Trains classification model
* Evaluates performance
* Saves trained model

### 5️⃣ Prediction Pipeline

* Accepts new input data
* Applies preprocessing
* Predicts customer personality cluster

---

## ▶️ Run Locally

### Clone Repository

```bash
git clone https://github.com/Ayush-12334/Customer-Categorization.git
cd Customer-Categorization
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
* Model monitoring and tracking

---

## 👨‍💻 Author

Ayush Ghadai
Bachelor's in Electronics and Computer Science
Machine Learning & Backend Development Enthusiast

---

⭐ If you found this project useful, consider giving it a star on GitHub!
