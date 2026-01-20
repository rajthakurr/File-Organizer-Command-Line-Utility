# File Type Organizer

A command-line utility that automatically organizes files in a directory by their type.

## Problem Statement

Managing files on a computer can become overwhelming, especially in folders like Downloads, Desktop, or project directories. Files with different extensions get mixed together, making it difficult to find what you need. This utility solves this problem by automatically:

- Scanning a directory
- Identifying file types by their extension
- Creating categorized subfolders (Images, Documents, Videos, etc.)
- Moving files into their appropriate categories
- Preventing duplicates and handling edge cases

**Real-world use case**: Clean up your Downloads folder in seconds by running a single command.

## How to Run

### Prerequisites
- Python 3.6 or higher
- No external libraries required (uses only standard library)

### Basic Usage

```bash
# Organize files in a specific directory
python file_organizer.py C:\Users\YourName\Downloads

# Or on Linux/Mac
python file_organizer.py ~/Downloads
```

### Preview Mode (Dry Run)

Before actually moving files, you can preview what will happen:

```bash
python file_organizer.py C:\Users\YourName\Downloads --preview
```

This shows what files would be moved without actually moving them.

### Full Examples

**Windows:**
```bash
python file_organizer.py D:\Documents
python file_organizer.py C:\Users\YourName\Downloads --preview
```

**Linux/Mac:**
```bash
python file_organizer.py ~/Downloads
python file_organizer.py ./my_messy_folder --preview
```

## File Category Mapping

The utility organizes files into the following categories:

| Category | File Types |
|----------|-----------|
| **Images** | .jpg, .jpeg, .png, .gif, .bmp, .svg, .ico, .webp |
| **Documents** | .pdf, .docx, .doc, .txt, .xlsx, .xls, .pptx, .ppt, .csv |
| **Videos** | .mp4, .mkv, .avi, .mov, .flv, .wmv, .webm |
| **Audio** | .mp3, .wav, .flac, .aac, .wma, .m4a, .ogg |
| **Archives** | .zip, .rar, .7z, .tar, .gz, .iso |
| **Code** | .py, .js, .html, .css, .java, .cpp, .c, .json, .xml, .yaml |
| **Others** | Any file type not listed above |

## Design Decisions

### 1. **Clean Architecture with Functions**
The code is organized into modular functions, each with a single responsibility:
- `get_category_for_extension()` - Maps file extensions to categories
- `create_category_folders()` - Creates necessary folders
- `organize_files()` - Main logic for scanning and moving files
- `print_summary()` - Displays operation results

### 2. **Error Handling**
- Validates that the target path exists and is a directory
- Handles permission errors gracefully
- Manages file name conflicts by appending a counter
- Tracks errors and reports them to the user

### 3. **Preview Mode**
Implemented the `--preview` flag to let users see what will happen before actual file movement. This is crucial for safety and confidence.

### 4. **User-Friendly Output**
Uses clear symbols and messages:
- ✓ Success operations
- ❌ Errors
- ⊝ Skipped files
- ⚠ Warnings (like renamed files)
- 📊 Summary statistics

### 5. **No External Dependencies**
Uses only Python standard library:
- `os` - Directory and file operations
- `shutil` - File movement
- `sys` - Command-line argument parsing

### 6. **Smart File Handling**
- Skips directories (only processes files)
- Handles files without extensions
- Prevents duplicate file names
- Skips files already in the correct category
- Provides clear feedback on what changed

### 7. **Extensible Category System**
File categories are stored in a dictionary (`FILE_CATEGORIES`), making it easy to add new file types without modifying the core logic.

## Output Example

```
📁 Starting file organization in: C:\Users\YourName\Downloads
✓ Created folder: Images/
✓ Created folder: Documents/
✓ Created folder: Videos/
✓ Created folder: Audio/
✓ Created folder: Archives/
✓ Created folder: Code/

✓ Moved: photo.jpg → Images/
✓ Moved: report.pdf → Documents/
✓ Moved: presentation.pptx → Documents/
✓ Moved: video.mp4 → Videos/
⊝ Skipped: readme.txt (already in Documents/)
✓ Moved: song.mp3 → Audio/
✓ Moved: backup.zip → Archives/
⚠ Renamed and moved: photo.jpg → Images/photo_1.jpg

==================================================
📊 ORGANIZATION SUMMARY
==================================================
Files to move: 7
Files skipped: 1
Errors encountered: 0

📝 Files moved:
   • photo.jpg → Images/
   • report.pdf → Documents/
   • presentation.pptx → Documents/
   • video.mp4 → Videos/
   • song.mp3 → Audio/
   • backup.zip → Archives/
   • photo.jpg → Images/photo_1.jpg
==================================================
```

## Features

✅ **Automatic categorization** - Files are organized by type  
✅ **Preview mode** - See what will change before it happens  
✅ **Error handling** - Graceful handling of edge cases  
✅ **Duplicate prevention** - Renames files if names conflict  
✅ **Clear feedback** - User-friendly output with symbols  
✅ **Summary statistics** - Shows what was done  
✅ **No external libraries** - Pure Python standard library  

## Limitations

- Only processes files in the root of the specified directory (doesn't recursively organize subdirectories)
- Requires read/write permissions to the target directory
- Works best with files that have proper extensions

## Future Enhancements (Optional)

- Recursive organization of subdirectories with `--recursive` flag
- Undo functionality to move files back
- Custom configuration file for user-defined categories
- GUI interface for easier operation
- Scheduling/automation capabilities






