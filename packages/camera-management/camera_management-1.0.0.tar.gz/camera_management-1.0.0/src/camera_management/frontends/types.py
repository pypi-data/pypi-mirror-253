import base64
import dataclasses
import enum
import pickle
import time
import typing

import numpy as np

from camera_management.tools.types import ImageResolution


@dataclasses.dataclass
class CameraInformation:
    custom_cam_name: str
    cam_uuid: str
    stream_resolution: ImageResolution


class CameraDicts(typing.TypedDict):
    cam_name: str
    info: CameraInformation


@dataclasses.dataclass
class DataUnit:
    timestamp: int = -1


@dataclasses.dataclass
class ImageProcessorData(DataUnit):
    """Event to carry current frame data of one thread."""

    # custom_cam_name: str
    image: np.ndarray = None
    curr_fps: float = None
    avg_fps: float = None
    meas_load_shares: dict = None


class ImageDicts(typing.TypedDict):
    cam_name: str
    data: ImageProcessorData


@dataclasses.dataclass
class ProcessedData(DataUnit):
    data: dict | str = None
    packed: bool = False

    def pack(self):
        """
        INSERT USEFUL DESCRIPTION WHEN SEEING THIS
        """
        data = pickle.dumps(self.data)
        self.data = base64.b64encode(data).decode("utf-8")
        self.packed = True
        return self

    def unpack(self):
        """
        INSERT USEFUL DESCRIPTION WHEN SEEING THIS
        """
        data = base64.b64decode(self.data)
        self.data = pickle.loads(data)
        self.packed = False
        return self

    @classmethod
    def load_from_dict(cls, content: dict):
        """
        INSERT USEFUL DESCRIPTION WHEN SEEING THIS
        """
        pd = cls(**content)
        if pd.packed:
            pd.unpack()
        return pd


@dataclasses.dataclass
class LoggingUnit:
    log: list = dataclasses.field(default_factory=list)
    index: int = -1
    max_entries: int = 10


@dataclasses.dataclass
class MeasConfig(DataUnit):
    measure_flm: bool = False
    measure_hands: bool = False
    measure_pose: bool = False
    measure_aruco: bool = False
    measure_hipcm: bool = False
    measure_chessb: bool = False
    track_head: bool = False


@dataclasses.dataclass
class ViewConfig(DataUnit):
    show_stream_meta_data: bool = False


@dataclasses.dataclass
class Control(DataUnit):
    pause_stream: bool = False
    store_images: bool = False


@dataclasses.dataclass
class Configs:
    meas = MeasConfig()
    view = ViewConfig()


class InterfaceData:
    def __init__(self) -> None:
        self.cam_info = CameraDicts()
        self.image_data = ImageDicts()
        self.configs = Configs()
        self.control = Control()
        self.state = HandlerState.INIT
        self.processed_data = ProcessedData()
        self.log_unit = LoggingUnit()

    def get_id_timestamps(self) -> dict:
        """
        INSERT USEFUL DESCRIPTION WHEN SEEING THIS
        """
        data = self.image_data
        return {id: data[id].timestamp for id in data.keys()}

    @property
    def log(self):
        """
        INSERT USEFUL DESCRIPTION WHEN SEEING THIS
        """
        return self.log_unit.log

    @log.setter
    def log(self, value):
        self.log_unit.index += 1
        self.log_unit.log.append((self.log_unit.index, time.time_ns(), value))
        if len(self.log_unit.log) > self.log_unit.max_entries:
            self.log_unit.log.pop(0)


class HandlerState(enum.IntEnum):
    """States of operation for the control thread of StreamThreadHandler."""

    INIT = -1
    STREAMING = 10
    PAUSED = 20
    STORING = 30
    EXIT = 99
    STOP = 100


if __name__ == "__main__":
    t = InterfaceData()

    t.image_data["test"] = ImageProcessorData()
    t.image_data["test2"] = ImageProcessorData(-555)
    print(t.image_data.keys())

    data = t.image_data
    ids = list(data.keys())
    msg = {id: data[id].timestamp for id in ids}
    id_str = "\t".join(ids)
    print(msg)

    print(t.get_id_timestamps())
