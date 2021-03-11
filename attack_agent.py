#!/usr/bin/env python3
import argparse
from utils.utils import read_records_from_json
from attack_manager import AttackManager
from condition import Condition


def main():
    parser = argparse.ArgumentParser(description="Attack agent")
    parser.add_argument('-f',
                        '--filename',
                        help='database filename',
                        dest='db_file')
    parser.add_argument('-p',
                        '--port',
                        help='Listener port number (default port is 10000)',
                        type=int,
                        default=10000)
    parser.add_argument('-ip',
                        help='Listener ip address',
                        type=str)
    args = parser.parse_args()
    if args.db_file is not None:
        database_records = read_records_from_json(args.db_file)
        manager = AttackManager(database_records)
        manager.update()
        print(manager)
        # assumed_target_state = {"protocol": "ip", "address": "127.0.0.1"}

        goal = Condition()
        goal.add(("shell", "EQ PERMANENT"))
        goal.add(("privilege", "EQ 0"))
        print(goal)
    else:
        print('invalid DB file')


if __name__ == "__main__":
    main()
