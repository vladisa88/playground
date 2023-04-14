import os
import time

import ray

import requests
# import httpx


@ray.remote
class Test:
    def __init__(self, match_id: int, client_id: int) -> None:
        self._match_id = match_id
        self._client_id = client_id

    def main(self) -> None:
        resp = requests.get("https://google.com")
        print("REQUEST STATUS CODE", resp.status_code)
        print(f"Match ID: {self._match_id}, client ID: {self._client_id}. DDDDD")


def main(match_id: int, client_id: int) -> None:
    ref = Test.remote(match_id, client_id)
    ref.main.remote()
    time.sleep(100)

if __name__ == "__main__":
    match_id = int(os.environ["MATCH_ID"])
    client_id = int(os.environ["CLIENT_ID"])
    main(match_id, client_id)
