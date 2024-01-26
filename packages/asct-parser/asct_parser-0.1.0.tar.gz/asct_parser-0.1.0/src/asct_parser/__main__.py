"""
Command-line application for the lib
"""
import argparse

from .asct_parser import parse_asctb
from .utils.util import load_asctb, save_csv


def main():
    """
    ASCT+B parser main script
    """
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument(
        "-g",
        "--gid",
        type=str,
        required=True,
        help="google spreadsheet gid"
    )

    arg_parser.add_argument(
        "-s",
        "--sheet_id",
        type=str,
        required=True,
        help="google spreadsheet sheet_id"
    )

    arg_parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=True,
        help="output path file"
    )
    args = arg_parser.parse_args()

    asct_json = load_asctb(args.gid, args.sheet_id)
    asct_parsed = parse_asctb(asct_json)
    save_csv(asct_parsed, args.output)


if __name__ == "__main__":
    main()
