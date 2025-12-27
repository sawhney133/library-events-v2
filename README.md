# Library Events Scraper

Automated web scraper that collects family-friendly events from multiple sources in the San Francisco Bay Area.

## Features

- **8 Event Sources:**
  - 4 Library systems (San Jose, Santa Clara, Palo Alto, Mountain View)
  - Home Depot Kids Workshops
  - Oakland Museum (OMCA) First Sunday events
  - KSB Skate Dojo sessions at Tracy Veterans Park
  - Eventbrite Bay Area events

- **Auto-Updates Daily:** GitHub Actions runs the scraper every day at midnight PST
- **Filtering:** Filter by location, date range, and source
- **Responsive Design:** Works on desktop and mobile

## Live Site

https://sawhney133.github.io/library-events-v2/

## How It Works

1. `library_website.py` scrapes events from all sources
2. Generates `index.html` with all events
3. GitHub Actions runs daily to update the data
4. GitHub Pages serves the static site

## Manual Update

Go to **Actions** → **Update Events Daily** → **Run workflow**

## Local Development

```bash
# Install dependencies
pip install requests beautifulsoup4

# Run scraper
python library_website.py

# Open index.html in browser
open index.html
```

## Event Sources

All events are scraped from public websites and are free to attend.
