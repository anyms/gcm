#!/usr/bin/env python 

from argparse import ArgumentParser
import os


class GCM:
    def __init__(self):
        parser = ArgumentParser(description="Github commit management tool")
        parser.add_argument("cmd", type=str, help="command to exucute")
        parser.add_argument("url", type=str, help="Github repo URL", nargs="?")
        self.args = parser.parse_args()

    def run(self):
        branch = os.popen("git branch").read().replace("*", "").strip()
        if self.args.cmd == "branch":
            os.system("git branch")
        elif self.args.cmd == "clone":
            if self.args.url is None:
                print("[Error] Repo URL required to clone")
                return
            os.system("git clone {}".format(self.args.url))
        else:
            print("adding files...")
            os.popen("git add .").read()
            print("commiting files...")
            os.popen('git commit -m "{}"'.format(self.args.cmd.replace('"', '\\"'))).read()
            print("pushing files...")
            os.popen("git push origin {}".format(branch)).read()
            print("done.")


if __name__ == "__main__":
    gcm = GCM()
    gcm.run()
