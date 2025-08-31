# 🏴‍☠️ Simple CTF Flag Checker

A lightweight **Flask app** that simulates a CTF challenge flag checker.

---

## 🚀 Features
- Submit challenge flags via API
- Flags are stored **securely as SHA256 hashes**
- Example challenges included:
  - `easy_challenge` → flag: `flag{easy123}`
  - `web_challenge` → flag: `flag{webCTF}`

---

## 📦 Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/Teraz1/ctf-flag-checker.git
   cd ctf-flag-checker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run app:
   ```bash
   python app.py
   ```

---

## 🎯 Usage
Submit a flag with `curl` or Postman:
```bash
curl -X POST http://127.0.0.1:5000/submit \\
  -H "Content-Type: application/json" \\
  -d '{"challenge": "easy_challenge", "flag": "flag{easy123}"}'
```

✅ Correct flag → `{ "status": "correct", "message": "Flag accepted ✅" }`  
❌ Wrong flag → `{ "status": "incorrect", "message": "Wrong flag ❌" }`

---

## ⚠️ Notes
- Flags are **hashed** (not stored in plain text).  
- This is an **educational demo** for CTF-style validation.  
