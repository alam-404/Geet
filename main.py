from subprocess import call
import os
from prompt_toolkit import prompt, print_formatted_text
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.output import ColorDepth
from pyfiglet import Figlet


from Geet.command import Command
from Geet import __version__, __title__, __description__


def splash() -> None:
    call("clear" if os.name == "posix" else "cls")
    figlet = Figlet(font="epic")
    epic_text = figlet.renderText(__title__)
    screen = f"<blue>{epic_text}</blue>\n\n<b>Geet</b> @ {__version__}\n<gray>{__description__}</gray>\n\nType help to get started."
    print_formatted_text(HTML(screen))


def main() -> int:
    splash()
    prefix = "> "
    player_text = ""
    command = Command()
    while 1:
        prompt_text = HTML(f"{player_text}<b>{prefix}</b>")
        try:
            command_text = prompt(
                prompt_text,
                completer=command.completer,
                complete_in_thread=True,
                color_depth=ColorDepth.TRUE_COLOR,
            ).lower()
        except KeyboardInterrupt:
            command.soft_exit()
            break
        else:
            if command_text.strip() in ["q", "quit", "exit"]:
                command.soft_exit()
                break
            success = command.execute(command_text=command_text)
            success_code = success["success"]
            success_message = success["message"]
            player_text = success["player_status"]
            if player_text:
                player_text = f"\n{player_text}\n"
            if not success_code:
                command.soft_exit()
                break
            success_message and print_formatted_text(HTML(success_message))
    return 0


if __name__ == "__main__":
    main()
