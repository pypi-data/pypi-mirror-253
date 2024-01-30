from .__init__ import spam
import argparse


def start_cmd(args):
    spam(
        message=args.message,
        startup_wait=args.sec,
        spam_amount=args.spam_amount,
    )


def main():
    parser = argparse.ArgumentParser(description="PyWhatsagspam")
    # Add flags/arguments
    parser.add_argument("--start", action="store_true", help="Start parameter")
    parser.add_argument("message", type=str, help="Another parameter")
    parser.add_argument("spam_amount", type=int, help="Number of times to be spammed")
    parser.add_argument(
        "sec", type=int, help="Seconds to wait before the spamming starts"
    )
    args = parser.parse_args()
    start_cmd(args=args)


if __name__ == "__main__":
    main()
