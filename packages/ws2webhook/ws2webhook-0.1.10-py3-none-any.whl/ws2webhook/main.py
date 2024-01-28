import json
import requests
import websocket
from typing import Optional
from logging import getLogger

class Ws2webhook:
    def __init__(self, websocket_endpoint: Optional[str] = None, webhook_endpoint: Optional[str] = None, remote_config_endpoint: Optional[str] = None) -> None:
        self.logger = getLogger(__name__)

        self.ws_init_endpoint = websocket_endpoint
        self.wh_init_endpoint_init = webhook_endpoint

        self.remote_config_endpoint = remote_config_endpoint

        self.ws_endpoint = websocket_endpoint if websocket_endpoint else ""
        self.ws_headers = {}
        self.ws_ping_interval = 0

        self.wh_endpoint = webhook_endpoint if webhook_endpoint else ""
        self.wh_headers = {}

        self._get_remote_config()

        self.ws_app = websocket.WebSocketApp(self.ws_endpoint, header=self.ws_headers, on_open=self._on_open, on_message=self._on_message, on_error=self._on_error, on_close=self._on_close)

    def run(self):
        self.logger.info("start establishing websocket connection")
        self.ws_app.run_forever(ping_interval=self.ws_ping_interval)

    def _on_message(self, ws, message) -> None:
        is_json = False
        try:
            data_json = json.loads(message)
        except:
            req = requests.post(self.wh_endpoint, headers=self.wh_headers, data=message)
        else:
            req = requests.post(self.wh_endpoint, headers=self.wh_headers, json=data_json)
            is_json = True
        in_json_str = " (in JSON format)" if is_json else ""
        self.logger.info(f"got a message: {message}\ndata sent: {req.status_code} {req.json()}{in_json_str}")

    def _on_error(self, ws, error) -> None:
        self.logger.info(f'error occurred: {error}')

    def _on_close(self, ws, close_status_code, close_msg) -> None:
        self.logger.info(f"disconnected streaming server: {close_status_code} {close_msg}")

    def _on_open(self, ws) -> None:
        self.logger.info("connected streaming server")

    def _get_remote_config(self) -> None:
        if self.remote_config_endpoint:
            self.logger.info(f"remote config endpoint detected and start fetching config: {self.remote_config_endpoint}")
            req = requests.get(self.remote_config_endpoint)
            data = req.json()
            if req.status_code == 200:
                self.logger.info(f"remote config received: {data}")
                if 'websocket' in data.keys():
                    self.logger.info("websocket config found on remote config")
                    self.ws_endpoint = data['websocket']['endpoint'] if 'endpoint' in data['websocket'].keys() else self.ws_endpoint
                    self.ws_headers = data['websocket']['headers'] if 'headers' in data['websocket'].keys() else self.ws_headers
                    self.ws_ping_interval = int(data['websocket']['ping_interval']) if 'ping_interval' in data['websocket'].keys() else self.ws_ping_interval

                if 'webhook' in data.keys():
                    self.logger.info("webhook config found on remote config")
                    self.wh_endpoint = data['webhook']['endpoint'] if 'endpoint' in data['webhook'].keys() else self.wh_endpoint
                    self.wh_headers = data['webhook']['headers'] if 'headers' in data['webhook'].keys() else self.wh_headers

            else:
                self.logger.info(f"remote config receive failed: {data}")
                raise ConnectionError
