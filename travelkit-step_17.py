# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: TravelKit
def dry_run_mode():
    import sys, os
    if len(sys.argv) > 1 and sys.argv[1] == "--dry-run":
        print("DRY RUN MODE: No changes will be made to files.")
        return True
    return False

def safe_write(filepath, content):
    is_dry = dry_run_mode()
    if not is_dry:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    else:
        print(f"[DRY RUN] Would write to {filepath}")
        return False

def safe_delete(filepath):
    is_dry = dry_run_mode()
    if not is_dry and os.path.exists(filepath):
        os.remove(filepath)
        return True
    elif is_dry:
        print(f"[DRY RUN] Would delete {filepath}")
        return True
    else:
        return False

def safe_rename(src, dst):
    import shutil
    is_dry = dry_run_mode()
    if not is_dry and os.path.exists(src):
        shutil.move(src, dst)
        return True
    elif is_dry:
        print(f"[DRY RUN] Would rename {src} to {dst}")
        return True
    else:
        return False

def safe_execute(command):
    import subprocess
    is_dry = dry_run_mode()
    if not is_dry:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print("Error:", result.stderr)
            return False
        return True
    else:
        print(f"[DRY RUN] Would execute: {command}")
        return True
