from abc import ABC,abstractmethod
from dataclasses import dataclass
from enum import Enum



@dataclass
class AudioPlayer(ABC):
    def __init__(self, volume: float, playback_rate: float):
        self.volume = volume
        self.playback_rate = playback_rate
        self.is_playing = False

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class MediaFormat(Enum):
    MP3 = "mp3"
    WAV = "wav"
    FLAC = "flac"


@dataclass
class FLACPlayer(AudioPlayer):
    volume: int
    playBackRate: float

    def play(self):
        print("Playing FLAC audio")

    def pause(self):
        print("Pausing FLAC audio")

    def stop(self):
        print("Stopping FLAC audio")

    def set_volume(self, volume: int):
        if 0 <= volume <= 100:
            self.volume = volume
            print("Volume set to", volume)
        else:
            print("Invalid volume level")

    def supports_type(self):
        return MediaFormat.FLAC


@dataclass
class MP3Player(AudioPlayer):
    volume: int
    playBackRate: float

    def play(self):
        print("Playing MP3 audio")

    def pause(self):
        print("Pausing MP3 audio")

    def stop(self):
        print("Stopping MP3 audio")

    def set_volume(self, volume: int):
        if 0 <= volume <= 100:
            self.volume = volume
            print("Volume set to", volume)
        else:
            print("Invalid volume level")

    def supports_type(self):
        return MediaFormat.MP3


@dataclass
class WAVPlayer(AudioPlayer):
    volume: int
    playBackRate: float

    def play(self):
        print("Playing WAV audio")

    def pause(self):
        print("Pausing WAV audio")

    def stop(self):
        print("Stopping WAV audio")

    def set_volume(self, volume: int):
        if 0 <= volume <= 100:
            self.volume = volume
            print("Volume set to", volume)
        else:
            print("Invalid volume level")

    def supports_type(self):
        return MediaFormat.WAV



class MP3AudioPlayer(AudioPlayer):
    def play(self):
        self.is_playing = True
        print("Playing MP3 file")

    def pause(self):
        self.is_playing = False
        print("Pausing MP3 file")

    def stop(self):
        self.is_playing = False
        print("Stopping MP3 file")


class WAVAudioPlayer(AudioPlayer):
    def play(self):
        self.is_playing = True
        print("Playing WAV file")

    def pause(self):
        self.is_playing = False
        print("Pausing WAV file")

    def stop(self):
        self.is_playing = False
        print("Stopping WAV file")


class FLACAudioPlayer(AudioPlayer):
    def play(self):
        self.is_playing = True
        print("Playing FLAC file")

    def pause(self):
        self.is_playing = False
        print("Pausing FLAC file")

    def stop(self):
        self.is_playing = False
        print("Stopping FLAC file")