from .cleaner import clean
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Clean commented-out code from Python files."
    )
    parser.add_argument("files", nargs="+", help="File(s) to clean.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Display the changes without applying them.",
    )

    args = parser.parse_args()

    print(f"Cleaning files: {args.files}")
    for file in args.files:
        print(f"Cleaning file: {file}")
        clean(file, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
