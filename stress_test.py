import time
from app import add_task, load_tasks

def run_stress_test():
    print("="*45)
    print("🚀 MEMULAI STRESS TEST: Menambahkan 1000 task...")
    print("="*45)
    
    # Mencatat waktu mulai
    start_time = time.time()
    
    # Looping sebanyak 1000 kali
    for i in range(1, 1001):
        task_name = f"Tugas Simulasi Beban OS ke-{i}"
        add_task(task_name)
        
    # Mencatat waktu selesai
    end_time = time.time()
    duration = end_time - start_time
    
    # Mengecek total data yang tersimpan di JSON sekarang
    total_tasks = len(load_tasks())
    
    print("\n" + "="*45)
    print("STRESS TEST SELESAI")
    print(f"Waktu Eksekusi   : {duration:.2f} detik")
    print(f"Total Task di JSON : {total_tasks} task")
    print("="*45)
    print("Catatan: Buka file tasks.json untuk melihat hasilnya!")

if __name__ == "__main__":
    run_stress_test()