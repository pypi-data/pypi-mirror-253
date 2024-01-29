#!/usr/bin/env python
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("exec", help="参数: [init, migrate, upgrade]")

    args = parser.parse_args()

    if args.exec == "init":
        print("init finished")

    else:
        print("参数错误")


if __name__ == '__main__':
    main()
