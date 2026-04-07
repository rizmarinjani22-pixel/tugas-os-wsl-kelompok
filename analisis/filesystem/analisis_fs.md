Poin 1: Hasil Observasi pwd (Print Working Directory)
Perintah pwd digunakan untuk mengetahui lokasi absolute path (jalur mutlak) direktori tempat kita sedang berada saat ini di dalam sistem operasi Linux. Berdasarkan hasil eksekusi pada terminal WSL, output yang dihasilkan adalah /home/fikri/tugas-os-wsl-kelompok. Hal ini membuktikan bahwa environment pengembangan (VS Code) kita benar-benar berjalan di atas filesystem Linux (Ubuntu/Debian), bukan di filesystem bawaan Windows (seperti C:\Users\...), dengan repositori proyek tersimpan dengan rapi di dalam direktori home milik user fikri.

Poin 2: Hasil Observasi ls -l
Perintah ls -l (list long format) digunakan untuk menampilkan daftar file di dalam direktori beserta rincian atributnya secara lengkap. Berdasarkan screenshot sebelum ada perubahan, perintah ini memperlihatkan beberapa informasi krusial untuk file app.py dan stress_test.py, antara lain: tipe file dan permission (contoh: -rw-r--r--), jumlah link direktori (1), nama Owner (fikri), nama Group (fikri), ukuran file dalam byte, serta tanggal dan waktu modifikasi terakhir.

Poin 3: Analisis Kolom Permission
Pada file app.py (sebelum dimodifikasi), kolom permission menunjukkan string -rw-r--r--. Berikut adalah rincian pembagian hak aksesnya:

Karakter pertama -: Menandakan bahwa ini adalah file biasa (bukan direktori/folder).

rw- (Owner): Owner atau pemilik file (yaitu fikri) memiliki hak untuk membaca (Read / r) dan mengedit/menulis (Write / w) file tersebut, namun tidak memiliki hak untuk mengeksekusinya sebagai program (Execute / x).

r-- (Group): Pengguna lain yang berada dalam kelompok (Group) yang sama dengan fikri hanya memiliki hak untuk membaca (Read / r) file tersebut. Mereka tidak bisa mengedit atau menjalankannya.

r-- (Others): Seluruh pengguna lain (Others) di luar owner dan group juga hanya diberikan hak akses baca (Read / r) saja.

Poin 4: Eksekusi Perintah chmod dan Dampaknya
Setelah menjalankan perintah chmod 755 app.py, dilakukan pengecekan kembali dengan ls -l. Terlihat perubahan drastis pada kolom permission app.py yang semula -rw-r--r-- berubah menjadi -rwxr-xr-x.
Angka 755 merepresentasikan izin akses secara oktal:

7 (rwx) untuk Owner: Pemilik kini bisa membaca, menulis, dan mengeksekusi file tersebut.

5 (r-x) untuk Group: Grup bisa membaca dan mengeksekusi file tersebut (tanpa bisa mengedit).

5 (r-x) untuk Others: Pengguna lain bisa membaca dan mengeksekusi file tersebut (tanpa bisa mengedit).
Dampaknya: File app.py kini dikenali oleh sistem operasi Linux sebagai sebuah program executable (dapat dijalankan langsung). Di terminal, nama file tersebut otomatis berubah warna (biasanya hijau) untuk menandakan statusnya yang kini bisa dieksekusi menggunakan perintah ./app.py.

Poin 5: Analisis Pengelolaan Linux & Implikasi Keamanan
Sistem operasi Linux mengelola seluruh komponennya dengan prinsip dasar "Everything is a file" (semuanya adalah file). Oleh karena itu, mekanisme permission (rwx) menjadi garda terdepan dalam menjaga keamanan sistem. Implikasi permission terhadap keamanan sangatlah vital:

Mencegah Modifikasi Tidak Sah: Dengan mengatur hak akses write (w) hanya pada owner, file kode sumber atau konfigurasi aplikasi (seperti kredensial database) akan aman dari modifikasi yang tidak disengaja atau serangan peretasan dari user lain.

Mencegah Eksekusi Program Berbahaya: Linux tidak mengizinkan sembarang file untuk dijalankan secara otomatis. Sebuah script hanya bisa dieksekusi jika user secara sadar memberikannya hak execute (x) melalui perintah chmod. Ini adalah benteng keamanan untuk mencegah berjalannya malware atau script perusak tanpa izin administrator.
