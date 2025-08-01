🕸️ TimesJobs Web Scraper - POC
===============================

This is a simple proof-of-concept (POC) Python project that performs web scraping to fetch the latest Python job listings from TimesJobs. It filters out jobs based on a user-provided unfamiliar skill, so you only see jobs that don’t require that skill.

💡 Features
-----------
- Scrapes recent Python job postings from TimesJobs
- Filters out listings containing a skill you are unfamiliar with
- Prints job details: company name, skills required, and the job link
- Automatically refreshes results every few minutes (commented out for testing)

🛠️ Requirements
----------------
- Python 3.x
- requests
- beautifulsoup4

Install dependencies:
    pip install requests beautifulsoup4 lxml

🚀 Usage
--------
    python main.py

You'll be prompted to enter an unfamiliar skill (e.g., `java`), and it will skip jobs that mention that skill.

📌 Note
-------
- The job refresh is currently set to every 10 minutes but commented out for development.
- This is a basic demo project and not intended for production use.

📚 Purpose
----------
This project serves as a basic POC for web scraping using BeautifulSoup and requests.
