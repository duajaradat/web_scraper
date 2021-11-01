#  Web Scraping

## Author : 

Du'a Jaradat

---

## Links and Resources

- [Web Scraping Code](https://github.com/duajaradat/web_scraper/blob/scraper/web_scraper/scraper.ipynb)
- [Pull Request](https://github.com/duajaradat/web_scraper/pull/1)

---
## Overview

Code up a web scraper that can automate the process of manually using the site.

---
## Feature Tasks and Requirements

- Scrape a Wikipedia page and record which passages need citations.
     - E.g. History of Mexico has a few “citations needed”.

- Your web scraper should report the number of citations needed.

- Your web scraper should identify those cases AND include the relevant passage.
     - E.g. Citation needed for “lorem spam and impsum eggs”
     - Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

---

## Implementation Notes

- Count function must be named    get_citations_needed_count
     - get_citations_needed takes in a url and returns an integer

- Report function must be named get_citations_needed_report
     - get_citations_needed_report takes in a url and returns a string

     - the string should be formatted with each citation needed on own line, in order found.

---     

## User Acceptance Tests

- verify that correct count of citations needed is calculated.

- verify that preceding passage

---

## Tools and Dependencies

- Poetry
- BeautifullSoap
- Requests



---

## Getting Started

- Clone down this repo
- cd web-scraper
- `poetry install`
- `poetry shell`



