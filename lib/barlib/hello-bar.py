from __future__ import print_function

import pprint
import sys

from barlib import num_cpus


def main():
    print('PYTHONPATH: {}'.format(pprint.pformat(sys.path)))
    print('Number of CPUs: {}'.format(num_cpus()))


if __name__ == "__main__":
    sys.exit(main())
