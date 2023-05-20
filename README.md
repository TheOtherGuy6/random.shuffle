This Python script allows you to play music files from a specified folder in a shuffled order. It utilizes the pydub library for audio playback and supports various audio formats such as WAV, WMA, FLAC, and MP3.

Usage

Make sure you have Python installed on your system (version 3.6 or higher).

Install the required dependencies by running the following command:

Copy code
pip install pydub
Modify the script to specify the path to your music folder:

python
Copy code
music_folder = r"D:\Music"  # Replace with the path to your music folder
Run the script using the following command:

python
Copy code
python music_player.py
Controls

To play the next song, simply wait for the current song to finish playing. The script will automatically proceed to the next song in the shuffled order.
To skip the current song, press Ctrl+C (SIGINT) in the terminal. The script will skip the current song and move to the next one.
To stop the script, press Ctrl+C twice in quick succession. The script will exit gracefully, and the shell will be closed.
Supported Audio Formats

The script supports the following audio formats:

WAV (.wav)
Windows Media Audio (.wma)
Free Lossless Audio Codec (.flac)
MP3 (.mp3)
Note

Make sure your music files are stored in the specified music folder or its subfolders.
The script shuffles the order in which the songs are played to provide variety.
The script keeps track of the number of times each song is played and the total song count.
Copyright information is displayed after each song is played.
The script records the start time and displays the elapsed time for each song.
This script assumes that the necessary dependencies (pydub) are installed and available in the Python environment.
License

This script is provided under the MIT License. Feel free to modify and use it according to your needs.

Author

This script was created by Wayne TheOtherGuy.
