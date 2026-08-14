# Changelog

All notable changes to this project will be documented in this file.

## [Version 1.1.5] - 2026-08-13
### Added
- **Dry-Run Preview:** Added a dry-run feature allowing users to preview changes before applying them (`dry_run` boolean parameter added to `rename_media_files()`).
- **HEIC Support:** Added support for `.HEIC` image files.
- **Natural Sorting:** Integrated the `natsort` library to handle alphanumeric sorting properly (e.g., "File 2" now correctly appears before "File 10").
- **Enhanced UI:** Utilized the `rich` package to format and display terminal outputs inside nested boxes for improved readability.

### Changed
- **File Prefixes:** Standardized all media files to be prefixed with `IMG_` regardless of their original file type.
- **File Retrieval Logic:** Reworked how files are appended to the file list. The program now fetches files according to OS-level ordering before applying natural sorting.
- **Code Refactoring:** 
  - Updated `get_unique_filename()` to ensure all variables have explicit declarations where possible.
  - Updated docstrings in `rename_media_files()` to document the new `dry_run` parameter.
