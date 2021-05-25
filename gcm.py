#!/usr/bin/env python 

from argparse import ArgumentParser
import os


class GCM:
    def __init__(self):
        parser = ArgumentParser(description="Github commit management tool")
        parser.add_argument("cmd", type=str, help="command to exucute")
        self.args = parser.parse_args()

    def run(self):
        branch = os.popen("git branch").read().replace("*", "").strip()
        if self.args.cmd == "branch":
            pass
        else:
            print("adding files...")
            os.system("git add .")
            print("commiting files...")
            os.system('git commit -m "{}"'.format(self.args.cmd.replace('"', '\\"')))
            print("pushing files...")
            os.system("git push origin {}".format(branch))
            print("done.")


if __name__ == "__main__":
    gcm = GCM()
    gcm.run()
