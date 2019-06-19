from core.storages import BaseStorageClient


class LocalStorageClient(BaseStorageClient):

    def __init__(self, storage_config):
        super(LocalStorageClient, self).__init__(storage_config)

    def download(self):
        print(self.__class__.__name__ + ' download')
        pass

    def upload(self):
        pass

    def list(self):
        pass

    def get_local_path(self):
        return self.storage_config['path']
