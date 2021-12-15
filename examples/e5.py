#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_scores(student, *scores):
    print(f"Student Name: {student}")
    for score in scores:
        print(score)


if __name__ == "__main__":
    print_scores("Jonathan", 100, 95, 88, 92, 99)
