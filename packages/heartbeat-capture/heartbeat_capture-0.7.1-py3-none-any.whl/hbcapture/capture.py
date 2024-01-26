import logging
import re
from datetime import datetime
from pytz import timezone
import numpy as np
import uuid
import os
from hbcapture.data import DataPoint

class CaptureFileMetadata:
    METADATA_START = "## BEGIN METADATA ##"
    METADATA_END = "## END METADATA ##"
    PATTERN_METADATA_START = r"## BEGIN METADATA ##"
    PATTERN_METADATA_END = r"## END METADATA ##"

    def __init__(self, capture_id: uuid.UUID, sample_rate: float):
        self.capture_id = capture_id
        self.sample_rate = sample_rate
        self.metadata = {}

    def set_metadata(self, key: str, value: str):
        self.metadata[key] = value

    def get_metadata(self, key: str):
        return self.metadata[key]

    def to_string(self) -> str:
        string = ""
        string += CaptureFileMetadata.METADATA_START + "\n"
        string += f"# CAPTURE_ID\t\t\t{self.capture_id}\n"
        string += f"# SAMPLE_RATE\t\t\t{self.sample_rate}\n"
        for key, value in self.metadata.items():
            tab_count = 4 - (len(key) - 8) / 4 
            tabs = "\t" * int(tab_count)
            string += f"# {key}{tabs}{value}\n"
        string += CaptureFileMetadata.METADATA_END + "\n"
        return string

    def parse_string(string: str):
        raise NotImplementedError()

    def __repr__(self):
        result = "HeartbeatCaptureFileMetadata {" % (self.capture_id, self.sample_rate)
        result += "\tcapture_id: %s, " % (self.capture_id)
        result += "\tsample_rate: %s, " % (self.sample_rate)
        for key, value in self.metadata.items():
            result += "\t%s: %s, " % (key, value)
        result += "}"
        return result

class CaptureFileWriter:
    def __init__(self, path: str, metadata: CaptureFileMetadata):
        self.path = path
        self.metadata = metadata
        self.logger = logging.getLogger("hb.capture.file.writer")
        self.file = None

        # TODO check if file exists?
        if os.path.exists(path):
            self.logger.warn(f"File {path} already exists")

    def __enter__(self):
        self.open()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def open(self):
        self.logger.debug(f"Opening file {self.path}")
        self.file = open(self.path, 'w')
        self.reset_file()

    def write_data(self, data: DataPoint):
        if self.file is None:
            self.logger.error("File not open")
            return
        self.file.write(data.generate_line() + "\n")
    
    def reset_file(self):
        if self.file is None:
            self.logger.error("File not open")
            return
        
        self.file.seek(0)
        self.file.truncate()
        self.metadata.set_metadata("CREATED", datetime.utcnow().isoformat())
        self.file.write(self.metadata.to_string())

    def close(self):
        if self.file is None:
            self.logger.error("File not open")
            return
        self.file.close()
        self.file = None
