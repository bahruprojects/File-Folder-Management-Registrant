# 📁 File & Folder Management Registrant

Program Python sederhana untuk **scanning dan mencatat** semua file dan folder dalam suatu direktori ke dalam format CSV.

## 🌟 Fitur

- ✅ **Auto-Scan Direktori** - Otomatis scan folder tempat program berada
- ✅ **Kategorisasi Lengkap** - Mengenali 100+ jenis file (gambar, video, audio, dokumen, dll)
- ✅ **Output CSV Otomatis** - Nama file CSV mengikuti nama folder
- ✅ **Path Tracking** - Mencatat alamat lengkap setiap file/folder
- ✅ **Skip File Program** - Tidak mencatat file program Python itu sendiri
- ✅ **UTF-8 Encoding** - Mendukung karakter Indonesia dan internasional
- ✅ **Progress Indicator** - Menampilkan progress scanning di console

## 📋 Kategori File yang Didukung

| Kategori | Format File |
|----------|-------------|
| **Picture** | .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp, .ico, .tiff, .psd, .raw |
| **Video** | .mp4, .avi, .mkv, .mov, .wmv, .flv, .webm, .m4v, .mpg, .mpeg, .3gp |
| **Audio** | .mp3, .wav, .flac, .aac, .ogg, .wma, .m4a, .opus |
| **Document** | .doc, .docx, .pdf, .txt, .rtf, .odt, .pages |
| **Spreadsheet** | .xls, .xlsx, .csv, .ods, .numbers |
| **Presentation** | .ppt, .pptx, .odp, .key |
| **Archive** | .zip, .rar, .7z, .tar, .gz, .bz2, .xz, .iso |
| **Code** | .py, .java, .cpp, .c, .js, .html, .css, .php, .rb, .go, .rs, .swift, .kt |
| **Database** | .sql, .db, .sqlite, .mdb, .accdb |
| **Executable** | .exe, .msi, .apk, .app, .deb, .rpm |
| **Font** | .ttf, .otf, .woff, .woff2 |
| **3D** | .obj, .fbx, .blend, .stl, .3ds, .dae |

## 🚀 Cara Menggunakan

### 1. Persiapan

Pastikan Python sudah terinstall di komputer Anda (Python 3.6+)
```bash
python --version
```

### 2. Download Program

Clone repository ini atau download file `file_scanner.py`:
```bash
git clone https://github.com/username/file-folder-scanner.git
cd file-folder-scanner
```

### 3. Jalankan Program

**Metode 1: Double-click** (Windows)
- Double-click file `file_scanner.py`

**Metode 2: Command Line**
```bash
python file_scanner.py
```

**Metode 3: Terminal (Linux/Mac)**
```bash
python3 file_scanner.py
```

### 4. Hasil Output

Program akan menghasilkan file CSV dengan nama sesuai folder tempat program berada.

**Contoh:** Jika program ada di folder `MyDocuments`, maka akan menghasilkan `MyDocuments.csv`

## 📊 Contoh Output CSV

| Nama Objek | Jenis Format | Kategori | Path |
|------------|--------------|----------|------|
| Foto Liburan | Folder | Folder | C:\Users\User\Documents\Foto Liburan |
| laporan.docx | File Document | .docx | C:\Users\User\Documents\laporan.docx |
| video_tutorial.mp4 | File Video | .mp4 | C:\Users\User\Documents\video_tutorial.mp4 |
| backup.zip | File Archive | .zip | C:\Users\User\Documents\backup.zip |
| musik.mp3 | File Audio | .mp3 | C:\Users\User\Documents\musik.mp3 |

## 💻 Contoh Penggunaan

### Screenshot Console
```
==================================================
PROGRAM PENCATATAN FILE DAN FOLDER
==================================================

Memulai scanning direktori: C:\Users\User\Documents\MyFolder
File CSV akan disimpan sebagai: MyFolder.csv

✓ Tercatat: Foto Liburan - Folder - Folder
  Path: C:\Users\User\Documents\MyFolder\Foto Liburan

✓ Tercatat: laporan.docx - File Document - .docx
  Path: C:\Users\User\Documents\MyFolder\laporan.docx

✓ Tercatat: video_tutorial.mp4 - File Video - .mp4
  Path: C:\Users\User\Documents\MyFolder\video_tutorial.mp4

==================================================
✓ Scanning selesai!
✓ Total item tercatat: 3
✓ File CSV tersimpan di: C:\Users\User\Documents\MyFolder\MyFolder.csv
==================================================

Program selesai dijalankan.
Tekan Enter untuk keluar...
```

## 🛠️ Kustomisasi

### Menambah Kategori File Baru

Edit bagian `categories` dalam fungsi `get_file_category()`:
```python
categories = {
    'picture': ['.jpg', '.jpeg', '.png', ...],
    'video': ['.mp4', '.avi', '.mkv', ...],
    # Tambahkan kategori baru di sini
    'your_category': ['.ext1', '.ext2', '.ext3'],
}
```

### Mengubah Nama Output CSV

Edit baris ini dalam fungsi `scan_directory_to_csv()`:
```python
# Dari:
csv_filename = f"{folder_name}.csv"

# Menjadi (contoh):
csv_filename = "hasil_scan.csv"
# atau
csv_filename = f"scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
```

## 📦 Dependencies

Program ini hanya menggunakan **library standard Python**, tidak perlu instalasi tambahan:

- `os` - Operasi sistem file
- `csv` - Membaca/menulis file CSV
- `pathlib` - Manipulasi path modern
- `datetime` - Timestamp (opsional)

## ⚠️ Catatan Penting

- Program hanya scan **satu level** (tidak recursive ke subfolder)
- File CSV dan program Python itu sendiri **tidak akan dicatat**
- Pastikan Anda memiliki **izin akses** ke folder yang akan di-scan
- Mendukung sistem operasi: **Windows, Linux, macOS**

## 🐛 Troubleshooting

### Program tidak jalan?
- Pastikan Python terinstall dengan benar
- Cek versi Python minimal 3.6+

### File CSV tidak muncul?
- Cek apakah ada pesan error di console
- Pastikan folder tidak read-only
- Cek permission folder

### Karakter aneh di CSV?
- Buka CSV dengan Excel atau LibreOffice Calc
- Program sudah menggunakan UTF-8-BOM encoding

## 📄 Lisensi

MIT License - Silakan digunakan dan dimodifikasi sesuai kebutuhan

## 👨‍💻 Kontributor

Dibuat dengan ❤️ menggunakan Python

## 🤝 Kontribusi

Kontribusi, issues, dan feature requests sangat diterima!

1. Fork repository ini
2. Buat branch fitur baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📞 Kontak & Dukungan

Jika ada pertanyaan atau masalah, silakan buat **Issue** di repository ini.

---

**⭐ Jangan lupa beri star jika program ini membantu Anda!**
