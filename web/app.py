import pandas as pd
from joblib import load
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/predict_gdp', methods=['POST'])
def predict_gdp():
    """
    Endpoint to accept JSON input and return predicted GDP per capita.
    """
    # Get JSON data from the request
    data = request.json

    # Extract continent from the data and convert to lowercase
    continent = data.pop("continent")
    continent = continent.lower()

    # Load the corresponding trained model based on the continent
    try:
        model = load(f"models/trained_predictor_{continent}.joblib")
    except FileNotFoundError:
        return "Model not found for the specified continent!", 404

    # Create a DataFrame from the remaining JSON data
    new_data = pd.DataFrame.from_dict(data, orient='index', columns=['value']).T

    # Predict GDP per capita using the loaded model
    try:
        predicted_gdp_per_capita = model.predict(new_data)[0]
    except Exception:
        return "Invalid Features Given", 500

    # Return predicted GDP per capita as JSON response
    return jsonify({'predicted_gdp_per_capita': predicted_gdp_per_capita})


if __name__ == '__main__':
    app.run(debug=True)
