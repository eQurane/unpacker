# File Organizer

A simple utility for reviewing files in a root folder (including nested subfolders), logging their information, and moving files by extension to a `.moved` folder near the root. It also allows restoring ("demoving") files using the log information.

## Features

- Recursively scans the specified root folder  
- Logs all file paths and their original locations  
- Moves files to `.moved` folder, grouped by extension  
- Can restore files to their original location using the generated log  
- Optional read-only mode (for safe testing)

## Usage

1. **Set folder permissions**  
   Make sure the target folder is **not** set to *read-only* in Windows folder properties.

2. **Run the script**  
   - Configure whether to just log or also move files
   - Run the script and monitor output/logs


## Notes

- A `.moved` folder will be created near the root directory.
- Moving and restoring files relies on accurate logging — do not edit the log manually.

## License

MIT License (or specify yours here)
