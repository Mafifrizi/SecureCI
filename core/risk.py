
class RiskEngine:
    SEVERITY_MAP = {"low": 10, "medium": 30, "high": 60}

    def calculate(self, findings):
        risk = 100
        for f in findings:
            risk -= self.SEVERITY_MAP.get(f["severity"], 0)
        return max(risk, 0)

    def summary(self, findings):
        summary = {"low": 0, "medium": 0, "high": 0}
        for f in findings:
            summary[f["severity"]] += 1
        return summary
