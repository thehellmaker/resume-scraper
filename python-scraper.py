import argparse
import platform_specific_scrapers.unstop.unstop_scraper as unstop_scraper

# Set up argument parser
parser = argparse.ArgumentParser(description='Scrape resumes from Unstop platform')
parser.add_argument('--job-url', '-u', type=str, help='The Unstop job URL to scrape resumes from', required=True)

# Parse arguments
args = parser.parse_args()

# Use the job URL from command line arguments
unstop_scraper.scrape_unstop_resumes(args.job_url)