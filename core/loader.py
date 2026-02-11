import importlib
import pkgutil
import os
from core.contract import PluginContract

def load_plugins():
    plugins = []

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    plugins_dir = os.path.join(base_dir, "plugins")

    for module_info in pkgutil.iter_modules([plugins_dir]):
        try:
            module = importlib.import_module(
                f"plugins.{module_info.name}.scanner"
            )

            for attr in dir(module):
                obj = getattr(module, attr)
                if (
                    isinstance(obj, type)
                    and issubclass(obj, PluginContract)
                    and obj is not PluginContract
                ):
                    plugins.append(obj())
        except Exception as e:
            print(f"[WARN] Plugin {module_info.name} failed: {e}")

    return plugins
