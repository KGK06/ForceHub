from pathlib import Path
from . import ForceBot
import sys
import importlib
import logging
import glob

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

for name in glob.glob(f"{Path().absolute()}/plugins/*.py"):
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        path = Path(f"{Path().absolute()}/plugins/{plugin_name.replace('.py', '')}.py")
        name = f"{Path().absolute()}.plugins.{plugin_name}"
        spec = importlib.util.spec_from_file_location(name, path)
        load = importlib.util.module_from_spec(spec)
        load.logger = logging.getLogger(plugin_name)
        spec.loader.exec_module(load)
        sys.modules[f"{Path().absolute()}.plugins." + plugin_name] = load

if __name__ == "__main__":
    print('Bot started...')
    ForceBot.run_until_disconnected()
                    
                    
