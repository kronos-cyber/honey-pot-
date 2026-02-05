# Agentic Honey-Pot for Scam Detection & Intelligence Extraction

## Problem Statement
Online scam messages are rapidly increasing, causing financial loss and user harm. Traditional systems only block scams but fail to gather intelligence that could help prevent future fraud.

## Solution Overview
We built an **Agentic AI Honeypot** that:
1. Detects scam messages using a trained ML model
2. Engages scammers using a believable AI persona
3. Safely extracts intelligence such as UPI IDs and phishing links
4. Terminates interaction ethically without real user involvement

The system is designed for **fraud analysis, threat intelligence, and user safety**.

---

## Architecture
1. **Input**: Incoming message (text)
2. **Vectorization**: TF-IDF converts text into numerical features
3. **Classification Model**: Logistic Regression predicts scam probability
4. **Agentic Layer**:
   - Engages scammer if confidence > threshold
   - Uses a controlled persona
5. **Intelligence Extraction**:
   - UPI IDs
   - Phishing URLs
6. **Ethical Exit**:
   - No real transactions
   - No sensitive user data used

---

## Model Training
- Algorithm: Logistic Regression
- Features: TF-IDF Vectorized Text
- Training Script: `train_model.py`
- Outputs:
  - `scam_model.pkl`
  - `vectorizer.pkl`

Training is performed **offline** and models are loaded during API runtime to ensure stability.

---

## Agentic Behavior
Once a scam is detected:
- The AI agent simulates a semi-digital user persona
- Continues conversation only to extract scam indicators
- Stops interaction after intelligence extraction
- Flags ethical termination

No real user credentials or financial actions are performed.

---

## API Endpoints

### Health Check
