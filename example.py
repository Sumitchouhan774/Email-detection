import joblib

model = joblib.load('spam_classifier.pkl')

emails = [
    "Congratulations! You've won a $1,000 Walmart gift card. Click here to claim now.",
    "Hi John, just wanted to check if you're free for a call tomorrow?",
    "URGENT: Your account has been compromised. Click to reset your password immediately!",
    "Hey, it was great seeing you at the reunion. Let’s catch up soon!",
    "Get 50% off your next purchase. Hurry, offer ends tonight!",
    "Meeting rescheduled to 3 PM on Thursday. Let me know if that works.",
    "Reminder: Your dentist appointment is scheduled for Monday at 11 AM."
] # you can add as many you can 

prediction = model.predict(emails)

# Interpret results
# 0 = Ham (legitimate email)
# 1 = Spam
print(prediction)