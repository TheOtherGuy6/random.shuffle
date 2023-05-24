<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.5;
        }

        h1 {
            font-weight: bold;
            margin-bottom: 20px;
        }

        code {
            font-family: Consolas, monospace;
            background-color: #f2f2f2;
            padding: 2px 4px;
            border-radius: 4px;
        }

        .highlight {
            background-color: #ffffcc;
        }

        .bold {
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Random Shuffle Music Player</h1>

    <p>This script is a random shuffle music player that plays music files from a specified folder in a random order. It uses the Pygame library to play the music and provides some additional information while playing each song.</p>

    <h2>Installation</h2>

    <p>To use this script, you need to have Python installed on your system. You can download Python from the official website: <a href="https://www.python.org/downloads/" target="_blank">https://www.python.org/downloads/</a></p>

    <p>This script requires the Pygame library. You can install Pygame using pip, which is a package installer for Python. Open a command prompt or terminal and run the following command:</p>

    <pre><code>pip install pygame</code></pre>

    <h2>Usage</h2>

    <ol>
        <li>Clone or download the script from the GitHub repository.</li>
        <li>Move the script to your desktop.</li>
        <li>Open a command prompt or terminal.</li>
        <li>Change the current directory to your desktop by running the following command:</li>
    </ol>

    <pre><code>cd %USERPROFILE%\Desktop</code></pre>

    <ol start="5">
        <li>Run the script using the following command:</li>
    </ol>

    <pre><code>python "random.shuffle(V3).py"</code></pre>

    <p>The music player will start playing random songs from the specified music folder.</p>

    <h2>Functionality</h2>

    <ol>
        <li>It imports necessary libraries and modules including <code>os</code>, <code>random</code>, <code>datetime</code>, <code>pygame</code>, and <code>signal</code>.</li>
        <li>The script defines two ANSI escape codes, <code class="highlight">BOLD</code> and <code class="highlight">RESET</code>, for formatting text.</li>
        <li>It initializes the <code class="highlight">music_folder</code> variable to the path of the music folder. Modify this variable to point to your music folder.</li>
        <li>The script searches for music files (with extensions .wav, .wma, .flac, .mp3) in the specified <code class="highlight">music_folder</code> and stores them in a list called <code class="highlight">music_files</code>. It stores both the folder path and filename for each music file.</li>
        <li>The list of music files is shuffled randomly using the <code class="highlight">random.shuffle()</code> function.</li>
        <li>It initializes variables <code class="highlight">song_count</code> (to keep track of the number of songs played), <code class="highlight">repeat_song_counter</code> (to count the number of times each song is repeated), <code class="highlight">skip_counter</code> (to count the number of song skips), and <code class="highlight">start_time</code> (to record the start time of the program).</li>
        <li>The script defines a signal handler function <code class="highlight">skip_song()</code> to handle the interruption signal (Ctrl+C) and increment the <code class="highlight">skip_counter</code> variable.</li>
        <li>It registers the <code class="highlight">skip_song()</code> function as the signal handler for the interruption signal (Ctrl+C).</li>
        <li>Inside a try-except block, the script initializes the Pygame mixer.</li>
        <li>It iterates through each music file in the shuffled <code class="highlight">music_files</code> list.</li>
        <li>For each file, it loads the file into the Pygame mixer based on its extension.</li>
        <li>The script increments the <code class="highlight">song_count</code> variable and updates the <code class="highlight">repeat_song_counter</code> for the current song.</li>
        <li>It calculates the current time, elapsed time, and formatted date.</li>
        <li>The script prints the following information for the current song:</li>
    </ol>

    <pre><code>
Now playing: <span class="bold">parent_folder - folder_name - filename</span>
Song count: <span class="bold">song_count</span>
Current time: <span class="bold">formatted_current_time</span>
Date: <span class="bold">formatted_date</span>
Elapsed time: <span class="bold">formatted_elapsed_time</span>
Repeat song counter: <span class="bold">repeat_song_counter[filename]</span>
    </code></pre>

    <ol start="15">
        <li>Inside a nested try-except block, the script plays the loaded music using the Pygame mixer and waits until the song finishes playing.</li>
        <li>If an exception is raised (indicating a skip signal from the signal handler), the script prints a message indicating the song skip and the current <code class="highlight">skip_counter</code> value.</li>
        <li>After each song is played, the script prints the copyright information and a message indicating shuffling of music.</li>
        <li>If the program is interrupted by the user (Ctrl+C), the script handles the <code class="highlight">KeyboardInterrupt</code> exception and prints a message indicating the interruption.</li>
        <li>Finally, the script prints a closing message and the copyright information.</li>
    </ol>

    <h2>Keyboard Interrupt (Ctrl+C)</h2>

    <p>If you want to stop the music player before it finishes playing all the songs, you can press Ctrl+C in the command prompt or terminal where the script is running. The program will print a closing message and exit gracefully.</p>

    <h2>License</h2>

    <p>This script is created by Wayne Fry and all rights are reserved.</p>
</body>
</html>
