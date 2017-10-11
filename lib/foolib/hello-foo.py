from __future__ import print_function

import sys

from foolib import url_content


def main():
    print(url_content('https://www.google.com'))


if __name__ == "__main__":
    sys.exit(main())
