#! /usr/bin/python3

from os import system

# Copyright 2026, Amlal El Mahrouss and Ne.org contributors.
# Open C++ Libraries is licensed under BSL-1.0

if __name__ == '__main__':
    print("precommit: running format.sh...")
    system("cd libs && cd tproc && git pull && cd ..")
    system("cd libs && cd fix && git pull && cd ..")
    system("cd libs && cd core && git pull && cd ..")
    system("git add libs/core libs/fix libs/tproc")
    system("git commit -s -S")


