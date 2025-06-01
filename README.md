---

# 🚢 Titanic Survival Predictor

This project is a simple **web application** that predicts whether a Titanic passenger would have survived or not based on user input. It uses a **logistic regression model** trained on the Titanic dataset from Kaggle.

The app is built using:

* **Flask** (backend framework)
* **HTML + Bootstrap** (frontend UI)
* **Scikit-learn** (machine learning)
* **Pickle** (to load the trained model and scaler)

---

## 🔍 Project Structure

```
├── app11.py               # Flask app
├── index.html             # Frontend template (Bootstrap form)
├── Project.ipynb          # Model training and preprocessing notebook
├── logreg_model.pkl       # Trained Logistic Regression model
├── scaler.pkl             # Scaler object for preprocessing
├── train.csv              # Titanic training data
├── test.csv               # Titanic test data
├── gender_submission.csv  # Sample submission (from Kaggle)
└── README.md              # Project documentation
```

---

## 🌟 Features

✅ Predicts survival based on:

* Passenger Class (Pclass)
* Sex
* Number of parents/children aboard (Parch)
* Fare paid
* Port of Embarkation

✅ **Web Interface** with Bootstrap

✅ **REST API endpoint** at `/api/predict`

✅ Preprocessing steps consistent with training:

* Missing value handling
* Label encoding
* One-hot encoding
* Scaling

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Nova6565/titanic-.git
```

### 2️⃣ Install required libraries

```bash
pip install flask pandas scikit-learn
```

### 3️⃣ Run the Flask app

```bash
python app11.py
```

The app will be live at:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🖥️ Usage

1️⃣ Go to the home page
2️⃣ Fill in the form fields:

* Pclass
* Sex
* Parch
* Fare
* Embarked

3️⃣ Click "Predict"

Result will show whether the passenger would have **Survived** or **Did Not Survive**.

---

## 📡 API Endpoint

### POST `/api/predict`

**Request body (JSON):**

```json
{
  "Pclass": 3,
  "Sex": "male",
  "Parch": 0,
  "Fare": 7.25,
  "Embarked": "S"
}
```

**Response:**

```json
{
  "prediction": 0
}
```

`prediction`:
`1` → Survived
`0` → Did Not Survive

---

## 🤖 Model Details

* Model: **Logistic Regression**
* Features used:

  * Pclass
  * Parch
  * Fare
  * Sex (encoded)
  * Embarked (one-hot)
* Scaler: StandardScaler

---

## 📂 Dataset

* Titanic Dataset from [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic)

Files used:

* `train.csv`
* `test.csv`

---

## 🏆 Future Improvements

* Improve model accuracy (try other classifiers)
* Add feature: Age
* Better UI design
* Deploy on cloud (Heroku, AWS, etc.)

---

## 🙏 Acknowledgements

* Kaggle Titanic Dataset
* Scikit-learn
* Flask

---
