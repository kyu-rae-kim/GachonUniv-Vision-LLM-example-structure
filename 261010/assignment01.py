# Main File to Run

import optional_files
from optional_files import bar


def foo():
    print("hello")


def main():
    foo()
    bar(should_print=optional_files.MY_BOOL)


if __name__ == "__main__":
    main()
