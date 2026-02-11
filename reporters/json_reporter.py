import json


class JsonReporter:
    def generate(self, findings, output_path="secureci-report.json"):
        report = {
            "tool": "SecureCI",
            "total_findings": len(findings),
            "severity_count": {
                "HIGH": sum(1 for f in findings if f["severity"] == "HIGH"),
                "MEDIUM": sum(1 for f in findings if f["severity"] == "MEDIUM"),
                "LOW": sum(1 for f in findings if f["severity"] == "LOW"),
            },
            "findings": findings
        }

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
