#  Aurix — AI-Powered Anomaly Detection System

> **Fintech ML Case Study** | Decision-Support for Digital Gold Transactions

---

## Overview

This project builds an **AI-driven anomaly detection system** for Aurix, a digital gold trading platform. The system identifies suspicious transactions in real time and routes them through a 3-tier decision layer — from normal processing to compliance alerts.

---

## Problem Statement

Among thousands of daily gold transactions, some are anomalous — unusually large, high-frequency, or occurring at suspicious times. These may indicate fraud, bot activity, or data errors. The challenge: **no labelled fraud data exists at launch**.

**Solution:** Unsupervised anomaly detection (Isolation Forest) that works without labels, combined with a supervised baseline (Random Forest) to demonstrate the improvement path once labels are available.

---

## Project Structure

```
aurix-ml/
├── notebooks/
│   └── aurix_anomaly_detection.ipynb   # Full analysis notebook
├── outputs/
│   ├── eda_overview.png                # EDA dashboard
│   ├── model_evaluation.png            # Confusion matrix + scores
│   ├── pca_projection.png             # 2D transaction space
│   └── decision_dashboard.png         # Alert tiers + timeline
└── README.md
```

---

## Methodology

### Part 1 — Problem Framing
- **Task type:** Unsupervised anomaly detection
- **Input:** Transaction amount, user history, gold price, time features
- **Output:** Anomaly score → decision tier (Normal / Watch / Alert)

### Part 2 — Data Simulation & EDA
- 15,000 transactions across 500 users over 12 months
- Gold prices simulated via Geometric Brownian Motion (GBM)
- 3% anomaly injection (amounts 10–100× normal)

### Part 3 — Models

| Model | Type | ROC-AUC | Use Case |
|-------|------|---------|----------|
| Isolation Forest | Unsupervised | — | Production (no labels needed) |
| Random Forest | Supervised | **0.9999** | Post-labelling improvement |

Evaluation metrics include precision, recall, and ROC-AUC for the supervised model.
For the unsupervised model, anomaly score distributions and threshold percentiles were analysed.

### Part 4 — Decision Layer

| Tier | Threshold | Action |
|------|-----------|--------|
| 🟢 Normal | < 75th pct | Pass through |
| 🟡 Watch | 75–95th pct | Flag for manual review |
| 🔴 Alert | > 95th pct | Block + notify compliance |

### Part 5 — Research Insights
- **Why Isolation Forest:** No labels required, handles high-dimensional data, fast inference
- **Limitation:** Synthetic data; real model needs calibration on actual Aurix transactions
- **Next step:** Label collection → XGBoost/LightGBM with SHAP explainability
- **Deployment:** FastAPI microservice behind Kafka event stream, < 50ms latency target

- **Business Impact:**
The decision layer reduces false positives by separating suspicious activity
into WATCH and ALERT tiers, allowing compliance teams to prioritise
investigations efficiently.
The notebook produces the following figures:

- **Visualizations:**
- Transaction distribution and user activity (EDA)
- PCA projection of transaction space
- Model evaluation confusion matrix
- Decision-tier alert timeline
  
---

## Key Results

- **15,000 transactions** analysed
- **750 ALERT** transactions flagged (5%)
- **3,000 WATCH** transactions queued for review (20%)
- **Random Forest ROC-AUC: 0.9999** (supervised upper bound)

---
## EDA Findings

- Transaction amounts follow a right-skewed distribution
- Most users perform fewer than 20 transactions per month
- Night transactions show higher anomaly concentration
- Large anomalies cluster during high volatility gold price periods
---
  
## Feature Engineering

| Feature | Description |
|---------|-------------|
| `amount_zscore` | How unusual is this amount for this user? |
| `amount_in_grams` | Amount normalised by live gold price |
| `momentum` | 3-day gold price momentum |
| `is_night` | Transaction between 00:00–06:00 |
| `user_tx_count` | Cumulative user activity level |

---

## Tech Stack

- Python 3.12
- scikit-learn (Isolation Forest, Random Forest)
- pandas, NumPy
- Matplotlib, Seaborn


jupyter notebook notebooks/aurix_anomaly_detection.ipynb
```
