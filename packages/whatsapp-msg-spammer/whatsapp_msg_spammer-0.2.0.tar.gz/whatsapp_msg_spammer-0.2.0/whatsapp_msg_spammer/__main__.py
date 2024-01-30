from .__init__ import spam

import argparse


def start_cmd(args):
    spam(
        message=args.message,
        spam_amount=args.repeat,
    )


def main():
    parser = argparse.ArgumentParser(description="PyWhatsagspam")

    # Add flags/arguments
    parser.add_argument("start", choices=["in"], help="Start parameter")
    parser.add_argument(
        "__sec",
        type=int,
        help="Seconds to wait before the spamming starts",
        metavar="__sec",
    )
    parser.add_argument("message", type=int, help="Another parameter")
    parser.add_argument("spam_amount", type=int, help="Number of times to be spammed")

    args = parser.parse_args()
    start_cmd(args=args)


if __name__ == "__main__":
    main()
