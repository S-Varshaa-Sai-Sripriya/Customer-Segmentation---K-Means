# Customer Segmentation K-means from scractch

📌 Overview

This project implements Customer Segmentation using KMeans Clustering to group customers into distinct segments based on purchasing behavior and demographics.

---

📊 Dataset Explanation

### Customer Segmentation Dataset
The dataset contains demographic and purchasing behavior information of customers, often used for clustering and segmentation tasks in marketing.

- **Number of Instances**: ~200  
- **Number of Features**: 4 numerical + 1 identifier  
- **Target Variable**: None (unsupervised learning)

**Feature Details**:

- `CustomerID` – Unique identifier for each customer.  
- `Gender` – Gender of the customer (Male/Female).  
- `Age` – Age of the customer.  
- `Annual Income (k$)` – Annual income of the customer in thousand dollars.  
- `Spending Score (1-100)` – Score assigned based on customer spending behavior.

This dataset is useful for:

- Unsupervised learning tasks like clustering.  
- Identifying distinct customer groups for targeted marketing.  

---


Features

    Data Preprocessing: Handling missing values, outlier removal, scaling

    Data Transformation: Feature selection & transformation for clustering

    KMeans Clustering with Elbow Method

    Evaluation using silhouette score & visualization

    Modular Architecture for reusability

    Logging & Exception Handling for production readiness

---

Model Workflow

    Data Ingestion → Download dataset

    Preprocessing → Missing value handling, scaling

    Transformation → Feature selection, dimensionality reduction (if required)

    Clustering → KMeans with optimal k via Elbow Method

    Evaluation → Silhouette Score + Cluster visualization
