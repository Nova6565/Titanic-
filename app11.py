# app.py
from flask import Flask, request, render_template, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model and preprocessing objects
with open('logreg_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Helper preprocess function (same as training)
def preprocess_input(data):

    df = pd.DataFrame([data])

    # Fill missing
    df['Fare'] = df['Fare'].fillna(df['Fare'].median())
    df['Embarked'] = df['Embarked'].fillna('S')

    # Encode Sex
    df['Sex_enc'] = df['Sex'].map({'male': 1, 'female': 0})

    # One-hot Embarked
    df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)
    for col in ['Embarked_Q', 'Embarked_S']:
        if col not in df:
            df[col] = 0

    # Select features
    features = ['Pclass','Parch','Fare','Sex_enc','Embarked_Q','Embarked_S']
    X = df[features]

    # Scale numeric
    X['Fare'] = scaler.transform(X[['Fare']]).ravel()
    return X

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    data = {
        'Pclass': int(request.form['Pclass']),
        'Sex': request.form['Sex'],
        'Parch': int(request.form['Parch']),
        'Fare': float(request.form['Fare']),
        'Embarked': request.form['Embarked']
    }
    X = preprocess_input(data)
    pred = model.predict(X)[0]
    result = 'Survived' if pred == 1 else 'Did Not Survive'
    return render_template('index.html', prediction=result)

@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.json
    X = preprocess_input(data)
    pred = model.predict(X)[0]
    return jsonify({'prediction': int(pred)})

if __name__ == '__main__':
    app.run(debug=True)
