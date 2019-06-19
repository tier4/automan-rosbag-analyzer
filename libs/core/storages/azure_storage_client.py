from core.storages import BaseStorageClient


class AzureStorageClient(BaseStorageClient):

    def __init__(self):
        super(AzureStorageClient, self).__init__()

    def download(self):
        pass

    def upload(self):
        pass

    def list(self):
        pass
