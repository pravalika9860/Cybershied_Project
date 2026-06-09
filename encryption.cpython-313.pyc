"""
encryption.py
=============
Handles AES-256 encryption for data at rest and TLS/SSL simulation for data in transit.
Part of: CyberShield - Protecting Sensitive Data with Encryption and Access Control
Author: GPI Internship Project | Cloud Counselage
"""

import os
import base64
import hashlib
import json
import time
from datetime import datetime
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet


# ─────────────────────────────────────────────
#  AES-256 Encryption (Data at Rest)
# ─────────────────────────────────────────────

class AES256Encryptor:
    """
    Provides AES-256-CBC encryption/decryption for sensitive data at rest.
    Keys are randomly generated and stored securely (never hardcoded).
    """

    KEY_SIZE = 32   # 256 bits
    IV_SIZE  = 16   # 128 bits

    def __init__(self):
        self.backend = default_backend()

    def generate_key(self) -> bytes:
        """Generate a cryptographically secure 256-bit key."""
        return os.urandom(self.KEY_SIZE)

    def generate_iv(self) -> bytes:
        """Generate a random Initialization Vector."""
        return os.urandom(self.IV_SIZE)

    def encrypt(self, plaintext: str, key: bytes) -> dict:
        """
        Encrypt plaintext using AES-256-CBC.
        Returns a dict with iv, ciphertext (base64), and checksum.
        """
        iv = self.generate_iv()
        padder = padding.PKCS7(128).padder()
        padded = padder.update(plaintext.encode()) + padder.finalize()

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded) + encryptor.finalize()

        checksum = hashlib.sha256(ciphertext).hexdigest()

        return {
            "algorithm"  : "AES-256-CBC",
            "iv"         : base64.b64encode(iv).decode(),
            "ciphertext" : base64.b64encode(ciphertext).decode(),
            "checksum"   : checksum,
            "timestamp"  : datetime.utcnow().isoformat() + "Z"
        }

    def decrypt(self, payload: dict, key: bytes) -> str:
        """Decrypt AES-256-CBC encrypted payload. Verifies checksum before decryption."""
        ciphertext = base64.b64decode(payload["ciphertext"])
        iv         = base64.b64decode(payload["iv"])

        # Integrity check
        computed = hashlib.sha256(ciphertext).hexdigest()
        if computed != payload["checksum"]:
            raise ValueError("INTEGRITY CHECK FAILED: Data may have been tampered with!")

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        padded = decryptor.update(ciphertext) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        return (unpadder.update(padded) + unpadder.finalize()).decode()


# ─────────────────────────────────────────────
#  RSA-2048 (Key Exchange / Asymmetric)
# ─────────────────────────────────────────────

class RSAKeyManager:
    """
    Manages RSA-2048 key pairs for secure AES key exchange (simulating TLS handshake).
    """

    def __init__(self, key_size: int = 2048):
        self.key_size = key_size
        self.backend  = default_backend()

    def generate_key_pair(self):
        """Generate RSA public/private key pair."""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=self.key_size,
            backend=self.backend
        )
        return private_key, private_key.public_key()

    def encrypt_key(self, aes_key: bytes, public_key) -> bytes:
        """Encrypt AES key with RSA public key (OAEP padding)."""
        return public_key.encrypt(
            aes_key,
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def decrypt_key(self, encrypted_key: bytes, private_key) -> bytes:
        """Decrypt AES key with RSA private key."""
        return private_key.decrypt(
            encrypted_key,
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )


# ─────────────────────────────────────────────
#  Key Rotation Manager
# ─────────────────────────────────────────────

class KeyRotationManager:
    """
    Manages encryption key lifecycle: generation, rotation, and expiry tracking.
    Keys are rotated every N seconds (configurable; default 30 days in production).
    """

    def __init__(self, rotation_interval_seconds: int = 2592000):  # 30 days
        self.rotation_interval = rotation_interval_seconds
        self.key_registry: dict = {}

    def register_key(self, key_id: str, key: bytes) -> dict:
        """Register a new key with metadata."""
        entry = {
            "key"        : base64.b64encode(key).decode(),
            "created_at" : time.time(),
            "expires_at" : time.time() + self.rotation_interval,
            "active"     : True,
            "rotations"  : 0
        }
        self.key_registry[key_id] = entry
        return entry

    def rotate_key(self, key_id: str) -> bytes:
        """Rotate a key and return the new key."""
        new_key = os.urandom(32)
        if key_id in self.key_registry:
            self.key_registry[key_id]["rotations"] += 1
            self.key_registry[key_id]["key"] = base64.b64encode(new_key).decode()
            self.key_registry[key_id]["created_at"] = time.time()
            self.key_registry[key_id]["expires_at"] = time.time() + self.rotation_interval
        return new_key

    def is_key_valid(self, key_id: str) -> bool:
        """Check if a key is active and not expired."""
        if key_id not in self.key_registry:
            return False
        entry = self.key_registry[key_id]
        return entry["active"] and time.time() < entry["expires_at"]

    def get_key_status_report(self) -> list:
        """Return status report of all registered keys."""
        report = []
        for kid, entry in self.key_registry.items():
            expired = time.time() > entry["expires_at"]
            report.append({
                "key_id"    : kid,
                "active"    : entry["active"] and not expired,
                "expired"   : expired,
                "rotations" : entry["rotations"],
                "expires_in": max(0, entry["expires_at"] - time.time())
            })
        return report


# ─────────────────────────────────────────────
#  Fernet (Simple Symmetric — for config data)
# ─────────────────────────────────────────────

class FernetEncryptor:
    """Simplified Fernet encryption for configuration and non-critical data."""

    def __init__(self):
        self.key = Fernet.generate_key()
        self.f   = Fernet(self.key)

    def encrypt(self, data: str) -> str:
        return self.f.encrypt(data.encode()).decode()

    def decrypt(self, token: str) -> str:
        return self.f.decrypt(token.encode()).decode()
