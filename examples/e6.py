#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_pet_names(owner, **pets):
    print(f"Owner Name: {owner}")
    for pet, name in pets.items():
        print(f"{pet}: {name}")


if __name__ == "__main__":
    print_pet_names(
        "Jonathan",
        dog="Brock", fish=["Larry", "Curly", "Moe"],
        turtle="Shelldon"
    )
