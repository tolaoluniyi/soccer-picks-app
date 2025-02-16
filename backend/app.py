from flask import Flask, jsonify
from predictor import predict_matches

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    predictions = predict_matches()
    return jsonify(predictions.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)
