# 🌱 Smart Agriculture Monitoring System – Soil Quality Prediction

> 🚀 An end-to-end Machine Learning + Flask project that predicts soil quality based on key environmental parameters. Built with scalability in mind, with future deployment on AWS Cloud in progress.

---

## 📌 Project Overview

This project aims to support sustainable farming practices by developing a **Smart Agriculture Monitoring System** that classifies **soil quality** into categories such as **Poor**, **Moderate**, and **Fertile** based on six vital soil parameters:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH value

The solution is built using a **Decision Tree Classifier** and delivered through a **Flask-based web application** that allows users to input soil data and get real-time predictions.

---

## 🎯 Objectives

- Automate soil quality prediction using ML.
- Provide a user-friendly web interface for prediction.
- Work towards scalable cloud deployment for real-world usage.

---

## 🧠 Tech Stack

| Technology | Usage |
|------------|--------|
| Python | Core programming |
| Pandas & NumPy | Data preprocessing |
| Scikit-learn | Machine learning (Decision Tree Classifier) |
| Flask | Web framework |
| HTML/CSS | Frontend design |
| AWS (Planned) | For deployment (SageMaker + EC2) |

---

## 🛠️ Features

- ✅ Input form for soil characteristics
- ✅ Real-time prediction using a trained ML model
- ✅ Clean and simple UI
- ✅ Model saved using `pickle`
- 🔜 **Cloud deployment on AWS** coming soon (work in progress)

---

## 📸 Screenshot

![Web UI Screenshot](https://github.com/Nandini19062994/soil_flask_app/blob/main/static/screenshot.png)

🤖 Model Details
Algorithm: DecisionTreeClassifier

Training Data: Soil nutrients (e.g., nitrogen, phosphorus), moisture, temperature, and humidity

Output Labels:

Poor

Moderate

Fertile

The model outputs a labelled prediction based on the input values.

🌐 Deployment (Upcoming Work)
Currently, the application runs locally. Cloud deployment using AWS SageMaker, IoT Core, and other AWS services is in progress and will be updated here shortly.


📌 Features
Easy-to-use web interface using Flask

Lightweight ML model with high accuracy

Real-time prediction of soil quality

Scalable for cloud and IoT integrations

🔮 Future Enhancements
Cloud hosting on AWS with auto-scaling

Real-time sensor integration via IoT Core

Crop recommendation system based on soil output

Dashboard visualization using Power BI/Tableau


👩‍💻 Author
Nandini Rai
Machine Learning Engineer | Data Science Enthusiast
GitHub: @Nandini19062994
LinkedIn: https://www.linkedin.com/in/nandini-rai-5b93a4272/

🚀 How to Run Locally
1️⃣ Clone the Repository
   ```bash
   git clone https://github.com/Nandini19062994/soil_flask_app.git
   cd soil_flask_app
2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows

3️⃣ Install Required Libraries
pip install -r requirements.txt

4️⃣ Run the Flask App
```bash
python predict.py

5️⃣ Open in Browser
Visit: http://127.0.0.1:5000/

----









