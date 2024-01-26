import argparse
from .generate_daily_summary import generate
from .summarize_diff import summarize_all_diffs
from .git_data_extract import extract_git_data
import os

def main():
    parser = argparse.ArgumentParser(description="Generate daily development reports.")
    parser.add_argument(
        "--repo",
        help="Path to the repository to generate the report for",
        required=True,
    )
    parser.add_argument(
        "--author",
        help="Name of the author to generate the report for",
        required=True,
    )
    # Add arguments as needed. For example:
    # parser.add_argument('--date', help='Date for the report', required=True)

    args = parser.parse_args()
    print("Generating daily development report...")
    print("Extracting git data...")
    extract_git_data(args.repo, args.author)  # Example usage
    print("Summarizing diffs...")
    summarize_all_diffs()
    print("Generating daily summary...")
    generate()
    # clean up the diffs.json file and summaries.txt file
    os.remove("diffs.json")
    os.remove("summaries.txt")
    print("Done!")