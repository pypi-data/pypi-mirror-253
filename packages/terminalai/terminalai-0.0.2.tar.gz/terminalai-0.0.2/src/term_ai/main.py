import argparse
import os
import sys

from term_ai.chat import get_response


def main():
    parser = argparse.ArgumentParser(description="Linux Terminal assistant")
    args = parser.parse_args()
    api_key = args.apikey
    os.system("clear")
    if len(sys.argv) == 0:
        print("Usage: termai <Query>")
        sys.exit(1)

    response = get_response(sys.argv[1])
    print(response)
