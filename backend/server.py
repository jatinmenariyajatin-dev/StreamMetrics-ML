from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Load trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return jsonify({
        "message": "Netflix Revenue Prediction API is Running..."
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        features = np.array([[
            float(data["ucan_members"]),
            float(data["emea_members"]),
            float(data["latam_members"]),
            float(data["apac_members"]),
            float(data["ucan_arpu"]),
            float(data["emea_arpu"]),
            float(data["latam_arpu"]),
            float(data["apac_arpu"])
        ]])

        prediction = model.predict(features)

        return jsonify({
            "prediction": round(float(prediction[0]), 2),
            "status": "success"
        })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)