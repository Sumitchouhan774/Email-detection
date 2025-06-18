import joblib

model = joblib.load('spam_classifier.pkl')

emails = [
    'Hey mohan, can we get together to watch footbal game tomorrow?',
    'Upto 20% discount on parking, exclusive offer just for you. Dont miss this reward!' 
]

prediction = model.predict(emails)
print(prediction)