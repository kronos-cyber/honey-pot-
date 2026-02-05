from fastapi import FastAPI, Header, HTTPException
import pickle, re
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Honey-pot API is running"
    }

API_KEY = "TEST_API_KEY"

# 🔹 Load model once (correct)
with open("scam_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def predict(text):
    X = vectorizer.transform([text])
    return float(model.predict_proba(X)[0][1])

def extract(text):
    upi = re.findall(r'\b\w+@\w+\b', text)
    url = re.findall(r'https?://\S+', text)
    return {
        "upi_id": upi[0] if upi else None,
        "phishing_url": url[0] if url else None
    }

@app.get("/health")
def health():
    return {"status": "ok", "service": "agentic-honeypot"}

# ✅ TEST ENDPOINT
@app.post("/api/v1/test")
def test(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return {"status": "success", "timestamp": datetime.utcnow()}

# ✅ MAIN ENDPOINT (GUVI COMPATIBLE)
@app.post("/api/v1/agentic-honeypot/analyze")
def analyze(data: dict, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    msg = data.get("message", "")
    score = predict(msg)

    if score < 0.7:
        return {
            "is_scam": False,
            "confidence": score
        }

    return {
        "is_scam": True,
        "confidence": score,
        "agent_engaged": True,
        "persona_used": "Semi-Digital User",
        "extracted_intelligence": extract(msg),
        "ethical_exit": True
    }