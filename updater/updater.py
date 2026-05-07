# Copyright 2026, Amlal El Mahrouss and contributors.
# Open C++ Libraries is licensed under BSL-1.0

# -*- coding: utf-8 -*-

import subprocess
import os

class UpdateFunctor:
    def __init__(self):
        subprocess.call(["git", "-C", "libs/tproc", "pull"])
        subprocess.call(["git", "-C", "libs/fix", "pull"])
        subprocess.call(["git", "-C", "libs/core", "pull"])
        subprocess.call(["git", "add", "libs/core", "libs/fix", "libs/tproc"])
        if (os.environ.get('UPDATER_NO_COMMIT', False) == False):
            subprocess.call(["git", "commit", "-s", "-S"])


def start():
    functor = UpdateFunctor()
    print("INFO: Updater: Functor called")

