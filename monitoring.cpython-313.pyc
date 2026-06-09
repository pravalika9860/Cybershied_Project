"""
monitoring.py
=============
Continuous monitoring, audit logging, and vulnerability assessment.
Part of: CyberShield - Protecting Sensitive Data with Encryption and Access Control
Author: GPI Internship Project | Cloud Counselage
"""

import os
import json
import time
import hashlib
import threading
from datetime import datetime, timedelta
from collections import defaultdict
from typing import Callable, Optional


# ─────────────────────────────────────────────
#  Immutable Audit Logger
# ─────────────────────────────────────────────

class AuditLogger:
    """
    Tamper-evident audit log using hash-chaining (blockchain-inspired).
    Every log entry is chained to the previous one — modification is detectable.
    """

    def __init__(self, log_path: str = "logs/audit.log"):
        self.log_path   = log_path
        self.entries    = []
        self.prev_hash  = "GENESIS"
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

    def _compute_hash(self, entry: dict) -> str:
        content = json.dumps(entry, sort_keys=True) + self.prev_hash
        return hashlib.sha256(content.encode()).hexdigest()

    def log(self, event_type: str, user_id: str, action: str,
            resource: str = "", status: str = "SUCCESS",
            ip_address: str = "127.0.0.1", details: dict = None):
        """Record a tamper-evident audit entry."""
        entry = {
            "timestamp"  : datetime.utcnow().isoformat() + "Z",
            "event_type" : event_type,
            "user_id"    : user_id,
            "action"     : action,
            "resource"   : resource,
            "status"     : status,
            "ip_address" : ip_address,
            "details"    : details or {}
        }
        entry["chain_hash"] = self._compute_hash(entry)
        self.prev_hash      = entry["chain_hash"]

        self.entries.append(entry)

        # Persist to file
        with open(self.log_path, "a") as f:
            f.write(json.dumps(entry) + "\n")

        return entry

    def verify_integrity(self) -> dict:
        """
        Verify the entire log chain has not been tampered with.
        Returns a report indicating any broken links.
        """
        prev = "GENESIS"
        issues = []
        for i, entry in enumerate(self.entries):
            test_entry = {k: v for k, v in entry.items() if k != "chain_hash"}
            expected   = hashlib.sha256(
                (json.dumps(test_entry, sort_keys=True) + prev).encode()
            ).hexdigest()
            if expected != entry["chain_hash"]:
                issues.append({"index": i, "entry": entry, "expected": expected})
            prev = entry["chain_hash"]

        return {
            "verified"    : len(issues) == 0,
            "total_entries": len(self.entries),
            "issues"      : issues,
            "checked_at"  : datetime.utcnow().isoformat()
        }

    def query(self, user_id: str = None, event_type: str = None,
              since_minutes: int = None) -> list:
        """Query audit entries with optional filters."""
        results = self.entries
        if user_id:
            results = [e for e in results if e.get("user_id") == user_id]
        if event_type:
            results = [e for e in results if e.get("event_type") == event_type]
        if since_minutes:
            cutoff = datetime.utcnow() - timedelta(minutes=since_minutes)
            results = [
                e for e in results
                if datetime.fromisoformat(e["timestamp"].rstrip("Z")) > cutoff
            ]
        return results

    def get_summary(self) -> dict:
        """Return statistics about logged events."""
        summary = defaultdict(int)
        user_activity = defaultdict(int)
        for e in self.entries:
            summary[e["event_type"]] += 1
            user_activity[e["user_id"]] += 1
        return {
            "total_events"   : len(self.entries),
            "by_event_type"  : dict(summary),
            "by_user"        : dict(user_activity),
            "last_event"     : self.entries[-1]["timestamp"] if self.entries else None
        }


# ─────────────────────────────────────────────
#  Intrusion Detection System (IDS)
# ─────────────────────────────────────────────

