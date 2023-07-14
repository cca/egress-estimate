#!/usr/bin/env python
from multiprocessing import Pool, Manager
import time

# https://pypi.org/project/apachelogs/
from apachelogs import LogParser

logparser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")


def create_or_add(key, value):
    if data.get(key) is None:
        data[key] = value
    else:
        data[key] += value


def parse_file(file):
    # our output, it will look like {'2022-01': 123123, '2022-02': 123123 }
    output = {}
    with open(file, 'r') as fh:
        lines = fh.readlines()
        print(f'Processing {file} ({len(lines)} lines)')
        for line in lines:
            response = logparser.parse(line)
            bytes = response.bytes_sent
            if bytes:
                month = response.request_time.strftime('%Y-%m')
                create_or_add(month, bytes)


def init_pool(d):
    global data
    data = d


def main(files):
    with Manager() as manager:
        data = manager.dict()
        with Pool(initializer=init_pool, initargs=(data,)) as pool:
            pool.map(parse_file, files)
        # @TODO output format(s), probably CSV is best
        print(data)


if __name__ == '__main__':
    start_time = time.time()
    import argparse
    parser = argparse.ArgumentParser(description='sum the egress of apache log files')
    parser.add_argument('files', nargs='+')
    files = parser.parse_args().files
    main(files)
    print(f"Done in {time.time() - start_time}")
