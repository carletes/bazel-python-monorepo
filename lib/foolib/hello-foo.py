from __future__ import print_function

import pprint
import sys

from foolib import url_content


def main():
    print('PYTHONPATH: {}'.format(pprint.pformat(sys.path)))
    url = 'https://www.ecmwf.int'
    content, num_cpus = url_content(url)
    print('Processed {} using {} CPU(s)'.format(url, num_cpus))
    print('Length of {}: {}'.format(url, len(content)))


if __name__ == "__main__":
    sys.exit(main())
