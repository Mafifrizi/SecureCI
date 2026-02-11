import os
import re
from core.contract import PluginContract

STRUCTURED_PATTERNS = {
    "AWS_ACCESS_KEY": r"AKIA[0-9A-Z]{16}",
    "GITHUB_TOKEN": r"ghp_[0-9A-Za-z]{36}",
    "JWT": r"eyJ[a-zA-Z0-9_-]+\.eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+"
}

KEYWORD_PATTERNS = [
    r"api[_-]?key",
    r"access[_-]?key",
    r"secret",
    r"token",
    r"password"
]

IGNORE_MARKER = "secureci-ignore"

IGNORED_EXTENSIONS = (
    ".exe", ".dll", ".png", ".jpg", ".jpeg", ".gif",
    ".zip", ".tar", ".gz", ".pyc", ".class"
)

class SecretScan(PluginContract):
    def scan(self, target_path):
        findings = []
        seen = set()

        for root, _, files in os.walk(target_path):
            for file in files:
                if file.endswith(IGNORED_EXTENSIONS):
                    continue

                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        lines = f.readlines()
                except Exception:
                    continue

                for idx, line in enumerate(lines, start=1):
                    if IGNORE_MARKER in line:
                        continue

                    key = (file_path, idx)
                    if key in seen:
                        continue

                    # HIGH confidence
                    for name, pattern in STRUCTURED_PATTERNS.items():
                        if re.search(pattern, line):
                            findings.append({
                                "severity": "HIGH",
                                "message": f"{name} detected in {file_path}:{idx}"
                            })
                            seen.add(key)
                            break

                    if key in seen:
                        continue

                    # MEDIUM heuristic
                    for kw in KEYWORD_PATTERNS:
                        if re.search(kw, line, re.IGNORECASE):
                            findings.append({
                                "severity": "MEDIUM",
                                "message": f"Possible secret keyword '{kw}' in {file_path}:{idx}"
                            })
                            seen.add(key)
                            break

        return findings