class IntrusionDetector:
    """
    Monitors for suspicious patterns:
    - Brute force login attempts
    - Unauthorized access attempts
    - Unusual data access volume
    - Off-hours access
    """

    BRUTE_FORCE_THRESHOLD = 5    # attempts per window
    BRUTE_FORCE_WINDOW    = 300  # 5-minute window
    HIGH_VOLUME_THRESHOLD = 50   # data reads per minute
    OFFICE_HOURS          = (8, 20)  # 8 AM to 8 PM

    def __init__(self, alert_handler: Optional[Callable] = None):
        self.alert_handler    = alert_handler or self._default_alert
        self.login_attempts   : dict = defaultdict(list)    # ip -> [timestamps]
        self.access_volume    : dict = defaultdict(list)    # user -> [timestamps]
        self.alerts           : list = []

    def _default_alert(self, alert: dict):
        self.alerts.append(alert)

    def _create_alert(self, severity: str, category: str,
                      description: str, details: dict = None):
        alert = {
            "alert_id"   : hashlib.md5(
                (str(time.time()) + category).encode()
            ).hexdigest()[:8].upper(),
            "timestamp"  : datetime.utcnow().isoformat() + "Z",
            "severity"   : severity,          # CRITICAL / HIGH / MEDIUM / LOW
            "category"   : category,
            "description": description,
            "details"    : details or {},
            "resolved"   : False
        }
        self.alert_handler(alert)
        return alert

    def check_brute_force(self, ip_address: str, success: bool) -> Optional[dict]:
        """Detect brute-force login attacks from an IP address."""
        now = time.time()
        self.login_attempts[ip_address] = [
            t for t in self.login_attempts[ip_address]
            if now - t < self.BRUTE_FORCE_WINDOW
        ]
        if not success:
            self.login_attempts[ip_address].append(now)

        count = len(self.login_attempts[ip_address])
        if count >= self.BRUTE_FORCE_THRESHOLD:
            return self._create_alert(
                severity    = "CRITICAL",
                category    = "BRUTE_FORCE",
                description = f"Brute-force attack detected from IP {ip_address}",
                details     = {"ip": ip_address, "attempts": count, "window_seconds": self.BRUTE_FORCE_WINDOW}
            )
        return None

    def check_access_volume(self, user_id: str) -> Optional[dict]:
        """Detect unusually high data access volume."""
        now = time.time()
        self.access_volume[user_id] = [
            t for t in self.access_volume[user_id] if now - t < 60
        ]
        self.access_volume[user_id].append(now)
        count = len(self.access_volume[user_id])
        if count > self.HIGH_VOLUME_THRESHOLD:
            return self._create_alert(
                severity    = "HIGH",
                category    = "HIGH_VOLUME_ACCESS",
                description = f"Unusually high data access by user '{user_id}': {count} reads/min",
                details     = {"user_id": user_id, "reads_per_minute": count}
            )
        return None

    def check_off_hours_access(self, user_id: str, role: str) -> Optional[dict]:
        """Flag off-hours access by non-admin roles."""
        hour = datetime.utcnow().hour
        start, end = self.OFFICE_HOURS
        if not (start <= hour < end) and role != "admin":
            return self._create_alert(
                severity    = "MEDIUM",
                category    = "OFF_HOURS_ACCESS",
                description = f"Off-hours data access by '{user_id}' (role: {role}) at {hour:02d}:00 UTC",
                details     = {"user_id": user_id, "role": role, "hour_utc": hour}
            )
        return None

    def check_unauthorized_permission(self, user_id: str, role: str, permission: str):
        """Log denied access attempts."""
        return self._create_alert(
            severity    = "HIGH",
            category    = "UNAUTHORIZED_ACCESS",
            description = f"User '{user_id}' (role: {role}) attempted unauthorized action: {permission}",
            details     = {"user_id": user_id, "role": role, "permission": permission}
        )

    def get_alerts(self, severity: str = None, resolved: bool = False) -> list:
        """Get current alerts, optionally filtered."""
        alerts = self.alerts
        if severity:
            alerts = [a for a in alerts if a["severity"] == severity]
        if not resolved:
            alerts = [a for a in alerts if not a["resolved"]]
        return alerts

    def resolve_alert(self, alert_id: str):
        """Mark an alert as resolved."""
        for alert in self.alerts:
            if alert["alert_id"] == alert_id:
                alert["resolved"] = True
                alert["resolved_at"] = datetime.utcnow().isoformat()
                return True
        return False


