#!/usr/bin/env python3

if __name__ == "__main__":

    import lib.cmd as cmd

    for f in ["/var/lib/dpkg/lock", "/var/cache/apt/archives/lock", "/var/cache/debconf/*.dat"]:
        try:
            cmd.run("rm", f)
        except:
            pass

    cmd.run("dpkg", "--configure", "-a")
