"""
Script for shuffling and playing music files.

License: [By using this script, you agree to the following terms and conditions:

This script is provided for educational and informational purposes only.
You may modify and distribute this script for personal use or within your organization.
You may not use this script for any commercial purposes without explicit permission from the author and copyright holder.
The author and copyright holder are not responsible for any damages or liabilities arising from the use of this script.
This script is provided as-is, without any warranty or guarantee of any kind.]

To run the script:
1. Open Command Prompt as administrator.
2. Navigate to your Desktop directory:
   cd %USERPROFILE%\Desktop
3. Execute the script using Python:
   python "random.shuffle(V4).py"

Make sure you have the following modules installed (use 'pip install [module_name]'):
- pygame
- mutagen

Note: This script assumes that you have a music folder located at 'E:\Music'.
      Modify the 'music_folder' variable accordingly if your music folder is in a different location.
"""

import os
import random
import datetime
import pygame
import signal
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen import File as MutagenFile

# ANSI escape code for bold text
BOLD = "\033[1m"
# ANSI escape code to reset text formatting
RESET = "\033[0m"

music_folder = r"E:\Music"  # Replace with the path to your music folder
music_files = []
for dirpath, dirnames, filenames in os.walk(music_folder):
    for filename in filenames:
        if filename.lower().endswith((".wav", ".wma", ".flac", ".mp3")):
            music_files.append((dirpath, filename))  # Store both the folder path and filename

random.shuffle(music_files)

song_count = 0  # Initialize the song count
repeat_song_counter = {}  # Initialize the repeat song counter dictionary
skip_counter = 0  # Initialize the song skip counter

start_time = datetime.datetime.now()  # Record the start time

def skip_song(signal, frame):
    global skip_counter
    skip_counter += 1
    raise Exception("Skip")

signal.signal(signal.SIGINT, skip_song)

try:
    pygame.mixer.init()

    for folder, filename in music_files:
        file_path = os.path.join(folder, filename)

        if filename.endswith(".mp3"):
            audio = MP3(file_path)
        elif filename.endswith(".flac"):
            audio = FLAC(file_path)
        elif filename.endswith(".wav"):
            audio = MutagenFile(file_path)
        elif filename.endswith(".wma"):
            audio = MutagenFile(file_path)

        duration = audio.info.length  # Get the duration of the audio file in seconds

        if duration > 480:  # Skip songs longer than 8 minutes (480 seconds)
            print(f"Skipping long track: {filename}")
            continue

        if filename not in repeat_song_counter:
            repeat_song_counter[filename] = 1
        else:
            repeat_song_counter[filename] += 1

        song_count += 1  # Increment the song count

        current_time = datetime.datetime.now()
        elapsed_time = current_time - start_time

        # Format current time as hh:mm AM/PM and include date as "Day, MM/DD/YYYY"
        formatted_current_time = current_time.strftime("%I:%M %p")
        formatted_elapsed_time = str(elapsed_time).split(".")[0]
        formatted_date = current_time.strftime("%A, %m/%d/%Y")

        parent_folder = os.path.basename(os.path.dirname(folder))
        folder_name = os.path.basename(folder)
        print("Now playing:", parent_folder, "-", folder_name, "-", filename)
        print("Song count:", song_count)
        print("Current time:", formatted_current_time)
        print("Date:", formatted_date)
        print("Elapsed time:", formatted_elapsed_time)
        print("Repeat song counter:", repeat_song_counter[filename])  # Print the repeat song counter for the current song

        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()

            # Wait until the song finishes playing
            while pygame.mixer.music.get_busy():
                pass

        except Exception as e:
            if str(e) == "Skip":
                print("\nSkipped the current song.")
                print("Song skip counter:", skip_counter)

        # Print copyright information after each song is played
        print(BOLD + "[Copyright: Wayne Fry. All rights reserved.]" + RESET)
        print(BOLD + "[Shuffling Music]" + RESET)

except KeyboardInterrupt:
    # Handle the KeyboardInterrupt exception (Ctrl+C) and print the copyright information
    print("\nProgram interrupted by user.")

# Print copyright information before exiting the script
print("Shell closed or program exited.")
print(BOLD + "Copyright Wayne Fry. All rights reserved." + RESET)
