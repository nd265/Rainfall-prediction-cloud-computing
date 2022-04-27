from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("<S3 path>")

# Return model's prediction for the given data
def return_prediction(data):

    return model.predict([data]).tolist()

# Home page route
@app.route("/")
def index():

    return """
    <h1>Welcome to our rain prediction service</h1>
    To use this service, make a JSON post request to the /predict url with 25 climate model outputs.
    """

# Predict route to get model prediction
@app.route('/predict', methods=['POST'])
def rainfall_prediction():
    
    # extracts the JSON content
    content = request.json
    # get the model prediction
    prediction = return_prediction(content["data"])
    # construct response object
    results = {"Input": content["data"], "Prediction": prediction}

    # jsonify the response object
    return jsonify(results)