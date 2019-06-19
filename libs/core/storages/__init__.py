class BaseStorageClient(object):
    def __init__(self, storage_config):
        self.storage_config = storage_config

    def download(self):
        raise NotImplementedError

    def upload(self):
        raise NotImplementedError

    def list(self):
        raise NotImplementedError
