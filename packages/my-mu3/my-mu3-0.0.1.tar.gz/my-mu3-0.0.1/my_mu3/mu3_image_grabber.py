import cv2
import multiprocessing
import numpy as np
import queue
import time
import urllib.request

# https://www.digicamsoft.com/itu/itu-t81-36.html
JPEG_IMAGE_START_MARKER = b"\xff\xd8"
JPEG_IMAGE_END_MARKER = b"\xff\xd9"
EXPECTED_SIZE = (240, 180)
NUM_CHANNELS = 3 # we have R,G,B
NUM_IMAGE_BYTES = EXPECTED_SIZE[0] * EXPECTED_SIZE[1] * NUM_CHANNELS


class Mu3ImageGrabber:
    def __init__(self, ip_address: str, max_q_size: int = 3, port: int = 8888,
                 url_postfix: str = "stream", byte_chunksize: int = 1024):
        """
        This is a class that will start a sub process to grab images via http streaming. An example full url
        would be 'http://192.168.1.174:8888/stream'
        :param ip_address: the ip address of the MU3 Sensor on the network, for example 192.168.1.174
        :param port: the port, usually 8888
        :param url_postfix: the postfix to stream video, usually stream
        """

        self.full_http_address = "http://" + ip_address + ":"  + str(port) + f"/{url_postfix}"
        self.byte_chunksize = byte_chunksize

        self.manager = multiprocessing.Manager()
        self.queue = self.manager.Queue(maxsize=max_q_size)
        self.num_images_from_camera = self.manager.Value("unsigned int", 0)
        self.exit_flag = self.manager.Value("signed short", 0)

        self.sub_process = multiprocessing.Process(target=Mu3ImageGrabber.get_images,
                                                   args=(self.full_http_address, self.queue,
                                                         self.byte_chunksize, self.num_images_from_camera,
                                                         self.exit_flag))
        self.images_grabbed = 0
        self.start_time = time.time()

    def start(self):
        self.start_time = time.time()
        self.sub_process.start()

    def stop(self):
        self.exit_flag.value = 1
        self.sub_process.join()
        fps = self.num_images_from_camera.value / (time.time() - self.start_time)
        print(f"fps: {round(fps, 2)}")

    def get_image(self, get_image_timeout: float = 0.2):
        """
        Returns None or an image if one is available.
        :return:
        """
        if self.queue.empty():
            return None
        else:
            try:
                return self.queue.get(block=True, timeout=get_image_timeout)
            except queue.Empty:
                return None

    @staticmethod
    def get_images(full_url: str, my_queue: queue.Queue, byte_chunksize: int,
                   num_images_from_cam: multiprocessing.Value, exit_flag: multiprocessing.Value):
        stream = urllib.request.urlopen(f"{full_url}")
        byte_arr = bytearray()

        while exit_flag.value != 1:
            byte_arr += stream.read(byte_chunksize)
            start_of_image = byte_arr.find(JPEG_IMAGE_START_MARKER)
            end_of_image = byte_arr.find(JPEG_IMAGE_END_MARKER)
            if start_of_image != -1 and end_of_image != -1:
                raw_bytes = bytes(byte_arr[start_of_image:end_of_image + 2])
                byte_arr = byte_arr[end_of_image + 2:]
                np_arr = np.frombuffer(raw_bytes, dtype=np.uint8)
                image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
                if image is None or image.size != NUM_IMAGE_BYTES:
                        continue
                else:
                    num_images_from_cam.value += 1
                    my_queue.put(image)