"""
data_classifier.py
==================
Identifies, classifies, and inventories sensitive data within the organization.
Implements GDPR / HIPAA awareness for data protection compliance.
Part of: CyberShield - Protecting Sensitive Data with Encryption and Access Control
Author: GPI Internship Project | Cloud Counselage
"""

import re
import json
from datetime import datetime
from typing import Any


# ─────────────────────────────────────────────
#  Sensitivity Classifications
# ─────────────────────────────────────────────

CLASSIFICATION_LEVELS = {
    "TOP_SECRET" : {"label": "Top Secret",  "color": "red",    "encrypt": True,  "mfa_required": True},
    "CONFIDENTIAL":{"label": "Confidential","color": "orange", "encrypt": True,  "mfa_required": True},
    "INTERNAL"   : {"label": "Internal",    "color": "yellow", "encrypt": True,  "mfa_required": False},
    "PUBLIC"     : {"label": "Public",      "color": "green",  "encrypt": False, "mfa_required": False},
}


# ─────────────────────────────────────────────
#  PII / PHI Detection Patterns
# ─────────────────────────────────────────────

SENSITIVE_PATTERNS = {
    "EMAIL"         : r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}",
    "PHONE"         : r"\b(\+?1[\-\s]?)?\(?\d{3}\)?[\-\s]?\d{3}[\-\s]?\d{4}\b",
    "CREDIT_CARD"   : r"\b(?:\d{4}[\-\s]?){3}\d{4}\b",
    "SSN"           : r"\b\d{3}-\d{2}-\d{4}\b",
    "IP_ADDRESS"    : r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "AADHAAR"       : r"\b\d{4}\s\d{4}\s\d{4}\b",          # Indian ID
    "PAN_CARD"      : r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",        # Indian PAN
    "PASSPORT"      : r"\b[A-Z][0-9]{7}\b",
    "BANK_ACCOUNT"  : r"\b\d{9,18}\b",
    "PASSWORD_HINT" : r"(?i)(password|passwd|pwd)\s*[:=]\s*\S+",
    "API_KEY"       : r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*[A-Za-z0-9_\-]{16,}",
}


class DataClassifier:
    """
    Scans text/records for sensitive data patterns and assigns a classification level.
    Used to build a data inventory and enforce appropriate protection controls.
    """

    def __init__(self):
        self.compiled = {
            name: re.compile(pattern)
            for name, pattern in SENSITIVE_PATTERNS.items()
        }
        self.inventory: list = []

    def scan_text(self, text: str, source_label: str = "unknown") -> dict:
        """
        Scan a string for sensitive data patterns.
        Returns classification and list of detected types (NOT the actual values).
        """
        detected = {}
        for ptype, pattern in self.compiled.items():
            matches = pattern.findall(text)
            if matches:
                detected[ptype] = len(matches)

        # Assign classification based on what was found
        classification = self._classify(detected)
        result = {
            "source"         : source_label,
            "scanned_at"     : datetime.utcnow().isoformat(),
            "detected_types" : detected,
            "classification" : classification,
            "policy"         : CLASSIFICATION_LEVELS[classification],
            "pii_found"      : len(detected) > 0
        }
        self.inventory.append(result)
        return result

    def scan_record(self, record: dict, source_label: str = "record") -> dict:
        """Scan a dictionary record for sensitive data."""
        combined = json.dumps(record)
        return self.scan_text(combined, source_label)

    def _classify(self, detected: dict) -> str:
        """Determine classification level from detected data types."""
        top_secret_types  = {"SSN", "CREDIT_CARD", "PASSWORD_HINT", "API_KEY", "AADHAAR", "PAN_CARD"}
        confidential_types = {"EMAIL", "PHONE", "PASSPORT", "BANK_ACCOUNT"}
        internal_types    = {"IP_ADDRESS"}

        found = set(detected.keys())
        if found & top_secret_types:
            return "TOP_SECRET"
        elif found & confidential_types:
            return "CONFIDENTIAL"
        elif found & internal_types:
            return "INTERNAL"
        return "PUBLIC"

    def get_inventory_report(self) -> dict:
        """Summarize the data inventory scan results."""
        total = len(self.inventory)
        by_class = {level: 0 for level in CLASSIFICATION_LEVELS}
        for item in self.inventory:
            by_class[item["classification"]] = by_class.get(item["classification"], 0) + 1

        all_types = {}
        for item in self.inventory:
            for t, count in item["detected_types"].items():
                all_types[t] = all_types.get(t, 0) + count

        return {
            "report_generated" : datetime.utcnow().isoformat(),
            "total_scanned"    : total,
            "by_classification": by_class,
            "detected_pii_types": all_types,
            "high_risk_count"  : by_class.get("TOP_SECRET", 0) + by_class.get("CONFIDENTIAL", 0),
            "compliance_gaps"  : [
                item for item in self.inventory
                if item["pii_found"] and not item["policy"]["encrypt"]
            ]
        }

    def redact(self, text: str) -> str:
        """Redact all sensitive data from text (for safe logging/display)."""
        redacted = text
        for ptype, pattern in self.compiled.items():
            redacted = pattern.sub(f"[REDACTED:{ptype}]", redacted)
        return redacted
