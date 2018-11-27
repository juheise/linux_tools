#!/usr/bin/env python3

if __name__ == "__main__":

    import lib.cmd as cmd
    import sys

    print("uname is " + cmd.get_string("uname", "-r"))

    for line in cmd.get_lines("dpkg",  "--list", "linux-image*"):
        parts = line.split()
        if parts[0].strip() != "ii":
            continue
        sys.stdout.write("removing " + parts[1] + "... ")
        sys.stdout.flush()
        cmd.get_string("sudo", "apt-get", "-y", "purge", parts[1])
        sys.stdout.write("ok\n")
        sys.stdout.flush()

    print("done!")
