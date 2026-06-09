"""
app.py — CyberShield Flask Web Application
==========================================
Python backend runs ALL real logic:
  - AES-256-CBC encryption/decryption
  - RSA-2048 OAEP key exchange
  - Key rotation manager
  - RBAC permission engine
  - TOTP MFA (RFC 6238)
  - PII detection & redaction
  - Audit logging (hash-chained)
  - Intrusion detection
  - Vulnerability scanner

Run:  python app.py
Then open:  http://127.0.0.1:5000
"""

from flask import Flask, render_template, request, jsonify, session
import os, sys
sys.path.insert(0, os.path.dirname(__file__))

from src.encryption      import AES256Encryptor, RSAKeyManager, KeyRotationManager
from src.access_control  import AuthManager, UserStore, RBACEngine
from src.monitoring      import AuditLogger, IntrusionDetector, VulnerabilityScanner
from src.data_classifier import DataClassifier

app = Flask(__name__)
app.secret_key = os.urandom(32)

# ── Global instances (in-memory for demo) ──
aes       = AES256Encryptor()
rsa_mgr   = RSAKeyManager()
km        = KeyRotationManager(rotation_interval_seconds=86400*30)
store     = UserStore()
auth_mgr  = AuthManager(store)
rbac      = RBACEngine()
classifier= DataClassifier()
logger    = AuditLogger("logs/audit.log")
ids       = IntrusionDetector()
scanner   = VulnerabilityScanner()

# Pre-generate RSA key pair once
_rsa_priv, _rsa_pub = rsa_mgr.generate_key_pair()

# Pre-create demo users
_demo_users = [
    ("alice",   "SuperSecure@123", "admin",        "alice@company.com"),
    ("bob",     "DataPass#456",    "data_analyst", "bob@company.com"),
    ("charlie", "EmpAccess!789",   "employee",     "charlie@company.com"),
    ("diana",   "Audit$Secure0",   "auditor",      "diana@company.com"),
]
for uid, pw, role, email in _demo_users:
    try:
        store.create_user(uid, pw, role, email)
    except ValueError:
        pass

# Pre-register demo keys
aes_key = aes.generate_key()
km.register_key("aes_key_001", aes_key)
km.register_key("session_key_003", aes.generate_key())
# Simulate a stale key
km.key_registry["db_key_002"] = {
    "key": "fake", "created_at": 0,
    "expires_at": 0, "active": True, "rotations": 0
}

# ════════════════════════════════════════════
#  PAGES
# ════════════════════════════════════════════

@app.route("/")
def index():
    return render_template("index.html")

# ════════════════════════════════════════════
#  API — DATA CLASSIFIER
# ════════════════════════════════════════════

@app.route("/api/classify", methods=["POST"])
def api_classify():
    text = request.json.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    result = classifier.scan_text(text, "web_input")
    return jsonify({
        "classification": result["classification"],
        "detected_types": list(result["detected_types"].keys()),
        "pii_found":      result["pii_found"],
        "policy":         result["policy"],
        "scanned_at":     result["scanned_at"],
    })

@app.route("/api/redact", methods=["POST"])
def api_redact():
    text = request.json.get("text", "")
    return jsonify({"redacted": classifier.redact(text), "original": text})

@app.route("/api/inventory", methods=["GET"])
def api_inventory():
    return jsonify(classifier.get_inventory_report())

# ════════════════════════════════════════════
#  API — ENCRYPTION
# ════════════════════════════════════════════

@app.route("/api/encrypt", methods=["POST"])
def api_encrypt():
    plaintext = request.json.get("plaintext", "")
    if not plaintext:
        return jsonify({"error": "No plaintext"}), 400
    key = aes.generate_key()
    payload = aes.encrypt(plaintext, key)
    # Store key in session so decrypt can use it
    session["last_key"] = key.hex()
    session["last_payload"] = payload
    return jsonify({
        "algorithm":  payload["algorithm"],
        "iv":         payload["iv"][:16] + "...",
        "ciphertext": payload["ciphertext"][:48] + "...",
        "checksum":   payload["checksum"][:32] + "...",
        "key_hex":    key.hex()[:32] + "...",
        "key_bits":   len(key) * 8,
        "timestamp":  payload["timestamp"],
    })

