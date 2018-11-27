import sys


def progress(title, x):
    """
    prints progress in %, overwriting the current line
    Example:
        progress("counting", 50) # produces:
        counting: [=========================________________________](50.00%)
    """

    fif = int(x/2)
    inv = 49-fif
    sys.stdout.write("\r" + title + ": [" + "="*fif + "_"*inv + "](" + "{0:.2f}".format(x) + "%)")
    sys.stdout.flush()
