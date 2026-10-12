# Dependency file for the main .py file (optional; as many as you need)

MY_BOOL = True


def bar(txt: str ="world", should_print: bool = False):
    if should_print:
        print(txt)
