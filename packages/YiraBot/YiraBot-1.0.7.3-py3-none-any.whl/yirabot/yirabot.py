import os
import sys
from bs4 import BeautifulSoup, Tag
import requests
import textwrap
import urllib.robotparser
import time
from datetime import datetime
from .crawl import crawl,crawl_content, get_html, seo_error_analysis, crawl_protected_page
from colorama import Fore



def main():
    if len(sys.argv) < 2:
        help()
    elif len(sys.argv) > 4:
        sys.exit("YiraBot: Too many arguments!")
    else:
        COMMAND = sys.argv[1]
        try:
            ARGUMENT = sys.argv[2]
        except IndexError:
            pass
        match COMMAND.lower():
            case "session":
                crawl_protected_page()
            case "get-html":
                try:
                    if ARGUMENT.startswith("https://") or ARGUMENT.startswith("http://"):
                        get_html(ARGUMENT)
                    else:
                        ARGUMENT = "https://" + ARGUMENT
                        get_html(ARGUMENT)
                except Exception as e:
                    sys.exit(f"YiraBot: Error Occured: {e}")

            case "check":
                try:
                    if ARGUMENT.startswith("https://") or ARGUMENT.startswith("http://"):
                        seo_error_analysis(ARGUMENT)
                    else:
                        ARGUMENT = "https://" + ARGUMENT
                        seo_error_analysis(ARGUMENT)
                except Exception as e:
                    sys.exit(f"YiraBot: Error Occured: {e}")

            case "crawl":
                try:
                    FLAG = sys.argv[3]
                except IndexError:
                    FLAG = None
                try:
                    if ARGUMENT.startswith("https://") or ARGUMENT.startswith("http://"):
                        if FLAG == "-file":
                            crawl(ARGUMENT, extract=True)
                        elif FLAG == "-json":
                            crawl(ARGUMENT, extract_json=True)
                        elif FLAG == None:
                            crawl(ARGUMENT)
                        else:
                            sys.exit(f"YiraBot: Unrecognized Flag: {FLAG}")
                    else:
                        ARGUMENT = "https://" + ARGUMENT
                        if FLAG == "-file":
                            crawl(ARGUMENT, extract=True)
                        elif FLAG == "-json":
                            crawl(ARGUMENT, extract_json=True)
                        elif FLAG == None:
                            crawl(ARGUMENT)
                        else:
                            sys.exit(f"YiraBot: Unrecognized Flag: {FLAG}")
                except UnboundLocalError:
                    sys.exit("YiraBot: Enter a link to crawl.")

            case "crawl-content":
                try:
                    FLAG = sys.argv[3]
                except IndexError:
                    FLAG = None
                try:
                    if ARGUMENT.startswith("https://") or ARGUMENT.startswith("http://"):
                        if FLAG == "-file":
                            crawl_content(ARGUMENT, extract=True)
                        elif FLAG == "-json":
                            crawl_content(ARGUMENT, extract_json=True)
                        elif FLAG == None:
                            crawl_content(ARGUMENT)
                        else:
                            sys.exit(f"YiraBot: Unrecognized Flag: {FLAG}")
                    else:
                        ARGUMENT = "https://" + ARGUMENT
                        if FLAG == "-file":
                            crawl_content(ARGUMENT, extract=True)
                        elif FLAG == "-json":
                            crawl_content(ARGUMENT, extract_json=True)
                        elif FLAG == None:
                            crawl_content(ARGUMENT)
                        else:
                            sys.exit(f"YiraBot: Unrecognized Flag: {FLAG}")
                except UnboundLocalError:
                    sys.exit("YiraBot: Enter a link to crawl.")
            case _:
                print("YiraBot: Unknown Command.")

def help():
    HELP_MESSAGE = Fore.RED + """
YiraBot Web Crawler v1.0.7.3
----------------------------------
Command Line Web Crawling and SEO Analysis Tool""" + Fore.MAGENTA + """

Usage:
    yirabot [command] <url> [flag] 

Commands:""" + Fore.CYAN + """

crawl
    - Basic Crawl: Performs a standard crawl of the specified URL.
    - Flags:
        -file: Saves data to a text file.
        -json: Saves data to a JSON file.

check
    - SEO Analysis: Analyzes SEO-related elements of the specified URL.

crawl-content
    - Content Crawl: Extracts main content from the specified URL.
    - Flags:
        -file: Saves content data to a text file.
        -json: Saves content data to a JSON file.

get-html
    - HTML Copy: Downloads and saves the complete HTML of the specified URL.

session
    - Protected Crawl: Starts a session for crawling authenticated pages.

""" + Fore.LIGHTBLUE_EX + """
For detailed documentation and examples, visit:
https://github.com/OwenOrcan/YiraBot-Crawler
    """ + Fore.RESET
    print(HELP_MESSAGE)


if __name__ == '__main__':
    main()