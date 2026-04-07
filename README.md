# 📚 Daftar Buku Bacaan

Aplikasi manajemen tugas berbasis terminal. 
User bisa menambah, menyelesaikan, dan menghapus 
task semua lewat command line. 
Data disimpan ke file JSON.

---

## 👥 Anggota Kelompok
- Muhammad Rafi Irhab Hasibuan (224443038)
- Muhammad Irsyad Salim Nugraha (224443036)
- Muhammad Kaisar Wibawa Utama (224443037)
- Rendiana Fauzi Gunawan (224443041)
- Zaki Rahman Adlilvry (224443047)
- Fikri Zaini (224443031)
- Salsabila Ramadhani Gusmi (224443041)
- Rizma Rinjani (224443043)
---

## ⚙️ Persiapan Awal (Wajib Dilakukan Sekali)

### 1. Install WSL di Windows
Buka **PowerShell** sebagai Administrator, lalu jalankan:
```bash
wsl --install
```
Setelah selesai, **restart PC** dan buka aplikasi **Ubuntu** dari Start Menu.
Buat username dan password untuk Linux kamu.

### 2. Install Python di WSL
Setelah masuk Ubuntu, jalankan:
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

### 3. Clone Repository Ini
```bash
git clone https://github.com/rizmarinjani22-pixel/tugas-os-wsl-kelompok
cd tugas-os-wsl-kelompok
```

---

## 🚀 Cara Menjalankan

Pastikan kamu sudah berada di folder project:
```bash
cd tugas-os-wsl-kelompok
```

Jalankan aplikasi dengan perintah:
```bash
python3 app.py [perintah]
```

---

## 📖 Daftar Perintah

### Melihat Semua Buku
```bash
python3 app.py list
```
Menampilkan semua buku yang ada di daftar beserta ID, judul, penulis, dan statusnya.

### Menambah Buku Baru
```bash
python3 app.py add "Judul Buku" "Nama Penulis"
```
Contoh:
```bash
python3 app.py add "Laskar Pelangi" "Andrea Hirata"
```

### Menandai Buku Sudah Dibaca
```bash
python3 app.py done [id]
```
Contoh — menandai buku dengan ID 1 sudah dibaca:
```bash
python3 app.py done 1
```

### Menghapus Buku
```bash
python3 app.py delete [id]
```
Contoh — menghapus buku dengan ID 2:
```bash
python3 app.py delete 2
```

---

## 📁 Struktur Project
tugas-os-wsl-kelompok/
├── app.py          # file utama aplikasi
├── books.json      # penyimpanan data buku
└── README.md       # dokumentasi ini

---

## 📝 Contoh Penggunaan
```bash
# Tambah beberapa buku
python3 app.py add "Laskar Pelangi" "Andrea Hirata"
python3 app.py add "Bumi Manusia" "Pramoedya Ananta Toer"

# Lihat daftar
python3 app.py list

# Tandai buku pertama sudah dibaca
python3 app.py done 1

# Hapus buku kedua
python3 app.py delete 2
```
