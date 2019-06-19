from core.storages.azure_storage_client import AzureStorageClient
from core.storages.local_storage_client import LocalStorageClient


class UnknownStorageError(Exception):
    pass


class StorageClientFactory(object):

    @staticmethod
    def create(storage_type, storage_config):
        if storage_type == 'AZURE':
            return AzureStorageClient(storage_config)
        elif storage_type == 'LOCAL_NFS':
            return LocalStorageClient(storage_config)
        raise UnknownStorageError
