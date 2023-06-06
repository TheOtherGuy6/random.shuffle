The script is designed to shuffle and play music files from a specified folder. It supports various audio formats, including WAV, WMA, FLAC, and MP3.

Before running the script, ensure that you have Python installed on your system. If Python is not installed, you can download and install it from the official Python website (https://www.python.org).

To run the script, follow these steps:

Open Command Prompt as an administrator.
Navigate to your Desktop directory using the command: cd %USERPROFILE%\Desktop.
Execute the script using Python: python "random.shuffle(V4).py".
The script requires two external modules: pygame and mutagen. If you haven't installed these modules, you can install them using the following commands in the Command Prompt:

Copy code
pip install pygame
pip install mutagen
Once the script is executed, it will shuffle the music files present in the specified folder (music_folder). The script assumes that the music folder is located at 'E:\Music'. Modify the music_folder variable if your music folder is located elsewhere.

The script uses the random.shuffle() function to randomize the order of the music files.

The script keeps track of the following information during playback:

Song Count: The number of songs played.
Current Time: The current time when each song starts playing.
Date: The date in the format "Day, MM/DD/YYYY".
Elapsed Time: The time elapsed since the script started running.
Repeat Song Counter: The number of times each song has been repeated.
The script uses the pygame module to play the music files. It initializes the mixer using pygame.mixer.init() and loads each music file using pygame.mixer.music.load(). It then plays the loaded music file using pygame.mixer.music.play().

If a song exceeds 8 minutes (480 seconds), it is skipped, and the script moves on to the next song.

The script handles the interruption signal (Ctrl+C) using the signal module. When interrupted, it prints the copyright information.

The script also includes a license agreement at the beginning. By using this script, you agree to the terms and conditions mentioned in the license.
