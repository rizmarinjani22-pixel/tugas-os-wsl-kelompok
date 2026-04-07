import json
import sys
import os

FILE_NAME = 'tasks.json'

# --- POINT 2: Fungsi load & save ---
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

# --- POINT 3: Fungsi Add ---
def add_task(text):
    tasks = load_tasks()
    new_id = tasks[-1]['id'] + 1 if tasks else 1
    new_task = {
        "id": new_id,
        "task": text,
        "status": "pending"
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"✅ Berhasil ditambahkan: {text} (ID: {new_id})")

# --- POINT 4: Fungsi List ---
def list_tasks():
    tasks = load_tasks()
    print("\n--- DAFTAR TUGAS ---")
    if not tasks:
        print("Kosong.")
    else:
        for t in tasks:
            print(f"[{t['id']}] {t['task']} - Status: {t['status']}")
    print("--------------------\n")

# --- POINT 5: Fungsi Done ---
def done_task(task_id):
    tasks = load_tasks()
    found = False
    
    for t in tasks:
        if t['id'] == task_id:
            t['status'] = "done"  
            found = True
            break
            
    if found:
        save_tasks(tasks)
        print(f"✅ Tugas dengan ID {task_id} berhasil ditandai selesai!")
    else:
        print(f"❌ Error: Tugas dengan ID {task_id} tidak ditemukan.")

# --- POINT 6: Fungsi Delete ---
def delete_task(task_id):
    tasks = load_tasks()
    initial_length = len(tasks)
    
    #filter list: simpan semua task KECUALI yang ID-nya sama dengan task_id
    tasks = [t for t in tasks if t['id'] != task_id]
    
    #jika panjang list berkurang, berarti ada yang berhasil dihapus
    if len(tasks) < initial_length:
        save_tasks(tasks)
        print(f"🗑️ Tugas dengan ID {task_id} berhasil dihapus!")
    else:
        print(f"❌ Error: Tugas dengan ID {task_id} tidak ditemukan.")

# --- BAGIAN EKSEKUSI (Agar bisa dipanggil di terminal) ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Gunakan: python app.py add 'nama' | list | done [id] | delete [id]")
    else:
        command = sys.argv[1].lower()
        
        if command == "add":
            if len(sys.argv) > 2:
                add_task(sys.argv[2])
            else:
                print("Masukkan teks tugasnya! Contoh: python app.py add 'Belajar OS'")
                
        elif command == "list":
            list_tasks()
            
        elif command == "done":
            # Cek apakah ada argumen ke-2 dan apakah itu angka
            if len(sys.argv) > 2 and sys.argv[2].isdigit():
                done_task(int(sys.argv[2])) # Ubah string ID jadi integer
            else:
                print("Masukkan ID tugas berupa angka! Contoh: python app.py done 1")
                
        elif command == "delete":
            # Cek apakah ada argumen ke-2 dan apakah itu angka
            if len(sys.argv) > 2 and sys.argv[2].isdigit():
                delete_task(int(sys.argv[2]))
            else:
                print("Masukkan ID tugas berupa angka! Contoh: python app.py delete 1")