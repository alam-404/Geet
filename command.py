from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit import print_formatted_text
from fetch import Fetch
from ui import Dialog
from player import Player


class Command:
    commands = {
        "play": None,
        "pause": None,
        "resume": None,
        "stop": None,
        "now": None,
    }
    completer = NestedCompleter(commands)
    player = Player()  # media player

    def __init__(self) -> None:
        pass

    def execute(self, command_text: str) -> dict:
        command, text = self.get_text(command_text)
        success = {"success": True, "message": ""}
        # match commands
        match command.lower():
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
                playing = self.player.play(stream_url)
                if playing:
                    success["message"] = (
                        f"<b><green>Playing: </green></b> {select['name']} by {select['artist']}"
                    )
                return success

            case "pause":
                message = self.player.toggle_play_pause()
                success["message"] = message
                return success
            case "resume":
                message = self.player.toggle_play_pause()
                success["message"] = message
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
