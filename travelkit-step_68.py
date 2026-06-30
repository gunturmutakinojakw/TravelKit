# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: TravelKit
from datetime import datetime, timedelta
import json
from pathlib import Path

def generate_changelog(repo_path: str = ".", days_back: int = 30) -> list[dict]:
    """Generate a compact changelog from git log without external dependencies."""
    logs = []
    try:
        # Run git log to get recent commits formatted as text
        import subprocess
        result = subprocess.run(
            ["git", "-C", repo_path, "log", "--oneline", "--since", f"{days_back} days ago"],
            capture_output=True, text=True, check=False
        )
        if not result.returncode == 0:
            return logs
        
        lines = result.stdout.strip().split("\n")
        for line in lines:
            if not line:
                continue
            # Parse simplified git log output: "hash (author) date message"
            parts = line.split(" ", 2)
            if len(parts) < 3:
                continue
            
            commit_hash, author_info, message = parts[0], parts[1] + " " + parts[2], ""
            
            # Extract short hash and clean message
            short_hash = commit_hash[:7]
            
            # Clean up the message to remove extra whitespace or newlines
            msg_parts = message.split("\n")
            if len(msg_parts) > 1:
                main_msg = msg_parts[0].strip()
                logs.append({
                    "hash": short_hash,
                    "message": main_msg,
                    "timestamp": datetime.now().isoformat(), # Placeholder for actual commit date parsing if needed
                    "author": author_info.split("(")[1].rstrip(")") if "(" in author_info else "Unknown"
                })
            else:
                logs.append({
                    "hash": short_hash,
                    "message": message.strip(),
                    "timestamp": datetime.now().isoformat(),
                    "author": author_info
                })
    except Exception:
        pass # Handle cases where git is not available or repo is empty
    
    return logs

def write_changelog_file(repo_path: str = ".", output_file: str = "CHANGELOG.md") -> None:
    """Write the generated changelog to a markdown file."""
    changelog_data = generate_changelog(repo_path)
    
    if not changelog_data:
        print("No recent commits found.")
        return

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# TravelKit Changelog\n\n")
        
        for entry in reversed(changelog_data): # Newest first
            date_str = entry.get("timestamp", "")[:10] if isinstance(entry["timestamp"], str) else ""
            author = entry.get("author", "Unknown")
            msg = entry.get("message", "")
            
            f.write(f"### {date_str} - [{author}]({repo_path})\n\n")
            f.write(f"{msg}\n\n---\n\n")

# Usage example (uncomment to run):
# write_changelog_file()
