#!/usr/bin/env python3

if __name__ == "__main__":

    from markdownify import markdownify
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("files", metavar='N', type=str, nargs='+')
    args = parser.parse_args()

    for file in args.files:
        with open(file, "r") as f:
            html = f.read()
        md = markdownify(html)
        with open(file + ".md", "w") as f:
            f.write(md)
