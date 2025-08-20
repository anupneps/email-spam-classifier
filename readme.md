# Email Spam Classifier

Hello developers! Welcome to this exciting project where we will build a complete Email Spam Classifier from the ground up.

Our end goal is to create a functional tool that can analyze the text of an email and accurately classify it as 'Spam' or 'Not Spam' (often called 'Ham').

We've split the entire project into three distinct parts to guide you from the basics to a fully functional machine learning model:

- **Part 1:** Manual Text Vectorization for Spam Detection  
- **Part 2:** Cleaning the Spam Dataset  
- **Part 3:** Training a Real ML Model with Scikit-learn  

In Machine Learning, vectorization refers to the process of converting text data into numerical vectors so that it can be fed into machine learning models.

---

## Part 1

Manually build a spam detector with basic Python, converting text to numerical vectors to learn the core logic of text classification.

### Problem Statement

Before a machine can learn from text, the text must be converted into numbers. The most common way to do this is through a process called vectorization.

Your task is to write a Python script that manually performs this conversion without using any machine learning libraries like Scikit-learn.

You will:

1. Start with a small list of sample text messages (called the corpus).
2. Write a function called `build_vocabulary(corpus)` that returns a sorted list of unique words across all messages in the corpus.
3. Write another function called `vectorize_text(text, vocabulary)` that takes a single message and the vocabulary, and returns a numerical vector showing how many times each vocabulary word appears in the message.
4. Use the above function to vectorize each message in the corpus and display their vector representations.

### Your output should look like this

**Vocabulary (36 words):**
