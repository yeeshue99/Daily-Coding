# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 11:18:13 2020

@author: yeesh
"""

import os


def main():
    i = 00
    cwd = "D:/Workspace/Python"
    for filename in os.listdir(cwd):
        if filename.endswith(".py"):
            dst = filename.replace(" ", "_")
            # dst = os.path.join(cwd, "I rock{0}.txt".format(i))
            src = filename

            os.rename(src, dst)
            i += 1


if __name__ == "__main__":
    main()
