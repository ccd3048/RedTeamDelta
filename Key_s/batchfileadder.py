import winreg
from pathlib import Path

def add_batch_to_startup(batch_path: str):
    try:
        batch_path = Path(batch_path).resolve()
        
        if not batch_path.exists():
            return False
        
        key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE) as key:
            winreg.SetValueEx(key, batch_path.stem, 0, winreg.REG_SZ, str(batch_path))
            return True
            
    except PermissionError:
        exit
    except Exception as e:
        exit

if __name__ == "__main__":
    batch_path = r"\keyScrambler.bat"
    if add_batch_to_startup(batch_path):
        print(f"Successfully added {batch_path} to startup")