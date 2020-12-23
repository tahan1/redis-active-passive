"""Small script to test active-passive replication between redis clusters

Inserts a 100 values into redis source DB and reads them from its replica.
The script prints the read values in inversed order.
"""
import redis
import argparse
import sys


RANGE_SET_KEY = 'range_set'


def write_redis_oss(host, port, password=None):
    """Sets 1-100 values in a set called 'range_set' in redis source host"""

    r = redis.Redis(
        host=host,
        port=port,
        password=password)

    r.sadd(RANGE_SET_KEY, *list(range(1, 101)))


def read_from_replica(host, port, password=None):
    """Gets the values in the set called 'range_set' in descending order"""

    r = redis.Redis(
        host=host,
        port=port,
        password=password)
    return r.sort(RANGE_SET_KEY, desc=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    requiredNamed = parser.add_argument_group('required named arguments')

    requiredNamed.add_argument('--source_host',
                               help='The IP adress to source db in the active-passive architecture, the redis host to write the data to.',
                               type=str,
                               default=None,
                               required=True)
    requiredNamed.add_argument('--source_port', help='The port number to source db.',
                               type=str,
                               default=None,
                               required=True)
    parser.add_argument('--source_password',
                        help='The password to source db if configured.',
                        type=str,
                        default=None)

    requiredNamed.add_argument('--dest_host',
                               help='The IP adress to destination db in the active-passive architecture, the redis host to read the data from.',
                               type=str,
                               default=None,
                               required=True)
    requiredNamed.add_argument('--dest_port', help='The port number to destination db.',
                               type=str,
                               default=None,
                               required=True)
    parser.add_argument('--dest_password',
                        help='The password to destination db if configured.',
                        type=str,
                        default=None)

    args = parser.parse_args()

    write_redis_oss(args.source_host, args.source_port, args.source_password)
    print(read_from_replica(args.dest_host, args.dest_port, args.dest_password))
