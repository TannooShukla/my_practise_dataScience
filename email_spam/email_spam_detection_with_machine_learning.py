# -*- coding: utf-8 -*-
"""oasis_Task_4_Email spam Detection with Machine Learning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/143T9_6O1tYvJiKSaEQX6_EuHdBFBPwC4

**Step 1: Import Required Libraries**
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

"""**Step 2: Load the Dataset**"""

# Load the dataset (your file is named 'spam.csv')
df = pd.read_csv('spam.csv', encoding='latin-1')

# Display first 5 rows to understand structure
print(df.head())

"""**Step 3: Clean the Dataset**"""

# Keep only necessary columns
df = df[['v1', 'v2']]

# Rename the columns
df.columns = ['label', 'message']

# Convert labels: 'ham' → 0, 'spam' → 1
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

""" **Step 4: Split the Data into Training and Testing Sets**"""

# Split into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    df['message'], df['label'], test_size=0.2, random_state=42
)

"""** Step 5: Text Vectorization using TF-IDF**"""

# Convert text messages to TF-IDF feature vectors
vectorizer = TfidfVectorizer(stop_words='english')

# Fit on training data and transform both training and test
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

"""**Step 6: Train the Machine Learning Model**"""

# Use Naive Bayes (works well with text)
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

"""**Step 7: Make Predictions and Evaluate the Model**"""

# Predict on the test set
y_pred = model.predict(X_test_tfidf)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

"""**Step 8: Test the Model on Custom Input**"""

def predict_message(msg):
    msg_tfidf = vectorizer.transform([msg])
    prediction = model.predict(msg_tfidf)[0]
    return "Spam" if prediction == 1 else "Not Spam"

# Example
print(predict_message("You won a free iPhone! Click here to claim."))  # Expected: Spam

