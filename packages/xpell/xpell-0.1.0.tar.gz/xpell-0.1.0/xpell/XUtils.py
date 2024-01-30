
import uuid

class _XUtils(object):
    def __init__(self):
        pass

    def merge_defaults_with_data(self, data, defaults):
        for key in defaults:
            if not data.get(key):
                data[key] = defaults[key]
        return data

    def guid(self):
        return str(uuid.uuid4())

    
XUtils = _XUtils()
_xu = XUtils