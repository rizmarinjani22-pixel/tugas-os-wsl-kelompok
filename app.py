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

# --- BAGIAN EKSEKUSI (Agar bisa dipanggil di terminal) ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Gunakan: python task.py add 'nama' ATAU python task.py list")
    else:
        command = sys.argv[1].lower()
        if command == "add":
            if len(sys.argv) > 2:
                add_task(sys.argv[2])
            else:
                print("Masukkan teks tugasnya!")
        elif command == "list":
            list_tasks()