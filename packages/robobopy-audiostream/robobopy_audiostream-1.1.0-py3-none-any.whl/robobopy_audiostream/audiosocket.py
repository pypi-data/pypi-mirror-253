import socket
import threading
import queue
import time

from robobopy_audiostream.Exceptions import ClosedConnection

MAX_ATTEMPTS = 5

class AudioSocket:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.socket = None
        self.queue = queue.Queue()
        self.connected = False
        self.audio_thread = None
        self.ping_thread = None
        self.connect_attempts = MAX_ATTEMPTS
 
    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(2)
        self.socket.bind(("", self.server_port))

        self.send_message("CONNECT-AUDIO")

        self.connect_attempts = MAX_ATTEMPTS

        while not self.connected and self.connect_attempts > 0:
            try:
                print(f"Connecting to Audio Streaming Server: {self.server_address}")
                data, _ = self.socket.recvfrom(4096)
                if data:
                    self.connected = True
                    return True
            except socket.timeout:
                self.connect_attempts -= 1

        print(f"Failed to connect after {MAX_ATTEMPTS} attempts.")
        return False

    def disconnect(self):
        self.socket.close()
        self.connected = False

    def send_message(self, message):
        self.socket.sendto(message.encode(), (self.server_address, self.server_port))

    def receive_data(self):
        while self.connected:
            if self.connect_attempts <= 0:
                print("Closed connection from Audio Streaming Server")
                raise ClosedConnection
            else:
                try:
                    data, _ = self.socket.recvfrom(4096)  # Adjust buffer size as needed
                    timestamp, parameter, audio_data = self.parse_packet(data)
                    self.queue.put((timestamp, parameter, audio_data))
                    self.connect_attempts = MAX_ATTEMPTS
                except Exception as e:
                    self.connect_attempts -= 1

    def parse_packet(self, data):
        timestamp = int.from_bytes(data[:8], byteorder='big')
        parameter = int.from_bytes(data[8:16], byteorder='big', signed=True)
        audio_data = data[16:]
        return timestamp, parameter, audio_data

    def start_audio_thread(self):
        self.audio_thread = threading.Thread(target=self.receive_data)
        self.audio_thread.start()

    def ping_server(self):
        while self.connected:
            self.send_message("PING")
            time.sleep(1)  # Adjust the interval as needed

    def start(self):
        self.connect()
        self.start_audio_thread()
        self.ping_thread = threading.Thread(target=self.ping_server)
        self.ping_thread.start()

    def stop(self):
        if self.connected:
            self.send_message("DISCONNECT-AUDIO")

        self.connected = False

        if self.ping_thread and self.ping_thread.is_alive():
            self.ping_thread.join()

        if self.audio_thread and self.audio_thread.is_alive():
            self.audio_thread.join()

        print("Disconnecting socket")
        self.disconnect()

    def emptyQueue(self):
        self.queue = queue.Queue()