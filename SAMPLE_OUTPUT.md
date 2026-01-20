# Sample Output Documentation

## Test Setup

### Test Environment
- **OS**: Windows 10/11
- **Python Version**: 3.8+
- **Directory**: `test_files/`

### Files Created for Testing
```
test_files/
├── photo1.jpg
├── photo2.png
├── report.pdf
├── notes.txt
├── presentation.pptx
├── spreadsheet.xlsx
├── video.mp4
├── movie.mkv
├── song.mp3
├── podcast.wav
├── archive.zip
├── backup.rar
├── script.py
├── style.css
├── data.json
├── readme (no extension)
└── unknown.xyz
```

---

## Test Case 1: Initial Organization (Normal Run)

### Command
```bash
python file_organizer.py ./test_files
```

### Expected Output
```
📁 Starting file organization in: ./test_files

✓ Created folder: Images/
✓ Created folder: Documents/
✓ Created folder: Videos/
✓ Created folder: Audio/
✓ Created folder: Archives/
✓ Created folder: Code/

✓ Moved: photo1.jpg → Images/
✓ Moved: photo2.png → Images/
✓ Moved: report.pdf → Documents/
✓ Moved: notes.txt → Documents/
✓ Moved: presentation.pptx → Documents/
✓ Moved: spreadsheet.xlsx → Documents/
✓ Moved: video.mp4 → Videos/
✓ Moved: movie.mkv → Videos/
✓ Moved: song.mp3 → Audio/
✓ Moved: podcast.wav → Audio/
✓ Moved: archive.zip → Archives/
✓ Moved: backup.rar → Archives/
✓ Moved: script.py → Code/
✓ Moved: style.css → Code/
✓ Moved: data.json → Code/
✓ Moved: 'readme' (no extension) → Others/
✓ Moved: unknown.xyz → Others/

==================================================
📊 ORGANIZATION SUMMARY
==================================================
Files to move: 17
Files skipped: 0
Errors encountered: 0

📝 Files moved:
   • photo1.jpg → Images/
   • photo2.png → Images/
   • report.pdf → Documents/
   • notes.txt → Documents/
   • presentation.pptx → Documents/
   • spreadsheet.xlsx → Documents/
   • video.mp4 → Videos/
   • movie.mkv → Videos/
   • song.mp3 → Audio/
   • podcast.wav → Audio/
==================================================
```

### Directory Structure After
```
test_files/
├── Images/
│   ├── photo1.jpg
│   └── photo2.png
├── Documents/
│   ├── report.pdf
│   ├── notes.txt
│   ├── presentation.pptx
│   └── spreadsheet.xlsx
├── Videos/
│   ├── video.mp4
│   └── movie.mkv
├── Audio/
│   ├── song.mp3
│   └── podcast.wav
├── Archives/
│   ├── archive.zip
│   └── backup.rar
├── Code/
│   ├── script.py
│   ├── style.css
│   └── data.json
└── Others/
    ├── readme
    └── unknown.xyz
```

---

## Test Case 2: Preview Mode (Dry Run)

### Command
```bash
python file_organizer.py ./test_files --preview
```

### Expected Output
```
📁 Starting file organization in: ./test_files
🔍 PREVIEW MODE - No files will be moved

✓ Created folder: Images/
✓ Created folder: Documents/
✓ Created folder: Videos/
✓ Created folder: Audio/
✓ Created folder: Archives/
✓ Created folder: Code/

→ Would move: photo1.jpg → Images/
→ Would move: photo2.png → Images/
→ Would move: report.pdf → Documents/
→ Would move: notes.txt → Documents/
→ Would move: presentation.pptx → Documents/
→ Would move: spreadsheet.xlsx → Documents/
→ Would move: video.mp4 → Videos/
→ Would move: movie.mkv → Videos/
→ Would move: song.mp3 → Audio/
→ Would move: podcast.wav → Audio/
→ Would move: archive.zip → Archives/
→ Would move: backup.rar → Archives/
→ Would move: script.py → Code/
→ Would move: style.css → Code/
→ Would move: data.json → Code/
→ Would move: 'readme' (no extension) → Others/
→ Would move: unknown.xyz → Others/

==================================================
📊 PREVIEW SUMMARY
==================================================
Files to move: 17
Files skipped: 0
Errors encountered: 0

📝 Files moved:
   • photo1.jpg → Images/
   • photo2.png → Images/
   • report.pdf → Documents/
   • notes.txt → Documents/
   • presentation.pptx → Documents/
   • spreadsheet.xlsx → Documents/
   • video.mp4 → Videos/
   • movie.mkv → Videos/
   • song.mp3 → Audio/
   • podcast.wav → Audio/
==================================================
```

**Note**: No files are actually moved with `--preview` flag.

---

## Test Case 3: Error Handling - Invalid Path

### Command
```bash
python file_organizer.py ./nonexistent_folder
```

### Expected Output
```
❌ Error: Path './nonexistent_folder' does not exist.

==================================================
📊 ORGANIZATION SUMMARY
==================================================
Files to move: 0
Files skipped: 0
Errors encountered: 0

==================================================
```

---

## Test Case 4: Running Without Arguments

### Command
```bash
python file_organizer.py
```

### Expected Output
```
File Type Organizer - Organize files by their type

Usage:
  python file_organizer.py <folder_path>        Organize files
  python file_organizer.py <folder_path> --preview  Preview changes

Example:
  python file_organizer.py C:\Downloads
  python file_organizer.py ./my_folder --preview
```

---

## Test Case 5: Second Run (Idempotent)

### Command
```bash
python file_organizer.py ./test_files
```

### Expected Output
```
📁 Starting file organization in: ./test_files

✓ Created folder: Images/
✓ Created folder: Documents/
✓ Created folder: Videos/
✓ Created folder: Audio/
✓ Created folder: Archives/
✓ Created folder: Code/

⊝ Skipped: photo1.jpg (already in Images/)
⊝ Skipped: photo2.png (already in Images/)
⊝ Skipped: report.pdf (already in Documents/)
⊝ Skipped: notes.txt (already in Documents/)
⊝ Skipped: presentation.pptx (already in Documents/)
⊝ Skipped: spreadsheet.xlsx (already in Documents/)
⊝ Skipped: video.mp4 (already in Videos/)
⊝ Skipped: movie.mkv (already in Videos/)
⊝ Skipped: song.mp3 (already in Audio/)
⊝ Skipped: podcast.wav (already in Audio/)
⊝ Skipped: archive.zip (already in Archives/)
⊝ Skipped: backup.rar (already in Archives/)
⊝ Skipped: script.py (already in Code/)
⊝ Skipped: style.css (already in Code/)
⊝ Skipped: data.json (already in Code/)
⊝ Skipped: 'readme' (no extension) (already in Others/)
⊝ Skipped: unknown.xyz (already in Others/)

==================================================
📊 ORGANIZATION SUMMARY
==================================================
Files to move: 0
Files skipped: 17
Errors encountered: 0

==================================================
```

**Note**: On second run, all files are skipped since they're already organized.

---
