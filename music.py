import pyaudio,wave,threading,numpy

class musicThread(threading.Thread):
	def __init__(self,volume=100):
		threading.Thread.__init__(self)
		self.volume=volume/100
	def run(self):
		self.quit=False
		audio = pyaudio.PyAudio()
		with wave.open('t.wav', "rb") as file:
			formatType=audio.get_format_from_width(file.getsampwidth())
			npType=eval(f"numpy.int{formatType}")
			stream = audio.open(format=pyaudio.paInt16,channels=file.getnchannels(),rate=file.getframerate(),frames_per_buffer=1024,output=True)
			data=file.readframes(1024)
			while len(data)>0 and not self.quit:
				data=(self.volume*numpy.frombuffer(data,npType)).astype(npType)
				stream.write(data)
				data=file.readframes(1024)
			stream.stop_stream()
			stream.close()
		audio.terminate()

if __name__ == "__main__":
	m=musicThread()
	m.start()
	m.join()