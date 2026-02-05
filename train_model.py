import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Simple scam dataset (you can expand later)
texts = [
    "Congratulations you won a lottery",
    "Click here to claim your prize",
    "Urgent verify your bank account",
    "Send OTP to continue",
    "This is not a scam trust us",
    "Hello how are you",
    "Let's meet tomorrow",
    "This is a normal conversation",
    "Project meeting at 10am",
    "Dinner tonight?"
]

labels = [
    1, 1, 1, 1, 1,   # Scam
    0, 0, 0, 0, 0    # Not scam
]

# Vectorizer
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(texts)

# Model
model = LogisticRegression()
model.fit(X, labels)

# Save model
with open("scam_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save vectorizer
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Training complete!")
print("📦 Files generated: scam_model.pkl & vectorizer.pkl")
