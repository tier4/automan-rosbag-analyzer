import json
import time
import requests
MAX_RETRY_COUNT = 3


class AutomanClient():

    @staticmethod
    def send_analyzer_result(automan_info, dataset_candidates, status):
        host = automan_info['host']
        path = automan_info['path']
        automan_url = host + path
        print(dataset_candidates)
        print(automan_url)
        data = {
            'dataset_candidates': dataset_candidates,
            'status': status
        }
        headers = {
            'Authorization': 'JWT ' + automan_info['jwt'],
            'Content-Type': 'application/json'
        }

        err_count = 0
        while err_count < MAX_RETRY_COUNT:
            try:
                res = requests.put(automan_url, data=json.dumps(data), headers=headers)
                return res
            except Exception as e:
                print(e)
                print("Try to resending complete signal to front server")
                time.sleep(1)
                err_count += 1

        raise Exception  # FIXME
