from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and fitted scaler
model = joblib.load('wine_quality_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect features from form
        features = [float(request.form['fixed_acidity']),
                    float(request.form['volatile_acidity']),
                    float(request.form['citric_acid']),
                    float(request.form['residual_sugar']),
                    float(request.form['chlorides']),
                    float(request.form['free_sulfur_dioxide']),
                    float(request.form['total_sulfur_dioxide']),
                    float(request.form['density']),
                    float(request.form['pH']),
                    float(request.form['sulphates']),
                    float(request.form['alcohol'])]
        
        # Scale the features
        features_scaled = scaler.transform(np.array(features).reshape(1, -1))
        
        # Make prediction
        prediction = model.predict(features_scaled)

        return render_template('result.html', prediction=prediction[0])
    except Exception as e:
        return render_template('index.html', prediction="Error: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)
