import pytest
import os
import datetime
import hbcapture
from hbcapture.data import DataPoint, DataPointFlags


def test_parse_data():
    line = "1706257309.000000,,20000.0,0.0,0.0,0.0,0,0.0,0.0,491,491,491,491,491,491,491"
    dp = hbcapture.data.parse(line)
    assert(dp.time == datetime.datetime(2024, 1, 26, 8, 21, 49))
    assert(dp.sample_rate == 20000)
    assert(dp.flags == DataPointFlags(False, False))
    assert(dp.data[0] == 491)
    assert(dp.lat == 0.0)
    assert(dp.lon == 0.0)
    assert(dp.elev == 0.0)
    assert(dp.angle == 0.0)
    assert(dp.speed == 0.0)
