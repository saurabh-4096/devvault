import sys
from devvault.scanner import scan_directory
from devvault.database import init_db, save_files, count_files, search_files


def main():
    init_db()

    if len(sys.argv) >= 3 and sys.argv[1] == "index":
        files = scan_directory(sys.argv[2])
        save_files(files)
        total = count_files()
        print(f"Indexed {len(files)} files. Total in database: {total}")

    elif len(sys.argv) >= 3 and sys.argv[1] == "search":
        query = " ".join(sys.argv[2:])
        results = search_files(query)
        if not results:
            print("No results found.")
        else:
            print(f"{len(results)} results found\n")
            for result in results:
                print(result["path"])
                print(f"  {result['preview']}\n")

    else:
        print("Usage: devvault index <path>  OR  devvault search <query>")


if __name__ == "__main__":
    main()