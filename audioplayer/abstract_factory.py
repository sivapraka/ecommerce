from abc import ABC, abstractmethod

from audioplayer.decoder import AudioDecoder, FLACDecoder, MP3Decoder
from audioplayer.model import MediaFormat
from audioplayer.player import AudioPlayer, FLACPlayer, MP3Player
from audioplayer.processor import AudioProcessor, MP3AudioProcessor, FLACAudioProcessor


class AudioFactory(ABC):
    @abstractmethod
    def supports_format(self) -> MediaFormat:
        pass

    @abstractmethod
    def create_audio_player(self, volume: float, playback_rate: float) -> AudioPlayer:
        pass

    @abstractmethod
    def create_audio_decoder(self, audio_data: bytes) -> AudioDecoder:
        pass

    @abstractmethod
    def create_audio_processor(self, audio_data: bytes) -> AudioProcessor:
        pass



class FLACAudioFactory(AudioFactory):
    def supports_format(self) -> MediaFormat:
        return MediaFormat.FLAC

    def create_audio_player(self, volume, playback_rate):
        return FLACPlayer(volume, playback_rate)

    def create_audio_decoder(self, audio_data):
        return FLACDecoder(audio_data)

    def create_audio_processor(self, audio_data):
        return FLACAudioProcessor(audio_data)


class MP3AudioFactory(AudioFactory):
    def supports_format(self) -> MediaFormat:
        return MediaFormat.MP3

    def create_audio_player(self, volume, playback_rate):
        return MP3Player(volume, playback_rate)

    def create_audio_decoder(self, audio_data):
        return MP3Decoder(audio_data)

    def create_audio_processor(self, audio_data):
        return MP3AudioProcessor(audio_data)