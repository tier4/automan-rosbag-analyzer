from core.storages.azure_storage_client import AzureStorageClient
from core.storages.local_storage_client import LocalStorageClient
from core.storages.s3_storage_client import S3StorageClient


class UnknownStorageError(Exception):
    pass


class StorageClientFactory(object):

    @staticmethod
    def create(storage_type, storage_config):
        if storage_type == 'AZURE':
            return AzureStorageClient(storage_config)
        elif storage_type == 'LOCAL_NFS':
            return LocalStorageClient(storage_config)
        elif storage_type == 'AWS_S3':
            return S3StorageClient(storage_config)
        raise UnknownStorageError
