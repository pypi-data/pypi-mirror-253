import yaml
import os
import sys
from pathlib import Path
from dotmap import DotMap

class Config:
    def __init__(self):
        self.path = ""
        if sys.platform.startswith('win32'):
            self.path = Path(os.getenv('APPDATA')) / 'ZSync' / 'config.yaml'
        elif sys.platform.startswith('darwin'):
            self.path = Path.home() / 'Library' / 'Preferences' / 'ZSync' / 'config.yaml'
        elif sys.platform.startswith('linux'):
            config_home = os.getenv('XDG_CONFIG_HOME', Path.home() / '.config')
            self.path = Path(config_home) / 'ZSync' / 'config.yaml'
        else:
            self.path = Path.home() / 'ZSync' / 'config.yaml'
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self._createConfig()
        else:
            self._loadConfig()

    def _createConfig(self):
        self.config = DotMap()
        self.config.records = []
        self._save()

    def _loadConfig(self):
        self.config = DotMap(yaml.load(self.path.read_text(), Loader=yaml.FullLoader))
        if not self.config.has_key('records'):
            self.config.records = []
            self._save()
    def _save(self):
        self.path.write_text(yaml.dump(self.config.toDict()))

    def addRecord(self, src, dest, mode):
        srcPath = Path(src).expanduser().resolve()
        destPath = Path(dest).expanduser().resolve()
        assert srcPath.exists() and destPath.exists(), f'{src} or {dest} does not exist'
        assert srcPath.is_dir() and destPath.is_dir(), f'{src} or {dest} is not a directory'
        self.config.records.append((str(srcPath), str(destPath), mode))
        self._save()

    def getRecords(self):
        return self.config.records

    def removeRecord(self, index):
        self.config.records.pop(index)
        self._save()