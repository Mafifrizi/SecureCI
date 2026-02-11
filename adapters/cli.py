
from core.engine import SecureCIEngine
from core.policy import PolicyEngine
from plugins.secret_scan.scanner import SecretScanner
from plugins.dependency_scan.scanner import DependencyScanner
from plugins.iac_scan.scanner import IaCScanner

def run_cli(scan_path, policy_file):
    engine = SecureCIEngine(
        plugins=[SecretScanner(), DependencyScanner(), IaCScanner()],
        policy=PolicyEngine(policy_file)
    )
    return engine.run(scan_path)
