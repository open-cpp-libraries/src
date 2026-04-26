# Copyright 2026, Amlal El Mahrouss and contributors.
# NeSystem is licensed under Apache-2.0.
# SPDX-Identifier: Apache-2.0

# -*- coding: utf-8 -*-

import updater

def updater_main():
    try:
        updater.start()
    except OSError:
        print("Updater failed.")

# The Upader starts here
if __name__ == '__main__':
    updater_main()

