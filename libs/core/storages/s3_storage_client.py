import os
import requests
from core.storages import BaseStorageClient


class S3StorageClient(BaseStorageClient):

    def __init__(self, storage_config):
        super(S3StorageClient, self).__init__(storage_config)
        os.mkdir('/s3')
        self.rosbag_path = '/s3/rosbag.bag'
        self.target_url = storage_config['target_url']

    def download(self, url=None):
        if url is None:
            url = self.target_url
        req = requests.get(url, stream=True)
        if req.status_code == 200:
            with open(self.rosbag_path, 'wb') as f:
                for chunk in req.iter_content(chunk_size=1024):
                    f.write(chunk)
        else:
            print('status_code = ' + str(req.status_code))

    def upload(self, path):
        pass

    def list(self):
        pass

    def get_local_path(self):
        return self.rosbag_path
