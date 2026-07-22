import os
import sys
import argparse
from pathlib import Path

# --- Configuration ---
VAULT_ROOT = Path(os.getenv("OBSIDIAN_VAULT_ROOT", r"D:\Obsidian\LLM-Wiki")).resolve()
RAW_DIR = VAULT_ROOT / "raw"
PROTECTED_DIRS = [RAW_DIR]

def is_safe_path(target_path: str) -> bool:
    """Check if the path is within the vault and avoids forbidden traversal."""
    try:
        # Resolve to absolute path, eliminating .. and symlinks
        target = Path(target_path).resolve()
        
        # 1. Reject if it escapes the vault root
        if not str(target).startswith(str(VAULT_ROOT)):
            print(f"❌ FIREWALL BLOCK: Path escapes vault root.\nAttempted: {target}")
            return False
            
        # 2. Check protected directory modification rules
        # For example, we shouldn't modify existing files in raw/
        for protected in PROTECTED_DIRS:
            if str(target).startswith(str(protected)):
                # Allow creating NEW files in raw/web, but not editing existing ones
                if target.exists() and not target.is_dir():
                    print(f"❌ FIREWALL BLOCK: Attempting to modify immutable source in {protected.name}/\nTarget: {target}")
                    return False

        return True
    except Exception as e:
        print(f"❌ FIREWALL BLOCK: Path resolution error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Obsidian-safe CLI Firewall")
    parser.add_argument("action", choices=["read", "write", "delete"], help="The action to perform")
    parser.add_argument("path", help="The target file path")
    parser.add_argument("--content", help="Content to write (if action is write)", default="")
    
    args = parser.parse_args()
    
    target = Path(args.path)
    
    # Run firewall checks
    if not is_safe_path(str(target)):
        sys.exit(1)
        
    print("✅ FIREWALL PASS: Path is safe.")
    
    # Execute the action if safe
    try:
        if args.action == "read":
            with open(target, 'r', encoding='utf-8') as f:
                print(f.read())
        elif args.action == "write":
            target.parent.mkdir(parents=True, exist_ok=True)
            with open(target, 'w', encoding='utf-8') as f:
                f.write(args.content)
            print(f"Successfully wrote to {target.name}")
        elif args.action == "delete":
            target.unlink()
            print(f"Successfully deleted {target.name}")
    except Exception as e:
        print(f"Operation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
