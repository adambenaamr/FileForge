# FileForge

**FileForge** is a lightweight Python CLI tool for batch renaming and organizing media files (images and videos) in a structured, predictable format.

It provides safe renaming with **dry-run support**, automatic conflict resolution, and clean terminal output using Rich.

## Features

* Batch rename images and videos in a directory
* Automatically moves files to a target directory
* Sequential naming with zero-padded counters (`IMG_0001`, `MOV_0002`, etc.)
* Dry-run mode to preview changes safely
* Handles naming conflicts automatically
* Clean CLI output using Rich panels
* Supports common image and video formats

## Supported Formats

### Images

`.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webp`

### Videos

`.mp4`, `.mov`, `.avi`, `.mkv`, `.wmv`, `.flv`, `.mpeg`

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/fileforge.git
cd fileforge
```

Install dependencies:

```bash
pip install rich click
```

## Usage

FileForge exposes a CLI command: `ff`

### Basic Syntax

```bash
ff <input_directory> <output_directory> --rename
```

### Dry Run

See what would happen without modifying files:

```bash
ff ./input ./output --rename --dry-run
```



### Start Indexing From a Custom Number

```bash
ff ./input ./output --rename --starting=100
```

This will begin naming from:

```
IMG_0100.png
IMG_0101.png
...
```

## Example Output

```
╭──────────────────── FileForge ────────────────────╮
│ [DRY RUN] IMG_1000.png -> IMG_0000.png            │
│ [DRY RUN] IMG_1001.png -> IMG_0001.png            │
│ [DRY RUN] IMG_1002.png -> IMG_0002.png            │
╰───────────────────────────────────────────────────╯
```

## How It Works

1. Scans input directory for media files
2. Sorts files alphabetically + numerically (when possible)
3. Filters supported image/video extensions
4. Generates sequential names (`IMG_XXXX` / `MOV_XXXX`)
5. Ensures filename uniqueness in output directory
6. Moves or simulates moves (`--dry-run`)
7. Displays results in a styled terminal panel

## Safety Features

* `--dry-run` prevents file modifications
* Automatic filename collision handling
* Output directory is created if it does not exist

## Project Structure

```
fileforge/
├── cli.py          # CLI entry point (ff command)
├── core.py         # Renaming + file logic
├── utils.py        # Rich output utilities
```

## Notes

* File ordering depends on OS listing + numeric sorting fallback
* Non-media files are ignored
* Existing files in output directory will not be overwritten

## Future Improvements

* Custom prefix support (`IMG`, `MOV`, etc.)
* Configurable digit padding
* Parallel processing for large datasets
* Interactive mode (confirm each rename)
* Progress bar support
* Recursive folder processing

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
