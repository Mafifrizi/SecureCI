import json
import os
from core.loader import load_plugins
from core.policy import Policy
from core.finding import Finding

BASELINE_PATH = "config/secureci_baseline.json"


class SecureCIEngine:
    def __init__(self, policy_path=None, generate_baseline=False):
        self.plugins = load_plugins()
        self.policy = Policy(policy_path)
        self.generate_baseline = generate_baseline
        self.baseline = self._load_baseline()

    def _load_baseline(self):
        if not os.path.exists(BASELINE_PATH):
            return set()

        with open(BASELINE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return set(data.get("ignored", []))

    def _save_baseline(self, findings):
        signatures = [f.signature() for f in findings]
        os.makedirs("config", exist_ok=True)

        with open(BASELINE_PATH, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "generated_at": "auto",
                    "ignored": signatures
                },
                f,
                indent=2
            )

    def scan(self, target_path):
        findings = []

        for plugin in self.plugins:
            results = plugin.scan(target_path)
            for r in results:
                findings.append(Finding(r["severity"], r["message"]))

        if self.generate_baseline:
            self._save_baseline(findings)
            return "BASELINE GENERATED", []

        filtered = [
            f for f in findings
            if f.signature() not in self.baseline
        ]

        status = self.policy.evaluate(filtered)
        return status, [f.to_dict() for f in filtered]
