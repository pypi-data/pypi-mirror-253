import click
import datetime as dt
import numpy as np
import random
import uuid
from pytz import timezone
from hbcapture.capture import CaptureFileWriter, CaptureFileMetadata
from hbcapture.data import DataPoint, DataPointFlags

@click.group()
def cli():
    pass

@click.command()
@click.option("--location", default="Earth")
@click.option("--node", default="SOFTWARE")
@click.option("--capture_id", default=uuid.uuid4())
@click.option("--file", default="capture.csv")
@click.argument('start')
@click.argument('end')
def generate(location, node, capture_id, file, start, end):
    dt_start = dt.datetime.fromtimestamp(float(start), tz=timezone('UTC'))
    dt_end = dt.datetime.fromtimestamp(float(end), tz=timezone('UTC'))

    capture_id = uuid.UUID(capture_id)

    print("Generating Heartbeat capture file from %s to %s" % (dt_start, dt_end))
    print("Will generate %d lines" % (dt_end - dt_start).total_seconds())

    sample_rate = 21010
    metadata = CaptureFileMetadata(capture_id, sample_rate)
    metadata.set_metadata("LOCATION", location)
    metadata.set_metadata("NODE_ID", node)
    
    node_id = "ET1234"
    capture_id = uuid.uuid4()
    
    with CaptureFileWriter(path=file, metadata=metadata) as writer:

        current_time = dt_start
        pulse_duration = 300
        after_length = 10

        print("Samples per line = %d" % (sample_rate * pulse_duration / 1000))
        counter = 0

        while current_time < dt_end:
            delay = (random.random() * 1)+4
            
            t_data = np.arange(0, (pulse_duration)/1000, 1/sample_rate)
            intensity = np.power(np.abs(np.sin(counter/40)), 1) 
            intensity = intensity + np.random.normal(0, 0.3, len(t_data))
            y_data = np.sin(2*np.pi*1000*t_data) * intensity
            data = np.concatenate([np.random.normal(0, 0.2, int(delay * sample_rate / 1000)), y_data])
            data = np.concatenate([data, np.random.normal(0, 0.2, int((after_length - delay) * sample_rate / 1000))])
            data = np.round(data * 512 + 512).astype(int)
            
            time = current_time + dt.timedelta(milliseconds= random.random() * 1000 / 2.0)
            # time = current_time
            writer.write_data(DataPoint(time=time, 
                                                        sample_rate=sample_rate, 
                                                        data=data))

            current_time += dt.timedelta(seconds = 1)
            counter += 1

            if counter % 3602 == 0:
                writer.next_file()
                print("Processed %d lines" % counter)
    

cli.add_command(generate)

if __name__ == '__main__':
    cli()