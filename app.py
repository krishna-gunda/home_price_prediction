from flask import Flask, render_template, request
import numpy as np
import pickle

# Load trained model
with open('House_Price.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form values in correct order
        values = [float(x) for x in request.form.values()]

        final_input = np.array([values])

        prediction = model.predict(final_input)[0]

        return render_template('index.html',
                               prediction_text=f"Predicted House Price: {round(prediction, 2)}")
    except Exception as e:
        return render_template('index.html',
                               prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)

