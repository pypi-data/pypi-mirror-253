from datetime import datetime
import numpy as np

class DataPoint:
    def __init__(self, time: datetime, sample_rate: int, data):
        self.time = time
        self.data = data
        self.flags = DataPointFlags(False, False)
        self.sample_rate = sample_rate
        self.lat = 0
        self.lon = 0
        self.elev = 0
        self.satellites = 0
        self.speed = 0
        self.angle = 0

    def generate_line(self) -> str:
        return "{time:.6f},{flags},{sample_rate},{lat},{lon},{elev},{satellites},{speed},{angle},".format(
            time=self.time.timestamp(),
            flags=self.flags.to_string(),
            sample_rate=self.sample_rate,
            lat=self.lat,
            lon=self.lon,
            elev=self.elev,
            satellites=self.satellites,
            speed=self.speed,
            angle=self.angle
        ) + ",".join([str(x) for x in self.data])
    
    def to_array(self) -> np.ndarray: 
        return np.array(self.data)
    
    def has_gps_fix(self) -> bool:
        return self.flags.gps
    
    def is_clipping(self) -> bool:
        return self.flags.clipping
    
class DataPointFlags:
    def __init__(self, gps: bool, clipping: bool):
        self.gps = gps
        self.clipping = clipping
        pass

    def __repr__(self):
        return "HeartbeatCaptureLineFlags(%s, %s)" % (self.gps, self.clipping)
    
    def to_string(self):
        flags = ""
        if self.gps:
            flags += "G"
        if self.clipping:
            flags += "O"

        return flags

    def parse(text: str):
        return DataPointFlags(gps=(text.find("G") != -1), clipping=(text.find("O") != -1))
    
    def __eq__(self, other):
        if isinstance(other, DataPointFlags):
            return self.gps == other.gps and self.clipping == other.clipping
        return False

def parse(text: str) -> DataPoint:
        parts = text.split(",")
        parts_time = float(parts[0])
        parts_flags = DataPointFlags.parse(parts[1])
        parts_sample_rate = float(parts[2])
        parts_lat = float(parts[3])
        parts_lon = float(parts[4])
        parts_elev = float(parts[5])
        parts_sats = int(parts[6])
        parts_speed = float(parts[7])
        parts_angle = float(parts[8])

        data = [int(x) for x in parts[9:]]

        capture_line = DataPoint(time=datetime.utcfromtimestamp(parts_time),
                                 sample_rate=parts_sample_rate,
                                 data=data)

        capture_line.flags = parts_flags
        capture_line.sample_rate = parts_sample_rate
        capture_line.lat = parts_lat
        capture_line.lon = parts_lon
        capture_line.elev = parts_elev
        capture_line.satellites = parts_sats
        capture_line.speed = parts_speed
        capture_line.angle = parts_angle

        return capture_line