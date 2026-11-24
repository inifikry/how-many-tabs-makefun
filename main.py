"""Write the entry number to /output/entry.txt.

Entry for make.fun bounty u-danu-how-many-tabs-do-you-have-open-d86e783d:
a single number, digits only, the honest count of open browser tabs.
"""

import os

ENTRY = "63"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
