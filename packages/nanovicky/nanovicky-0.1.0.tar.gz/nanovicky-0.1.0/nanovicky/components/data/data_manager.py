import os
from typing import List, Dict
import json
import logging

from tinydb import TinyDB
import requests

from components import BaseComponent
from models import Input


class API:
    def __init__(self, host: str, port: int = None, ssl: str = "http") -> None:
        self._host: str = host
        self._port: int = port
        self._ssl: str = ssl

        # Token buffer if the request implies a token
        self._token: str = None

    def update_token(self, token: str):
        self._token = token

    def url(self) -> str:
        if self._port is not None:
            return f"{self._ssl}://{self._host}:{self._port}"
        return f"{self._ssl}://{self._host}"

    def authenticate(self, route: str, credentials: Dict[str, str]):
        try:
            success, result, _ = self.request("POST", route, credentials)
            if success:
                self._token = result["token"]
        except KeyError:
            logging.error("The token field was not found in response")
        return self

    def request(self, method: str, route: str, body=None, header={}, params=None):
        if self._token is not None:
            header["Authorization"] = f"Bearer {self._token}"
        header["Content-Type"] = "application/json"

        result = requests.request(
            method=method,
            url=f"{self.url()}/{route}",
            data=json.dumps(body),
            headers=header,
        )

        content = None
        try:
            content = result.json()
        except Exception:
            content = result

        if 200 <= result.status_code < 300:
            return True, content, result.status_code

        logging.error(f"Received status code {result.status_code}")
        return False, content


class TinyDatabase:
    def __init__(self, name: str, collection: str) -> None:
        self._name: str = name

        # Ensure the database file is created before the database is initialized
        if not os.path.exists("/data/ivslite"):
            logging.warning("The data path add to be created")
            os.makedirs("/data/ivslite")

        file = open(f"/data/ivslite/{self._name}.json", "w")
        file.close()

        self._db = TinyDB(f"/data/ivslite/{self._name}.json")
        self._collection = self._db.table(collection)

    def post(self, data: Dict = None, datas: List[Dict] = None):
        if isinstance(data, Dict):
            self._collection.insert(data)

        if isinstance(data, List):
            [self._collection.insert(d) for d in data]

    def get(self):
        return self._collection.all()

    def delete(self, datas: List[Dict]):
        return self._collection.remove(doc_ids=[ids for ids in datas])


class DataManagerComponent(BaseComponent):
    def __init__(self, name: str):
        super().__init__(name=name)
        self._inputs["data"] = Input()
        self._db = TinyDatabase("IVSLite", "counting")
        self._api = API("box.preprod.ivstore.fr", ssl="https")

    def initiate(self):
        try:
            self._api.authenticate("token", {"token": "tokenEDSMigration"})
        except requests.ConnectionError:
            logging.error(self.log_message(">>> Error : could not connect to API"))

    def do(self):
        data = self._inputs["data"].get()
        if data is not None and data != []:
            print(f"Inserting data in the database : {data}")
            self._db.post(data)

        stored_data = [(data.doc_id, data) for data in self._db.get()]
        if stored_data:
            try:
                for id, data in stored_data:
                    result, content, code = self._api.request(
                        "POST", "boxes/1/customers", data
                    )
                    if result:
                        self._db.delete([id])
                        # ...
                    elif code == 401:
                        self._api.authenticate("token", {"token": "tokenEDSMigration"})
                        result, content, _ = self._api.request(
                            "POST", "boxes/1/customers", data
                        )
                        if result:
                            self._db.delete([id])
                        else:
                            print(
                                f"Even after re-authentication, an error occured while sending the datas : {content}"
                            )
                    else:
                        print(f"An error occured while sending the datas : {content}")
            except requests.ConnectionError:
                pass
                # print(">>> You are not connected to internet, data won't be send.")
