import json
import logging
import typing
from datetime import datetime

import cv2
import requests
import tabulate

from camera_management import SETTINGS
from camera_management.frontends import receiver, types
from camera_management.tools.camera_dataclasses import CameraDescription
from camera_management.tools.types import VideoDevice


class manager_interface:
    def __init__(self, host="127.0.0.1", port=8090, autostart=True):
        self.host = host
        self.port = port
        self.base_url = f"http://{self.host}:{self.port}"
        self.camera_interfaces = []

        if autostart:
            infos = self.get_configured_cams()
            for info in infos:
                self.camera_interfaces.append((basic_Interface(host=self.host, port=int(info["PORT"])), int(info["PORT"])))
                print(self.camera_interfaces[-1][0])

            header = infos[0].keys()
            rows = [x.values() for x in infos]
            print(tabulate.tabulate(rows, header))

    def get_interface_by_index(self, idx: int):
        """
        Get a camera by its index in the internal list of interfaces.
        """
        return self.camera_interfaces[idx]

    def get_interface_by_port(self, port: int):
        """
        Get a camera interface by its port number (normally starting from 8091)
        """
        active = []
        for interface in self.camera_interfaces:
            active.append(interface[1])
            if interface[1] == port:
                return interface[0]
        raise ValueError(f"Port {port} is not a valid port. Current active ports are: {active}")

    def get_available_cams(self, verbose=False) -> list[VideoDevice]:
        """
        Returns a list of all the available cams the camera manager knows about (usually all connected cams).

        :param verbose: Also prints the list if set to true
        :return: List of available cams
        """
        cams = []
        try:
            response = requests.get(self.base_url + "/available_cams")
            for cam_json in response.json():
                cam = VideoDevice(**cam_json)
                cams.append(cam)

            if verbose:
                print(f"All available cams for {self.base_url} are:")
                for cam in cams:
                    print(f"\t{cam.product} @ {cam.path}")

        except ConnectionError as ce:
            logging.warning(f"{ce.strerror}, please start the REST-API Application or connect network.")
            return []

    def get_configured_cams(self, verbose=False) -> list[dict]:
        """
        Returns a list of all the  cams the camera manager currently handles and their status.

        :param verbose: Also prints the list if set to true
        :return: List of handled cams
        """
        try:
            response = requests.get(self.base_url + "/info")
            cam_status = response.json()

            if verbose:
                print(f"All handled cams for {self.base_url} are:")
                header = cam_status[0].keys()
                rows = [x.values() for x in cam_status]
                print(tabulate.tabulate(rows, header))

            if cam_status is None:
                raise OSError("There are no cameras to connect to.")
            return cam_status
        except ConnectionError as ce:
            print(f"{ce.strerror}, please start the REST-API Application or connect network.")


