from robobopy_audiostream.audiosocket import AudioSocket

class RoboboAudio:
    def __init__(self, ip, robot_id=0):
        self.port = 40406 + (robot_id * 10)
        self.ip = ip
        self.audio_socket = AudioSocket(self.ip, self.port)
        
    def connect(self):
        if not self.audio_socket.connected:
            self.audio_socket.start()
        else:
            print("Can't connect to server")
            
    def disconnect(self):
        if (self.audio_socket.connected):
            self.audio_socket.stop()
    
    def getAudioBytes(self):
        if (self.audio_socket.connected):
            timestamp, parameter, audio_data = self.audio_socket.queue.get()
            return audio_data
        else:
            return None
    
    def getAudioWithMetadata(self):
        if (self.audio_socket.connected):
            timestamp, parameter, audio_data = self.audio_socket.queue.get()
            return (timestamp, parameter, audio_data)
        else:
            return None
    
    def syncAudioQueue(self):
        self.audio_socket.emptyQueue()
    
    def isConnected(self):
        return self.audio_socket.connected