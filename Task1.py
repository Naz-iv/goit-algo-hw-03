import os
import shutil
import argparse


def dir_lookup(path: str) -> list[str]:
    files = []
    try:
        dir_contents = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: Source directory '{path}' not found.")
        raise

    for entry in dir_contents:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            files.extend(list_files(full_path))
        else:
            files.append(full_path)

    return files


def files_copy_and_order(files: list[str], final_dir: str) -> None:
    for file_path in files:
        _, file_extension = os.path.splitext(file_path)
        file_extension = file_extension.strip(".")

        if not file_extension:
            destination = os.path.join(final_dir, "Unknown type")
        else:
            destination = os.path.join(final_dir, file_extension)

        try:
            os.makedirs(destination, exist_ok=True)
        except OSError as e:
            print(f"Error creating directory '{destination}': {e}")
            raise

        try:
            shutil.copy(file_path, destination)
        except OSError as e:
            print(f"Error copying '{file_path}' to '{destination}': {e}")
            raise


def main():
    parser = argparse.ArgumentParser(
        description="Files copying and ordering by extension"
    )
    parser.add_argument(
        "-s", "--src", help="Path to source directory"
    )
    parser.add_argument(
        "-d", "--dest", nargs="?", default="dist",
        help="Path to destination directory (default: dist)"
    )
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        print(f"Error: {e}")
        parser.print_help()
        return

    try:
        origin_dir = os.path.abspath(args.src)
    except TypeError:
        print(f"Source destination is required! See help below!")
        parser.print_help()
        return

    final_dir = os.path.abspath(args.dest)

    print(f"Looking up files in {origin_dir}")

    files = dir_lookup(origin_dir)

    try:
        files_copy_and_order(files, final_dir)
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    print("Operation completed!")


if __name__ == "__main__":
    main()
