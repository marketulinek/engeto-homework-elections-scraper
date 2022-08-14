"""
projekt_3.py: treti projekt do Engeto Online Python Akademie

author: Marketa
discord: jsem opozdilec z minuleho behu akademie a pouzivali jsme Slack :-D
"""
from validation import validate_command_inputs
from scraper import scrape_data
import sys


validate_command_inputs(sys.argv)

data = scrape_data(sys.argv[1])