import subprocess


def get_lines(*args):
    out = subprocess.check_output(args).decode("utf-8").strip()
    return out.split("\n")


def get_string(*args):
    return subprocess.check_output(args).decode("utf-8").strip()


def run(*args):
    subprocess.check_output(args)
