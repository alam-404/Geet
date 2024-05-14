from vlc import MediaPlayer, Media
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import HTML
from .utils import Utils


class Player:
    def __init__(self) -> None:
        self.media_player = MediaPlayer()
        self.media_info = {}
        pass

    def play(self, stream_url: str) -> int:
        media = Media(stream_url)
        self.media_player.set_media(media)
        if self.media_player.is_playing():
            self.media_player.stop()
        self.media_player.play()

        current_state = ""
        while 1:
            player_state = self.state().lower()
            if player_state == "playing":
                break
            elif player_state == "error":
                return [0, ""]
            elif player_state != current_state:
                print_formatted_text(
                    HTML(f"<b><yellow>{player_state.capitalize()}</yellow></b>")
                )

            current_state = player_state

        position = self.get_current_position()
        return [1, position]

    def toggle_play_pause(self, state: str) -> str:
        if not self.media_player.get_media():
            return "There is no song playing."

        if state == "pause":
            if not self.media_player.is_playing():
                return "<b>Already Paused</b>"
            self.media_player.pause()
            return "<b><orange>Paused</orange></b>"
        elif state == "resume":
            if self.media_player.is_playing():
                return "<b>Already Playing</b>"
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

    def state(self) -> str:
        player_state = self.media_player.get_state().value
        states = {
            0: "NothingSpecial",
            1: "Opening",
            2: "Buffering",
            3: "Playing",
            4: "Paused",
            5: "Stopped",
            6: "Ended",
            7: "Error",
        }
        return states[player_state]
