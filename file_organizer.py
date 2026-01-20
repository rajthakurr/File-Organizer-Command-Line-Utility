"""
File Type Organizer - A command-line utility to organize files by their type
"""

import os
import shutil
import sys
import io

# Enable UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# File type mapping
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.webp'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.ppt', '.csv'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.webm'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.wma', '.m4a', '.ogg'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.iso'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.json', '.xml', '.yaml'],
}


def get_category_for_extension(extension):
    """
    Get the category folder name for a given file extension.
    
    Args:
        extension (str): File extension (e.g., '.pdf')
    
    Returns:
        str: Category name or 'Others' if not found
    """
    extension = extension.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return 'Others'


def create_category_folders(target_path, preview_mode=False):
    """
    Create category folders if they don't already exist.
    
    Args:
        target_path (str): Path to the target directory
        preview_mode (bool): If True, don't actually create folders
    
    Returns:
        list: List of created or existing categories
    """
    categories = list(FILE_CATEGORIES.keys()) + ['Others']
    created_folders = []
    
    for category in categories:
        folder_path = os.path.join(target_path, category)
        
        if not os.path.exists(folder_path):
            if not preview_mode:
                os.makedirs(folder_path)
                print(f"[+] Created folder: {category}/")
            created_folders.append(category)
        else:
            created_folders.append(category)
    
    return created_folders


def organize_files(target_path, preview_mode=False):
    """
    Scan the target directory and organize files by type.
    
    Args:
        target_path (str): Path to the directory to organize
        preview_mode (bool): If True, preview changes without actually moving files
    
    Returns:
        dict: Statistics about the organization
    """
    stats = {
        'moved': 0,
        'skipped': 0,
        'errors': 0,
        'files_moved': []
    }
    
    # Validate path
    if not os.path.exists(target_path):
        print(f"[ERROR] Path '{target_path}' does not exist.")
        return stats
    
    if not os.path.isdir(target_path):
        print(f"[ERROR] '{target_path}' is not a directory.")
        return stats
    
    print(f"\n[*] Starting file organization in: {target_path}")
    if preview_mode:
        print("[INFO] PREVIEW MODE - No files will be moved\n")
    else:
        print()
    
    # Create category folders
    create_category_folders(target_path, preview_mode)
    
    # Get all files in the directory (not subdirectories)
    try:
        items = os.listdir(target_path)
    except PermissionError:
        print(f"[ERROR] Permission denied when accessing '{target_path}'.")
        return stats
    
    # Organize files
    for item in items:
        item_path = os.path.join(target_path, item)
        
        # Skip if it's a directory
        if os.path.isdir(item_path):
            continue
        
        # Get file extension
        _, extension = os.path.splitext(item)
        
        # Handle files without extension
        if not extension:
            category = 'Others'
            display_name = f"'{item}' (no extension)"
        else:
            category = get_category_for_extension(extension)
            display_name = item
        
        destination_folder = os.path.join(target_path, category)
        destination_path = os.path.join(destination_folder, item)
        
        # Skip if file is already in the right place
        if os.path.dirname(item_path) == destination_folder:
            print(f"[SKIP] {display_name} (already in {category}/)")
            stats['skipped'] += 1
            continue
        
        try:
            if preview_mode:
                print(f"[-->] Would move: {display_name} -> {category}/")
            else:
                # Handle file name conflicts
                if os.path.exists(destination_path):
                    base, ext = os.path.splitext(item)
                    counter = 1
                    while os.path.exists(os.path.join(destination_folder, f"{base}_{counter}{ext}")):
                        counter += 1
                    destination_path = os.path.join(destination_folder, f"{base}_{counter}{ext}")
                    print(f"[WARN] Renamed and moved: {display_name} -> {category}/{os.path.basename(destination_path)}")
                else:
                    print(f"[OK] Moved: {display_name} -> {category}/")
                
                shutil.move(item_path, destination_path)
            
            stats['moved'] += 1
            stats['files_moved'].append(f"{display_name} -> {category}/")
        
        except Exception as e:
            print(f"[ERROR] Error moving {display_name}: {str(e)}")
            stats['errors'] += 1
    
    return stats


def print_summary(stats, preview_mode=False):
    """
    Print a summary of the organization operation.
    
    Args:
        stats (dict): Statistics from the organization
        preview_mode (bool): If True, indicate this was a preview
    """
    print("\n" + "="*50)
    if preview_mode:
        print("SUMMARY - PREVIEW MODE")
    else:
        print("SUMMARY - ORGANIZATION COMPLETE")
    print("="*50)
    print(f"Files moved: {stats['moved']}")
    print(f"Files skipped: {stats['skipped']}")
    print(f"Errors: {stats['errors']}")
    
    if stats['files_moved']:
        print("\nFiles affected:")
        for file_info in stats['files_moved'][:10]:  # Show first 10
            print(f"  {file_info}")
        if len(stats['files_moved']) > 10:
            print(f"  ... and {len(stats['files_moved']) - 10} more")
    
    print("="*50 + "\n")


def main():
    """Main entry point for the application"""
    
    # Parse command-line arguments
    if len(sys.argv) < 2:
        print("File Type Organizer - Organize files by their type")
        print("\nUsage:")
        print("  python file_organizer.py <folder_path>        Organize files")
        print("  python file_organizer.py <folder_path> --preview  Preview changes\n")
        print("Example:")
        print("  python file_organizer.py C:\\Downloads")
        print("  python file_organizer.py ./my_folder --preview\n")
        sys.exit(1)
    
    target_path = sys.argv[1]
    preview_mode = '--preview' in sys.argv
    
    # Run organization
    stats = organize_files(target_path, preview_mode)
    
    # Print summary
    if stats['moved'] > 0 or stats['errors'] > 0:
        print_summary(stats, preview_mode)
    
    # Exit with appropriate code
    if stats['errors'] > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
