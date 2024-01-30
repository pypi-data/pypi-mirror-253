

import json
import uuid
import threading
import websocket
from .XUtils import _xu

class MessageType:
    TEXT = 'Text'
    JSON = 'JSON'

class WormholeEvents:
    WormholeOpen = "wormhole-open"
    WormholeClose = "wormhole-close"
    ResponseDataArrived = "wh-data-res"

class WormholeInstance:
    def __init__(self):
        self._ws = None
        self._ready = False
        self._data_waiters = {}
        self._listener = None

    def open(self, url):
        def on_message(ws, message):
            message = json.loads(message)
            print("message")
            data = message['data']
            waiter_id = data.get('eid')
            if waiter_id in self._data_waiters:
                self._data_waiters[waiter_id](data)

        def on_open(ws):
            self._ready = True
            print("Wormhole has been created")

        def on_close(ws, close_status_code, close_msg):
            self._ready = False
            print("Wormholer is closed...")

        websocket.enableTrace(True)
        self._ws = websocket.WebSocketApp(url,
                                          on_message=on_message,
                                          on_open=on_open,
                                          on_close=on_close)
        threading.Thread(target=self._ws.run_forever).start()

    def close(self):
        if self._ws:
            self._ws.close()

    def send(self, message, callback, message_type=MessageType.JSON):
        if self._ws:
            wormhole_message = self.create_message(message, message_type)
            self._data_waiters[wormhole_message['id']] = callback
            self._ws.send(json.dumps(wormhole_message))

    def send_sync(self, message, message_type=MessageType.JSON, timeout=10):
        """
        Sends a message synchronously and waits for a response.
        :param message: The message to send.
        :param message_type: The type of the message.
        :param timeout: Maximum time in seconds to wait for a response.
        :return: The response message or None if timeout occurs.
        """
        if not self._ws:
            raise Exception("WebSocket is not connected")

        response_event = threading.Event()
        response_data = {}

        def callback(data):
            response_data['result'] = data
            response_event.set()

        wormhole_message = self.create_message(message, message_type)
        self._data_waiters[wormhole_message['id']] = callback
        self._ws.send(json.dumps(wormhole_message))

        # Wait for the response or timeout
        response_event.wait(timeout)
        return response_data.get('result')

    def create_message(self, msg, message_type):
        message_id = _xu.guid()
        return {
            'id': message_id,
            'type': message_type,
            'data': json.dumps(msg)
        }

Wormholes = WormholeInstance()

