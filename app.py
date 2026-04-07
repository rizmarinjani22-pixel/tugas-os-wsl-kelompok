import os
import time

# Menampilkan identitas proses sesuai tugas
print("=== ANALISIS SISTEM OPERASI ===")
print(f"Nama Aplikasi : MyOSAnalyzer")
print(f"Process ID (PID): {os.getpid()}")
print("-------------------------------")
print("Aplikasi sedang berjalan... Tekan Ctrl+C untuk berhenti.")

try:
    while True:
        # Melakukan sedikit perhitungan agar CPU terpakai sedikit
        _ = 100 * 100
        time.sleep(1)
except KeyboardInterrupt:
    print("\nProses dihentikan oleh pengguna.")