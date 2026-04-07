import os
import time
import psutil # Pastikan ini ada, kalau error ketik: pip install psutil

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # Konversi ke MB

print("="*40)
print("   MY OS ANALYZER - KELOMPOK WSL   ")
print("="*40)
print(f"✅ Process ID (PID) : {os.getpid()}")
print(f"✅ User Running     : {os.getlogin() if os.name != 'nt' else 'User'}")
print(f"✅ Lokasi File      : {os.path.abspath(__file__)}")
print("-"*40)

try:
    print("Aplikasi sedang berjalan...")
    while True:
        mem = get_memory_usage()
        print(f"📊 Real-time Memory Usage: {mem:.2f} MB", end="\r")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n\n[!] Aplikasi dihentikan oleh user (Ctrl+C)")
    print("="*40)