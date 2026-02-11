from core.contract import PluginContract

class IaCScanner(PluginContract):
    name = "iac_scan"

    def scan(self, target_path):
        return []
