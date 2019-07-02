#!/usr/bin/env python
import argparse
import json
import os
from rosbag.bag import Bag
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../libs'))
from core.storage_client_factory import StorageClientFactory
from core.automan_client import AutomanClient

MSG_DATA_TYPE_MAP = {
    'sensor_msgs/CompressedImage': 'IMAGE',
    'sensor_msgs/Image': 'IMAGE',
    'sensor_msgs/PointCloud2': 'PCD'
}

IMAGE = 1
PCD = 2
ANNOTATION_DATA_TYPE_MAP = {
    'BB2D': IMAGE,
    'BB2D3D': IMAGE | PCD
}


class RosbagAnalyzer(object):

    @classmethod
    def analyze(cls, file_path, label_type):
        try:
            bag = Bag(file_path)
            dataset_candidates = []
            for topic_name, info in bag.get_type_and_topic_info().topics.items():
                if info.msg_type in MSG_DATA_TYPE_MAP.keys():
                    candidate = {
                        "analyzed_info": {
                            "topic_name": topic_name,
                            "msg_type": info.msg_type,
                        },
                        "data_type": MSG_DATA_TYPE_MAP[info.msg_type],
                        "frame_count": info.message_count
                    }
                    dataset_candidates.append(candidate)
            if cls.__is_label_type_valid(dataset_candidates, label_type):
                return dataset_candidates, 'analyzed'
            return [], 'invalid'
        except Exception as e:
            # FIXME
            raise(e)

    @staticmethod
    def __is_label_type_valid(dataset_candidates, label_type):
        require_object = ANNOTATION_DATA_TYPE_MAP[label_type]
        rosbag_object = 0
        for candidate in dataset_candidates:
            if candidate['data_type'] == 'IMAGE':
                rosbag_object = rosbag_object | IMAGE
            elif candidate['data_type'] == 'PCD':
                rosbag_object = rosbag_object | PCD
        if require_object & rosbag_object == require_object:
            return True
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--storage_type', required=True)
    parser.add_argument('--storage_info', required=True)
    parser.add_argument('--automan_info', required=True)
    args = parser.parse_args()

    storage_client = StorageClientFactory.create(
        args.storage_type,
        json.loads(args.storage_info)
    )
    storage_client.download()
    path = storage_client.get_local_path()
    label_type = json.loads(args.automan_info)['label_type']
    results, status = RosbagAnalyzer.analyze(path, label_type)
    AutomanClient.send_analyzer_result(json.loads(args.automan_info), results, status)
