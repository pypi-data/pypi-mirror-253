import pickle
import threading
import time

import requests

from camera_management.tools.types import ImageResolution

from . import types


class BaseReceiver(threading.Thread):
    def __init__(self, url: str, name: str = "BaseRecorder", stop_evt: threading.Event = None):
        super().__init__(name=name, daemon=True)
        self.url = url

        if stop_evt is None:
            self.stop_evt = threading.Event()
        else:
            self.stop_evt = stop_evt

    def run(self) -> None:
        """
        INSERT USEFUL DESCRIPTION WHEN SEEING THIS.
        """
        self.start_time = time.time()

        while not self.stop_evt.is_set():
            try:
                response = requests.get(self.url)
                self.logic(response)
            except ConnectionError as ce:
                print(f"{ce.strerror}, please start the REST-API Application or connect network.")

    def logic(self, response: requests.Response) -> None:
        """
        INSERT USEFUL DESCRIPTION WHEN SEEING THIS.
        """
        pass

    def stop(self):
        """
        Stop recording.

        Joins thread and stores collected data to file.
        """
        self.stop_evt.set()
        self.join()
        # self.store_to_file()


class LogReceiver(BaseReceiver):
    def __init__(self, url: str, cb=None, name: str = "LogRecorder", stop_evt: threading.Event = None):
        super().__init__(url=url, name=name, stop_evt=stop_evt)

        self.last_index = -1
        self.cb = cb

    def logic(self, response: requests.Response) -> None:
        """
        INSERT USEFUL DESCRIPTION WHEN SEEING THIS
        """
        data = response.json()
        last_index = data["index"]
        if last_index > self.last_index:
            if self.cb:
                self.cb(data)
            self.last_index = last_index
        time.sleep(0.05)


class PDReceiver(BaseReceiver):
    def __init__(self, url: str, cb=None, name: str = "ProcessedDataRecorder", stop_evt: threading.Event = None):
        super().__init__(url=url, name=name, stop_evt=stop_evt)

        self.last_timestamp = -1
        self.cb = cb

    def logic(self, response: requests.Response) -> None:
        """
        INSERT USEFUL DESCRIPTION WHEN SEEING THIS
        """
        data = response.json()
        pd = types.ProcessedData.load_from_dict(data)

        if pd.timestamp > self.last_timestamp:
            if self.cb:
                self.cb(pd)
            self.last_timestamp = pd.timestamp
        time.sleep(0.05)


class ImageReceiver(BaseReceiver):
    def __init__(self, url: str, url_info: str, cb=None, name: str = "ImageRecorder", stop_evt: threading.Event = None):
        super().__init__(url=url, name=name, stop_evt=stop_evt)

        self.tracked = dict()
        self.url_info = url_info
        self.cb = cb
        self.last_update = -1
        # self.stream_infos = self.get_stream_infos()
        # self.status = {key: -1 for key in self.stream_infos.keys()}

    def get_stream_infos(self) -> types.CameraDicts:
        """
        INSERT USEFUL DESCRIPTION WHEN SEEING THIS
        """
        cam_dicts = None
        try:
            response = requests.get(self.url_info)

            cam_dicts = dict()
            for key, cam_info in response.json().items():
                stream_resolution = ImageResolution(**cam_info.pop("stream_resolution"))
                cam = types.CameraInformation(**cam_info, stream_resolution=stream_resolution)
                cam_dicts[key] = cam

        except ConnectionError as ce:
            print(f"{ce.strerror}, please start the REST-API Application or connect network.")
        return cam_dicts

    def fetch_data(self):
        """
        INSERT USEFUL DESCRIPTION WHEN SEEING THIS
        """
        data = None
        try:
            response = requests.get(self.url)
            data: types.ImageProcessorData = pickle.loads(response.content)
        except ConnectionError as ce:
            print(f"{ce.strerror}, please start the REST-API Application or connect network.")

        return data

    def logic(self, response: requests.Response) -> None:
        """
        INSERT USEFUL DESCRIPTION WHEN SEEING THIS
        """
        data = pickle.loads(response.content)
        if data.timestamp > self.last_update:
            if self.cb:
                self.cb(data)
            self.last_update = data.timestamp
        else:
            time.sleep(0.01)


def setup_and_run():
    """
    INSERT USEFUL DESCRIPTION WHEN SEEING THIS
    """
    rcv = LogReceiver(host="localhost", port=8090)
    rcv.start()

    # while True:
    for i in range(4):
        time.sleep(1)

    rcv.stop()


if __name__ == "__main__":
    setup_and_run()