class basic_Interface:
    """
    A basic interface to get data from and configure a camera stream.
    """

    def __init__(self, host="127.0.0.1", port=8091, log_cb=None, stream_cb=None, data_cb=None, bw=False, undistort=True, rotate=0):
        """
        A basic interface to get data from and configure a camera stream.

        :param host: The host IP address.
        :param port: The host port.
        :param log_cb: Callback function for logging !!! NOT YET IMPLEMENTED !!!
        :param data_cb: Callback function for calculated data !!! NOT YET IMPLEMENTED !!!
        :param stream_cb: Callback for the actual video stream.
        :param bw: Should the stream be black and white or color?
        :param undistort: Should the stream be distorted? (Only applicable if the camera config .json has calibration values)
        :param rotate: Rotates the image in 90 degree steps.
        """
        self.host = host
        self.port = port
        self.log_cb = log_cb
        self.stream_cb = stream_cb
        self.data_cb = data_cb

        self.base_url = f"http://{self.host}:{self.port}"
        self.last_log_index = -1
        self.headers = {"Content-type": "application/json", "Accept": "application/json"}
        self._bw = bw
        self._undistort = undistort
        self._rotate = rotate

        # self.log_rcv = receiver.LogReceiver(
        #     url=f"{self.base_url}/log",
        #     cb=self._update_log,
        # )

        self.stream_rcv = receiver.ImageReceiver(
            url=f"{self.base_url}/data/imageProcessor",
            url_info=f"{self.base_url}/info/cameras",
            cb=self._update_stream,
        )
        # self.stream_infos = self.stream_rcv.stream_infos

        # self.data_rcv = receiver.PDReceiver(
        #     url=f"{self.base_url}/data/processed",
        #     cb=self._update_processed_data,
        # )
        # self.log_rcv.start()
        self.stream_rcv.start()
        # self.data_rcv.start()

    def fetch_data(self):
        """
        Returns the newest image of the camera stream.
        """
        return self.stream_rcv.fetch_data()

    def _restart_stream_receiver(self, rcv: receiver.ImageReceiver):
        rcv.stop()
        self.stream_rcv = receiver.ImageReceiver(
            url=f"{self.base_url}/data/imageProcessor",
            url_info=f"{self.base_url}/info/cameras",
            cb=self._update_stream,
        )
        self.stream_rcv.start()

    def __str__(self):
        return f"basic_Interface listening on {self.base_url}"

    def set_log_cb(self, callback: typing.Callable) -> None:
        """
        INSERT USEFUL DESCRIPTION WHEN SEEING THIS
        """
        self.log_cb = callback

    @property
    def rotate(self):
        """
        Image rotate setting of the camera stream.

        """
        return self._rotate

    @rotate.setter
    def rotate(self, value: bool):
        if not isinstance(value, int) or value not in [0, 90, 180, 270]:
            logging.warning(f'{value} is of type {type(value)}. Only int values in [0, 90, 180, 270] are allowed for "rotate" setting.')
        else:
            self._rotate = value
            resp = requests.post(
                f"{self.base_url}/settings/pre_processing",
                json.dumps({"rotate": value}),
                headers=self.headers,
            )
            if resp.status_code != 200:
                logging.warning(f'Something went wrong while applying "rotate" setting. (HTTP Error Code {resp.status_code})')

    def get_general_setting(self, argument: cv2.CAP_PROP_SETTINGS) -> dict | None:
        """
        Gets the currently configured setting for the chosen argument.

        :param argument: The setting you want to query. Use cv2.CAP_xxx arguments.
        :return: A dict containing the argument and the current value.
        """
        if isinstance(argument, SETTINGS):
            argument = argument.value
        resp = requests.get(f"{self.base_url}/settings/camera", params={"settings": argument})
        if resp.status_code != 200:
            logging.warning(f"Something went wrong while fetching general setting. (HTTP Error Code {resp.status_code})")
            logging.warning(f"Error Message: {resp.content}")
            return {"Error": resp.content}
        else:
            return resp.json()

    def set_general_setting(self, argument: SETTINGS | int, value):
        """
        Sets the currently configured setting for the chosen argument.

        :param argument: The setting you want to query. Use cv2.CAP_xxx arguments.
        :param val: The value you want to set.
        """
        if isinstance(argument, SETTINGS):
            argument = argument.value
        resp = requests.post(f"{self.base_url}/settings/camera", json.dumps({"settings": (argument, value)}))
        if resp.status_code != 200:
            logging.warning(f"Something went wrong while applying general setting. (HTTP Error Code {resp.status_code})")
            logging.warning(f"Error Message: {resp.content}")
            return f"Error: {resp.content}"

        else:
            return resp.content

    @property
    def description(self):
        """
        Get the current configuration of the Camera.

        :return: A json-style representation of the calibration.
        """
        resp = requests.get(f"{self.base_url}/description")
        if resp.status_code != 200:
            logging.warning(f"Something went wrong while fetching configuration setting. (HTTP Error Code {resp.status_code}). Error: {resp.content}")
            logging.warning(f"Error Message: {resp.content}")
            return {"Error": resp.content}
        else:
            return resp.json()

    @description.setter
    def description(self, config: CameraDescription):
        # TODO: Make setter
        pass

    @property
    def undistort(self):
        """
        Distortion setting of the camera stream.

        """
        return self._undistort

    @undistort.setter
    def undistort(self, value: bool):
        if not isinstance(value, bool):
            logging.warning(f'{value} is of type {type(value)}. Only boolean values are allowed for "undistort" setting.')
        else:
            self._undistort = value
            resp = requests.post(
                f"{self.base_url}/settings/pre_processing",
                json.dumps({"undistort": value}),
                headers=self.headers,
            )
            if resp.status_code != 200:
                logging.warning(
                    f'Something went wrong while applying "undistort" setting. (HTTP Error Code {resp.status_code}). Error: {resp.content}'
                )

    @property
    def bw(self):
        """
        Black and white setting of the camera stream.

        """
        return self._bw

    @bw.setter
    def bw(self, value: bool):
        if not isinstance(value, bool):
            logging.warning(f'{value} is of type {type(value)}. Only boolean values are allowed for "Black and White" setting.')
        else:
            self._bw = value
            resp = requests.post(
                f"{self.base_url}/settings/pre_processing",
                json.dumps({"bw": value}),
                headers=self.headers,
            )
            if resp.status_code != 200:
                logging.warning(
                    f'Something went wrong while applying "black and white" setting. (HTTP Error Code {resp.status_code}). Error: {resp.content}'
                )

    def _update_log(self, data: dict):
        clog = types.LoggingUnit(**data)
        current_index = clog.index
        if current_index > self.last_log_index:
            if self.log_cb:
                new_logs = [(e[1], e[2]) for e in clog.log[-(current_index - self.last_log_index) :]]

                lines = list()
                for ts, line in new_logs:
                    ts = datetime.fromtimestamp(ts * 1e-9)
                    line = f'[{ts.isoformat(sep="T", timespec="milliseconds")}] {line}'
                    lines.append(line)

                self.log_cb("\n".join(lines), timestamp=False)
            self.last_log_index = current_index

    def set_stream_cb(self, callback: typing.Callable) -> None:
        """
        INSERT USEFUL DESCRIPTION WHEN SEEING THIS
        """
        self.stream_cb = callback
        self._restart_stream_receiver(self.stream_rcv)

    def _update_stream(self, data: types.ImageProcessorData):
        if self.stream_cb:
            self.stream_cb(data)

    def set_data_cb(self, callback: typing.Callable) -> None:
        """
        INSERT USEFUL DESCRIPTION WHEN SEEING THIS
        """
        self.data_cb = callback
        self.data_rcv.cb = self.data_cb

    def _update_processed_data(self, data: types.ProcessedData) -> None:
        if self.data_cb:
            self.data_cb(data)
