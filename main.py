from flask import Flask, render_template, request
import pickle
import os

# Initialize the Flask application
app = Flask(__name__)

# --- Load Model and Vectorizer ---
# Use absolute paths to ensure the files are found regardless of where the script is run
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'spam_model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'vectorizer.pkl')

# Load the pre-trained model and vectorizer
# Add a try-except block to handle missing files gracefully.
try:
    with open(MODEL_PATH, 'rb') as model_file:
        model = pickle.load(model_file)
    with open(VECTORIZER_PATH, 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
except FileNotFoundError:
    print("Model files not found! Please run model.py first to train and save them.")
    model = None
    vectorizer = None
# --- END ---

# Define the main route for the home page
@app.route('/')
def home():
    # This function just needs to render the HTML template.
    return render_template('index.html')

# Define the route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    if model and vectorizer and request.method == 'POST':
        # 1. Get the email text from the form submission.
        #    The textarea in the HTML has name="email_text".
        email_text = request.form['email_text']

        # 2. Transform the input text using the LOADED vectorizer.
        #    The vectorizer expects a list of strings.
        email_vector = vectorizer.transform([email_text])

        # 3. Make a prediction using the LOADED model.
        prediction = model.predict(email_vector)

        # 4. Determine the result string ('Spam' or 'Not Spam').
        #    The model predicts 1 for spam, 0 for not spam.

        if prediction[0] == 1:
            result = 'Spam'
            result_class = 'spam'
        else:
            result = 'Not Spam'
            result_class = 'not-spam'

        result = 'Spam' if prediction[0] == 1 else 'Not Spam'
        
        # 5. Render the home page again, passing the prediction result to the template.
        return render_template('index.html', prediction=result, result_class=result_class)
    else:
        return render_template('index.html', prediction="Error: Model not loaded.")

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)