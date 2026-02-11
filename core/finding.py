class Finding:
    def __init__(self, severity, message):
        self.severity = severity
        self.message = message

    def signature(self):
        return f"{self.severity}|{self.message}"

    def to_dict(self):
        return {
            "severity": self.severity,
            "message": self.message
        }
