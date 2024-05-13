from vlc import MediaPlayer, Media
from prompt_toolkit import print_formatted_text


class Player:
    def __init__(self) -> None:
        self.media_player = MediaPlayer()
        pass

    def play(self, stream_url: str) -> int:
        media = Media(stream_url)
        self.media_player.set_media(media)
        if not self.media_player.is_playing():
            self.media_player.stop()
        self.media_player.play()
        return 1

    def toggle_play_pause(self) -> int:
        if self.media_player.is_playing():
            self.media_player.pause()
            message = "<b><orange>Paused</orange></b>"
        else:
            if not self.media_player.get_media():
                message = "There is no song playing."
            else:
                message = "<b><orange>Resumed</orange></b>"
            self.media_player.play()
        return message

    def stop(self) -> int:
        self.media_player.stop()
