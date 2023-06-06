# Music Shuffling and Playing Script

The script is designed to shuffle and play music files from a specified folder. It supports various audio formats, including WAV, WMA, FLAC, and MP3.

## Prerequisites

Before running the script, ensure that you have Python installed on your system. If Python is not installed, you can download and install it from the official Python website: [https://www.python.org](https://www.python.org).

## Usage

To run the script, follow these steps:

1. Open Command Prompt as an administrator.
2. Navigate to your Desktop directory using the command:

<pre>cd %USERPROFILE%\Desktop</pre>

3. Execute the script using Python:

<pre>python "random.shuffle(V4).py"</pre>

The script requires two external modules: **pygame** and **mutagen**. If you haven't installed these modules, you can install them using the following commands in the Command Prompt:

<pre>pip install pygame</pre>
<pre>pip install mutagen</pre>


## Configuration

Once the script is executed, it will shuffle the music files present in the specified folder (`music_folder`). The script assumes that the music folder is located at 'E:\Music'. Modify the `music_folder` variable in the script if your music folder is located elsewhere.

## Features

The script keeps track of the following information during playback:

- **Song Count**: The number of songs played.
- **Current Time**: The current time when each song starts playing.
- **Date**: The date in the format "Day, MM/DD/YYYY".
- **Elapsed Time**: The time elapsed since the script started running.
- **Repeat Song Counter**: The number of times each song has been repeated.

The script uses the **pygame** module to play the music files. It initializes the mixer using `pygame.mixer.init()` and loads each music file using `pygame.mixer.music.load()`. It then plays the loaded music file using `pygame.mixer.music.play()`.

If a song exceeds 8 minutes (480 seconds), it is skipped, and the script moves on to the next song.

The script handles the interruption signal (Ctrl+C) using the **signal** module. When interrupted, it prints the copyright information.

## License

The script is provided for educational and informational purposes only. You may modify and distribute this script for personal use or within your organization. However, you may not use this script for any commercial purposes without explicit permission from the author and copyright holder. The author and copyright holder are not responsible for any damages or liabilities arising from the use of this script. The script is provided as-is, without any warranty or guarantee of any kind.

---

**Note:** This README provides a brief overview of the script. For more detailed explanations and instructions, please refer to the script itself.

