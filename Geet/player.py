from vlc import MediaPlayer, Media
from prompt_toolkit import print_formatted_text
from .utils import Utils
import time


class Player:
    def __init__(self) -> None:
        self.media_player = MediaPlayer()
        self.media_info = {}
        pass

    def play(self, stream_url: str) -> int:
        media = Media(stream_url)
        self.media_player.set_media(media)
        if not self.media_player.is_playing():
            self.media_player.stop()
        self.media_player.play()
        time.sleep(10)
        position = self.get_current_position()
        return [1, position]

    def toggle_play_pause(self, state: str) -> int:
        if not self.media_player.get_media():
            return "There is no song playing."

        if state == "pause":
            if not self.media_player.is_playing():
                return "<b>Already Paused</p>"
            self.media_player.pause()
            return "<b><orange>Paused</orange></b>"
        elif state == "resume":
            if self.media_player.is_playing():
                return "<b>Already Playing</p>"
            self.media_player.play()
            return "<b><orange>Resumed</orange></b>"

    def get_current_position(self) -> str:
        total_time = self.media_player.get_length()
        current_time = self.media_player.get_time()
        if total_time < 0:
            pass
        total_time_format = Utils().format_time(total_time)
        current_time_format = Utils().format_time(current_time)
        time_format_text = f"{current_time_format}/{total_time_format}"
        return time_format_text

    def stop(self) -> str:
        if not self.media_player.get_media():
            message = "There is no song playing."
        else:
            message = "<b><orange>Stopped</orange></b>"
        self.media_player.stop()
        return message
