# Geet

## Overview

Geet is a music player that no one asked for.

## Project Details

### Dependencies

This project is written in Python and used the following packages:

1. **[prompt_toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/pages/getting_started.html)**: Used for creating a command-line interface (CLI) for user interaction.
2. **[python-vlc](https://wiki.videolan.org/Python_bindings/)**: Python binding for vlc. It used for controlling the player like playing, pausing, resuming, stopping etc.

## Installation

To use **Geet**, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/alam-404/Geet
    ```
2. Change the directory:
   ```sh
   cd Geet
   ```
3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the script:

    ```sh
    python main.py
    ```

## Basic Usage
To play a song -
```
> play song_name
```
It will fetch the song url from JioSaavn. And the use arrow keys to select the song then click on play.

In case of you want to play song from youtube -
```
> play --yt song_name
```

Type `help` to see more commands.

## Acknowledgments

Special thanks to [JioSaavn Unofficila API](https://saavn.dev/) and [yt-dlp](https://github.com/yt-dlp/yt-dlp)

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

This project is a personal project and not actively maintained. However, contributions are welcome. If you find any bugs or have suggestions for improvements, feel free to submit a pull request or open an issue.

