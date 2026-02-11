# 🔐 SecureCI

**SecureCI** is a lightweight **DevSecOps security scanning tool** designed to help developers and DevOps teams detect security issues **early**, both locally and inside CI/CD pipelines.

SecureCI focuses on **clarity, extensibility, and predictable CI behavior**, without trying to replace heavyweight enterprise security platforms.

> ⚠️ **Project Status**  
> **ALPHA / BETA** — Core features are working and stable, but internal structure and APIs may still change.

---

## 🌍 What is SecureCI? | Apa itu SecureCI?

### 🇬🇧 English
SecureCI scans a target project directory and identifies common security risks using a **plugin-based architecture**.  
It is designed to be:
- Simple to run
- Transparent in its output
- Safe to integrate as a CI security gate

### 🇮🇩 Bahasa Indonesia
SecureCI melakukan pemindaian pada folder project target untuk mendeteksi risiko keamanan umum menggunakan arsitektur **berbasis plugin**.  
Tool ini dibuat agar:
- Mudah digunakan
- Output jelas dan tidak membingungkan
- Aman dipakai di pipeline CI/CD

---

## ✨ Key Features | Fitur Utama

- 🔌 **Plugin-based scanners**
- 🔐 **Secret scanning**
  - `.env` files
  - Text files
  - Hardcoded credentials
- 📦 **Dependency vulnerability scanning**
- 🏗️ **Infrastructure-as-Code (IaC) scanning**
- 🚦 **Severity-based decision engine**
  - HIGH
  - MEDIUM
  - LOW
- 📉 **Baseline support**
  - Ignore known findings safely
  - Still detect new issues
- 📄 **Multiple output formats**
  - Terminal (human-readable)
  - JSON
  - SARIF (GitHub Security)
- 🤖 **CI/CD ready**
  - Deterministic exit codes
  - Predictable behavior

---

## 📂 Project Structure

```text
SecureCI/
├── secureci.py                 # CLI entrypoint
├── core/                       # Core engine & domain logic
│   ├── engine.py
│   ├── policy.py
│   ├── finding.py
│   ├── loader.py
│   ├── severity.py
│   └── contract.py
├── plugins/                    # Security scanners
│   ├── secret_scan/
│   ├── dependency_scan/
│   └── iac_scan/
├── reporters/                  # Output reporters
│   ├── json_reporter.py
│   └── sarif_reporter.py
├── config/                     # Configuration & baseline
│   ├── secureci_policy.yaml
│   ├── default_policy.yaml
│   └── secureci_baseline.json
└── .github/
    └── workflows/              # CI integration
```
---

## 🚀 Installation

```
git clone https://github.com/Mafifrizi/SecureCI.git
cd SecureCI
```
**Python 3.9+ is recommended.**

---

## ▶️ Basic Usage | Cara Pakai Dasar

```
python secureci.py <target_path>
```
**Example:**

```
python secureci.py ../target_project
```

---

## 📤 Output Formats

- Terminal (default)

```
python secureci.py ../target_project
```

- JSON

```
python secureci.py ../target_project --format json
```

- SARIF (GitHub Security)

```
python secureci.py ../target_project --format sarif
```

---

## 🚦 Severity & Exit Codes
```text
| Severity|  Result              | Exit Code |
|---------|----------------------|-----------|
| HIGH    | FAIL                 | 1         |
| MEDIUM  | PASS (WITH WARNINGS) | 0         |
| LOW     | PASS (WITH WARNINGS) | 0         |
```

This behavior makes SecureCI safe to use as a CI security gate.

--- 

## 🧱 Baseline Support

- Generate a baseline from current findings:

```
python secureci.py ../target_project --generate-baseline
```

- This creates:

```
config/secureci_baseline.json
```

### Baseline allows teams to:
- Accept known issues intentionally
- Reduce CI noise
- Still detect new or reintroduced vulnerabilities

--- 

## ⚙️ Policy Configuration

- Policy files are located in:

```
config/secureci_policy.yaml
```

### Policies control
- Severity evaluation
- FAIL / WARN behavior

--- 

## 🤖 CI/CD Usage

### SecureCI is designed for CI environments:
- Clear and deterministic exit codes
- Machine-readable output formats
- SARIF support for GitHub Security tab

### Typical use case:
- Block pull requests if HIGH findings exist
- Still report MEDIUM / LOW findings to developers

---

## ⚠️ Project Status
```text
SecureCI is currently in ALPHA / BETA stage.

✔ Core functionality works
✔ Suitable for learning, experimentation, and early adoption
❗ Internal APIs and structure may change
❗ Not yet recommended for production-critical pipelines
```

---

## 🤝 Contribution & Feedback
```text
This project is under active development.
Feedback, issues, and ideas are welcome.
```

--- 

## 🧠 Closing Notes | Penutup
```text
SecureCI was built with a simple principle:
Security tools should be understandable, auditable, and developer-friendly.
If SecureCI helps you detect security issues earlier in your workflow, then it has already done its job.
```

---

## 🔐 Happy secure coding.