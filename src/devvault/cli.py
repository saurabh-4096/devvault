import sys
from devvault.scanner import scan_directory


def main():
    if len(sys.argv) < 3 or sys.argv[1] != "index":
        print("Usage: devvault index <path>")
        return
    files = scan_directory(sys.argv[2])
    print(f"Indexed {len(files)} files")


if __name__ == "__main__":
    main()