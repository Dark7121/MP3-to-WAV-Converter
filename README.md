# MP3-to-WAV-Converter
To run this script, you would need to have Python installed on your computer and the pydub library installed. 
If you don't have python installed in your computer go to this link:
https://phoenixnap.com/kb/how-to-install-python-3-windows
Also, if you don't have pip installed in your computer, please follow the solutio provided in the line(up).

After installing the python and pip, click windows button and search "Terminal". There you can type 'python' or 'pip' to check that it installed propely or not.

Now, you can install the pydub library using pip:
$pip install pydub

To use the script, save the Python file (e.g., MP3_to_WAV.py) and run it from the command line with the input and output folders as arguments:
$python convert_audio.py path/to/mp3/files path/to/output/folder

The script will convert all the MP3 files in the input folder to WAV files and save them in the output folder. If the output folder doesn't exist, it will be created automatically. Once the conversion is complete, the script will print a message to the console.
