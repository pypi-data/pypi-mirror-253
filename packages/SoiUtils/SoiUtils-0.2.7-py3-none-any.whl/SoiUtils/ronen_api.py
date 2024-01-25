from threading import Thread
import socket
import json
from cv2 import VideoCapture
import select
from queue import Queue, Full
import logging

class SendResults():
    def __init__(self, server_url, port):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((server_url, self.port))

    def run(self, results_dict):
        self.socket.sendall(f'{json.dumps(results_dict)}\n'.encode('utf-8'))

    def close(self):
        self.socket.close()


class CaptureThread(Thread):
    def __init__(self, uri: str, queue: Queue,sub_sampling_factor:int):
        """
        sub_sampling_factor - indicates the freqency of the sampling, 1 means that each frame will be inserted to the queue,
        2 menas that every second frame will be inserted and etc'
        """
        super(CaptureThread, self).__init__()
        self.uri = uri
        self.queue = queue
        self.closed = False
        self.finished = False
        self.sub_sampling_factor = sub_sampling_factor
        self._sub_sampling_residual = 0

    def run(self):
        print("starting video capture thread...")
        cap = VideoCapture(self.uri)
        try:
            while cap.isOpened() and not self.closed:
                ret, frame = cap.read()
                if ret:
                    if self._sub_sampling_residual == 0:
                        logging.debug('Inserting to queue') 
                        try:
                            self.queue.put_nowait(frame)
                        except Full:
                            logging.warning("Video Capture Queue is full, skipping frame")
                    else:
                        logging.debug(f'The residual is {self._sub_sampling_residual} therefore the frame is not inserted')
                    
                    self._sub_sampling_residual = (self._sub_sampling_residual+1) % self.sub_sampling_factor
        finally:
            self.finished = True
            cap.release()
    def isFinished(self):
        return self.finished

    def close(self):
        self.closed = True


class TelemetryThread(Thread):
    def __init__(self, server_url: str, port: int, bufsize: int):
        super(TelemetryThread, self).__init__()
        self.server_url = server_url
        self.port = port
        self.bufsize = bufsize
        self.closed = False
        self.finished = False
        self.latest_telemetry = None

    def run(self):
        print("starting api thread...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.server_url, self.port))
            s.setblocking(False)
            while not self.closed:
                ready = select.select([s], [], [], 1)
                if ready[0]:
                    data, addr = s.recvfrom(self.bufsize)
                    temp = json.loads(data.decode('UTF-8'))

                    if temp["messageType"] == "telemetry":
                        self.latest_telemetry = temp
        finally:
            self.finished = True
            s.close()

    def isFinished(self):
        return self.finished

    def getLatestAsDict(self):
        return self.latest_telemetry.copy()

    def close(self):
        self.closed = True
