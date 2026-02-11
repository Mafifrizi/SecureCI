import json
import uuid


class SarifReporter:
    def generate(self, findings, output_path="secureci.sarif"):
        sarif = {
            "version": "2.1.0",
            "runs": [{
                "tool": {
                    "driver": {
                        "name": "SecureCI",
                        "informationUri": "https://github.com/Mafifrizi/SecureCI",
                        "rules": []
                    }
                },
                "results": []
            }]
        }

        for f in findings:
            rule_id = str(uuid.uuid4())
            sarif["runs"][0]["tool"]["driver"]["rules"].append({
                "id": rule_id,
                "shortDescription": {
                    "text": f["message"]
                }
            })
            sarif["runs"][0]["results"].append({
                "ruleId": rule_id,
                "level": "error" if f["severity"] == "HIGH" else "warning",
                "message": {
                    "text": f["message"]
                }
            })

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(sarif, f, indent=2)
