import atexit
import json
import os
import pathlib
import signal
import subprocess
import sys
import threading
import time

import tabulate
from flask import Flask, jsonify, render_template, request
from waitress import serve

from camera_management.tools.config_tools import check_config, write_configuration_file
from camera_management.tools.create_description import get_descriptions
from camera_management.tools.system_analyzer import get_connected_cams
from camera_management.tools.types import VideoDevice


class ManagerApp(threading.Thread):
    """
    This is the main backend class.

    It tries to connect to all physically connected camera devices and creates sockets for each device.
    This class runs on port 8090. Each socket for each camera runs on the nextmost port (8091+).
    """

    def __init__(self, path_to_configs: pathlib.Path, autostart: bool = True, choose_cameras=False):
        """
        This is the main backend class.

        It tries to connect to all physically connected camera devices and creates sockets for each device.
        This class runs on port 8090. Each socket for each camera runs on the nextmost port (8091+).

        :param path_to_configs: The path to the configs of the camera you want to use.
        :param autostart: If set to true the manager will automatically start sockets for all cameras that are configured (meaning: all cameras it finds a config file for)
        :param choose_cameras: If set to true the manager will ask which cameras you want to start.
        """
        super().__init__(name="Manager")

        self._flask = Flask(__name__)
        self._subprocess_dict = {}
        self._port = 8090
        self._path = path_to_configs
        self._configs = {}
        self._chosen_cameras = None
        self._cam_config_path = pathlib.Path(__file__).parent.parent / "camera_app/temp/"

        self.cam_status = []
        self.available_cameras = None

        if autostart and choose_cameras:
            raise ValueError("You can not use autostart and chose_cameras in conjunction.")

        if not autostart:
            if choose_cameras:
                self.available_cameras = self._get_video_device()
            else:
                while self.available_cameras is None:
                    time.sleep(1)
        else:
            self.available_cameras = get_connected_cams()

        @atexit.register
        def __exit():
            for key, value in self._subprocess_dict.items():
                os.kill(value.pid, signal.SIGTERM)

        @self._flask.route("/info", methods=["GET"])
        def get_camera_info():
            method = request.method
            if method != "GET":
                print("WTF?")
            return jsonify(self.cam_status)

        @self._flask.get("/config")
        def get_cam_config():
            port = request.args.get("port", default=None, type=int)
            return jsonify(self._configs[port])

        @self._flask.route("/", methods=["GET", "POST"])
        def index():
            """
            Start page.
            """
            method = request.method
            if method != "GET":
                print("WTF?")
            return render_template("index.html")

        @self._flask.route("/available_cams", methods=["GET"])
        def available_cams():
            """
            Start page.
            """
            method = request.method
            if method != "GET":
                print("WTF?")
            cams = get_connected_cams()
            return jsonify([cam.to_dict() for cam in cams])

        @self._flask.route("/config/calibration", methods=["GET"])
        def config_calibration():
            """
            Start page.
            """
            method = request.method
            if method != "GET":
                print("WTF")
            print(jsonify({key: value.to_dict() for key, value in self._configs.items()}).json)
            return render_template(
                "calibration.html", configs=self._configs, configs_json=jsonify({key: value.to_dict() for key, value in self._configs.items()}).json
            )

    def _prepare_cam_descriptions(self):
        type_configs = get_descriptions(self._path / "type_configs/")
        individual_configs = get_descriptions(self._path / "individual_configs/")
        ignored_configs = []
        i = 1

        for cam in self.available_cameras:
            status = {
                "CAM TYPE": cam.product,
                "CAM SERIAL": None,
                "CONFIG TYPE": False,
                "CONFIG INDIVIDUAL": False,
                "PORT": None,
                "PORT ACTIVE": False,
                "CALIBRATION AVAILABLE": False,
            }

            for iconfig in individual_configs:
                if iconfig in ignored_configs:
                    continue
                with open(iconfig) as icfg:
                    json_icfg = json.load(icfg)

                json_icfg = check_config(json_icfg, mode="individual", config_path=iconfig)
                if json_icfg is None:
                    ignored_configs.append(iconfig)
                    continue

                if sys.platform.upper() == "DARWIN":
                    serial = cam.unique_id
                    json_serial = json_icfg.information.device.unique_id

                else:
                    serial = cam.serial
                    json_serial = json_icfg.information.device.serial

                status["CAM SERIAL"] = serial

                if json_serial == serial:
                    port = self._port + i
                    i += 1

                    json_icfg.information.device = cam
                    self._configs[port] = {"CONFIG TYPE": None, "CONFIG MODEL": json_icfg}
                    write_configuration_file(filename=f"{port}.json", cam_config_path=self._cam_config_path, content=json_icfg.model_dump())

                    self._subprocess_dict[port] = subprocess.Popen(
                        [sys.executable, f"{pathlib.Path(__file__).parent.parent / 'camera_app/camera_interface.py'}", f"{port}"]
                    )
                    status["CONFIG INDIVIDUAL"] = True
                    status["PORT"] = port
                    status["PORT ACTIVE"] = True
                    status["CALIBRATION AVAILABLE"] = True
                    self.cam_status.append(status)
                    break

            if status["PORT ACTIVE"]:
                continue

            for tconfig in type_configs:
                if tconfig in ignored_configs:
                    continue
                with open(tconfig) as tcfg:
                    json_tcfg = json.load(tcfg)

                json_tcfg = check_config(json_tcfg, "type", tconfig)

                if json_tcfg is None:
                    ignored_configs.append(tconfig)
                    continue

                serial = cam.serial
                status["CAM SERIAL"] = serial

                if json_tcfg.information.device.product == cam.product:
                    port = self._port + i
                    i += 1

                    json_tcfg.information.device = cam
                    self._configs[port] = {"CONFIG TYPE": json_tcfg, "CONFIG MODEL": None}
                    write_configuration_file(filename=f"{port}.json", cam_config_path=self._cam_config_path, content=json_tcfg.model_dump())
                    self._subprocess_dict[port] = subprocess.Popen(
                        [sys.executable, f"{pathlib.Path(__file__).parent.parent / 'camera_app/camera_interface.py'}", f"{port}"]
                    )
                    status["CONFIG TYPE"] = True
                    status["PORT"] = port
                    status["PORT ACTIVE"] = True
                    status["CALIBRATION AVAILABLE"] = json_tcfg.calibration.available
                    self.cam_status.append(status)
                    break

    def _get_video_device(self) -> list[VideoDevice]:
        streams: list[VideoDevice] = get_connected_cams(verbose=True)
        idx = [int(x) for x in input("\nEnter the stream indeces seperated by whitespace: ").split()]
        return [streams[i] for i in idx]

    def run(self):
        """
        Runs the manager application.
        """

        self._prepare_cam_descriptions()
        if not self.cam_status:
            raise ValueError(f"No valid Camera Descriptions were found in {self._path}. Please provide a valid .json file.")

        header = self.cam_status[0].keys()
        rows = [x.values() for x in self.cam_status]
        print(tabulate.tabulate(rows, header))

        serve(self._flask, host="0.0.0.0", port=self._port)
