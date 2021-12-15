#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_these(a=None, b=None, c=None):
    print(a, "is stored in a")
    print(b, "is stored in b")
    print(c, "is stored in c")


if __name__ == "__main__":
    print_these(c=3, a=1)
