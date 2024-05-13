from prompt_toolkit import prompt, print_formatted_text
from prompt_toolkit.formatted_text import HTML

from command import Command


def main() -> int:
    prefix = "> "
    prompt_text = HTML(f"<b>{prefix}</b>")
    command = Command()
    while 1:
        try:
            command_text = prompt(
                prompt_text,
                completer=command.completer,
                complete_in_thread=True,
            ).lower()
        except KeyboardInterrupt:
            break
        else:
            if command_text.strip() == "":
                continue
            if command_text.strip() in ["q", "quit", "exit"]:
                break
            success = command.execute(command_text=command_text)
            success_code = success["success"]
            success_message = success["message"]
            if not success_code:
                break
            success_message and print_formatted_text(HTML(success_message))

    return 0


if __name__ == "__main__":
    main()
