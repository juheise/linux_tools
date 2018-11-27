import sys


def progress(title, x):
    """
    prints progress in %, overwriting the current line. Values above 100 and below 0 will be clipped.
    Example:
        progress("counting", 50) # produces:
        counting: [=========================________________________](50.00%)
    """

    if x < 0:
        x = 0
    if x > 100:
        x = 100

    fif = int(x/2)
    inv = 49-fif
    sys.stdout.write("\r" + title + ": [" + "="*fif + "_"*inv + "](" + "{0:.2f}".format(x) + "%)")
    sys.stdout.flush()