@app.route("/api/decrypt", methods=["POST"])
def api_decrypt():
    payload = session.get("last_payload")
    key_hex = session.get("last_key")
    if not payload or not key_hex:
        return jsonify({"error": "No encrypted data in session. Encrypt first."}), 400
    key = bytes.fromhex(key_hex)
    try:
        plaintext = aes.decrypt(payload, key)
        return jsonify({"plaintext": plaintext, "integrity": "VERIFIED"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/rsa_handshake", methods=["POST"])
def api_rsa_handshake():
    key = aes.generate_key()
    encrypted_key = rsa_mgr.encrypt_key(key, _rsa_pub)
    recovered_key = rsa_mgr.decrypt_key(encrypted_key, _rsa_priv)
    match = recovered_key == key
    return jsonify({
        "key_size_bits":   2048,
        "padding":         "OAEP-SHA256",
        "aes_key_sample":  key.hex()[:16] + "...",
        "encrypted_sample":encrypted_key.hex()[:20] + "...",
        "match":           match,
        "steps": [
            "RSA-2048 key pair generated (e=65537)",
            "AES-256 session key generated: " + key.hex()[:16] + "...",
            "AES key encrypted with RSA public key (OAEP)",
            "AES key decrypted with RSA private key",
            "Key match verification: " + str(match).upper(),
        ]
    })

@app.route("/api/key_status", methods=["GET"])
def api_key_status():
    return jsonify(km.get_key_status_report())

@app.route("/api/rotate_key", methods=["POST"])
def api_rotate_key():
    key_id = request.json.get("key_id")
    if not key_id:
        return jsonify({"error": "No key_id"}), 400
    new_key = km.rotate_key(key_id)
    return jsonify({
        "key_id":  key_id,
        "new_key": new_key.hex()[:16] + "...",
        "valid":   km.is_key_valid(key_id),
        "report":  km.get_key_status_report(),
    })

# ════════════════════════════════════════════
#  API — ACCESS CONTROL
# ════════════════════════════════════════════

@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.json
    uid, pw = data.get("username",""), data.get("password","")
    try:
        result = auth_mgr.authenticate(uid, pw)
        session["mfa_user"] = uid
        session["mfa_otp"]  = result["otp_hint"]
        logger.log("AUTH", uid, "LOGIN_ATTEMPT", "auth_service", "MFA_REQUIRED")
        return jsonify({"status": "mfa_required", "user": uid,
                        "otp": result["otp_hint"]})  # shown for demo
    except PermissionError as e:
        logger.log("AUTH", uid, "LOGIN_BLOCKED", "auth_service", "LOCKED")
        return jsonify({"error": str(e)}), 403
    except Exception as e:
        logger.log("AUTH", uid, "LOGIN_FAILED", "auth_service", "FAILED")
        return jsonify({"error": str(e)}), 401

@app.route("/api/verify_mfa", methods=["POST"])
def api_verify_mfa():
    otp = request.json.get("otp","")
    uid = session.get("mfa_user")
    if not uid:
        return jsonify({"error": "No login attempt in progress"}), 400
    try:
        token = auth_mgr.verify_mfa_and_login(uid, otp)
        session["token"] = token
        user = store.get_user(uid)
        logger.log("AUTH", uid, "LOGIN_SUCCESS", "auth_service", "SUCCESS")
        return jsonify({"token": token[:16]+"...", "user": uid,
                        "role": user["role"], "session_minutes": 60})
    except Exception as e:
        return jsonify({"error": str(e)}), 401

@app.route("/api/check_permission", methods=["POST"])
def api_check_permission():
    role = request.json.get("role","")
    perm = request.json.get("permission","")
    allowed = rbac.has_permission(role, perm)
    logger.log("RBAC", "system", f"CHECK_{perm}", role,
               "GRANTED" if allowed else "DENIED")
    return jsonify({"role": role, "permission": perm, "allowed": allowed,
                    "all_permissions": rbac.get_permissions(role)})

@app.route("/api/permission_matrix", methods=["GET"])
def api_permission_matrix():
    return jsonify(rbac.compare_roles())

@app.route("/api/users", methods=["GET"])
def api_users():
    return jsonify(store.list_users())

# ════════════════════════════════════════════
#  API — MONITORING
# ════════════════════════════════════════════

@app.route("/api/log_event", methods=["POST"])
def api_log_event():
    d = request.json
    entry = logger.log(
        d.get("event_type","SYSTEM"),
        d.get("user_id","unknown"),
        d.get("action","ACTION"),
        d.get("resource",""),
        d.get("status","SUCCESS"),
    )
    return jsonify({"logged": True, "chain_hash": entry["chain_hash"][:16]+"..."})

@app.route("/api/audit_log", methods=["GET"])
def api_audit_log():
    return jsonify({"entries": logger.entries[-20:], "summary": logger.get_summary()})

@app.route("/api/verify_chain", methods=["GET"])
def api_verify_chain():
    return jsonify(logger.verify_integrity())

@app.route("/api/simulate_attack", methods=["POST"])
def api_simulate_attack():
    attack = request.json.get("type","brute_force")
    alerts = []
    if attack == "brute_force":
        for _ in range(6):
            a = ids.check_brute_force("203.0.113.42", success=False)
            if a:
                alerts.append(a)
                break
        logger.log("IDS", "system", "BRUTE_FORCE_DETECTED", "auth_service", "ALERT")
    elif attack == "unauthorized":
        a = ids.check_unauthorized_permission("charlie","employee","delete_data")
        alerts.append(a)
        logger.log("IDS", "charlie", "UNAUTH_ACCESS", "hr_database", "DENIED")
    elif attack == "off_hours":
        a = ids.check_off_hours_access("bob","data_analyst")
        if a: alerts.append(a)
    return jsonify({"alerts": alerts, "total_alerts": len(ids.get_alerts())})

# ════════════════════════════════════════════
#  API — VULNERABILITY SCANNER
# ════════════════════════════════════════════

@app.route("/api/vuln_scan", methods=["POST"])
def api_vuln_scan():
    d = request.json
    users = store.list_users()
    config = {
        "users":           users,
        "mfa_status":      {u["user_id"]: d.get("mfa_enabled", True) for u in users},
        "key_ages":        {"aes_key_001": d.get("key_age", 5),
                            "db_key_002":  d.get("key_age", 5)},
        "tls_version":     d.get("tls_version","TLS1.3"),
        "password_policy": {"min_length": d.get("pw_min_length",12),
                            "require_special": True}
    }
    result = scanner.scan(config)
    return jsonify(result)

# ════════════════════════════════════════════

if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    print("\n" + "═"*55)
    print("  🛡  CyberShield Flask Web App")
    print("  Open your browser: http://127.0.0.1:5000")
    print("═"*55 + "\n")
    app.run(debug=True, port=5000)
