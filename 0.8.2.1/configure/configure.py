#!/usr/bin/env python

import argparse


def read_file(file_path):
    with open(file_path, 'r') as s:
        return s.readlines()


def write_file(file_path, lines):
    with open(file_path, 'w') as s:
        return s.writelines(lines)


def update(lines, dic):
    for idx, line in enumerate(lines):
        key_to_remove = None
        for k, v in dic.iteritems():
            if (k + '=') in line:
                lines[idx] = (k + '=' + v + '\n')
                key_to_remove = k
        if None != key_to_remove:
            del dic[key_to_remove]
    for k, v in dic.iteritems():
        lines.append(k + '=' + v + '\n')


def init():
    parse = argparse.ArgumentParser(
        description="configure is a Python script to configure Apache Kafka's server.properties file." +
        "You can add or override any Apache Kafka broker config by specifying key=value (eg. ./configure.py broker.id=1 num.partitions=2)",
        version='1')

    parse.add_argument('-i', '--input', help="Specify the input file")
    parse.add_argument('-o', '--output', help="Specify the output file", default='/kafka/server.properties')
    parse.add_argument('-d', '--dryrun', action='store_true', help="Dry run")
    return parse

if __name__ == "__main__":
    parser = init()
    args, broker_args = parser.parse_known_args()

    lines = ['log.dirs=/kafka/data\n', 'zookeeper.connect=zk:2181\n'] if not args.input else read_file(args.input)
    update(lines, dict({arg.partition("=")[::2] for arg in broker_args}))

    print 'Your new server.properties'
    for line in lines:
        print '\t', line[:-1]

    if args.dryrun:
        print ''
        print 'Dryrun done. Nothing has been written'
        print ''
    else:
        try:
            write_file(args.output, lines)
        except TypeError as e:
            print
            print 'TypeError', e
            print
        except IOError as e:
            print
            print 'IO Error:', e.strerror
            print


