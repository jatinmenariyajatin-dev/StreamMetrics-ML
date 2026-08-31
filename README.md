# StreamMetrics-ML

## 📌 Project Overview

**StreamMetrics-ML** is a Machine Learning based Flask API that predicts Netflix revenue using regional membership and ARPU (Average Revenue Per User) data.

The API accepts Netflix business metrics through a JSON request and returns the predicted revenue.

## 🚀 Features

* Netflix Revenue Prediction
* Machine Learning model integration
* Flask REST API
* CORS support
* JSON-based API requests
* Trained model loaded using Joblib
* Error handling for invalid requests

## 🛠️ Technologies Used

* Python
* Flask
* Flask-CORS
* NumPy
* Joblib
* Scikit-learn
* Machine Learning

## 📂 Project Structure

```text
StreamMetrics-ML/
│
├── server.py
├── model.pkl
├── requirements.txt
└── README.md
```

## 📊 Input Features

The prediction model uses the following 8 features:

| Feature         | Description                    |
| --------------- | ------------------------------ |
| `ucan_members`  | UCAN region members            |
| `emea_members`  | EMEA region members            |
| `latam_members` | LATAM region members           |
| `apac_members`  | APAC region members            |
| `ucan_arpu`     | UCAN Average Revenue Per User  |
| `emea_arpu`     | EMEA Average Revenue Per User  |
| `latam_arpu`    | LATAM Average Revenue Per User |
| `apac_arpu`     | APAC Average Revenue Per User  |

## ⚙️ Installation

Clone the repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Go to the project directory:

```bash
cd StreamMetrics-ML
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ Run the API

Start the Flask server:

```bash
python server.py
```

The API will run on:

```text
http://localhost:5000
```

## 🔗 API Endpoints

### 1. Home

**GET**

```text
/
```

Example:

```text
http://localhost:5000/
```

Response:

```json
{
    "message": "Netflix Revenue Prediction API is Running..."
}
```

### 2. Predict Revenue

**POST**

```text
/predict
```

Example:

```text
http://localhost:5000/predict
```

### 📥 Request Body

Send the following JSON data:

```json
{
    "ucan_members": 75000000,
    "emea_members": 90000000,
    "latam_members": 50000000,
    "apac_members": 40000000,
    "ucan_arpu": 15.5,
    "emea_arpu": 10.2,
    "latam_arpu": 8.5,
    "apac_arpu": 7.8
}
```

### 📤 Response

```json
{
    "prediction": 12345.67,
    "status": "success"
}
```

The actual prediction value depends on the trained `model.pkl`.

## 🤖 Machine Learning Model

The trained Machine Learning model is stored in:

```text
model.pkl
```

The Flask application loads the model using Joblib:

```python
model = joblib.load("model.pkl")
```

The model receives the 8 input features and generates the predicted Netflix revenue.

## 🔄 API Workflow

```text
User / Frontend
      ↓
POST /predict
      ↓
JSON Input
      ↓
Feature Processing
      ↓
Machine Learning Model
      ↓
Revenue Prediction
      ↓
JSON Response
```

## 🧪 Testing

You can test the API using:

* Postman
* Thunder Client
* REST Client
* Frontend application

## 👨‍💻 Author

**Jatin Menariya**

## 📄 License

This project is available for educational and portfolio purposes.
