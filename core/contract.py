from abc import ABC, abstractmethod
from typing import List
from core.finding import Finding

class PluginContract(ABC):

    @abstractmethod
    def scan(self, target_path: str) -> List[Finding]:
        pass
