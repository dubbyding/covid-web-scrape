# covid-web-scrape
    Scraping `https://covid19.mohp.gov.np/` using selenium.
    Selenium was used since the site is updated using Javascript hence, automated
    browsing method was more feasible.

    Inside MOHPNepalScrape, put json file which is downloaded from Settings->Project
    Setting->Service Account then rename it to `file.json`. 

## Create Virtual Environment
    Create virtual environment by:
### In Windows
    python -m venv env
### In Linux
    python3 -m venv env

## Installing requirements
### In Windows
    pip install -r requirements.txt
### In Linux
    pip3 install -r requirements.txt