
from audio.products import (
    AudioPlayer, MediaFormat, MP3Player, WAVPlayer, FLACPlayer,
)


class AudioPlayerFactory:
    @staticmethod
    def create_audio_player(format_: MediaFormat, volume: int, playback_rate: float) -> AudioPlayer:
        format = format_.value.lower()
        if format == "mp3":
            return MP3Player(volume, playback_rate)
        elif format == "wav":
            return WAVPlayer(volume, playback_rate)
        elif format == "flac":
            return FLACPlayer(volume, playback_rate)
        else:
            raise ValueError(f"Unsupported audio format: {format}")