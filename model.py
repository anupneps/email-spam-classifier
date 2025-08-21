import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle

print("--- Starting Model Training ---")

# 1. Load the CLEANED dataset
#    The data is in 'spam_cleaned.csv'. No further cleaning is needed here.
df = pd.read_csv('spam_cleaned.csv')

# 2. Split data into features (X) and labels (y)

X = df['message']  # The text messages
y = df['label']    # The labels (0 for ham, 1 for spam

# 3. Split data into training and testing sets
#    Use a 80/20 split and a random_state for reproducibility.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training set size: {len(X_train)}, Test set size: {len(X_test)}")
print("--- Data split into training and testing sets ---")
print(f"Example training data: {X_train.head()}")
print(f"Example training labels: {y_train.head()}")
print(f"Example test data: {X_test.head()}")
print(f"Example test labels: {y_test.head()}")

# 4. Vectorize the text data
#    Initialize a CountVectorizer and fit it ONLY on the training data.
#    Then transform both the training and testing data.

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 5. Train the Naive Bayes classifier
#    Initialize a MultinomialNB model and train it with the vectorized training data.
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# 6. Evaluate the model (optional but good practice)
#    Make predictions on the test set and calculate the accuracy.
# <-- Predict on X_test_vec
accuracy = accuracy_score(y_test, model.predict(X_test_vec))
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# 7. Save the trained model AND the vectorizer
#    Use pickle to save both objects to .pkl files.
#    This is crucial, as you need the SAME vectorizer for prediction.

with open('spam_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)


print("--- Model and Vectorizer saved successfully! ---")
