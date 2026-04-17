# 🚀 Web3 API Security Dashboard

An AI-powered Web3 API Security Monitoring Dashboard that detects anomalies in blockchain traffic using the Isolation Forest algorithm. The system provides real-time monitoring, visualization, and alerting through an interactive Streamlit dashboard.

---

## 📌 Project Overview

Web3 applications rely heavily on APIs for transactions such as DeFi, NFTs, and oracle data. These APIs are vulnerable to abnormal traffic and attacks.

This project simulates real-time Web3 API traffic and uses Machine Learning to detect anomalies and visualize them in a user-friendly dashboard.

---

## 🎯 Objectives

- Monitor API traffic in real-time  
- Detect anomalies using AI (Isolation Forest)  
- Visualize blockchain activity  
- Provide live alerts for suspicious behavior  

---

## ⚙️ Features

- 📈 Real-time API traffic monitoring  
- 🤖 AI-based anomaly detection  
- 🔴 Red spike visualization for anomalies  
- 🌐 Chain-wise traffic analysis (Ethereum, Polygon, etc.)  
- 📊 Confusion matrix & performance metrics  
- 🚨 Live alert system  
- 🔄 Auto-refresh dashboard  

---

## 🧠 Machine Learning Model

This project uses **Isolation Forest**, an unsupervised learning algorithm for anomaly detection.

**Why Isolation Forest?**
- Works well with unlabeled data  
- Efficient for large datasets  
- Detects rare and abnormal patterns  

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (Dashboard UI)
- **Pandas** (Data processing)
- **Plotly** (Visualization)
- **Scikit-learn** (Machine Learning)

---

## 📊 Dashboard Components

- 🔝 **Metrics Section** (Requests, Anomalies, Accuracy, Precision, Recall)  
- 📈 **Traffic Graph** (API activity over time)  
- 🌐 **Chain-wise Analysis**  
- 🚨 **Anomaly Detection Graph (Red Points)**  
- 📊 **Confusion Matrix**  
- 📊 **Latency Distribution**  
- 🚨 **Live Alerts Table**  

---

## 🔄 Real-Time Simulation

The system simulates live API traffic using dynamically generated data and updates the dashboard automatically to mimic real-world monitoring.

---

---

## ▶️ How to Run

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/web3-api-security-dashboard.git
cd web3-api-security-dashboard
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Application
streamlit run streamlit_app.py
📁 Project Structure
web3-api-security-dashboard/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   └── dataset.csv (optional)
│
├── README.md
└── requirements.txt
