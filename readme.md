# 📧 Email Spam Classifier

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey?logo=flask)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3-orange?logo=scikit-learn)

A **machine learning project** that classifies emails as **Spam** or **Not Spam (Ham)**.  
Built using **Python**, **Scikit-learn**, and **Flask**, this project takes raw email text and predicts spam with a trained Naive Bayes model.

> This project is a solution to the [CodeChef ML Email Spam Classifier](https://www.codechef.com/practice/machine-learning-projects).

---

## 📝 Features

- Clean and preprocess raw email text
- Vectorize emails using `CountVectorizer`
- Train a **Naive Bayes** classifier
- Deploy as a web app with **Flask**
- Instant spam prediction from user input

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/email-spam-classifier.git
cd email-spam-classifier
```

### 2. Install Dependencies

```bash
pip install --no-cache-dir pandas numpy scikit-learn flask
```

### 3. Prepare the Data

- Place the `spam.csv` file in the root folder.
- Run `data_cleaner.py` to clean the dataset and generate `spam_cleaned.csv`.

### 4. Train the Model

```bash
python model.py
```
- Run `model.py` to vectorize the cleaned data and train the Naive Bayes model.
- Generates `model.pkl` and `vectorizer.pkl` for the Flask app.

### 5. Run the Web App

```bash
python main.py
```

- Open [http://127.0.0.1:5000](http://127.0.0.1:5000)
- Paste email text and click **Check for Spam**

---

## 📂 Project Structure

```
email-spam-classifier/
│
├── model.py           # Train and save the ML model
├── main.py            # Flask app for predictions
├── index.html         # HTML template for input
├── spam.csv           # Raw dataset
├── spam_cleaned.csv   # Cleaned dataset
├── model.pkl          # Saved ML model
└── vectorizer.pkl     # Saved CountVectorizer
```

---

## 💻 Example Usage

```python
from joblib import load

model = load("model.pkl")
vectorizer = load("vectorizer.pkl")

email = ["Congratulations! You've won a prize. Click here to claim."]
vectorized_email = vectorizer.transform(email)
prediction = model.predict(vectorized_email)

print("Spam" if prediction[0] == 1 else "Not Spam")
```

---

## 🧠 How It Works

- **Data Cleaning** – Remove unnecessary columns, handle missing values, convert labels (`ham` → 0, `spam` → 1).
- **Text Vectorization** – Transform email text into numerical vectors with `CountVectorizer`.
- **Model Training** – Train a Naive Bayes classifier on the vectorized emails.
- **Deployment** – Serve the model with Flask and provide a web interface.

---

## 🛠 Technologies Used

- Python 3.x
- Pandas & NumPy
- Scikit-learn
- Flask

---


