import yaml

class Policy:
    def __init__(self, policy_path=None):
        pass

    def evaluate(self, findings):
        """
        findings: list[Finding]
        return: string status
        """

        has_high = any(f.severity == "HIGH" for f in findings)
        has_medium = any(f.severity == "MEDIUM" for f in findings)

        if has_high:
            return "FAIL"
        if has_medium:
            return "PASS (WITH WARNINGS)"
        return "PASS"

