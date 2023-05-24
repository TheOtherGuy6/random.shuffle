# Random Shuffle Music Player

This script is a random shuffle music player that plays music files from a specified folder in a random order. It uses the Pygame library to play the music and provides some additional information while playing each song.

## Installation

To use this script, you need to have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

This script requires the Pygame library. You can install Pygame using pip, which is a package installer for Python. Open a command prompt or terminal and run the following command:

```
pip install pygame
```

## Usage

1. Clone or download the script from the GitHub repository.

2. Move the script to your desktop.

3. Open a command prompt or terminal.

4. Change the current directory to your desktop by running the following command:

```
cd %USERPROFILE%\Desktop
```

5. Run the script using the following command:

```
python "random.shuffle(V3).py"
```

6. The music player will start playing random songs from the specified music folder.

## Functionality

The script performs the following steps:

1. It imports necessary libraries and modules including `os`, `random`, `datetime`, `pygame`, and `signal`.

2. The script defines two ANSI escape codes, `BOLD` and `RESET`, for formatting text.

3. It initializes the `music_folder` variable to the path of the music folder. Modify this variable to point to your music folder.

4. The script searches for music files (with extensions .wav, .wma, .flac, .mp3) in the specified `music_folder` and stores them in a list called `music_files`. It stores both the folder path and filename for each music file.

5. The list of music files is shuffled randomly using the `random.shuffle()` function.

6. It initializes variables `song_count` (to keep track of the number of songs played), `repeat_song_counter` (to count the number of times each song is repeated), `skip_counter` (to count the number of song skips), and `start_time` (to record the start time of the program).

7. The script defines a signal handler function `skip_song()` to handle the interruption signal (Ctrl+C) and increment the `skip_counter` variable.

8. It registers the `skip_song()` function as the signal handler for the interruption signal (Ctrl+C).

9. Inside a try-except block, the script initializes the Pygame mixer.

10. It iterates through each music file in the shuffled `music_files` list.

11. For each file, it loads the file into the Pygame mixer based on its extension.

12. The script increments the `song_count` variable and updates the `repeat_song_counter` for the current song.

13. It calculates the current time, elapsed time, and formatted date.

14. The script prints the following information for the current song:

    - Parent folder, folder name, and filename.
    - Song count.
    - Current time.
    - Date.
    - Elapsed time.
    - Repeat song counter for the current song.

15. Inside a nested try-except block, the script plays the loaded music using the Pygame mixer and waits until the song finishes playing.

16. If an exception is raised (indicating a skip signal from the signal handler), the script prints a message indicating the song skip and the current `skip_counter` value.

17. After each song is played, the script prints the copyright information and a message indicating shuffling of music.

18. If the program is interrupted by the user (Ctrl+C), the script handles the `KeyboardInterrupt` exception and prints a message indicating the

 interruption.

19. Finally, the script prints a closing message and the copyright information.

## Keyboard Interrupt (Ctrl+C)

If you want to stop the music player before it finishes playing all the songs, you can press Ctrl+C in the command prompt or terminal where the script is running. The program will print a closing message and exit gracefully.

## License

This script is created by Wayne Fry and all rights are reserved.
