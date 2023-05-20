This Python script allows you to play music files from a specified folder in a shuffled order. It utilizes the pydub library for audio playback and supports various audio formats such as WAV, WMA, FLAC, and MP3.

Usage
Make sure you have Python installed on your system (version 3.6 or higher).

Install the required dependencies by running the following command:

<pre>
pip install pydub
</pre>

Modify the script to specify the path to your music folder:

<pre>
music_folder = r"D:\Music"  # Replace with the path to your music folder
</pre>



To run the script, follow these steps:

Save the script as "random.shuffle(V2).py" on your desktop.

Open the Command Prompt as an administrator:
Press the Windows key on your keyboard.
Type "Command Prompt" in the search bar.
Right-click on "Command Prompt" and select "Run as administrator."

<pre>
Type the following command and press Enter: cd %USERPROFILE%\Desktop
</pre>

Execute the script using the Python interpreter:

<pre>
Type the following command and press Enter: python "random.shuffle(V2).py"
</pre>

The script will start running and display the output in the Command Prompt window.

Alternatively, you can simply double-click the "random.shuffle(V2).py" file on your desktop. 
This will automatically execute the script using the default Python interpreter on your system, and the output will be displayed in the Command Prompt window that opens.







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

