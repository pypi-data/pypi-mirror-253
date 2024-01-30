from time import sleep
from multiprocessing import Process
from threading import Thread

import cv2 as opencv
from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
from requests import get

from models import Frame
from components import BaseComponent
from models import FrameInput, Input


class WebStreamerComponent(BaseComponent):
    def __init__(self, name: str, host: str = "127.0.0.1", port: int = 5000):
        super().__init__(name=name)
        self._inputs = {"frames": Input()}

        self._host: str = host
        self._port: int = port

        self._app: Flask = Flask(self._name)
        CORS(self._app)

        self._server = None
        self._current_frame: Frame = None

    def convert(self, format: str = "jpg"):
        """Converts frames and yield it to display it on the web."""

        try:
            while self._running:
                frame = self._current_frame
                if frame is not None:
                    buffer = opencv.imencode(f".{format}", frame.image)[1]
                    image = buffer.tobytes()
                    yield (
                        b"--BOUNDARYSTRING0\r\n"
                        b"Content-Type: image/jpeg\r\n\r\n" + image + b"\r\n"
                    )
                else:
                    print("Image is None")
                    sleep(1)
        except StopIteration:
            print("Waiting for frames (stream must be reloaded)...")
            sleep(0.1)

    def initiate(self) -> None:
        """Launch a streamer on the host:port url, reachable from a browser.

        Args:
            frames (Generator[Frame, None, None], optional): The frames to stream. Defaults to None.
        """

        @self._app.route("/")
        @cross_origin()
        def index():
            return Response(
                self.convert(),
                mimetype="multipart/x-mixed-replace; boundary=BOUNDARYSTRING0",
            )

        self._server = Thread(
            target=self._app.run,
            kwargs={"host": self._host, "port": self._port, "use_reloader": False},
            daemon=True,
        )
        self._server.start()

    def do(self):
        self._current_frame = self._inputs["frames"].get()
        sleep(1 / 25)
