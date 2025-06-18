# Email Spam Classifier

A machine learning model that classifies emails as spam or non-spam (ham) using Naive Bayes classification.

## Overview

This project provides a trained machine learning model that can predict whether an email message is spam or legitimate. The model was trained on a dataset of labeled emails and uses Natural Language Processing techniques to make predictions.

## Requirements

- Python 3.x
- Required packages:
  ```bash
  pip install scikit-learn joblib
  ```

## Usage

1. Make sure you have the `spam_classifier.pkl` model file in your working directory.

2. Here's a simple example of how to use the model:
```python
import joblib

# Load the trained model
model = joblib.load('spam_classifier.pkl')

# Prepare your email messages
emails = [
    'Your message here',
    'Another message to test'
]

# Get predictions
predictions = model.predict(emails)

# Interpret results
# 0 = Ham (legitimate email)
# 1 = Spam
print(predictions)
```

### Example

```python
emails = [
    'Hey friend, can we get together to watch football game tomorrow?',
    'Upto 20% discount on parking, exclusive offer just for you. Dont miss this reward!'
] # you can add as many as you need to test or check
predictions = model.predict(emails)
# Output: [0, 1] (First message is ham, second is spam)
```

## Model Information

- The model uses a pipeline that combines:
  - `CountVectorizer` for text feature extraction
  - `MultinomialNB` (Multinomial Naive Bayes) for classification
- Achieved accuracy score of ~98% on test data
- Trained on a dataset containing both spam and legitimate emails

## Training the Model

If you want to retrain the model, you can use the provided [naive_bayes_email_det.ipynb](naive_bayes_email_det.ipynb) Jupyter notebook. The notebook contains the complete training process including:
- Data preprocessing
- Model training
- Evaluation
- Model saving

## Files Description

- `spam_classifier.pkl`: The trained model file
- `example.py`: Example script showing how to use the model
- `naive_bayes_email_det.ipynb`: Jupyter notebook containing the model training process
- `spam.csv`: Dataset used for training (if included)
