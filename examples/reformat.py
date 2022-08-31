
import argparse
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
sys.path.append(current_dir.as_posix() + "/../")

from waist.utils import reformat


def make_parse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--infile",
        default="../assets/data/sample.csv",
        type=str,
        help="plese set in filename",
    )
    parser.add_argument(
        "--outfile",
        default="../assets/data/measure.csv",
        type=str,
        help="plese set out filename",
    )

    return parser.parse_args()


def main():
    args = make_parse()
    infile = Path(args.infile).expanduser()
    outfile = Path(args.outfile).expanduser()

    df = reformat(infile, in_unit="inch")
    df.to_csv(outfile)


if __name__ == "__main__":
    main()
