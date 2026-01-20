# Quick Start Guide

## Installation & Setup

### Prerequisites
- Python 3.6 or higher
- No additional packages needed

### Step 1: Verify Python
```bash
python --version
```

Expected output: `Python 3.6.0` or higher

### Step 2: Navigate to Project
```bash
cd d:\Internship\Project
```

### Step 3: Run the Program

#### Option A: Organize a folder
```bash
python file_organizer.py C:\Users\YourName\Downloads
```

#### Option B: Preview before organizing
```bash
python file_organizer.py C:\Users\YourName\Downloads --preview
```

---

## Common Commands

### Organize Downloads (Windows)
```bash
python file_organizer.py C:\Users\YourName\Downloads
```

### Organize Downloads (Linux/Mac)
```bash
python file_organizer.py ~/Downloads
```

### Preview changes in current directory
```bash
python file_organizer.py . --preview
```

### Organize Desktop
```bash
python file_organizer.py C:\Users\YourName\Desktop
```

---

## Output Meanings

| Symbol | Meaning |
|--------|---------|
| `[+]` | Folder created |
| `[OK]` | File successfully moved |
| `[SKIP]` | File already in correct location |
| `[WARN]` | File renamed due to conflict |
| `[-->]` | Preview: would move this file |
| `[ERROR]` | Error encountered |
| `[INFO]` | Information message |

---

## File Categories

**Images**: .jpg, .jpeg, .png, .gif, .bmp, .svg, .ico, .webp

**Documents**: .pdf, .docx, .doc, .txt, .xlsx, .xls, .pptx, .ppt, .csv

**Videos**: .mp4, .mkv, .avi, .mov, .flv, .wmv, .webm

**Audio**: .mp3, .wav, .flac, .aac, .wma, .m4a, .ogg

**Archives**: .zip, .rar, .7z, .tar, .gz, .iso

**Code**: .py, .js, .html, .css, .java, .cpp, .c, .json, .xml, .yaml

**Others**: Everything else (including files with no extension)

---

## Tips

💡 **Always preview first**: Use `--preview` before actual organization

💡 **Works on messy folders**: Great for Downloads, Desktop, or project folders

💡 **Safe to run multiple times**: Already organized files are skipped

💡 **Handles edge cases**: Files without extensions, unknown types, duplicates

💡 **Cross-platform**: Works on Windows, Linux, and Mac

---

## Troubleshooting

### Issue: "Python not found"
**Solution**: Make sure Python is installed and in your PATH
```bash
python --version
```

### Issue: Permission denied error
**Solution**: Ensure you have write access to the target folder
- Close any files open from that directory
- Run as administrator if needed

### Issue: Files not moving
**Solution**: Check if files are already organized
- Run with `--preview` to see status
- Check subdirectories if files are nested

### Issue: Wrong categorization
**Solution**: Edit FILE_CATEGORIES dictionary in file_organizer.py
- Add or remove file extensions
- Modify category names as needed

---

## Example Workflows

### Workflow 1: Clean Downloads Folder
```bash
# Step 1: Preview
python file_organizer.py C:\Users\YourName\Downloads --preview

# Step 2: Review output and verify categorization

# Step 3: Organize
python file_organizer.py C:\Users\YourName\Downloads

# Step 4: Check results
explorer C:\Users\YourName\Downloads
```

### Workflow 2: Organize Project Files
```bash
# From project directory
cd D:\MyProject\files

# Preview organization
python file_organizer.py . --preview

# Organize
python file_organizer.py .

# Verify
dir
```

---

## File Structure

```
File Type Organizer/
├── file_organizer.py          # Main program
├── README.md                  # Full documentation
├── SAMPLE_OUTPUT.md           # Expected outputs
├── TESTING_RESULTS.md         # Test results
└── QUICK_START.md             # This file
```

---

## Advanced Usage

### Customize Categories
Edit `file_organizer.py` and modify the `FILE_CATEGORIES` dictionary:

```python
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    # Add more categories as needed
}
```

### Organize Specific File Types
Manually run Python to move specific types:
```python
python -c "from file_organizer import *; organize_files('.')"
```

---

## Support

For issues or questions:
1. Check SAMPLE_OUTPUT.md for example usage
2. Check TESTING_RESULTS.md for test cases
3. Review code comments in file_organizer.py
4. Check error messages (they describe the issue)

---

## Assignment Submission Checklist

✅ Source code (`file_organizer.py`)
✅ README.md (problem description, how to run, design decisions)
✅ SAMPLE_OUTPUT.md (example outputs)
✅ TESTING_RESULTS.md (actual test execution)
✅ Clean code with proper functions
✅ Error handling implemented
✅ Standard libraries only
✅ No external dependencies

All requirements met! Ready for submission.
