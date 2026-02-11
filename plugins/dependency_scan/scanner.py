import os
import json
from core.contract import PluginContract

# Hardcoded minimal vuln DB (LEVEL 4 STARTER)
VULNERABLE_DEPENDENCIES = {
    "lodash": ["4.17.20"],
    "requests": ["2.19.0", "2.20.0"],
    "django": ["2.2.0", "2.2.1"]
}

class DependencyScan(PluginContract):
    def scan(self, target_path):
        findings = []

        # /---- Python: requirements.txt ----/
        req_path = os.path.join(target_path, "requirements.txt")
        if os.path.exists(req_path):
            with open(req_path, "r", encoding="utf-8") as f:
                for line in f:
                    if "==" in line:
                        name, version = line.strip().split("==")
                        if name in VULNERABLE_DEPENDENCIES:
                            if version in VULNERABLE_DEPENDENCIES[name]:
                                findings.append({
                                    "severity": "HIGH",
                                    "message": f"Vulnerable dependency {name}=={version}"
                                })

        # /---- Node: package.json ----/
        pkg_path = os.path.join(target_path, "package.json")
        if os.path.exists(pkg_path):
            with open(pkg_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                deps = data.get("dependencies", {})
                for name, version in deps.items():
                    clean_version = version.replace("^", "").replace("~", "")
                    if name in VULNERABLE_DEPENDENCIES:
                        if clean_version in VULNERABLE_DEPENDENCIES[name]:
                            findings.append({
                                "severity": "HIGH",
                                "message": f"Vulnerable dependency {name}@{clean_version}"
                            })

        return findings
