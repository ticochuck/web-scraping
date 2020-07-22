# Web Scraping

[Link to Latest PR]()

## Description
It’s wonderful when someone has gone to the effort to expose their site’s data through an API

But not everyone can (or wants to) do that.

No problem. Let’s code up a web scraper that can automate the process of manually using the site.

## Feature Tasks and Requirements

- Scrape a Wikipedia page and record which passages need citations
    - E.g. [History of Mexico](https://en.wikipedia.org/wiki/History_of_Mexico) has 7 “citation needed” cases, as of this writing.
- Your web scraper should report the number of citations needed.
- Your web scraper should identify those cases AND include the relevant passage.
    - E.g. Citation needed for “lorem spam and impsum eggs”
    - Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.


## Implementation Notes
- Count function must be named get_citations_needed_count
    - get_citations_needed takes in a url and returns an integer

- Report function must be named    get_citations_needed_report
    - get_citations_needed_report takes in a url and returns a string
the string should be formatted with each citation needed on own line, in order found.
    - Module must be named scraper.py


## User Acceptance Tests
- verify that correct count of citations needed is calculated
- verify that preceding passage

## Challenges


## References


## Lab17 - Web Scraping

[Canvas Assignment](https://canvas.instructure.com/courses/2045906/assignments/15160040)

## Author

[Chuck Li Villalobos](https://github.com/ticochuck)
