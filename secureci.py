import sys
from core.engine import SecureCIEngine

if len(sys.argv) < 2:
    print("Usage: python secureci.py <target_path> [--generate-baseline]")
    sys.exit(1)

target = sys.argv[1]
generate_baseline = "--generate-baseline" in sys.argv

engine = SecureCIEngine(generate_baseline=generate_baseline)
status, findings = engine.scan(target)

print(f"SECURITY STATUS: {status}")

if status == "BASELINE GENERATED":
    print("Baseline created at config/secureci_baseline.json")
    sys.exit(0)

if findings:
    print("\nFindings:")
    for f in findings:
        print(f"- [{f['severity']}] {f['message']}")

if status.startswith("FAIL"):
    sys.exit(1)
