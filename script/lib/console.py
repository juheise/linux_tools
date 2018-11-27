import sys


def progress(title, x):
    fif = int(x/2)
    inv = 49-fif
    sys.stdout.write("\r" + title + ": [" + "="*fif + "_"*inv + "](" + "{0:.2f}".format(x) + "%)")
    sys.stdout.flush()
