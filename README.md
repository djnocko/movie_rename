This script is tailored to refine the naming convention of movies within a specified folder while ensuring it excludes format of the file.
By renaming the downloaded movies, it enhances their overall format, promoting better organization and readability for Plex and Jellyfin for example.

For instance:

Original:
Jackie.Brown.1997.1080p.BluRay.x265-X.mp4
The.Breakfast.Club.1985.REMASTERED.1080p.BluRay.H264.AAC5.1.mp4
Speed.2.Cruise.Control.1997.1080p.STZ.WEB-DL.AAC.2.0.H.264.mkv

After Renaming:
Jackie Brown (1997).mp4
The Breakfast Club (1985).mp4
Speed 2 Cruise Control (1997).mkv


In Windows, if you wish to create a shortcut on your desktop, for example, to automate the execution of this script, follow these steps:

Create a local file named renameFiles.bat
Add the following content to the file:

@echo off
setlocal

python "D:\YourScript\Folder\renameFiles2.py"

pause

This batch file executes the Python script renameFiles2.py located at D:\YourScript\Folder\, ensuring seamless execution. The pause command keeps the command prompt window open after execution, allowing you to view any messages or errors."