import json
from .base import ExtensionBase


class DictX(ExtensionBase, dict):
    @staticmethod
    def accept(data):
        return json.loads(data)
    
    def dumps(self):
        return json.dumps(self)
