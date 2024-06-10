from subprocess import call
from pathlib import Path
import sys


def collect_all_files() -> list[Path]:
    """
    Search recursively all folders for .c and .h files
    """
    return list(Path('.').rglob('*.[ch]'))


def check_formatting(files_list: list[Path]) -> int:
    """
    Check if all files are formatted correctly.
    Return the number of files that are not formatted correctly.
    """
    error_count = 0
    for file in files_list:
        return_code = call(['clang-format', '--style=file',
                           '--dry-run', '-Werror', str(file)])
        if return_code != 0:
            error_count += 1
    return error_count


def main():
    files_to_format = collect_all_files()

    print('Checking if all files are formatted correctly...')
    error_count = check_formatting(files_to_format)
    if error_count > 0:
        print(f'{error_count} files are not formatted correctly')
        sys.exit(1)


if __name__ == '__main__':
    main()
