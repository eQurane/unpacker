File Organizer
A simple utility for reviewing files in a root folder (including nested subfolders), logging their information, and moving files by extension to a .moved folder in the root. It also allows restoring ("demoving") files using the log information.

Features
Recursively scans the specified root folder

Logs all file paths and their original locations

Moves files to .moved folder, grouped by extension

Can restore files to their original location using the generated log

Optional read-only mode (for safe testing)

Usage
Set folder permissions:
Make sure the target folder is not set to read-only in Windows folder properties.

Run the script:
You can configure the script to either just log or also move files.

Notes
The .moved folder is automatically created in the root directory if it doesn’t exist.

Moving and restoring actions are based entirely on the log file.
