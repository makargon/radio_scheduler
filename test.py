from audioplayer import AudioPlayer
from time import sleep

p = AudioPlayer("media/audio/radio_5_Ср_1.mp3")
p.play(block=False)
sleep(10)

p.stop()