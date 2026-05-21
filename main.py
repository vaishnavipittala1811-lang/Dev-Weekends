import argparse
from analyzer.parser import parse_log_file
from analyzer.stats import generate_statistics
from analyzer.reporter import print_report


def main():
    parser = argparse.ArgumentParser(description="Log Analyzer")
    parser.add_argument("logfile", help="Path to log file")
    parser.add_argument("--top", type=int, default=10)

    args = parser.parse_args()

    parsed_data = parse_log_file(args.logfile)
    stats = generate_statistics(parsed_data, top_n=args.top)

    print_report(stats)


if __name__ == "__main__":
    main()