from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit import print_formatted_text
from .fetch import Fetch
from .ui import Dialog
from .player import Player


class Command:
    commands = {
        "play": {"--yt": None},
        "pause": None,
        "resume": None,
        "stop": None,
        "now": None,
    }
    completer = NestedCompleter.from_nested_dict(commands)
    player = Player()  # media player

    def __init__(self) -> None:
        self.song_name = ""
        pass

    # execute the cli command
    def execute(self, command_text: str) -> dict:
        # get the text form prompt
        command, text = self.get_text(command_text)
        success = {"success": True, "message": "", "player_status": ""}

        # match commands
        match command.lower().strip():
            case "play":
                if text.strip() == "":
                    success["message"] = "You have to provide a query to search song."
                    return success
                fetch = Fetch()
                is_yt = text.split(" ")[0] == "--yt"
                if is_yt:
                    query = text.replace("--yt", "", 1)
                    # "fetch from yt"
                    success["success"] = False
                    success["message"] = "Command not done yet!"
                    return success

                # fetch from jiosaavn
                else:
                    res = fetch.from_saavn(query=text)

                status_code = res["code"]
                message = res["message"]
                if status_code != 200:
                    success["message"] = message
                    return success
                select = Dialog().radio_select(res["data"]).run()
                if not select:
                    success["message"] = "You have to select a song to play!"
                    return success
                stream_url = select["url"]
                playing, position = self.player.play(stream_url)
                if playing:
                    self.song_name = f"{select['name']} by {select['artist']}"
                    player_message = (
                        f"<b><green>Playing: </green></b> {self.song_name}\n{position}"
                    )
                    success["player_status"] = player_message
                return success

            case "pause":
                message = self.player.toggle_play_pause("pause")
                success["message"] = message

                position = self.player.get_current_position()
                player_message = f"<b><lightgreen>Paused: </lightgreen></b> {self.song_name}\n{position}"
                success["player_status"] = player_message
                return success

            case "resume":
                message = self.player.toggle_play_pause("resume")
                success["message"] = message
                position = self.player.get_current_position()
                player_message = f"<b><lightgreen>Playing: </lightgreen></b> {self.song_name}\n{position}"
                success["player_status"] = player_message
                return success

            case "now":
                position = self.player.get_current_position()
                player_message = (
                    f"<b><green>Now Playing: </green></b> {self.song_name}\n{position}"
                )
                success["message"] = player_message
                success["player_status"] = (
                    f"<b><green>Playing: </green></b> {self.song_name}\n{position}"
                )
                return success

            case "stop":
                message = self.player.stop()
                success["message"] = message
                return success

            case "":
                if not self.song_name:
                    return success

                position = self.player.get_current_position()
                player_message = f"<b><green>{self.player.state().capitalize()} </green></b> {self.song_name}\n{position}"
                success["player_status"] = player_message
                return success

            case _:
                success["message"] = "<b><red>No command found</red></b>"
                return success

    def get_text(self, command_text: str) -> list:
        sep_commands = command_text.split(" ")
        text = " ".join(
            [command for command in sep_commands if command not in self.commands]
        )
        return [sep_commands[0], text]

    def soft_exit(self) -> None:
        self.player.stop()
        print_formatted_text("See Ya!!")
