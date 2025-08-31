from flask import Flask, request, jsonify
import hashlib, sqlite3

app = Flask(__name__)

DB_NAME = "flags.db"

def sha256_hash(value):
    return hashlib.sha256(value.encode()).hexdigest()

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS flags (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        challenge TEXT UNIQUE,
                        flag_hash TEXT NOT NULL)''')
    # Example challenge flags (hashes only)
    cursor.execute("INSERT OR IGNORE INTO flags (challenge, flag_hash) VALUES (?, ?)",
                   ("easy_challenge", sha256_hash("flag{easy123}")))
    cursor.execute("INSERT OR IGNORE INTO flags (challenge, flag_hash) VALUES (?, ?)",
                   ("web_challenge", sha256_hash("flag{webCTF}")))
    conn.commit()
    conn.close()

@app.before_request
def setup():
    init_db()

@app.route("/submit", methods=["POST"])
def submit_flag():
    data = request.get_json()
    challenge = data.get("challenge")
    submitted_flag = data.get("flag")

    if not challenge or not submitted_flag:
        return jsonify({"status": "error", "message": "Missing data"}), 400

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT flag_hash FROM flags WHERE challenge=?", (challenge,))
    row = cursor.fetchone()
    conn.close()

    if row and sha256_hash(submitted_flag) == row[0]:
        return jsonify({"status": "correct", "message": "Flag accepted ✅"}), 200
    else:
        return jsonify({"status": "incorrect", "message": "Wrong flag ❌"}), 403

if __name__ == "__main__":
    app.run(debug=True)
