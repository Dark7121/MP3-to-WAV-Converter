import os
import sys
from pydub import AudioSegment

# Get the input and output folders from command line arguments
input_folder = #provide the MP3 file path
output_folder = #provide the WAV file path, where it the store the output file as WAV

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all the MP3 files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".mp3"):
        # Load the MP3 file
        mp3_path = os.path.join(input_folder, filename)
        audio = AudioSegment.from_file(mp3_path, format="mp3")

        # Create the output WAV file path
        wav_filename = os.path.splitext(filename)[0] + ".wav"
        wav_path = os.path.join(output_folder, wav_filename)

        # Export the WAV file
        audio.export(wav_path, format="wav")

# Print a message when the conversion is complete
print("Conversion complete.")
