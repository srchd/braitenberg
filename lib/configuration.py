import yaml
import os
from pathlib import Path


class Configuration:
    SCRIPT_DIR = Path(__file__).resolve()
    CONFIGS_DIR = os.path.join(SCRIPT_DIR.parent.parent, 'configs')
    LOG_DIR = os.path.join(SCRIPT_DIR.parent.parent, 'logs')

    def parse_config(self, config) -> None:
        if not os.path.isfile(config):
            raise FileNotFoundError(f"The provided file {config} does not exist!")
            
        if not config.endswith('.yml'):
            raise FileNotFoundError(f"The provided file {config} is not a valid config file!")

        with open(config, 'r') as f:
            self._parsed_config = yaml.safe_load(f)

        return self._parsed_config
    
    def write_config(self, config, path) -> None:
        if not path.endswith('.yml'):
            raise FileNotFoundError(f"The provided file {path} is not a valid config file!")
        
        with open(path, 'w') as f:
            yaml.safe_dump(config, f)
    