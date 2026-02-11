SEVERITY_ORDER = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

def rank(severity: str) -> int:
    return SEVERITY_ORDER.index(severity)

def is_equal_or_higher(a: str, b: str) -> bool:
    return rank(a) >= rank(b)
