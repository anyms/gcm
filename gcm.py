#!/usr/bin/env python 

from argparse import ArgumentParser
import os


class GCM:
    def __init__(self):
        parser = ArgumentParser(description="Github commit management tool")
        parser.add_argument("cmd", type=str, help="command to exucute")
        self.args = parser.parse_args()

    def run(self):
        if self.args.cmd == "branch":
            pass
        else:
            os.popen("git add .")
            os.popen("git commit -m '{}'".format(self.args.cmd))
            os.popen("git push")


if __name__ == "__main__":
    gcm = GCM()
    gcm.run()
