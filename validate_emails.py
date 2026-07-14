import re
import sys

EMAIL_PATTERN = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


def is_valid_email(address):
    return bool(EMAIL_PATTERN.match(address))


def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else "emails.txt"

    with open(input_path, "r") as f:
        for line in f:
            address = line.strip()
            if address and is_valid_email(address):
                print(address)


if __name__ == "__main__":
    main()