# ─────────────────────────────────────────────
#  Vulnerability Scanner
# ─────────────────────────────────────────────

class VulnerabilityScanner:
    """
    Simulates a periodic security configuration audit.
    Checks common misconfigurations and policy violations.
    """

    def __init__(self):
        self.last_scan = None
        self.findings  = []

    def scan(self, config: dict) -> dict:
        """
        Run a vulnerability assessment against a config dict.
        config keys: users (list), key_ages (dict), mfa_status (dict),
                     open_ports (list), tls_version (str), password_policy (dict)
        """
        self.findings = []
        self.last_scan = datetime.utcnow().isoformat()

        # Check 1: MFA enforcement
        for uid, mfa_on in config.get("mfa_status", {}).items():
            if not mfa_on:
                self.findings.append({
                    "severity": "HIGH",
                    "check"   : "MFA_NOT_ENABLED",
                    "detail"  : f"User '{uid}' does not have MFA enabled",
                    "remediation": "Enable TOTP MFA for all user accounts"
                })

        # Check 2: Stale encryption keys
        for kid, age_days in config.get("key_ages", {}).items():
            if age_days > 30:
                self.findings.append({
                    "severity": "HIGH",
                    "check"   : "STALE_KEY",
                    "detail"  : f"Key '{kid}' is {age_days} days old (max: 30 days)",
                    "remediation": "Rotate encryption key immediately"
                })

        # Check 3: TLS version
        tls = config.get("tls_version", "TLS1.2")
        if tls in ("TLS1.0", "TLS1.1", "SSL3"):
            self.findings.append({
                "severity": "CRITICAL",
                "check"   : "INSECURE_TLS",
                "detail"  : f"Using deprecated protocol: {tls}",
                "remediation": "Upgrade to TLS 1.3"
            })

        # Check 4: Password policy
        pp = config.get("password_policy", {})
        if pp.get("min_length", 0) < 12:
            self.findings.append({
                "severity": "MEDIUM",
                "check"   : "WEAK_PASSWORD_POLICY",
                "detail"  : f"Minimum password length is {pp.get('min_length', 0)} (recommended: 12+)",
                "remediation": "Update password policy to require 12+ character passwords"
            })

        # Check 5: Default/admin users
        for user in config.get("users", []):
            if user.get("user_id", "").lower() in ("admin", "root", "administrator", "test"):
                self.findings.append({
                    "severity": "MEDIUM",
                    "check"   : "DEFAULT_USERNAME",
                    "detail"  : f"Default username detected: '{user['user_id']}'",
                    "remediation": "Rename default accounts to non-obvious usernames"
                })

        critical = sum(1 for f in self.findings if f["severity"] == "CRITICAL")
        high     = sum(1 for f in self.findings if f["severity"] == "HIGH")
        medium   = sum(1 for f in self.findings if f["severity"] == "MEDIUM")

        risk_score = (critical * 40) + (high * 20) + (medium * 5)
        risk_level = (
            "CRITICAL" if risk_score >= 80
            else "HIGH"   if risk_score >= 40
            else "MEDIUM" if risk_score >= 20
            else "LOW"
        )

        return {
            "scan_time"       : self.last_scan,
            "total_findings"  : len(self.findings),
            "critical"        : critical,
            "high"            : high,
            "medium"          : medium,
            "risk_score"      : risk_score,
            "overall_risk"    : risk_level,
            "findings"        : self.findings,
            "compliant"       : len(self.findings) == 0
        }
