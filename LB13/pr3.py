#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def done_laboratories(*args):
    if args:
        laboratories = tuple(int(arg) for arg in args)
        return laboratories
    else:
        return None


if __name__ == "__main__":
    labs = [i for i in input("Enter the numbers of laboratories: ").split()]
    print(f"You have defended these laboratories: {done_laboratories(*labs)}")
