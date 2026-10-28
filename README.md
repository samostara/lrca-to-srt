# lrca-to-srt

A simple program to make .srt caption files from Lyrica .lrca files.

Is currently a command-line exclusive tool. You can run it through the command `python lrca-to-srt -f <input_file>`. `<input_file>` is the directory and filename of the lrca file, which defaults to `file.lrca` if no file is specified.

This will output each individual text block in your project as its own line, and manual cleaning is required.