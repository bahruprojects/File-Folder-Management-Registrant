import os
import csv
from pathlib import Path
from datetime import datetime

def get_file_category(file_path):
    """Menentukan kategori file berdasarkan ekstensinya"""
    
    # Jika folder
    if os.path.isdir(file_path):
        return "Folder", "Folder"
    
    # Mendapatkan ekstensi file
    extension = Path(file_path).suffix.lower()
    
    # Mapping kategori berdasarkan ekstensi
    categories = {
        # Gambar/Picture
        'picture': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico', '.tiff', '.psd', '.raw'],
        
        # Video
        'video': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.mpg', '.mpeg', '.3gp'],
        
        # Audio
        'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.opus'],
        
        # Dokumen
        'document': ['.doc', '.docx', '.pdf', '.txt', '.rtf', '.odt', '.pages'],
        
        # Spreadsheet
        'spreadsheet': ['.xls', '.xlsx', '.csv', '.ods', '.numbers'],
        
        # Presentasi
        'presentation': ['.ppt', '.pptx', '.odp', '.key'],
        
        # Archive/Compressed
        'archive': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.iso'],
        
        # Programming/Code
        'code': ['.py', '.java', '.cpp', '.c', '.js', '.html', '.css', '.php', '.rb', '.go', '.rs', '.swift', '.kt'],
        
        # Database
        'database': ['.sql', '.db', '.sqlite', '.mdb', '.accdb'],
        
        # Executable
        'executable': ['.exe', '.msi', '.apk', '.app', '.deb', '.rpm'],
        
        # Font
        'font': ['.ttf', '.otf', '.woff', '.woff2'],
        
        # 3D
        '3d': ['.obj', '.fbx', '.blend', '.stl', '.3ds', '.dae'],
    }
    
    # Mencari kategori file
    for category, extensions in categories.items():
        if extension in extensions:
            return f"File {category.title()}", extension if extension else "No Extension"
    
    # Jika tidak ditemukan kategori
    if extension:
        return "File Other", extension
    else:
        return "File No Extension", "No Extension"

def scan_directory_to_csv():
    """Scan direktori dan simpan hasilnya ke CSV"""
    
    # Mendapatkan direktori program saat ini
    current_dir = Path(__file__).parent.resolve()
    
    # Mendapatkan nama folder untuk nama CSV
    folder_name = current_dir.name
    csv_filename = f"{folder_name}.csv"
    csv_path = current_dir / csv_filename
    
    print(f"Memulai scanning direktori: {current_dir}")
    print(f"File CSV akan disimpan sebagai: {csv_filename}\n")
    
    # List untuk menyimpan data
    data_list = []
    
    # Scanning semua item di direktori
    try:
        for item in current_dir.iterdir():
            # Skip file CSV output agar tidak mencatat dirinya sendiri
            if item.name == csv_filename:
                continue
            
            # Skip file Python program ini sendiri (opsional)
            if item.name == Path(__file__).name:
                continue
            
            # Mendapatkan informasi file/folder
            item_name = item.name
            jenis_format, kategori = get_file_category(item)
            item_path = str(item.resolve())  # Path lengkap
            
            # Menambahkan ke list
            data_list.append({
                'Nama Objek': item_name,
                'Jenis Format': jenis_format,
                'Kategori': kategori,
                'Path': item_path
            })
            
            print(f"✓ Tercatat: {item_name} - {jenis_format} - {kategori}")
            print(f"  Path: {item_path}\n")
    
    except PermissionError as e:
        print(f"Error: Tidak memiliki izin untuk mengakses beberapa file/folder")
    
    # Menyimpan ke CSV
    if data_list:
        with open(csv_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
            fieldnames = ['Nama Objek', 'Jenis Format', 'Kategori', 'Path']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data_list)
        
        print(f"\n{'='*50}")
        print(f"✓ Scanning selesai!")
        print(f"✓ Total item tercatat: {len(data_list)}")
        print(f"✓ File CSV tersimpan di: {csv_path}")
        print(f"{'='*50}")
    else:
        print("\nTidak ada file atau folder yang ditemukan untuk dicatat.")

if __name__ == "__main__":
    print("="*50)
    print("PROGRAM PENCATATAN FILE DAN FOLDER")
    print("="*50)
    print()
    
    scan_directory_to_csv()
    
    print("\nProgram selesai dijalankan.")
    input("Tekan Enter untuk keluar...")
# ```

## Cara Menggunakan:

# 1. **Simpan file Python** ini di folder yang ingin Anda scan
# 2. **Jalankan program** dengan double-click atau melalui terminal:
# ```
#    python nama_file.py