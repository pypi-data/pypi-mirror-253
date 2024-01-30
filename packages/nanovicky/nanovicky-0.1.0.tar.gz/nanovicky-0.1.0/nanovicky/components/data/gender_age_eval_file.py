import os
from typing import List, Dict
import json
import logging

from components import BaseComponent
from models import Input


class GenderAgeEvalFile(BaseComponent):
    def __init__(self, name: str, file_path: str):
        super().__init__(name=name)
        self._inputs["data"] = Input()
        self._file_path: str = file_path

    def initiate(self):
        try:
            file = open(self._file_path, "w")
            file.close()
        except Exception as error:
            logging.error(self.log_message(f">>> Error : {error}"))

    def do(self):
        data = self._inputs["data"].get()

        if data is not None and data != []:
            file = open(self._file_path, "a")
            [
                file.write(
                    f'{d["timestamp"]},{d["x"]},{d["y"]},{d["width"]},{d["height"]},{d["gender"]},{d["age"]}\n'
                )
                for d in data
            ]
