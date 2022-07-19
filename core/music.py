# weird bug: strange noise when volume is too small
import pyaudio,wave,threading,numpy,time

class musicThread(threading.Thread):
	def __init__(self,path,startTime,volume,offset):
		threading.Thread.__init__(self)
		self.path=path
		self.startTime=startTime-offset/1000
		self.volume=volume/100
	def run(self):
		self.quit=False
		audio=pyaudio.PyAudio()
		with wave.open(self.path) as file:
			formatType=audio.get_format_from_width(file.getsampwidth())
			npType=eval(f"numpy.int{formatType}")
			stream=audio.open(format=pyaudio.paInt16,channels=file.getnchannels(),rate=file.getframerate(),frames_per_buffer=1024,output=True)
			while time.perf_counter()<self.startTime:
				pass
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