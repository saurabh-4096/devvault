import sys
from devvault.scanner import scan_directory
from devvault.database import init_db, save_files, count_files


def main():
    if len(sys.argv) < 3 or sys.argv[1] != "index":
        print("Usage: devvault index <path>")
        return

    init_db()
    files = scan_directory(sys.argv[2])
    save_files(files)
    total = count_files()
    print(f"Indexed {len(files)} files. Total in database: {total}")


if __name__ == "__main__":
    main()